# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-06T04:22:29.614290+00:00`
- Price records: `672`
- Market context records: `5844`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `10128`

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

- `news_risk_high->fx_1h` score `1.9507` n `30` status `ready` deltaP `23.6327` edge `0.0189` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `0.8012` n `30` status `ready` deltaP `11.0878` edge `0.0755` maxDD `-2.0691`
- `market_context_high->equity_4h` score `0.756` n `260` status `ready` deltaP `7.8565` edge `0.1564` maxDD `-6.9958`
- `news_risk_high->crypto_alt_1h` score `0.1632` n `30` status `ready` deltaP `4.5709` edge `0.0366` maxDD `-1.6923`
- `market_context_high->fx_1h` score `-0.3246` n `260` status `ready` deltaP `1.0686` edge `-0.0002` maxDD `-0.5499`
- `market_context_high->equity_1h` score `-0.3405` n `260` status `ready` deltaP `4.7582` edge `0.0406` maxDD `-5.0555`
- `news_risk_high->metal_1h` score `-0.4281` n `30` status `ready` deltaP `1.3872` edge `-0.0275` maxDD `-1.2643`
- `market_context_high->metal_1h` score `-0.4784` n `260` status `ready` deltaP `3.4385` edge `0.0043` maxDD `-2.0339`
- `market_context_high->commodity_1h` score `-0.511` n `260` status `ready` deltaP `-0.6172` edge `-0.0013` maxDD `-2.1412`
- `market_context_high->equity_24h` score `-0.6864` n `232` status `ready` deltaP `16.5888` edge `0.3401` maxDD `-31.6316`
- `market_context_high->crypto_major_1h` score `-0.7897` n `260` status `ready` deltaP `3.5237` edge `0.0428` maxDD `-6.2348`
- `market_context_high->index_1h` score `-0.828` n `260` status `ready` deltaP `1.451` edge `0.0061` maxDD `-0.7819`
- `market_context_high->crypto_alt_1h` score `-0.9926` n `260` status `ready` deltaP `2.135` edge `0.0365` maxDD `-6.6758`
- `market_context_high->index_4h` score `-1.1747` n `260` status `ready` deltaP `0.5136` edge `0.0147` maxDD `-3.165`
- `news_risk_high->index_1h` score `-1.2354` n `30` status `ready` deltaP `-12.3952` edge `-0.0243` maxDD `-1.1161`
- `market_context_high->fx_4h` score `-1.7118` n `260` status `ready` deltaP `-3.3678` edge `-0.0021` maxDD `-2.2593`
- `market_context_high->fx_24h` score `-1.7516` n `232` status `ready` deltaP `5.8549` edge `0.0182` maxDD `-5.5435`
- `market_context_high->metal_4h` score `-2.0981` n `260` status `ready` deltaP `-4.2472` edge `-0.0403` maxDD `-8.6964`
- `market_context_high->commodity_4h` score `-2.3235` n `260` status `ready` deltaP `-0.0258` edge `-0.0128` maxDD `-7.1188`
- `market_context_high->crypto_major_4h` score `-2.8696` n `260` status `ready` deltaP `7.2913` edge `0.1495` maxDD `-25.6458`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
