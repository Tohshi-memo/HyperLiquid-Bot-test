# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-25T23:22:25.244917+00:00`
- Price records: `672`
- Market context records: `7927`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14745`

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

- `market_context_high->equity_24h` score `16.5678` n `82` status `ready` deltaP `25.7749` edge `1.343` maxDD `-6.0681`
- `market_context_high->metal_24h` score `8.3901` n `82` status `ready` deltaP `39.3414` edge `0.4369` maxDD `0.0`
- `market_context_high->equity_4h` score `6.7369` n `91` status `ready` deltaP `24.8681` edge `0.4849` maxDD `-5.1426`
- `market_context_high->commodity_24h` score `3.4251` n `82` status `ready` deltaP `27.3586` edge `0.2563` maxDD `-6.5945`
- `market_context_high->index_4h` score `2.8024` n `91` status `ready` deltaP `28.8336` edge `0.0773` maxDD `-0.8791`
- `market_context_high->metal_4h` score `2.7675` n `91` status `ready` deltaP `24.789` edge `0.1276` maxDD `-0.979`
- `market_context_high->equity_1h` score `1.7577` n `91` status `ready` deltaP `13.4294` edge `0.1387` maxDD `-4.2072`
- `market_context_high->crypto_alt_4h` score `1.367` n `91` status `ready` deltaP `9.8298` edge `0.1601` maxDD `-3.9374`
- `market_context_high->index_24h` score `1.2938` n `82` status `ready` deltaP `10.7851` edge `0.161` maxDD `-1.3621`
- `market_context_high->fx_24h` score `1.2589` n `82` status `ready` deltaP `26.7107` edge `0.0356` maxDD `-3.0343`
- `market_context_high->crypto_major_4h` score `1.1208` n `91` status `ready` deltaP `11.2654` edge `0.1901` maxDD `-6.7444`
- `market_context_high->index_1h` score `1.0468` n `91` status `ready` deltaP `15.9819` edge `0.0237` maxDD `-0.7743`
- `market_context_high->metal_1h` score `0.6288` n `91` status `ready` deltaP `8.8406` edge `0.0313` maxDD `-0.6936`
- `market_context_high->crypto_major_1h` score `0.5782` n `91` status `ready` deltaP `10.739` edge `0.0434` maxDD `-1.6021`
- `market_context_high->crypto_alt_1h` score `0.242` n `91` status `ready` deltaP `4.9928` edge `0.041` maxDD `-1.4603`
- `market_context_high->fx_1h` score `-0.3768` n `91` status `ready` deltaP `0.6039` edge `0.0013` maxDD `-0.2715`
- `market_context_high->commodity_1h` score `-0.3864` n `91` status `ready` deltaP `1.2936` edge `-0.0013` maxDD `-1.5486`
- `market_context_high->commodity_4h` score `-0.503` n `91` status `ready` deltaP `2.7372` edge `0.0163` maxDD `-2.4502`
- `market_context_high->fx_4h` score `-0.5809` n `91` status `ready` deltaP `3.1589` edge `0.0053` maxDD `-0.9813`
- `market_context_high->unknown_1h` score `-1.8312` n `91` status `ready` deltaP `8.3915` edge `-0.1662` maxDD `-1.054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
