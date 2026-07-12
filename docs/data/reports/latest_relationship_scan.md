# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-12T11:37:28.418276+00:00`
- Price records: `672`
- Market context records: `6493`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5861`

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

- `news_risk_high->crypto_alt_24h` score `12.8143` n `32` status `ready` deltaP `34.6512` edge `0.8516` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `6.4852` n `32` status `ready` deltaP `53.8995` edge `0.1811` maxDD `0.0`
- `market_context_high->unknown_24h` score `6.2155` n `157` status `ready` deltaP `14.9985` edge `0.748` maxDD `-15.0689`
- `news_risk_high->crypto_major_24h` score `4.6166` n `32` status `ready` deltaP `18.4846` edge `0.5466` maxDD `-4.2368`
- `news_risk_high->fx_4h` score `3.9468` n `38` status `ready` deltaP `41.9851` edge `0.0536` maxDD `-0.0345`
- `news_risk_high->commodity_24h` score `2.8168` n `32` status `ready` deltaP `27.3559` edge `0.0729` maxDD `-0.3101`
- `market_context_high->unknown_1h` score `2.7883` n `181` status `ready` deltaP `-4.4909` edge `0.3524` maxDD `-3.2083`
- `news_risk_high->fx_1h` score `1.8485` n `38` status `ready` deltaP `23.1296` edge `0.0179` maxDD `-0.1113`
- `market_context_high->commodity_24h` score `0.7736` n `157` status `ready` deltaP `9.2229` edge `0.1898` maxDD `-5.2791`
- `market_context_high->index_4h` score `0.7029` n `169` status `ready` deltaP `14.5371` edge `0.0293` maxDD `-0.4108`
- `market_context_high->unknown_4h` score `0.6232` n `169` status `ready` deltaP `-14.8946` edge `0.3918` maxDD `-10.5788`
- `market_context_high->crypto_alt_4h` score `0.617` n `169` status `ready` deltaP `10.9031` edge `0.1341` maxDD `-6.7632`
- `news_risk_high->crypto_major_1h` score `0.5989` n `38` status `ready` deltaP `5.4283` edge `0.0943` maxDD `-2.6299`
- `news_risk_high->crypto_alt_1h` score `0.1085` n `38` status `ready` deltaP `1.959` edge `0.0518` maxDD `-2.0756`
- `market_context_high->metal_4h` score `-0.3404` n `169` status `ready` deltaP `9.3675` edge `0.043` maxDD `-2.7056`
- `news_risk_high->index_24h` score `-0.4196` n `32` status `ready` deltaP `5.1235` edge `-0.0008` maxDD `-2.3058`
- `market_context_high->equity_4h` score `-0.439` n `169` status `ready` deltaP `8.656` edge `0.0559` maxDD `-8.2573`
- `market_context_high->fx_1h` score `-0.5103` n `181` status `ready` deltaP `-1.6451` edge `-0.0021` maxDD `-0.8555`
- `market_context_high->commodity_1h` score `-0.5792` n `181` status `ready` deltaP `-0.4873` edge `-0.0027` maxDD `-2.1314`
- `market_context_high->metal_1h` score `-0.6083` n `181` status `ready` deltaP `-0.1693` edge `0.0009` maxDD `-1.8877`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
