# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-25T10:51:27.348997+00:00`
- Price records: `672`
- Market context records: `4716`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7424`

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

- `market_context_high->unknown_1h` score `76.9783` n `144` status `ready` deltaP `14.3131` edge `6.3612` maxDD `-1.674`
- `market_context_high->unknown_4h` score `5.0775` n `144` status `ready` deltaP `13.855` edge `0.4518` maxDD `-4.6834`
- `market_context_high->unknown_24h` score `3.0176` n `135` status `ready` deltaP `15.6598` edge `0.2394` maxDD `-4.7201`
- `market_context_high->commodity_1h` score `-0.3014` n `144` status `ready` deltaP `2.4077` edge `0.0249` maxDD `-2.0345`
- `market_context_high->index_4h` score `-0.6752` n `144` status `ready` deltaP `4.4716` edge `-0.0041` maxDD `-5.9823`
- `market_context_high->commodity_4h` score `-0.9188` n `144` status `ready` deltaP `9.1294` edge `0.0321` maxDD `-9.1941`
- `market_context_high->fx_4h` score `-0.9232` n `144` status `ready` deltaP `-1.2026` edge `-0.0021` maxDD `-1.9927`
- `market_context_high->equity_4h` score `-1.0701` n `144` status `ready` deltaP `2.7947` edge `0.0211` maxDD `-8.8203`
- `market_context_high->equity_1h` score `-1.1737` n `144` status `ready` deltaP `-1.7423` edge `0.0125` maxDD `-5.5624`
- `market_context_high->fx_1h` score `-1.2828` n `144` status `ready` deltaP `-4.9859` edge `-0.0057` maxDD `-1.1038`
- `market_context_high->index_1h` score `-1.6169` n `144` status `ready` deltaP `-3.7841` edge `-0.0091` maxDD `-2.6999`
- `market_context_high->crypto_alt_1h` score `-3.1403` n `144` status `ready` deltaP `-0.4907` edge `-0.0706` maxDD `-22.2982`
- `market_context_high->crypto_major_1h` score `-3.653` n `144` status `ready` deltaP `-0.8317` edge `-0.0875` maxDD `-27.356`
- `market_context_high->metal_1h` score `-4.3802` n `144` status `ready` deltaP `-5.0275` edge `-0.0747` maxDD `-17.2107`
- `market_context_high->commodity_24h` score `-4.3955` n `135` status `ready` deltaP `17.1065` edge `0.0701` maxDD `-30.7016`
- `market_context_high->fx_24h` score `-4.8021` n `135` status `ready` deltaP `-13.044` edge `-0.0172` maxDD `-5.3476`
- `market_context_high->crypto_alt_4h` score `-8.0253` n `144` status `ready` deltaP `-2.185` edge `-0.1486` maxDD `-63.9243`
- `market_context_high->index_24h` score `-8.4119` n `135` status `ready` deltaP `-10.6366` edge `-0.0926` maxDD `-29.3321`
- `market_context_high->metal_4h` score `-8.6315` n `144` status `ready` deltaP `3.2012` edge `-0.2426` maxDD `-64.494`
- `market_context_high->crypto_major_4h` score `-10.728` n `144` status `ready` deltaP `-2.4221` edge `-0.2692` maxDD `-81.8692`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
