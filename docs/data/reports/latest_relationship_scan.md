# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-12T21:22:26.842262+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `12697`

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

- `risk_on_high->unknown_24h` score `12839.9485` n `30` status `ready` deltaP `15.4514` edge `1069.8927` maxDD `0.0`
- `risk_on_and_context->unknown_24h` score `12839.9485` n `30` status `ready` deltaP `15.4514` edge `1069.8927` maxDD `0.0`
- `market_context_high->unknown_24h` score `12172.196` n `70` status `ready` deltaP `12.5943` edge `1014.2709` maxDD `-0.082`
- `news_risk_high->unknown_1h` score `382.8964` n `82` status `ready` deltaP `-5.6996` edge `31.9882` maxDD `-1.7068`
- `news_risk_high->crypto_major_24h` score `18.7285` n `75` status `ready` deltaP `40.0625` edge `1.4368` maxDD `-8.7873`
- `news_risk_high->crypto_alt_24h` score `17.4522` n `75` status `ready` deltaP `31.5069` edge `1.2931` maxDD `-2.2369`
- `risk_on_high->crypto_alt_24h` score `13.1448` n `30` status `ready` deltaP `33.5069` edge `0.895` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `13.1448` n `30` status `ready` deltaP `33.5069` edge `0.895` maxDD `-0.8386`
- `market_context_high->crypto_alt_24h` score `12.6993` n `70` status `ready` deltaP `27.3165` edge `0.9589` maxDD `-3.9523`
- `risk_on_high->equity_24h` score `10.2822` n `30` status `ready` deltaP `43.4028` edge `0.5675` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `10.2822` n `30` status `ready` deltaP `43.4028` edge `0.5675` maxDD `0.0`
- `market_context_high->equity_24h` score `9.7722` n `70` status `ready` deltaP `43.4028` edge `0.525` maxDD `0.0`
- `news_risk_high->equity_24h` score `7.6283` n `75` status `ready` deltaP `19.4028` edge `0.6321` maxDD `-4.7276`
- `news_risk_high->index_24h` score `6.5377` n `75` status `ready` deltaP `44.7708` edge `0.264` maxDD `-0.0797`
- `news_risk_high->metal_24h` score `5.7269` n `75` status `ready` deltaP `34.4583` edge `0.2919` maxDD `-0.5503`
- `risk_on_high->index_24h` score `5.3919` n `30` status `ready` deltaP `53.4375` edge `0.0973` maxDD `-0.005`
- `risk_on_and_context->index_24h` score `5.3919` n `30` status `ready` deltaP `53.4375` edge `0.0973` maxDD `-0.005`
- `market_context_high->index_24h` score `3.2875` n `70` status `ready` deltaP `35.3422` edge `0.0777` maxDD `-0.1483`
- `market_context_high->commodity_24h` score `2.9989` n `70` status `ready` deltaP `33.2689` edge `0.042` maxDD `-0.1105`
- `risk_on_high->commodity_24h` score `2.4725` n `30` status `ready` deltaP `28.507` edge `0.0253` maxDD `-0.0777`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
