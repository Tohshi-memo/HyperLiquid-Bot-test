# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-10T04:37:37.228302+00:00`
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

- `market_context_high->commodity_4h` score `1.3792` n `166` status `ready` deltaP `15.5745` edge `0.0784` maxDD `-2.7169`
- `market_context_high->fx_24h` score `0.8616` n `140` status `ready` deltaP `19.3453` edge `0.0236` maxDD `-1.4613`
- `market_context_high->commodity_1h` score `0.7342` n `173` status `ready` deltaP `9.8828` edge `0.0296` maxDD `-0.7439`
- `market_context_high->fx_4h` score `-0.1104` n `166` status `ready` deltaP `7.2068` edge `0.006` maxDD `-1.1228`
- `market_context_high->fx_1h` score `-0.1521` n `173` status `ready` deltaP `4.4642` edge `-0.0006` maxDD `-0.8933`
- `market_context_high->index_24h` score `-0.614` n `140` status `ready` deltaP `2.3512` edge `0.0863` maxDD `-5.9181`
- `market_context_high->index_4h` score `-0.7577` n `166` status `ready` deltaP `-1.4381` edge `-0.0093` maxDD `-1.26`
- `market_context_high->equity_1h` score `-0.8241` n `173` status `ready` deltaP `-1.9686` edge `-0.0055` maxDD `-4.6286`
- `market_context_high->metal_1h` score `-0.842` n `173` status `ready` deltaP `-5.1209` edge `-0.0102` maxDD `-2.0884`
- `market_context_high->index_1h` score `-0.845` n `173` status `ready` deltaP `-2.7465` edge `-0.0044` maxDD `-0.8168`
- `market_context_high->crypto_alt_1h` score `-1.5409` n `173` status `ready` deltaP `-8.7804` edge `-0.0369` maxDD `-5.5029`
- `market_context_high->metal_24h` score `-1.5619` n `140` status `ready` deltaP `-4.38` edge `0.0272` maxDD `-2.9193`
- `market_context_high->equity_24h` score `-1.6996` n `140` status `ready` deltaP `-2.2371` edge `0.1876` maxDD `-21.1456`
- `market_context_high->metal_4h` score `-2.0624` n `166` status `ready` deltaP `-7.8184` edge `-0.0359` maxDD `-6.1111`
- `market_context_high->equity_4h` score `-2.8365` n `166` status `ready` deltaP `-8.3989` edge `-0.1031` maxDD `-7.6983`
- `market_context_high->crypto_major_1h` score `-3.5573` n `173` status `ready` deltaP `-9.8785` edge `-0.0572` maxDD `-10.5372`
- `market_context_high->crypto_alt_4h` score `-3.9596` n `166` status `ready` deltaP `-11.5486` edge `-0.1549` maxDD `-15.3937`
- `market_context_high->crypto_alt_24h` score `-4.3486` n `140` status `ready` deltaP `-11.0367` edge `-0.1445` maxDD `-4.5445`
- `market_context_high->crypto_major_24h` score `-4.9267` n `140` status `ready` deltaP `-3.1696` edge `-0.14` maxDD `-14.2873`
- `market_context_high->unknown_1h` score `-7.5487` n `173` status `ready` deltaP `-4.7636` edge `-0.5516` maxDD `-1.323`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
