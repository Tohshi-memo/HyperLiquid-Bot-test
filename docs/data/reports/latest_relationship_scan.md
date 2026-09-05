# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-05T13:07:27.183441+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11019`

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

- `risk_on_high->unknown_4h` score `22.6615` n `140` status `ready` deltaP `5.3833` edge `1.9144` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `22.6615` n `140` status `ready` deltaP `5.3833` edge `1.9144` maxDD `-2.2797`
- `market_context_high->unknown_4h` score `10.7271` n `228` status `ready` deltaP `6.0976` edge `0.9263` maxDD `-2.8419`
- `news_risk_high->crypto_alt_24h` score `7.4819` n `37` status `ready` deltaP `25.1783` edge `0.4826` maxDD `-0.8236`
- `news_risk_high->commodity_24h` score `3.942` n `37` status `ready` deltaP `21.1806` edge `0.1873` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `3.6558` n `37` status `ready` deltaP `17.1803` edge `0.2314` maxDD `-0.9693`
- `news_risk_high->metal_4h` score `2.2846` n `37` status `ready` deltaP `23.0842` edge `0.0586` maxDD `-0.7692`
- `news_risk_high->commodity_4h` score `1.9544` n `37` status `ready` deltaP `12.0386` edge `0.1027` maxDD `-0.2737`
- `news_risk_high->equity_1h` score `1.5847` n `37` status `ready` deltaP `13.0847` edge `0.0839` maxDD `-0.7924`
- `news_risk_high->metal_1h` score `1.2334` n `37` status `ready` deltaP `14.7152` edge `0.024` maxDD `-0.2118`
- `news_risk_high->crypto_major_1h` score `1.1643` n `37` status `ready` deltaP `6.1661` edge `0.0742` maxDD `-0.4628`
- `news_risk_high->index_1h` score `1.1251` n `37` status `ready` deltaP `14.1245` edge `0.013` maxDD `-0.0724`
- `news_risk_high->crypto_major_24h` score `1.0288` n `37` status `ready` deltaP `16.5776` edge `0.299` maxDD `-18.2098`
- `news_risk_high->crypto_alt_1h` score `0.9045` n `37` status `ready` deltaP `8.8769` edge `0.0427` maxDD `-0.7867`
- `news_risk_high->crypto_alt_4h` score `0.6323` n `37` status `ready` deltaP `6.3983` edge `0.0429` maxDD `-1.296`
- `news_risk_high->fx_24h` score `0.5025` n `37` status `ready` deltaP `15.0947` edge `0.0428` maxDD `-3.1244`
- `market_context_high->equity_24h` score `0.2694` n `191` status `ready` deltaP `15.6759` edge `0.3646` maxDD `-20.7654`
- `risk_on_high->crypto_major_24h` score `0.1957` n `119` status `ready` deltaP `20.1433` edge `0.7652` maxDD `-56.9519`
- `risk_on_and_context->crypto_major_24h` score `0.1957` n `119` status `ready` deltaP `20.1433` edge `0.7652` maxDD `-56.9519`
- `risk_on_high->metal_1h` score `0.0275` n `152` status `ready` deltaP `11.0345` edge `0.0012` maxDD `-1.699`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
