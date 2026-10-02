# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-02T07:07:36.815107+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4890`

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

- `market_context_high->unknown_1h` score `340.65` n `50` status `ready` deltaP `9.5269` edge `28.3289` maxDD `-0.0598`
- `market_context_high->unknown_4h` score `287.5073` n `50` status `ready` deltaP `8.8415` edge `23.9` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `13.6019` n `60` status `ready` deltaP `39.2014` edge `0.8931` maxDD `-1.0093`
- `market_context_high->crypto_major_24h` score `11.0663` n `50` status `ready` deltaP `36.1667` edge `0.8227` maxDD `-9.3299`
- `news_risk_high->equity_24h` score `9.0972` n `60` status `ready` deltaP `36.7014` edge `0.5619` maxDD `-2.8784`
- `market_context_high->crypto_alt_24h` score `8.7489` n `50` status `ready` deltaP `16.5347` edge `0.7898` maxDD `-11.6768`
- `market_context_high->crypto_major_4h` score `6.8413` n `50` status `ready` deltaP `17.5427` edge `0.5235` maxDD `-3.294`
- `market_context_high->crypto_alt_4h` score `4.8401` n `50` status `ready` deltaP `15.5793` edge `0.4288` maxDD `-7.6792`
- `news_risk_high->crypto_alt_4h` score `3.602` n `89` status `ready` deltaP `14.1186` edge `0.3404` maxDD `-6.4152`
- `market_context_high->equity_24h` score `3.1029` n `50` status `ready` deltaP `14.7014` edge `0.486` maxDD `-11.8957`
- `market_context_high->fx_4h` score `2.9093` n `50` status `ready` deltaP `32.689` edge `0.038` maxDD `-0.0791`
- `market_context_high->crypto_alt_1h` score `2.8258` n `50` status `ready` deltaP `13.6048` edge `0.2111` maxDD `-3.6387`
- `market_context_high->crypto_major_1h` score `2.7913` n `50` status `ready` deltaP `13.5509` edge `0.1873` maxDD `-2.2692`
- `market_context_high->fx_1h` score `1.4627` n `50` status `ready` deltaP `20.491` edge `0.0117` maxDD `-0.113`
- `news_risk_high->equity_4h` score `1.2847` n `89` status `ready` deltaP `21.8707` edge `0.0885` maxDD `-2.9013`
- `market_context_high->index_24h` score `1.0185` n `50` status `ready` deltaP `16.1806` edge `0.0798` maxDD `-1.2338`
- `news_risk_high->commodity_24h` score `0.977` n `60` status `ready` deltaP `18.1597` edge `0.1166` maxDD `-3.9922`
- `news_risk_high->crypto_alt_1h` score `0.6863` n `101` status `ready` deltaP `5.0305` edge `0.0799` maxDD `-2.4998`
- `news_risk_high->fx_24h` score `0.6022` n `60` status `ready` deltaP `15.7639` edge `0.0265` maxDD `-0.3507`
- `news_risk_high->metal_24h` score `0.516` n `60` status `ready` deltaP `0.0` edge `0.1704` maxDD `-2.192`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
