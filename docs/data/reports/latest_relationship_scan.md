# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-14T04:37:30.685223+00:00`
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

- `market_context_high->unknown_24h` score `424.8401` n `75` status `ready` deltaP `2.1944` edge `35.4028` maxDD `-0.4606`
- `news_risk_high->equity_24h` score `36.6677` n `53` status `ready` deltaP `35.23` edge `2.8914` maxDD `-3.6503`
- `market_context_high->equity_24h` score `28.434` n `75` status `ready` deltaP `29.7708` edge `2.3252` maxDD `-9.0005`
- `market_context_high->crypto_alt_24h` score `16.7634` n `75` status `ready` deltaP `47.5834` edge `1.3312` maxDD `-16.4511`
- `news_risk_high->crypto_major_24h` score `15.3187` n `53` status `ready` deltaP `42.0434` edge `1.8802` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `11.2414` n `53` status `ready` deltaP `36.2402` edge `0.8082` maxDD `-7.0416`
- `news_risk_high->commodity_24h` score `6.3704` n `53` status `ready` deltaP `42.5347` edge `0.2473` maxDD `0.0`
- `market_context_high->index_24h` score `5.6793` n `75` status `ready` deltaP `32.8542` edge `0.2634` maxDD `-0.0653`
- `news_risk_high->metal_4h` score `5.0709` n `53` status `ready` deltaP `48.2254` edge `0.1387` maxDD `-1.0104`
- `news_risk_high->index_24h` score `4.9984` n `53` status `ready` deltaP `30.8667` edge `0.2411` maxDD `-0.4279`
- `market_context_high->metal_24h` score `4.2573` n `75` status `ready` deltaP `41.3334` edge `0.3594` maxDD `-3.7989`
- `news_risk_high->crypto_major_4h` score `3.918` n `53` status `ready` deltaP `21.353` edge `0.3329` maxDD `-9.2335`
- `news_risk_high->equity_1h` score `3.6523` n `53` status `ready` deltaP `19.5119` edge `0.2373` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `2.9801` n `53` status `ready` deltaP `26.8638` edge `0.0946` maxDD `-0.3611`
- `news_risk_high->metal_1h` score `2.344` n `53` status `ready` deltaP `27.3867` edge `0.0382` maxDD `-0.3692`
- `news_risk_high->index_4h` score `2.1139` n `53` status `ready` deltaP `21.5083` edge `0.0764` maxDD `-0.8235`
- `news_risk_high->crypto_alt_4h` score `2.0237` n `53` status `ready` deltaP `26.0411` edge `0.2497` maxDD `-10.1088`
- `news_risk_high->crypto_alt_24h` score `1.6904` n `53` status `ready` deltaP `14.4261` edge `0.5711` maxDD `-29.0448`
- `news_risk_high->index_1h` score `1.2622` n `53` status `ready` deltaP `17.0263` edge `0.0218` maxDD `-0.4103`
- `news_risk_high->crypto_major_1h` score `0.7473` n `53` status `ready` deltaP `18.0431` edge `0.0807` maxDD `-7.0808`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
