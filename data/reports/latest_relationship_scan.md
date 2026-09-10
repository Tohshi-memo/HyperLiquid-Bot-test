# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-10T04:37:32.900022+00:00`
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

- `risk_on_high->crypto_alt_24h` score `13.6179` n `100` status `ready` deltaP `29.8958` edge `0.9585` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `13.6179` n `100` status `ready` deltaP `29.8958` edge `0.9585` maxDD `-0.8386`
- `market_context_high->crypto_alt_24h` score `9.5354` n `222` status `ready` deltaP `22.2832` edge `0.7288` maxDD `-3.9523`
- `risk_on_high->crypto_alt_4h` score `7.2194` n `100` status `ready` deltaP `37.378` edge `0.3896` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `7.2194` n `100` status `ready` deltaP `37.378` edge `0.3896` maxDD `-1.9733`
- `risk_on_high->crypto_major_24h` score `5.3831` n `100` status `ready` deltaP `21.5139` edge `0.9535` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `5.3831` n `100` status `ready` deltaP `21.5139` edge `0.9535` maxDD `-24.5429`
- `risk_on_high->crypto_major_4h` score `5.1253` n `100` status `ready` deltaP `26.561` edge `0.3359` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `5.1253` n `100` status `ready` deltaP `26.561` edge `0.3359` maxDD `-3.8693`
- `risk_on_high->index_24h` score `2.967` n `100` status `ready` deltaP `30.5069` edge `0.0481` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `2.967` n `100` status `ready` deltaP `30.5069` edge `0.0481` maxDD `-0.0051`
- `market_context_high->equity_24h` score `2.6504` n `222` status `ready` deltaP `14.4097` edge `0.1248` maxDD `0.0`
- `market_context_high->index_24h` score `2.3373` n `222` status `ready` deltaP `25.3988` edge `0.0648` maxDD `-0.1483`
- `risk_on_high->crypto_alt_1h` score `1.1352` n `100` status `ready` deltaP `4.6108` edge `0.0991` maxDD `-1.1521`
- `risk_on_and_context->crypto_alt_1h` score `1.1352` n `100` status `ready` deltaP `4.6108` edge `0.0991` maxDD `-1.1521`
- `risk_on_high->equity_24h` score `1.1228` n `100` status `ready` deltaP `14.4097` edge `-0.0025` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `1.1228` n `100` status `ready` deltaP `14.4097` edge `-0.0025` maxDD `0.0`
- `risk_on_high->equity_4h` score `1.0636` n `100` status `ready` deltaP `20.689` edge `-0.0152` maxDD `-1.0611`
- `risk_on_and_context->equity_4h` score `1.0636` n `100` status `ready` deltaP `20.689` edge `-0.0152` maxDD `-1.0611`
- `risk_on_high->commodity_24h` score `1.0458` n `100` status `ready` deltaP `11.2569` edge `0.0342` maxDD `-0.4346`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
