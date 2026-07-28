# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-28T12:22:33.887457+00:00`
- Price records: `672`
- Market context records: `8195`
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

- `news_risk_high->unknown_24h` score `8417.0067` n `43` status `ready` deltaP `36.9792` edge `701.1707` maxDD `0.0`
- `market_context_high->equity_24h` score `20.9069` n `44` status `ready` deltaP `43.4501` edge `1.5436` maxDD `-4.9489`
- `market_context_high->equity_4h` score `11.2925` n `45` status `ready` deltaP `45.9485` edge `0.639` maxDD `-0.0094`
- `market_context_high->metal_24h` score `8.9743` n `44` status `ready` deltaP `45.8333` edge `0.4423` maxDD `0.0`
- `news_risk_high->equity_4h` score `7.7719` n `51` status `ready` deltaP `28.5629` edge `0.4907` maxDD `-1.6766`
- `market_context_high->crypto_alt_24h` score `5.8646` n `44` status `ready` deltaP `14.0625` edge `0.8788` maxDD `-10.3206`
- `market_context_high->index_4h` score `4.362` n `45` status `ready` deltaP `38.6077` edge `0.1104` maxDD `-0.0092`
- `market_context_high->metal_4h` score `3.9315` n `45` status `ready` deltaP `38.0623` edge `0.0917` maxDD `-0.0926`
- `market_context_high->equity_1h` score `3.6987` n `45` status `ready` deltaP `19.0153` edge `0.1961` maxDD `-0.1718`
- `news_risk_high->crypto_major_4h` score `2.9621` n `51` status `ready` deltaP `15.5099` edge `0.3422` maxDD `-2.6011`
- `news_risk_high->equity_1h` score `2.9526` n `54` status `ready` deltaP `21.9783` edge `0.1304` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.9419` n `51` status `ready` deltaP `25.6666` edge `0.0931` maxDD `-0.191`
- `market_context_high->crypto_major_24h` score `2.8609` n `44` status `ready` deltaP `13.5417` edge `0.675` maxDD `-24.5466`
- `market_context_high->index_24h` score `2.3767` n `44` status `ready` deltaP `20.7071` edge `0.2329` maxDD `-1.2995`
- `news_risk_high->crypto_major_1h` score `2.0237` n `54` status `ready` deltaP `13.9` edge `0.1157` maxDD `-1.1783`
- `news_risk_high->crypto_alt_1h` score `1.8854` n `54` status `ready` deltaP `15.3027` edge `0.0985` maxDD `-1.1388`
- `market_context_high->fx_24h` score `1.48` n `44` status `ready` deltaP `28.346` edge `0.0656` maxDD `-0.5196`
- `news_risk_high->crypto_alt_4h` score `1.4367` n `51` status `ready` deltaP `17.4707` edge `0.2069` maxDD `-5.8012`
- `market_context_high->index_1h` score `1.3666` n `45` status `ready` deltaP `24.2315` edge `0.0275` maxDD `-0.1069`
- `news_risk_high->metal_4h` score `1.2243` n `51` status `ready` deltaP `11.6571` edge `0.0711` maxDD `-0.7433`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
