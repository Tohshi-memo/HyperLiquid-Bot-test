# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-19T19:22:36.114501+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8502`

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

- `news_risk_high->crypto_major_24h` score `51.2586` n `72` status `ready` deltaP `27.9513` edge `4.1744` maxDD `-5.8019`
- `market_context_high->unknown_4h` score `48.4428` n `121` status `ready` deltaP `-3.4909` edge `4.0835` maxDD `-0.5326`
- `news_risk_high->crypto_alt_24h` score `44.7951` n `72` status `ready` deltaP `33.6806` edge `3.6463` maxDD `-9.3661`
- `risk_on_high->unknown_4h` score `32.0158` n `31` status `ready` deltaP `-17.7272` edge `2.8087` maxDD `-0.4694`
- `risk_on_and_context->unknown_4h` score `32.0158` n `31` status `ready` deltaP `-17.7272` edge `2.8087` maxDD `-0.4694`
- `risk_on_high->commodity_24h` score `9.9952` n `31` status `ready` deltaP `48.7847` edge `0.5077` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `9.9952` n `31` status `ready` deltaP `48.7847` edge `0.5077` maxDD `0.0`
- `news_risk_high->equity_24h` score `9.0032` n `72` status `ready` deltaP `37.5` edge `0.5045` maxDD `-0.0053`
- `market_context_high->commodity_24h` score `7.7666` n `121` status `ready` deltaP `40.5202` edge `0.4296` maxDD `-0.8682`
- `news_risk_high->crypto_alt_4h` score `5.603` n `98` status `ready` deltaP `21.0085` edge `0.4478` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `4.2421` n `98` status `ready` deltaP `21.3134` edge `0.3372` maxDD `-8.0625`
- `news_risk_high->crypto_alt_1h` score `3.276` n `98` status `ready` deltaP `18.9234` edge `0.1934` maxDD `-2.058`
- `market_context_high->commodity_4h` score `2.6387` n `121` status `ready` deltaP `27.4051` edge `0.079` maxDD `-0.345`
- `news_risk_high->crypto_major_1h` score `2.3659` n `98` status `ready` deltaP `19.6719` edge `0.1183` maxDD `-2.8494`
- `risk_on_high->commodity_4h` score `2.2987` n `31` status `ready` deltaP `25.5655` edge `0.0561` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.2987` n `31` status `ready` deltaP `25.5655` edge `0.0561` maxDD `-0.1313`
- `news_risk_high->metal_24h` score `1.7285` n `72` status `ready` deltaP `22.5694` edge `0.078` maxDD `-2.4203`
- `market_context_high->commodity_1h` score `1.4486` n `121` status `ready` deltaP `18.0024` edge `0.0259` maxDD `-0.3491`
- `news_risk_high->metal_4h` score `0.849` n `98` status `ready` deltaP `19.4344` edge `0.0466` maxDD `-2.0994`
- `risk_on_high->commodity_1h` score `0.8085` n `31` status `ready` deltaP `15.4964` edge `0.0189` maxDD `-0.1507`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
