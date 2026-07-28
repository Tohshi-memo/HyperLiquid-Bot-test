# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-28T06:07:36.554825+00:00`
- Price records: `672`
- Market context records: `8168`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11778`

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

- `news_risk_high->unknown_24h` score `8404.4086` n `37` status `ready` deltaP `37.1528` edge `700.1197` maxDD `0.0`
- `market_context_high->equity_24h` score `18.8507` n `62` status `ready` deltaP `44.3885` edge `1.366` maxDD `-4.9489`
- `market_context_high->equity_4h` score `9.3292` n `63` status `ready` deltaP `38.1001` edge `0.5469` maxDD `-0.5442`
- `news_risk_high->equity_4h` score `9.1207` n `43` status `ready` deltaP `34.4087` edge `0.5512` maxDD `-0.6428`
- `market_context_high->metal_24h` score `8.141` n `62` status `ready` deltaP `41.4931` edge `0.4018` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `5.5233` n `43` status `ready` deltaP `20.6431` edge `0.3832` maxDD `-2.1767`
- `market_context_high->index_4h` score `4.0355` n `63` status `ready` deltaP `36.791` edge `0.0953` maxDD `-0.0092`
- `market_context_high->equity_1h` score `3.6113` n `63` status `ready` deltaP `21.4595` edge `0.1782` maxDD `-0.6254`
- `news_risk_high->equity_1h` score `3.4255` n `47` status `ready` deltaP `25.5797` edge `0.1458` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.927` n `43` status `ready` deltaP `24.5355` edge `0.0994` maxDD `-0.191`
- `market_context_high->index_1h` score `1.8914` n `63` status `ready` deltaP `21.8777` edge `0.0256` maxDD `-0.1069`
- `market_context_high->index_24h` score `1.8806` n `62` status `ready` deltaP `18.6044` edge `0.1841` maxDD `-1.3621`
- `news_risk_high->metal_4h` score `1.8188` n `43` status `ready` deltaP `16.7186` edge `0.0869` maxDD `-0.7433`
- `market_context_high->metal_4h` score `1.7479` n `63` status `ready` deltaP `21.5544` edge `0.0642` maxDD `-0.979`
- `market_context_high->fx_24h` score `1.553` n `62` status `ready` deltaP `21.9254` edge `0.0536` maxDD `-0.6283`
- `news_risk_high->crypto_major_1h` score `1.5263` n `47` status `ready` deltaP `8.6125` edge `0.1095` maxDD `-1.1783`
- `news_risk_high->crypto_alt_1h` score `1.272` n `47` status `ready` deltaP `9.5107` edge `0.086` maxDD `-1.1388`
- `news_risk_high->crypto_alt_4h` score `1.1777` n `43` status `ready` deltaP `12.8651` edge `0.2044` maxDD `-5.8012`
- `market_context_high->commodity_24h` score `1.1004` n `62` status `ready` deltaP `28.2314` edge `0.2414` maxDD `-15.7497`
- `market_context_high->crypto_major_1h` score `0.7182` n `63` status `ready` deltaP `8.849` edge `0.0419` maxDD `-1.6171`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
