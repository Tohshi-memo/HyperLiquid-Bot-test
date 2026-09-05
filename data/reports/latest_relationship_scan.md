# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-05T19:07:25.226357+00:00`
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

- `risk_on_high->unknown_4h` score `20.2875` n `139` status `ready` deltaP `-2.2822` edge `1.9064` maxDD `-7.7112`
- `risk_on_and_context->unknown_4h` score `20.2875` n `139` status `ready` deltaP `-2.2822` edge `1.9064` maxDD `-7.7112`
- `market_context_high->unknown_4h` score `7.9224` n `228` status `ready` deltaP `1.2329` edge `0.8988` maxDD `-9.4124`
- `news_risk_high->crypto_alt_24h` score `6.9359` n `37` status `ready` deltaP `25.1783` edge `0.4371` maxDD `-0.8236`
- `news_risk_high->commodity_24h` score `3.8035` n `37` status `ready` deltaP `20.1389` edge `0.1827` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `3.3468` n `37` status `ready` deltaP `16.723` edge `0.2087` maxDD `-0.9693`
- `news_risk_high->metal_4h` score `2.3771` n `37` status `ready` deltaP `24.1513` edge `0.0592` maxDD `-0.7692`
- `news_risk_high->commodity_4h` score `1.7377` n `37` status `ready` deltaP `9.5996` edge `0.1009` maxDD `-0.2737`
- `news_risk_high->equity_1h` score `1.5632` n `37` status `ready` deltaP `12.7853` edge `0.0841` maxDD `-0.7924`
- `news_risk_high->metal_1h` score `1.2586` n `37` status `ready` deltaP `15.0146` edge `0.0241` maxDD `-0.2118`
- `news_risk_high->index_1h` score `1.1263` n `37` status `ready` deltaP `14.1245` edge `0.0131` maxDD `-0.0724`
- `news_risk_high->crypto_major_1h` score `1.0815` n `37` status `ready` deltaP `5.717` edge `0.0703` maxDD `-0.4628`
- `news_risk_high->crypto_alt_1h` score `0.9201` n `37` status `ready` deltaP `8.8769` edge `0.044` maxDD `-0.7867`
- `news_risk_high->fx_24h` score `0.7205` n `37` status `ready` deltaP `17.6989` edge `0.0436` maxDD `-3.1244`
- `news_risk_high->crypto_major_24h` score `0.702` n `37` status `ready` deltaP `16.5776` edge `0.2571` maxDD `-18.2098`
- `market_context_high->equity_24h` score `0.5915` n `172` status `ready` deltaP `13.0733` edge `0.3967` maxDD `-20.7654`
- `news_risk_high->crypto_alt_4h` score `0.4543` n `37` status `ready` deltaP `5.1788` edge `0.0362` maxDD `-1.296`
- `risk_on_high->index_1h` score `0.0078` n `145` status `ready` deltaP `7.2466` edge `-0.0026` maxDD `-0.5764`
- `risk_on_and_context->index_1h` score `0.0078` n `145` status `ready` deltaP `7.2466` edge `-0.0026` maxDD `-0.5764`
- `news_risk_high->commodity_1h` score `-0.034` n `37` status `ready` deltaP `5.5754` edge `0.0031` maxDD `-0.9036`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
