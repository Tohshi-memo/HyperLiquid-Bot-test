# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-24T20:07:24.498116+00:00`
- Price records: `672`
- Market context records: `1771`
- Flow alert records: `6998`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8872`

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

- `market_context_high->metal_24h` score `7.1602` n `178` status `ready` deltaP `28.4079` edge `0.6499` maxDD `-12.7414`
- `market_context_high->crypto_alt_4h` score `6.162` n `194` status `ready` deltaP `21.7076` edge `0.5454` maxDD `-9.1295`
- `news_risk_high->commodity_4h` score `5.8434` n `30` status `ready` deltaP `27.124` edge `0.3716` maxDD `-3.5713`
- `market_context_high->crypto_major_4h` score `4.7248` n `194` status `ready` deltaP `22.935` edge `0.4814` maxDD `-10.9117`
- `market_context_high->index_24h` score `3.7603` n `178` status `ready` deltaP `18.6447` edge `0.3119` maxDD `-4.1604`
- `market_context_high->equity_4h` score `3.2227` n `194` status `ready` deltaP `17.2366` edge `0.2631` maxDD `-5.0894`
- `market_context_high->unknown_4h` score `3.2056` n `194` status `ready` deltaP `14.0778` edge `0.4004` maxDD `-11.1695`
- `news_risk_high->commodity_1h` score `3.0863` n `30` status `ready` deltaP `24.1218` edge `0.1281` maxDD `-1.2043`
- `market_context_high->equity_24h` score `2.6424` n `178` status `ready` deltaP `17.0919` edge `0.5961` maxDD `-33.1875`
- `market_context_high->unknown_24h` score `2.4282` n `178` status `ready` deltaP `14.4584` edge `0.638` maxDD `-35.8966`
- `market_context_high->index_4h` score `1.0355` n `194` status `ready` deltaP `12.764` edge `0.1101` maxDD `-3.7119`
- `market_context_high->crypto_alt_1h` score `0.8668` n `194` status `ready` deltaP `8.1301` edge `0.1204` maxDD `-4.1892`
- `news_risk_high->fx_4h` score `0.8087` n `30` status `ready` deltaP `20.2643` edge `-0.0042` maxDD `-0.1774`
- `market_context_high->crypto_major_24h` score `0.3453` n `178` status `ready` deltaP `19.0739` edge `0.7602` maxDD `-62.3533`
- `market_context_high->crypto_major_1h` score `0.3155` n `194` status `ready` deltaP `5.2704` edge `0.0985` maxDD `-3.9211`
- `news_risk_high->unknown_4h` score `0.193` n `30` status `ready` deltaP `9.3699` edge `0.0346` maxDD `-2.7857`
- `market_context_high->equity_1h` score `0.1339` n `194` status `ready` deltaP `5.5513` edge `0.055` maxDD `-2.8014`
- `market_context_high->index_1h` score `-0.1532` n `194` status `ready` deltaP `4.3213` edge `0.0216` maxDD `-1.7205`
- `market_context_high->metal_4h` score `-0.1638` n `194` status `ready` deltaP `13.017` edge `0.1614` maxDD `-12.5349`
- `news_risk_high->unknown_1h` score `-0.4582` n `30` status `ready` deltaP `16.7066` edge `-0.1229` maxDD `-2.1115`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
