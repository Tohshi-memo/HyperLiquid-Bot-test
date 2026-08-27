# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-27T23:22:28.826033+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11831`

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

- `news_risk_high->unknown_24h` score `52.3758` n `50` status `ready` deltaP `11.6319` edge `4.2871` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `23.505` n `50` status `ready` deltaP `37.8403` edge `1.7506` maxDD `-2.8629`
- `news_risk_high->unknown_4h` score `12.6724` n `50` status `ready` deltaP `24.6402` edge `0.9017` maxDD `-0.1279`
- `news_risk_high->metal_24h` score `4.9324` n `50` status `ready` deltaP `46.0903` edge `0.108` maxDD `-0.0053`
- `news_risk_high->equity_24h` score `4.8134` n `50` status `ready` deltaP `27.2292` edge `0.3124` maxDD `-4.7584`
- `news_risk_high->fx_4h` score `3.7921` n `50` status `ready` deltaP `44.2866` edge `0.0298` maxDD `-0.0559`
- `news_risk_high->unknown_1h` score `2.9612` n `50` status `ready` deltaP `16.3772` edge `0.1732` maxDD `-0.8495`
- `market_context_high->unknown_24h` score `2.9514` n `128` status `ready` deltaP `5.3819` edge `0.2833` maxDD `-3.1917`
- `news_risk_high->index_24h` score `2.7722` n `50` status `ready` deltaP `31.2292` edge `0.0379` maxDD `-0.2064`
- `market_context_high->unknown_4h` score `2.2294` n `148` status `ready` deltaP `17.8024` edge `0.1078` maxDD `-0.5894`
- `news_risk_high->fx_1h` score `1.5204` n `50` status `ready` deltaP `20.3533` edge `0.008` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `1.2517` n `50` status `ready` deltaP `17.5629` edge `0.0151` maxDD `-0.2301`
- `news_risk_high->equity_4h` score `1.0222` n `50` status `ready` deltaP `20.0549` edge `0.0278` maxDD `-2.105`
- `market_context_high->unknown_1h` score `0.8377` n `148` status `ready` deltaP `8.6745` edge `0.057` maxDD `-1.6015`
- `news_risk_high->commodity_1h` score `0.5004` n `50` status `ready` deltaP `14.0` edge `0.0021` maxDD `-0.5024`
- `news_risk_high->index_1h` score `0.1374` n `50` status `ready` deltaP `7.6587` edge `0.0005` maxDD `-0.0486`
- `news_risk_high->metal_1h` score `0.0882` n `50` status `ready` deltaP `5.2515` edge `-0.0011` maxDD `-0.1413`
- `news_risk_high->metal_4h` score `-0.0541` n `50` status `ready` deltaP `7.9207` edge `-0.0042` maxDD `-0.249`
- `news_risk_high->index_4h` score `-0.1123` n `50` status `ready` deltaP `4.7988` edge `-0.0017` maxDD `-0.1719`
- `market_context_high->metal_4h` score `-0.4164` n `148` status `ready` deltaP `6.7856` edge `-0.0069` maxDD `-3.3377`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
