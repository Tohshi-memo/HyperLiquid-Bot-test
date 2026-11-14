# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-14T04:07:31.746840+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `10338`

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

- `market_context_high->unknown_24h` score `420.7973` n `75` status `ready` deltaP `2.1944` edge `35.0659` maxDD `-0.4606`
- `news_risk_high->equity_24h` score `36.5549` n `53` status `ready` deltaP `35.23` edge `2.882` maxDD `-3.6503`
- `market_context_high->equity_24h` score `28.3212` n `75` status `ready` deltaP `29.7708` edge `2.3158` maxDD `-9.0005`
- `market_context_high->crypto_alt_24h` score `16.8054` n `75` status `ready` deltaP `47.5834` edge `1.3347` maxDD `-16.4511`
- `news_risk_high->crypto_major_24h` score `15.2773` n `53` status `ready` deltaP `42.0434` edge `1.8749` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `11.2354` n `53` status `ready` deltaP `36.2402` edge `0.8077` maxDD `-7.0416`
- `news_risk_high->commodity_24h` score `6.3306` n `53` status `ready` deltaP `42.1875` edge `0.2463` maxDD `0.0`
- `market_context_high->index_24h` score `5.6396` n `75` status `ready` deltaP `32.507` edge `0.2624` maxDD `-0.0653`
- `news_risk_high->metal_4h` score `5.0685` n `53` status `ready` deltaP `48.2254` edge `0.1385` maxDD `-1.0104`
- `news_risk_high->index_24h` score `4.9586` n `53` status `ready` deltaP `30.5195` edge `0.2401` maxDD `-0.4279`
- `market_context_high->metal_24h` score `4.2424` n `75` status `ready` deltaP `41.3334` edge `0.3575` maxDD `-3.7989`
- `news_risk_high->crypto_major_4h` score `3.8012` n `53` status `ready` deltaP `21.0481` edge `0.3252` maxDD `-9.2335`
- `news_risk_high->equity_1h` score `3.626` n `53` status `ready` deltaP `19.2125` edge `0.2371` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `2.9533` n `53` status `ready` deltaP `26.5589` edge `0.0944` maxDD `-0.3611`
- `news_risk_high->metal_1h` score `2.3188` n `53` status `ready` deltaP `27.0873` edge `0.0381` maxDD `-0.3692`
- `news_risk_high->index_4h` score `2.0883` n `53` status `ready` deltaP `21.2034` edge `0.0763` maxDD `-0.8235`
- `news_risk_high->crypto_alt_4h` score `1.9657` n `53` status `ready` deltaP `25.7363` edge `0.2443` maxDD `-10.1088`
- `news_risk_high->crypto_alt_24h` score `1.7177` n `53` status `ready` deltaP `14.4261` edge `0.5746` maxDD `-29.0448`
- `news_risk_high->index_1h` score `1.2502` n `53` status `ready` deltaP `16.8766` edge `0.0218` maxDD `-0.4103`
- `news_risk_high->crypto_major_1h` score `0.7395` n `53` status `ready` deltaP `18.0431` edge `0.0797` maxDD `-7.0808`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
