# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-26T11:07:32.915677+00:00`
- Price records: `672`
- Market context records: `7978`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11787`

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

- `market_context_high->equity_24h` score `16.1594` n `82` status `ready` deltaP `23.8651` edge `1.3217` maxDD `-6.0681`
- `market_context_high->metal_24h` score `8.0912` n `82` status `ready` deltaP `35.8752` edge `0.4351` maxDD `0.0`
- `market_context_high->equity_4h` score `6.5424` n `96` status `ready` deltaP `25.6775` edge `0.4633` maxDD `-5.1426`
- `market_context_high->commodity_24h` score `3.9584` n `82` status `ready` deltaP `28.4002` edge `0.2938` maxDD `-6.5945`
- `market_context_high->index_4h` score `2.6877` n `96` status `ready` deltaP `27.985` edge `0.0734` maxDD `-0.8791`
- `market_context_high->metal_4h` score `2.5537` n `96` status `ready` deltaP `22.9421` edge `0.1221` maxDD `-0.979`
- `market_context_high->equity_1h` score `1.6752` n `102` status `ready` deltaP `14.1239` edge `0.1272` maxDD `-4.2072`
- `market_context_high->index_24h` score `1.1192` n `82` status `ready` deltaP `8.7018` edge `0.1525` maxDD `-1.3621`
- `market_context_high->crypto_alt_4h` score `1.0687` n `96` status `ready` deltaP `9.1463` edge `0.1398` maxDD `-3.9374`
- `market_context_high->fx_24h` score `1.0537` n `82` status `ready` deltaP `24.2801` edge `0.0347` maxDD `-3.0343`
- `market_context_high->index_1h` score `1.0438` n `102` status `ready` deltaP `16.3037` edge `0.0213` maxDD `-0.7743`
- `market_context_high->crypto_major_4h` score `0.855` n `96` status `ready` deltaP `9.9085` edge `0.177` maxDD `-6.7444`
- `market_context_high->metal_1h` score `0.6896` n `102` status `ready` deltaP `10.0358` edge `0.0284` maxDD `-0.6936`
- `market_context_high->crypto_major_1h` score `0.5694` n `102` status `ready` deltaP `11.0162` edge `0.0406` maxDD `-1.6171`
- `market_context_high->crypto_alt_1h` score `-0.1022` n `102` status `ready` deltaP `-0.3816` edge `0.0327` maxDD `-1.4603`
- `market_context_high->fx_1h` score `-0.2598` n `102` status `ready` deltaP `0.363` edge `0.001` maxDD `-0.2715`
- `market_context_high->fx_4h` score `-0.6373` n `96` status `ready` deltaP `2.7083` edge `0.0036` maxDD `-0.9813`
- `market_context_high->commodity_1h` score `-0.734` n `102` status `ready` deltaP `0.6864` edge `-0.004` maxDD `-1.9395`
- `market_context_high->commodity_4h` score `-0.9591` n `96` status `ready` deltaP `2.2312` edge `0.0084` maxDD `-3.589`
- `market_context_high->unknown_1h` score `-2.0139` n `102` status `ready` deltaP `5.8677` edge `-0.1646` maxDD `-1.054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
