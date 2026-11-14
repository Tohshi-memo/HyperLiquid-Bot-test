# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-14T03:37:31.000329+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `10320`

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

- `market_context_high->unknown_24h` score `416.6165` n `75` status `ready` deltaP `2.1944` edge `34.7175` maxDD `-0.4606`
- `news_risk_high->equity_24h` score `36.4373` n `53` status `ready` deltaP `35.23` edge `2.8722` maxDD `-3.6503`
- `market_context_high->equity_24h` score `28.2036` n `75` status `ready` deltaP `29.7708` edge `2.306` maxDD `-9.0005`
- `market_context_high->crypto_alt_24h` score `16.8546` n `75` status `ready` deltaP `47.5834` edge `1.3388` maxDD `-16.4511`
- `news_risk_high->crypto_major_24h` score `15.2329` n `53` status `ready` deltaP `42.0434` edge `1.8692` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `11.227` n `53` status `ready` deltaP `36.2402` edge `0.807` maxDD `-7.0416`
- `news_risk_high->commodity_24h` score `6.2932` n `53` status `ready` deltaP `41.8403` edge `0.2455` maxDD `0.0`
- `market_context_high->index_24h` score `5.5998` n `75` status `ready` deltaP `32.1598` edge `0.2614` maxDD `-0.0653`
- `news_risk_high->metal_4h` score `5.0661` n `53` status `ready` deltaP `48.2254` edge `0.1383` maxDD `-1.0104`
- `news_risk_high->index_24h` score `4.9188` n `53` status `ready` deltaP `30.1723` edge `0.2391` maxDD `-0.4279`
- `market_context_high->metal_24h` score `4.2261` n `75` status `ready` deltaP `41.3334` edge `0.3554` maxDD `-3.7989`
- `news_risk_high->crypto_major_4h` score `3.7014` n `53` status `ready` deltaP `20.8957` edge `0.3179` maxDD `-9.2335`
- `news_risk_high->equity_1h` score `3.6092` n `53` status `ready` deltaP `19.0628` edge `0.2367` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `2.9813` n `53` status `ready` deltaP `26.8638` edge `0.0947` maxDD `-0.3611`
- `news_risk_high->metal_1h` score `2.3176` n `53` status `ready` deltaP `27.0873` edge `0.038` maxDD `-0.3692`
- `news_risk_high->index_4h` score `2.058` n `53` status `ready` deltaP `20.8985` edge `0.0758` maxDD `-0.8235`
- `news_risk_high->crypto_alt_4h` score `1.9172` n `53` status `ready` deltaP `25.5838` edge `0.2391` maxDD `-10.1088`
- `news_risk_high->crypto_alt_24h` score `1.7496` n `53` status `ready` deltaP `14.4261` edge `0.5787` maxDD `-29.0448`
- `news_risk_high->index_1h` score `1.225` n `53` status `ready` deltaP `16.5772` edge `0.0217` maxDD `-0.4103`
- `news_risk_high->crypto_major_1h` score `0.7169` n `53` status `ready` deltaP `18.0431` edge `0.0768` maxDD `-7.0808`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
