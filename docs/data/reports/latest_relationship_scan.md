# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-30T03:07:34.550174+00:00`
- Price records: `672`
- Market context records: `5209`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5650`

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

- `market_context_high->unknown_24h` score `15.6054` n `103` status `ready` deltaP `33.9637` edge `1.093` maxDD `-0.8515`
- `market_context_high->crypto_major_24h` score `14.7335` n `103` status `ready` deltaP `30.8792` edge `1.3881` maxDD `-22.6266`
- `market_context_high->crypto_alt_24h` score `10.3182` n `103` status `ready` deltaP `30.2167` edge `0.9971` maxDD `-23.4292`
- `market_context_high->unknown_4h` score `5.2501` n `155` status `ready` deltaP `18.9644` edge `0.4133` maxDD `-5.5109`
- `market_context_high->crypto_alt_4h` score `4.5563` n `155` status `ready` deltaP `13.8464` edge `0.4473` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `4.4154` n `155` status `ready` deltaP `14.0696` edge `0.5034` maxDD `-14.0065`
- `market_context_high->unknown_1h` score `2.6144` n `155` status `ready` deltaP `8.9878` edge `0.2221` maxDD `-2.7986`
- `market_context_high->crypto_alt_1h` score `0.6512` n `155` status `ready` deltaP `4.9527` edge `0.1174` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `0.628` n `155` status `ready` deltaP `6.8524` edge `0.1312` maxDD `-6.9639`
- `market_context_high->fx_24h` score `0.5616` n `103` status `ready` deltaP `13.5046` edge `0.0463` maxDD `-0.8294`
- `market_context_high->equity_4h` score `0.5184` n `155` status `ready` deltaP `7.855` edge `0.1547` maxDD `-7.4425`
- `market_context_high->equity_1h` score `-0.0376` n `155` status `ready` deltaP `5.819` edge `0.0546` maxDD `-5.0555`
- `market_context_high->metal_1h` score `-0.1122` n `155` status `ready` deltaP `4.2611` edge `0.0164` maxDD `-2.0682`
- `market_context_high->index_1h` score `-0.1523` n `155` status `ready` deltaP `3.9869` edge `0.0111` maxDD `-1.0296`
- `market_context_high->fx_1h` score `-0.276` n `155` status `ready` deltaP `1.5096` edge `-0.0002` maxDD `-0.6194`
- `market_context_high->fx_4h` score `-0.601` n `155` status `ready` deltaP `3.1865` edge `0.0051` maxDD `-1.6047`
- `market_context_high->index_24h` score `-0.6329` n `103` status `ready` deltaP `12.4124` edge `-0.0004` maxDD `-7.413`
- `market_context_high->commodity_1h` score `-0.6335` n `155` status `ready` deltaP `0.1265` edge `-0.0012` maxDD `-2.4692`
- `market_context_high->index_4h` score `-0.6366` n `155` status `ready` deltaP `5.1436` edge `0.0244` maxDD `-2.9391`
- `market_context_high->metal_4h` score `-1.3605` n `155` status `ready` deltaP `-0.1023` edge `0.0266` maxDD `-9.3609`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
