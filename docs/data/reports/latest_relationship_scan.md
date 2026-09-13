# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-13T14:37:28.734399+00:00`
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

- `market_context_high->unknown_24h` score `17950.4465` n `56` status `ready` deltaP `8.596` edge `1495.8334` maxDD `-0.613`
- `risk_on_high->unknown_24h` score `12818.1919` n `30` status `ready` deltaP `12.6436` edge `1068.1041` maxDD `-0.1252`
- `risk_on_and_context->unknown_24h` score `12818.1919` n `30` status `ready` deltaP `12.6436` edge `1068.1041` maxDD `-0.1252`
- `news_risk_high->unknown_1h` score `419.2191` n `82` status `ready` deltaP `-4.8014` edge `35.0091` maxDD `-1.7068`
- `news_risk_high->crypto_major_24h` score `18.2716` n `82` status `ready` deltaP `38.0236` edge `1.4162` maxDD `-9.098`
- `news_risk_high->crypto_alt_24h` score `18.2545` n `82` status `ready` deltaP `34.6509` edge `1.339` maxDD `-2.2369`
- `risk_on_high->crypto_alt_24h` score `9.1121` n `30` status `ready` deltaP `25.0574` edge `0.6377` maxDD `-1.9661`
- `risk_on_and_context->crypto_alt_24h` score `9.1121` n `30` status `ready` deltaP `25.0574` edge `0.6377` maxDD `-1.9661`
- `news_risk_high->equity_24h` score `8.4444` n `82` status `ready` deltaP `24.5122` edge `0.7183` maxDD `-6.5742`
- `news_risk_high->index_24h` score `6.796` n `82` status `ready` deltaP `48.2842` edge `0.2621` maxDD `-0.0797`
- `market_context_high->crypto_alt_24h` score `5.6683` n `56` status `ready` deltaP `19.5812` edge `0.6866` maxDD `-4.5683`
- `news_risk_high->metal_24h` score `4.5564` n `82` status `ready` deltaP `24.2431` edge `0.2635` maxDD `-0.6334`
- `market_context_high->commodity_24h` score `4.1138` n `56` status `ready` deltaP `39.8276` edge `0.0773` maxDD `0.0`
- `risk_on_high->commodity_24h` score `4.0478` n `30` status `ready` deltaP `39.8276` edge `0.0718` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `4.0478` n `30` status `ready` deltaP `39.8276` edge `0.0718` maxDD `0.0`
- `risk_on_high->equity_24h` score `3.0196` n `30` status `ready` deltaP `35.0` edge `0.309` maxDD `-10.4165`
- `risk_on_and_context->equity_24h` score `3.0196` n `30` status `ready` deltaP `35.0` edge `0.309` maxDD `-10.4165`
- `market_context_high->metal_24h` score `2.4625` n `56` status `ready` deltaP `17.0567` edge `0.1327` maxDD `-0.6293`
- `risk_on_high->index_24h` score `2.3968` n `30` status `ready` deltaP `44.1379` edge `0.0582` maxDD `-1.6138`
- `risk_on_and_context->index_24h` score `2.3968` n `30` status `ready` deltaP `44.1379` edge `0.0582` maxDD `-1.6138`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
