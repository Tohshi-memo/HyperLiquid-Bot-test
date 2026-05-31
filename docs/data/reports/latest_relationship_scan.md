# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-31T13:52:21.036753+00:00`
- Price records: `672`
- Market context records: `2463`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9224`

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

- `news_risk_high->crypto_alt_24h` score `21.7907` n `33` status `ready` deltaP `45.2336` edge `1.5732` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `21.5412` n `33` status `ready` deltaP `55.8239` edge `1.4669` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `19.052` n `33` status `ready` deltaP `29.0878` edge `1.4252` maxDD `-2.1831`
- `news_risk_high->crypto_major_24h` score `13.0065` n `33` status `ready` deltaP `24.6212` edge `0.9778` maxDD `-3.3119`
- `news_risk_high->index_24h` score `9.0208` n `33` status `ready` deltaP `27.178` edge `0.5916` maxDD `-1.3507`
- `news_risk_high->unknown_24h` score `7.0742` n `33` status `ready` deltaP `24.2266` edge `0.4506` maxDD `-1.4744`
- `market_context_high->unknown_24h` score `5.8425` n `112` status `ready` deltaP `21.8998` edge `0.3737` maxDD `-1.626`
- `market_context_high->crypto_alt_4h` score `3.9667` n `136` status `ready` deltaP `20.5882` edge `0.4612` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `3.9261` n `136` status `ready` deltaP `18.1761` edge `0.387` maxDD `-10.1468`
- `news_risk_high->fx_24h` score `3.6406` n `33` status `ready` deltaP `36.1585` edge `0.0808` maxDD `-0.1442`
- `news_risk_high->commodity_4h` score `3.4908` n `33` status `ready` deltaP `23.0137` edge `0.2046` maxDD `-3.0367`
- `news_risk_high->metal_4h` score `2.7628` n `33` status `ready` deltaP `13.0636` edge `0.3579` maxDD `-3.93`
- `market_context_high->crypto_major_24h` score `2.4586` n `112` status `ready` deltaP `11.9047` edge `0.6251` maxDD `-25.1408`
- `news_risk_high->equity_4h` score `1.8494` n `33` status `ready` deltaP `-9.211` edge `0.3812` maxDD `-3.2819`
- `news_risk_high->fx_4h` score `1.8086` n `33` status `ready` deltaP `22.8613` edge `0.0167` maxDD `-0.1382`
- `news_risk_high->unknown_1h` score `1.4839` n `33` status `ready` deltaP `18.7988` edge `0.0415` maxDD `-1.4536`
- `market_context_high->unknown_4h` score `1.4803` n `136` status `ready` deltaP `9.5409` edge `0.1618` maxDD `-3.4972`
- `news_risk_high->fx_1h` score `1.132` n `33` status `ready` deltaP `15.7685` edge `0.0148` maxDD `-0.0473`
- `market_context_high->index_24h` score `0.9084` n `112` status `ready` deltaP `5.2083` edge `0.1005` maxDD `-1.0948`
- `market_context_high->crypto_major_1h` score `0.8081` n `136` status `ready` deltaP `8.7839` edge `0.1282` maxDD `-4.2199`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
