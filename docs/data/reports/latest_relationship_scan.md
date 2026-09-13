# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-13T14:52:29.429801+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13362`

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

- `market_context_high->unknown_24h` score `17910.9797` n `56` status `ready` deltaP `8.596` edge `1492.5445` maxDD `-0.613`
- `risk_on_high->unknown_24h` score `12000.6803` n `31` status `ready` deltaP `12.8587` edge `999.9767` maxDD `-0.1252`
- `risk_on_and_context->unknown_24h` score `12000.6803` n `31` status `ready` deltaP `12.8587` edge `999.9767` maxDD `-0.1252`
- `news_risk_high->unknown_1h` score `419.1963` n `82` status `ready` deltaP `-4.8014` edge `35.0072` maxDD `-1.7068`
- `news_risk_high->crypto_major_24h` score `18.2896` n `82` status `ready` deltaP `38.0236` edge `1.4177` maxDD `-9.098`
- `news_risk_high->crypto_alt_24h` score `18.2701` n `82` status `ready` deltaP `34.6509` edge `1.3403` maxDD `-2.2369`
- `risk_on_high->crypto_alt_24h` score `9.1641` n `31` status `ready` deltaP `25.9176` edge `0.6363` maxDD `-1.9661`
- `risk_on_and_context->crypto_alt_24h` score `9.1641` n `31` status `ready` deltaP `25.9176` edge `0.6363` maxDD `-1.9661`
- `news_risk_high->equity_24h` score `8.4978` n `82` status `ready` deltaP `24.6846` edge `0.7216` maxDD `-6.5742`
- `news_risk_high->index_24h` score `6.8158` n `82` status `ready` deltaP `48.4566` edge `0.2626` maxDD `-0.0797`
- `market_context_high->crypto_alt_24h` score `5.5739` n `56` status `ready` deltaP `19.5812` edge `0.6745` maxDD `-4.5683`
- `news_risk_high->metal_24h` score `4.5564` n `82` status `ready` deltaP `24.2431` edge `0.2635` maxDD `-0.6334`
- `market_context_high->commodity_24h` score `4.1186` n `56` status `ready` deltaP `39.8276` edge `0.0777` maxDD `0.0`
- `risk_on_high->commodity_24h` score `4.055` n `31` status `ready` deltaP `39.8276` edge `0.0724` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `4.055` n `31` status `ready` deltaP `39.8276` edge `0.0724` maxDD `0.0`
- `market_context_high->metal_24h` score `2.4048` n `56` status `ready` deltaP `17.0567` edge `0.133` maxDD `-0.7051`
- `risk_on_high->equity_24h` score `2.3317` n `31` status `ready` deltaP `32.5918` edge `0.2609` maxDD `-12.0063`
- `risk_on_and_context->equity_24h` score `2.3317` n `31` status `ready` deltaP `32.5918` edge `0.2609` maxDD `-12.0063`
- `risk_on_high->index_24h` score `2.1517` n `31` status `ready` deltaP `41.7297` edge `0.0502` maxDD `-1.87`
- `risk_on_and_context->index_24h` score `2.1517` n `31` status `ready` deltaP `41.7297` edge `0.0502` maxDD `-1.87`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
