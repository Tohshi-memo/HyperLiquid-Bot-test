# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-14T03:52:25.428340+00:00`
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

- `market_context_high->unknown_24h` score `418.7465` n `75` status `ready` deltaP `2.1944` edge `34.895` maxDD `-0.4606`
- `news_risk_high->equity_24h` score `36.4985` n `53` status `ready` deltaP `35.23` edge `2.8773` maxDD `-3.6503`
- `market_context_high->equity_24h` score `28.2648` n `75` status `ready` deltaP `29.7708` edge `2.3111` maxDD `-9.0005`
- `market_context_high->crypto_alt_24h` score `16.821` n `75` status `ready` deltaP `47.5834` edge `1.336` maxDD `-16.4511`
- `news_risk_high->crypto_major_24h` score `15.2516` n `53` status `ready` deltaP `42.0434` edge `1.8716` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `11.2306` n `53` status `ready` deltaP `36.2402` edge `0.8073` maxDD `-7.0416`
- `news_risk_high->commodity_24h` score `6.3119` n `53` status `ready` deltaP `42.0139` edge `0.2459` maxDD `0.0`
- `market_context_high->index_24h` score `5.6197` n `75` status `ready` deltaP `32.3334` edge `0.2619` maxDD `-0.0653`
- `news_risk_high->metal_4h` score `5.0673` n `53` status `ready` deltaP `48.2254` edge `0.1384` maxDD `-1.0104`
- `news_risk_high->index_24h` score `4.9387` n `53` status `ready` deltaP `30.3459` edge `0.2396` maxDD `-0.4279`
- `market_context_high->metal_24h` score `4.2339` n `75` status `ready` deltaP `41.3334` edge `0.3564` maxDD `-3.7989`
- `news_risk_high->crypto_major_4h` score `3.7398` n `53` status `ready` deltaP `20.8957` edge `0.3211` maxDD `-9.2335`
- `news_risk_high->equity_1h` score `3.6236` n `53` status `ready` deltaP `19.2125` edge `0.2369` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `2.9667` n `53` status `ready` deltaP `26.7114` edge `0.0945` maxDD `-0.3611`
- `news_risk_high->metal_1h` score `2.3176` n `53` status `ready` deltaP `27.0873` edge `0.038` maxDD `-0.3692`
- `news_risk_high->index_4h` score `2.0726` n `53` status `ready` deltaP `21.051` edge `0.076` maxDD `-0.8235`
- `news_risk_high->crypto_alt_4h` score `1.9336` n `53` status `ready` deltaP `25.5838` edge `0.2412` maxDD `-10.1088`
- `news_risk_high->crypto_alt_24h` score `1.7278` n `53` status `ready` deltaP `14.4261` edge `0.5759` maxDD `-29.0448`
- `news_risk_high->index_1h` score `1.237` n `53` status `ready` deltaP `16.7269` edge `0.0217` maxDD `-0.4103`
- `news_risk_high->crypto_major_1h` score `0.7278` n `53` status `ready` deltaP `18.0431` edge `0.0782` maxDD `-7.0808`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
