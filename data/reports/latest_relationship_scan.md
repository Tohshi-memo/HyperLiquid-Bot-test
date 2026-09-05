# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-05T19:22:25.599390+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10591`

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

- `risk_on_high->unknown_4h` score `20.6303` n `138` status `ready` deltaP `-2.5429` edge `1.9367` maxDD `-7.7112`
- `risk_on_and_context->unknown_4h` score `20.6303` n `138` status `ready` deltaP `-2.5429` edge `1.9367` maxDD `-7.7112`
- `market_context_high->unknown_4h` score `7.9464` n `228` status `ready` deltaP `1.2329` edge `0.9008` maxDD `-9.4124`
- `news_risk_high->crypto_alt_24h` score `6.9119` n `37` status `ready` deltaP `25.1783` edge `0.4351` maxDD `-0.8236`
- `news_risk_high->commodity_24h` score `3.8059` n `37` status `ready` deltaP `20.1389` edge `0.1829` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `3.3288` n `37` status `ready` deltaP `16.723` edge `0.2072` maxDD `-0.9693`
- `news_risk_high->metal_4h` score `2.3771` n `37` status `ready` deltaP `24.1513` edge `0.0592` maxDD `-0.7692`
- `news_risk_high->commodity_4h` score `1.7243` n `37` status `ready` deltaP `9.4471` edge `0.1008` maxDD `-0.2737`
- `news_risk_high->equity_1h` score `1.5775` n `37` status `ready` deltaP `12.935` edge `0.0843` maxDD `-0.7924`
- `news_risk_high->metal_1h` score `1.2706` n `37` status `ready` deltaP `15.1643` edge `0.0241` maxDD `-0.2118`
- `news_risk_high->index_1h` score `1.1263` n `37` status `ready` deltaP `14.1245` edge `0.0131` maxDD `-0.0724`
- `news_risk_high->crypto_major_1h` score `1.0863` n `37` status `ready` deltaP `5.717` edge `0.0707` maxDD `-0.4628`
- `news_risk_high->crypto_alt_1h` score `0.9058` n `37` status `ready` deltaP `8.7272` edge `0.0438` maxDD `-0.7867`
- `news_risk_high->fx_24h` score `0.7367` n `37` status `ready` deltaP `17.8725` edge `0.0438` maxDD `-3.1244`
- `news_risk_high->crypto_major_24h` score `0.6809` n `37` status `ready` deltaP `16.5776` edge `0.2544` maxDD `-18.2098`
- `market_context_high->equity_24h` score `0.6044` n `171` status `ready` deltaP `12.9203` edge `0.3988` maxDD `-20.7654`
- `news_risk_high->crypto_alt_4h` score `0.4277` n `37` status `ready` deltaP `5.0264` edge `0.035` maxDD `-1.296`
- `risk_on_high->index_1h` score `0.0078` n `145` status `ready` deltaP `7.2466` edge `-0.0026` maxDD `-0.5764`
- `risk_on_and_context->index_1h` score `0.0078` n `145` status `ready` deltaP `7.2466` edge `-0.0026` maxDD `-0.5764`
- `news_risk_high->commodity_1h` score `-0.0426` n `37` status `ready` deltaP `5.4257` edge `0.003` maxDD `-0.9036`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
