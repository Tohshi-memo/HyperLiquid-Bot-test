# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-11T10:07:25.667189+00:00`
- Price records: `672`
- Market context records: `6380`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11072`

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

- `news_risk_high->crypto_alt_24h` score `14.1793` n `32` status `ready` deltaP `37.6736` edge `0.9452` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `6.3546` n `32` status `ready` deltaP `52.7778` edge `0.1777` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `4.2942` n `32` status `ready` deltaP `17.5347` edge `0.5116` maxDD `-4.2368`
- `news_risk_high->commodity_24h` score `4.1965` n `32` status `ready` deltaP `36.4583` edge `0.1272` maxDD `-0.3101`
- `news_risk_high->fx_4h` score `3.923` n `32` status `ready` deltaP `40.4726` edge `0.0617` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.3727` n `32` status `ready` deltaP `28.5928` edge `0.021` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `1.5068` n `32` status `ready` deltaP `14.5771` edge `0.1427` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.859` n `32` status `ready` deltaP `10.7223` edge `0.0848` maxDD `-1.6923`
- `market_context_high->metal_4h` score `0.4788` n `220` status `ready` deltaP `14.9612` edge `0.0413` maxDD `-2.7056`
- `market_context_high->unknown_1h` score `0.2355` n `226` status `ready` deltaP `-5.4992` edge `0.1571` maxDD `-3.7317`
- `market_context_high->index_4h` score `0.1812` n `220` status `ready` deltaP `9.1852` edge `0.0215` maxDD `-0.4108`
- `news_risk_high->unknown_1h` score `-0.2669` n `32` status `ready` deltaP `6.5307` edge `-0.0313` maxDD `-0.7581`
- `market_context_high->metal_24h` score `-0.2904` n `144` status `ready` deltaP `19.0973` edge `0.0923` maxDD `-11.8809`
- `market_context_high->metal_1h` score `-0.3941` n `226` status `ready` deltaP `3.6498` edge `0.0029` maxDD `-1.8877`
- `market_context_high->index_1h` score `-0.6328` n `226` status `ready` deltaP `-1.7964` edge `0.0028` maxDD `-0.7564`
- `market_context_high->fx_1h` score `-0.6898` n `226` status `ready` deltaP `-0.3895` edge `-0.0015` maxDD `-0.9376`
- `news_risk_high->metal_1h` score `-0.7169` n `32` status `ready` deltaP `-2.5449` edge `-0.0252` maxDD `-1.6464`
- `news_risk_high->index_24h` score `-0.7331` n `32` status `ready` deltaP `0.5208` edge `-0.0103` maxDD `-2.3058`
- `market_context_high->commodity_24h` score `-0.8037` n `144` status `ready` deltaP `-5.5556` edge `0.1204` maxDD `-6.2457`
- `market_context_high->equity_4h` score `-0.8597` n `220` status `ready` deltaP `7.2506` edge `0.0499` maxDD `-8.2573`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
