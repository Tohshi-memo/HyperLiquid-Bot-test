# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-28T11:07:31.052184+00:00`
- Price records: `672`
- Market context records: `5033`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10200`

## Conditions

- `news_risk_high`: News Risk is elevated.
- `macro_risk_high`: Macro Risk is elevated.
- `risk_on_high`: Risk-On score is elevated.
- `market_context_high`: Market Context is supportive.
- `polymarket_volume_spike`: Polymarket 24h volume z-score is elevated.
- `flow_alert_high`: Flow Alert score is elevated.
- `news_and_polymarket`: News Risk and Polymarket volume spike happen together.
- `risk_on_and_context`: Risk-On and Market Context are both supportive.
- `macro_and_flow`: Macro Risk and Flow Alert are elevated together.

## Top Patterns

- `market_context_high->unknown_1h` score `14.045` n `95` status `ready` deltaP `2.3416` edge `1.2049` maxDD `-1.674`
- `market_context_high->unknown_4h` score `9.1171` n `93` status `ready` deltaP `22.2118` edge `0.7139` maxDD `-5.5109`
- `market_context_high->crypto_major_4h` score `5.4515` n `93` status `ready` deltaP `16.4897` edge `0.5028` maxDD `-8.3416`
- `market_context_high->crypto_alt_4h` score `5.2804` n `93` status `ready` deltaP `14.1785` edge `0.4849` maxDD `-7.8181`
- `market_context_high->metal_4h` score `1.2404` n `93` status `ready` deltaP `13.2392` edge `0.123` maxDD `-1.9651`
- `market_context_high->equity_1h` score `0.8335` n `95` status `ready` deltaP `8.0397` edge `0.0732` maxDD `-2.5875`
- `market_context_high->crypto_major_1h` score `0.707` n `95` status `ready` deltaP `5.9202` edge `0.1112` maxDD `-4.6734`
- `market_context_high->equity_4h` score `0.3892` n `93` status `ready` deltaP `2.5112` edge `0.1713` maxDD `-6.3852`
- `market_context_high->metal_1h` score `0.3613` n `95` status `ready` deltaP `6.3693` edge `0.0373` maxDD `-1.3057`
- `market_context_high->crypto_alt_1h` score `0.1591` n `95` status `ready` deltaP `5.0315` edge `0.0891` maxDD `-5.5126`
- `market_context_high->fx_24h` score `-0.0314` n `74` status `ready` deltaP `9.7316` edge `0.0073` maxDD `-1.7626`
- `market_context_high->index_4h` score `-0.1654` n `93` status `ready` deltaP `3.4094` edge `0.0396` maxDD `-1.0893`
- `market_context_high->commodity_1h` score `-0.3191` n `95` status `ready` deltaP `1.5695` edge `0.0146` maxDD `-1.278`
- `market_context_high->index_1h` score `-0.6145` n `95` status `ready` deltaP `1.5742` edge `0.0124` maxDD `-0.5946`
- `market_context_high->commodity_4h` score `-0.7862` n `93` status `ready` deltaP `3.8503` edge `-0.0012` maxDD `-5.021`
- `market_context_high->fx_4h` score `-1.0181` n `93` status `ready` deltaP `-4.3732` edge `-0.0025` maxDD `-1.2426`
- `market_context_high->fx_1h` score `-1.7063` n `95` status `ready` deltaP `-11.3662` edge `-0.0054` maxDD `-0.5482`
- `market_context_high->metal_24h` score `-3.7002` n `74` status `ready` deltaP `5.7292` edge `0.0329` maxDD `-32.9721`
- `market_context_high->unknown_24h` score `-4.3382` n `74` status `ready` deltaP `27.0364` edge `-0.5075` maxDD `-1.4072`
- `market_context_high->commodity_24h` score `-4.6146` n `74` status `ready` deltaP `0.7601` edge `-0.0858` maxDD `-27.5371`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
