# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-11T01:22:23.941461+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11744`

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

- `market_context_high->fx_24h` score `1.1121` n `145` status `ready` deltaP `20.4064` edge `0.0374` maxDD `-1.4613`
- `market_context_high->commodity_4h` score `0.9545` n `168` status `ready` deltaP `12.4201` edge `0.0682` maxDD `-2.7169`
- `market_context_high->commodity_1h` score `0.6429` n `180` status `ready` deltaP `8.9055` edge `0.0285` maxDD `-0.7439`
- `market_context_high->fx_4h` score `-0.0675` n `168` status `ready` deltaP `6.6928` edge `0.0067` maxDD `-0.4647`
- `market_context_high->fx_1h` score `-0.1215` n `180` status `ready` deltaP `4.5276` edge `-0.0006` maxDD `-0.613`
- `market_context_high->metal_1h` score `-1.2924` n `180` status `ready` deltaP `-5.2195` edge `-0.0093` maxDD `-2.0884`
- `market_context_high->index_1h` score `-1.3338` n `180` status `ready` deltaP `-7.0758` edge `-0.0052` maxDD `-1.0359`
- `market_context_high->equity_1h` score `-1.4598` n `180` status `ready` deltaP `-6.0545` edge `-0.0191` maxDD `-6.8818`
- `market_context_high->unknown_24h` score `-1.5887` n `145` status `ready` deltaP `-14.5772` edge `0.2102` maxDD `-9.6329`
- `market_context_high->metal_24h` score `-1.6002` n `145` status `ready` deltaP `2.5482` edge `-0.0179` maxDD `-2.9283`
- `market_context_high->index_24h` score `-1.9143` n `145` status `ready` deltaP `-8.0751` edge `0.0137` maxDD `-6.7563`
- `market_context_high->index_4h` score `-1.9734` n `168` status `ready` deltaP `-8.1446` edge `-0.0197` maxDD `-1.5693`
- `market_context_high->crypto_alt_1h` score `-2.7243` n `180` status `ready` deltaP `-9.9201` edge `-0.0423` maxDD `-6.4874`
- `market_context_high->metal_4h` score `-3.2886` n `168` status `ready` deltaP `-8.5439` edge `-0.0407` maxDD `-6.1111`
- `market_context_high->commodity_24h` score `-3.426` n `145` status `ready` deltaP `5.7109` edge `0.0381` maxDD `-30.5656`
- `market_context_high->crypto_major_1h` score `-3.8288` n `180` status `ready` deltaP `-10.642` edge `-0.0577` maxDD `-11.9002`
- `market_context_high->equity_4h` score `-4.6043` n `168` status `ready` deltaP `-17.6829` edge `-0.1615` maxDD `-15.8728`
- `market_context_high->crypto_major_24h` score `-6.0313` n `145` status `ready` deltaP `-10.6604` edge `-0.1702` maxDD `-31.2243`
- `market_context_high->crypto_alt_4h` score `-7.0963` n `168` status `ready` deltaP `-14.8882` edge `-0.1573` maxDD `-20.1177`
- `market_context_high->equity_24h` score `-8.1965` n `145` status `ready` deltaP `-7.9197` edge `-0.2085` maxDD `-49.4962`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
