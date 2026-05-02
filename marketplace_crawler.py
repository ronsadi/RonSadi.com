#!/usr/bin/env python3
"""Second-place marketplace deal crawler + pricing playbook for weighted keyboards.

This tool is intentionally API-key-free so it can run immediately.
It assembles live search URLs for major second-hand marketplaces and
applies a value model to estimate fair target and negotiated net price.
"""

from dataclasses import dataclass
from urllib.parse import quote_plus


@dataclass
class ModelPolicy:
    model: str
    quality_tier: str
    fair_low: int
    fair_high: int
    walkaway: int
    opening_offer: int
    ceiling_offer: int


def recommended_models_for_weighted_keyboard() -> list[ModelPolicy]:
    """Prescriptive shortlist for entry-to-mid value with strong used liquidity."""
    return [
        ModelPolicy("Yamaha P-45", "Best floor value", 260, 340, 360, 220, 320),
        ModelPolicy("Roland FP-10", "Best key action per dollar", 320, 420, 450, 280, 400),
        ModelPolicy("Casio CDP-S110", "Lowest-cost acceptable weighted 88", 180, 280, 300, 150, 260),
    ]


def build_search_urls(location: str, model: str) -> dict[str, str]:
    q = quote_plus(f"{model} weighted keyboard")
    loc = quote_plus(location)
    return {
        "Facebook Marketplace": f"https://www.facebook.com/marketplace/{loc}/search/?query={q}",
        "OfferUp": f"https://offerup.com/search/?q={q}",
        "Craigslist Orlando": f"https://orlando.craigslist.org/search/msa?query={q}",
        "eBay Used": f"https://www.ebay.com/sch/i.html?_nkw={q}&LH_ItemCondition=3000",
        "Mercari": f"https://www.mercari.com/search/?keyword={q}",
    }


def negotiation_message(model: ModelPolicy) -> str:
    return (
        f"Hey! I can pick up today, cash, no hassle. "
        f"I’m comparing a few {model.model} listings and my budget is tight. "
        f"If the keys, speakers, and pedal input all work, I can do ${model.opening_offer} now. "
        f"If you include stand/pedal, I can stretch to ${model.ceiling_offer}. "
        "I can meet at a police-safe exchange spot and be there within the hour."
    )


def main() -> None:
    location = "Orlando, Florida"
    item = "weighted keyboard"
    print(f"Item: {item}")
    print(f"Location: {location}\n")
    print("Recommended value policies:\n")
    for m in recommended_models_for_weighted_keyboard():
        print(f"- {m.model} ({m.quality_tier})")
        print(f"  Fair range: ${m.fair_low}-${m.fair_high}")
        print(f"  Walk-away cap: ${m.walkaway}")
        print(f"  Open at: ${m.opening_offer} | Ceiling: ${m.ceiling_offer}")
        print("  Search URLs:")
        for source, url in build_search_urls(location, m.model).items():
            print(f"    • {source}: {url}")
        print("  Prewritten negotiation message:")
        print(f"    {negotiation_message(m)}\n")


if __name__ == "__main__":
    main()
