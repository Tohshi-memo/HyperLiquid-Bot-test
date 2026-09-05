# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-05T08:52:27.814411+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10935`

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

- `risk_on_high->unknown_4h` score `21.367` n `140` status `ready` deltaP `8.297` edge `1.7871` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `21.367` n `140` status `ready` deltaP `8.297` edge `1.7871` maxDD `-2.2797`
- `market_context_high->unknown_4h` score `10.182` n `228` status `ready` deltaP `8.673` edge `0.8637` maxDD `-2.8419`
- `news_risk_high->crypto_alt_24h` score `7.3223` n `37` status `ready` deltaP `25.1783` edge `0.4693` maxDD `-0.8236`
- `news_risk_high->commodity_24h` score `4.243` n `37` status `ready` deltaP `24.1319` edge `0.1927` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `3.6822` n `37` status `ready` deltaP `17.1803` edge `0.2336` maxDD `-0.9693`
- `news_risk_high->metal_4h` score `2.114` n `37` status `ready` deltaP `21.1025` edge `0.0576` maxDD `-0.7692`
- `news_risk_high->commodity_4h` score `1.9324` n `37` status `ready` deltaP `11.7337` edge `0.1029` maxDD `-0.2737`
- `news_risk_high->equity_1h` score `1.653` n `37` status `ready` deltaP `13.8332` edge `0.0846` maxDD `-0.7924`
- `news_risk_high->crypto_major_1h` score `1.2278` n `37` status `ready` deltaP `6.6152` edge `0.0765` maxDD `-0.4628`
- `news_risk_high->index_1h` score `1.2006` n `37` status `ready` deltaP `15.0227` edge `0.0133` maxDD `-0.0724`
- `news_risk_high->metal_1h` score `1.1963` n `37` status `ready` deltaP `14.2661` edge `0.0239` maxDD `-0.2118`
- `news_risk_high->crypto_alt_1h` score `0.8938` n `37` status `ready` deltaP `8.5775` edge `0.0438` maxDD `-0.7867`
- `news_risk_high->crypto_alt_4h` score `0.5759` n `37` status `ready` deltaP `6.3983` edge `0.0382` maxDD `-1.296`
- `news_risk_high->crypto_major_24h` score `0.5061` n `37` status `ready` deltaP `14.147` edge `0.2482` maxDD `-18.2098`
- `news_risk_high->fx_24h` score `0.286` n `37` status `ready` deltaP `12.8378` edge `0.0398` maxDD `-3.1244`
- `risk_on_high->metal_1h` score `0.0972` n `151` status `ready` deltaP `12.3151` edge `0.0016` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `0.0972` n `151` status `ready` deltaP `12.3151` edge `0.0016` maxDD `-1.699`
- `news_risk_high->commodity_1h` score `0.0018` n `37` status `ready` deltaP `6.1742` edge `0.0037` maxDD `-0.9036`
- `market_context_high->equity_24h` score `-0.0331` n `192` status `ready` deltaP `15.7986` edge `0.325` maxDD `-20.7654`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
