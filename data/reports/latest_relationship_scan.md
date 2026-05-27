# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-27T18:52:23.558239+00:00`
- Price records: `672`
- Market context records: `2066`
- Flow alert records: `7842`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9145`

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

- `market_context_high->crypto_major_4h` score `9.6376` n `206` status `ready` deltaP `34.0249` edge `0.6293` maxDD `-1.9063`
- `market_context_high->crypto_alt_4h` score `8.967` n `206` status `ready` deltaP `26.2979` edge `0.6864` maxDD `-5.1574`
- `market_context_high->unknown_4h` score `6.5867` n `206` status `ready` deltaP `21.3755` edge `0.4813` maxDD `-2.6599`
- `market_context_high->unknown_24h` score `5.5237` n `205` status `ready` deltaP `19.4177` edge `0.8629` maxDD `-35.8966`
- `market_context_high->equity_4h` score `3.5537` n `206` status `ready` deltaP `19.4545` edge `0.2759` maxDD `-5.0894`
- `market_context_high->index_4h` score `2.051` n `206` status `ready` deltaP `15.4467` edge `0.1363` maxDD `-1.8022`
- `market_context_high->crypto_major_1h` score `1.8474` n `206` status `ready` deltaP `14.1547` edge `0.1582` maxDD `-3.2225`
- `market_context_high->equity_24h` score `1.6412` n `205` status `ready` deltaP `20.297` edge `0.4913` maxDD `-33.1875`
- `market_context_high->crypto_alt_1h` score `1.5076` n `206` status `ready` deltaP `11.1607` edge `0.1626` maxDD `-4.9097`
- `market_context_high->index_24h` score `1.3935` n `205` status `ready` deltaP `8.799` edge `0.1803` maxDD `-4.1604`
- `market_context_high->equity_1h` score `0.4381` n `206` status `ready` deltaP `8.2714` edge `0.0602` maxDD `-2.6402`
- `market_context_high->unknown_1h` score `0.3947` n `206` status `ready` deltaP `5.4081` edge `0.0688` maxDD `-3.0902`
- `market_context_high->crypto_major_24h` score `0.3367` n `205` status `ready` deltaP `20.5106` edge `0.7499` maxDD `-62.3533`
- `market_context_high->index_1h` score `-0.0648` n `206` status `ready` deltaP `4.2062` edge `0.0256` maxDD `-1.3898`
- `market_context_high->fx_24h` score `-0.2809` n `205` status `ready` deltaP `13.5446` edge `0.0256` maxDD `-2.811`
- `market_context_high->metal_4h` score `-0.5585` n `206` status `ready` deltaP `11.6741` edge `0.1379` maxDD `-11.9812`
- `market_context_high->metal_1h` score `-0.7584` n `206` status `ready` deltaP `4.1466` edge `0.0279` maxDD `-5.166`
- `market_context_high->fx_1h` score `-0.7915` n `206` status `ready` deltaP `-0.5988` edge `0.0008` maxDD `-0.3548`
- `market_context_high->fx_4h` score `-1.3823` n `206` status `ready` deltaP `-4.0878` edge `0.0002` maxDD `-1.0513`
- `market_context_high->metal_24h` score `-1.9414` n `205` status `ready` deltaP `10.5359` edge `0.1581` maxDD `-23.2095`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
