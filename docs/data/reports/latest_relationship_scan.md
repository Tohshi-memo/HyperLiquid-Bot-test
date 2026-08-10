# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-10T04:07:34.843164+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `10952`

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

- `market_context_high->commodity_4h` score `1.4525` n `164` status `ready` deltaP `16.311` edge `0.0796` maxDD `-2.7169`
- `market_context_high->fx_24h` score `0.8814` n `139` status `ready` deltaP `19.4869` edge `0.0243` maxDD `-1.4613`
- `market_context_high->commodity_1h` score `0.7354` n `173` status `ready` deltaP `9.8828` edge `0.0297` maxDD `-0.7439`
- `market_context_high->fx_4h` score `-0.1166` n `164` status `ready` deltaP `7.0122` edge `0.0065` maxDD `-1.1228`
- `market_context_high->fx_1h` score `-0.1599` n `173` status `ready` deltaP `4.3145` edge `-0.0006` maxDD `-0.8933`
- `market_context_high->index_24h` score `-0.6193` n `139` status `ready` deltaP `2.1507` edge `0.0872` maxDD `-5.9181`
- `market_context_high->index_4h` score `-0.7701` n `164` status `ready` deltaP `-1.6769` edge `-0.0093` maxDD `-1.26`
- `market_context_high->metal_1h` score `-0.8248` n `173` status `ready` deltaP `-4.8215` edge `-0.01` maxDD `-2.0884`
- `market_context_high->equity_1h` score `-0.835` n `173` status `ready` deltaP `-2.1183` edge `-0.0059` maxDD `-4.6286`
- `market_context_high->index_1h` score `-0.8714` n `173` status `ready` deltaP `-3.0459` edge `-0.0046` maxDD `-0.8168`
- `market_context_high->metal_24h` score `-1.4112` n `139` status `ready` deltaP `-3.8507` edge `0.031` maxDD `-2.8346`
- `market_context_high->crypto_alt_1h` score `-1.5324` n `173` status `ready` deltaP `-8.6307` edge `-0.0368` maxDD `-5.5029`
- `market_context_high->equity_24h` score `-1.6086` n `139` status `ready` deltaP `-2.0396` edge `0.1897` maxDD `-21.1456`
- `market_context_high->metal_4h` score `-2.076` n `164` status `ready` deltaP `-8.0792` edge `-0.0359` maxDD `-6.1111`
- `market_context_high->equity_4h` score `-2.7416` n `164` status `ready` deltaP `-8.0792` edge `-0.1014` maxDD `-7.6983`
- `market_context_high->crypto_major_1h` score `-3.5597` n `173` status `ready` deltaP `-9.8785` edge `-0.0574` maxDD `-10.5372`
- `market_context_high->crypto_alt_4h` score `-3.979` n `164` status `ready` deltaP `-11.8902` edge `-0.1551` maxDD `-15.3937`
- `market_context_high->crypto_alt_24h` score `-4.3579` n `139` status `ready` deltaP `-11.2423` edge `-0.1439` maxDD `-4.5445`
- `market_context_high->crypto_major_24h` score `-4.8676` n `139` status `ready` deltaP `-2.6866` edge `-0.1383` maxDD `-14.2873`
- `market_context_high->unknown_1h` score `-7.5164` n `173` status `ready` deltaP `-4.6139` edge `-0.5499` maxDD `-1.323`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
