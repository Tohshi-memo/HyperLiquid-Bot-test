# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-10T05:37:29.368648+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9978`

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

- `risk_on_high->crypto_alt_24h` score `13.6904` n `96` status `ready` deltaP `30.382` edge `0.9613` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `13.6904` n `96` status `ready` deltaP `30.382` edge `0.9613` maxDD `-0.8386`
- `market_context_high->crypto_alt_24h` score `9.8149` n `218` status `ready` deltaP `22.7463` edge `0.749` maxDD `-3.9523`
- `risk_on_high->crypto_alt_4h` score `7.2354` n `96` status `ready` deltaP `37.3222` edge `0.3913` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `7.2354` n `96` status `ready` deltaP `37.3222` edge `0.3913` maxDD `-1.9733`
- `risk_on_high->crypto_major_4h` score `5.1059` n `96` status `ready` deltaP `25.8384` edge `0.3391` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `5.1059` n `96` status `ready` deltaP `25.8384` edge `0.3391` maxDD `-3.8693`
- `risk_on_high->crypto_major_24h` score `4.6761` n `96` status `ready` deltaP `20.8333` edge `0.8674` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `4.6761` n `96` status `ready` deltaP `20.8333` edge `0.8674` maxDD `-24.5429`
- `risk_on_high->index_24h` score `2.9177` n `96` status `ready` deltaP `31.0764` edge `0.0402` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `2.9177` n `96` status `ready` deltaP `31.0764` edge `0.0402` maxDD `-0.0051`
- `market_context_high->equity_24h` score `2.6579` n `218` status `ready` deltaP `15.1042` edge `0.1208` maxDD `0.0`
- `market_context_high->index_24h` score `2.3653` n `218` status `ready` deltaP `25.9445` edge `0.0635` maxDD `-0.1483`
- `risk_on_high->commodity_24h` score `1.4045` n `96` status `ready` deltaP `14.2361` edge `0.0408` maxDD `-0.16`
- `risk_on_and_context->commodity_24h` score `1.4045` n `96` status `ready` deltaP `14.2361` edge `0.0408` maxDD `-0.16`
- `risk_on_high->crypto_alt_1h` score `1.1758` n `96` status `ready` deltaP `5.1772` edge `0.0987` maxDD `-1.1521`
- `risk_on_and_context->crypto_alt_1h` score `1.1758` n `96` status `ready` deltaP `5.1772` edge `0.0987` maxDD `-1.1521`
- `risk_on_high->equity_4h` score `1.1517` n `96` status `ready` deltaP `21.9258` edge `-0.0161` maxDD `-1.0611`
- `risk_on_and_context->equity_4h` score `1.1517` n `96` status `ready` deltaP `21.9258` edge `-0.0161` maxDD `-1.0611`
- `risk_on_high->equity_1h` score `1.0132` n `96` status `ready` deltaP `16.4671` edge `0.0025` maxDD `-0.228`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
