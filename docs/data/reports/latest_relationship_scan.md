# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-24T18:22:12.918084+00:00`
- Price records: `672`
- Market context records: `1763`
- Flow alert records: `6976`
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

- `market_context_high->metal_24h` score `7.1923` n `172` status `ready` deltaP `27.8787` edge `0.6561` maxDD `-12.7414`
- `market_context_high->crypto_alt_4h` score `6.1762` n `195` status `ready` deltaP `21.7949` edge `0.546` maxDD `-9.1295`
- `market_context_high->crypto_major_4h` score `4.7254` n `195` status `ready` deltaP `23.3615` edge `0.4786` maxDD `-10.9117`
- `market_context_high->index_24h` score `4.0059` n `172` status `ready` deltaP `18.7298` edge `0.3318` maxDD `-4.1604`
- `market_context_high->equity_4h` score `3.2171` n `195` status `ready` deltaP `17.3608` edge `0.2618` maxDD `-5.0894`
- `market_context_high->unknown_24h` score `3.1591` n `172` status `ready` deltaP `14.7004` edge `0.6973` maxDD `-35.8966`
- `news_risk_high->commodity_1h` score `3.1007` n `30` status `ready` deltaP `24.2715` edge `0.1283` maxDD `-1.2043`
- `market_context_high->unknown_4h` score `3.0545` n `195` status `ready` deltaP `13.4795` edge `0.3918` maxDD `-11.1695`
- `market_context_high->equity_24h` score `2.8314` n `172` status `ready` deltaP `17.0987` edge `0.6118` maxDD `-33.1875`
- `market_context_high->index_4h` score `1.0314` n `195` status `ready` deltaP `12.7728` edge `0.1097` maxDD `-3.7119`
- `market_context_high->crypto_alt_1h` score `0.7774` n `195` status `ready` deltaP `7.4328` edge `0.1176` maxDD `-4.1892`
- `market_context_high->crypto_major_24h` score `0.5941` n `172` status `ready` deltaP `19.1981` edge `0.7801` maxDD `-62.3533`
- `market_context_high->crypto_major_1h` score `0.2707` n `195` status `ready` deltaP `5.0407` edge `0.0963` maxDD `-3.9211`
- `market_context_high->equity_1h` score `0.0892` n `195` status `ready` deltaP `5.1428` edge `0.054` maxDD `-2.8014`
- `market_context_high->index_1h` score `-0.1513` n `195` status `ready` deltaP `4.3751` edge `0.0214` maxDD `-1.7205`
- `market_context_high->metal_4h` score `-0.2086` n `195` status `ready` deltaP `12.6056` edge `0.1584` maxDD `-12.5349`
- `news_risk_high->fx_1h` score `-0.5014` n `30` status `ready` deltaP `-5.5788` edge `-0.0009` maxDD `-0.0948`
- `market_context_high->metal_1h` score `-0.5258` n `195` status `ready` deltaP `5.5758` edge `0.029` maxDD `-6.3532`
- `market_context_high->fx_24h` score `-0.5485` n `172` status `ready` deltaP `7.6348` edge `0.0083` maxDD `-1.3925`
- `news_risk_high->unknown_1h` score `-0.5494` n `30` status `ready` deltaP `16.1078` edge `-0.1306` maxDD `-2.1115`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
