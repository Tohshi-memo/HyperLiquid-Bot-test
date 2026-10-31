# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-31T06:22:30.072848+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7609`

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

- `market_context_high->unknown_24h` score `1587.1479` n `134` status `ready` deltaP `-4.8741` edge `132.3378` maxDD `-1.1049`
- `news_risk_high->unknown_1h` score `112.2161` n `98` status `ready` deltaP `-5.0439` edge `9.4136` maxDD `-0.9571`
- `market_context_high->unknown_4h` score `40.617` n `134` status `ready` deltaP `1.9407` edge `3.3851` maxDD `-0.3966`
- `market_context_high->equity_24h` score `8.0915` n `134` status `ready` deltaP `20.1312` edge `0.8158` maxDD `-14.0571`
- `news_risk_high->crypto_alt_4h` score `7.1733` n `92` status `ready` deltaP `23.3629` edge `0.5081` maxDD `-3.6198`
- `market_context_high->index_24h` score `4.0829` n `134` status `ready` deltaP `39.0832` edge `0.098` maxDD `-0.1315`
- `news_risk_high->crypto_alt_1h` score `0.9967` n `98` status `ready` deltaP `8.6948` edge `0.108` maxDD `-3.9659`
- `market_context_high->metal_1h` score `0.386` n `134` status `ready` deltaP `10.9036` edge `0.0147` maxDD `-0.3659`
- `market_context_high->commodity_4h` score `0.3721` n `134` status `ready` deltaP `14.5477` edge `0.0559` maxDD `-1.0837`
- `market_context_high->metal_4h` score `0.3082` n `134` status `ready` deltaP `14.6114` edge `0.0317` maxDD `-1.8344`
- `market_context_high->equity_1h` score `0.1767` n `134` status `ready` deltaP `4.033` edge `0.0754` maxDD `-2.3383`
- `market_context_high->crypto_major_1h` score `-0.0324` n `134` status `ready` deltaP `7.1655` edge `0.0523` maxDD `-5.2213`
- `market_context_high->fx_1h` score `-0.101` n `134` status `ready` deltaP `3.5794` edge `-0.001` maxDD `-0.1986`
- `market_context_high->equity_4h` score `-0.1268` n `134` status `ready` deltaP `0.8668` edge `0.1364` maxDD `-6.008`
- `market_context_high->commodity_1h` score `-0.2074` n `134` status `ready` deltaP `2.8421` edge `0.0152` maxDD `-0.4475`
- `market_context_high->fx_4h` score `-0.4649` n `134` status `ready` deltaP `0.4414` edge `-0.0027` maxDD `-0.4545`
- `market_context_high->metal_24h` score `-0.5384` n `134` status `ready` deltaP `3.9257` edge `0.1695` maxDD `-10.5088`
- `market_context_high->index_1h` score `-0.7564` n `134` status `ready` deltaP `-1.1976` edge `0.0008` maxDD `-1.1344`
- `news_risk_high->index_1h` score `-0.8562` n `98` status `ready` deltaP `1.8636` edge `-0.0038` maxDD `-1.3981`
- `news_risk_high->fx_1h` score `-0.8953` n `98` status `ready` deltaP `-6.0002` edge `-0.0047` maxDD `-0.6065`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
