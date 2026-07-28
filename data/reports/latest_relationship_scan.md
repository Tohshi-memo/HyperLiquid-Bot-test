# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-28T09:52:26.281477+00:00`
- Price records: `672`
- Market context records: `8184`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5904`

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

- `news_risk_high->unknown_24h` score `8648.5059` n `43` status `ready` deltaP `36.9792` edge `720.4623` maxDD `0.0`
- `market_context_high->equity_24h` score `19.7436` n `47` status `ready` deltaP `42.8745` edge `1.4505` maxDD `-4.9489`
- `market_context_high->equity_4h` score `10.8858` n `48` status `ready` deltaP `45.0204` edge `0.6113` maxDD `-0.0094`
- `market_context_high->metal_24h` score `8.6038` n `47` status `ready` deltaP `44.0972` edge `0.423` maxDD `0.0`
- `news_risk_high->equity_4h` score `7.9107` n `49` status `ready` deltaP `28.7364` edge `0.497` maxDD `-1.3479`
- `market_context_high->crypto_alt_24h` score `4.4625` n `47` status `ready` deltaP `10.871` edge `0.761` maxDD `-12.5753`
- `market_context_high->index_4h` score `4.2574` n `48` status `ready` deltaP `38.1098` edge `0.105` maxDD `-0.0092`
- `market_context_high->metal_4h` score `3.2022` n `48` status `ready` deltaP `31.9106` edge `0.0759` maxDD `-0.4094`
- `market_context_high->equity_1h` score `3.1648` n `48` status `ready` deltaP `16.5045` edge `0.1726` maxDD `-0.512`
- `news_risk_high->equity_1h` score `3.1004` n `53` status `ready` deltaP `23.2262` edge `0.1344` maxDD `-1.1366`
- `news_risk_high->crypto_major_4h` score `3.059` n `49` status `ready` deltaP `15.4928` edge `0.352` maxDD `-2.382`
- `news_risk_high->index_4h` score `2.8059` n `49` status `ready` deltaP `23.9516` edge `0.0932` maxDD `-0.191`
- `market_context_high->index_24h` score `2.1362` n `47` status `ready` deltaP `19.0344` edge `0.2134` maxDD `-1.3142`
- `news_risk_high->crypto_major_1h` score `2.0916` n `53` status `ready` deltaP `14.4193` edge `0.1179` maxDD `-1.1783`
- `news_risk_high->crypto_alt_1h` score `1.774` n `53` status `ready` deltaP `14.1199` edge `0.0971` maxDD `-1.1388`
- `news_risk_high->metal_4h` score `1.4746` n `49` status `ready` deltaP `13.8408` edge `0.0774` maxDD `-0.7433`
- `news_risk_high->crypto_alt_4h` score `1.3521` n `49` status `ready` deltaP `15.9501` edge `0.2062` maxDD `-5.8012`
- `market_context_high->fx_24h` score `1.2548` n `47` status `ready` deltaP `24.7193` edge `0.0609` maxDD `-0.5196`
- `market_context_high->index_1h` score `1.2171` n `48` status `ready` deltaP `21.5818` edge `0.026` maxDD `-0.1069`
- `market_context_high->crypto_major_24h` score `0.9692` n `47` status `ready` deltaP `10.3502` edge `0.5241` maxDD `-29.1746`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
