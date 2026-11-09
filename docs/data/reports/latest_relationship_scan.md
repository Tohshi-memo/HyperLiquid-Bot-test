# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-09T16:07:31.167006+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9286`

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

- `market_context_high->equity_24h` score `6.3138` n `34` status `ready` deltaP `10.3963` edge `0.6973` maxDD `-16.9034`
- `market_context_high->commodity_24h` score `1.938` n `34` status `ready` deltaP `4.1463` edge `0.1926` maxDD `-1.6995`
- `market_context_high->index_24h` score `0.8652` n `34` status `ready` deltaP `9.6712` edge `0.0927` maxDD `-2.3671`
- `market_context_high->fx_24h` score `0.7096` n `34` status `ready` deltaP `10.8558` edge `-0.0026` maxDD `-0.1843`
- `market_context_high->metal_1h` score `-0.3041` n `88` status `ready` deltaP `4.2461` edge `0.014` maxDD `-1.4122`
- `market_context_high->commodity_1h` score `-0.5397` n `88` status `ready` deltaP `-0.1565` edge `0.0001` maxDD `-1.7935`
- `market_context_high->index_4h` score `-0.5941` n `88` status `ready` deltaP `2.9379` edge `0.002` maxDD `-2.4871`
- `market_context_high->commodity_4h` score `-0.8554` n `88` status `ready` deltaP `-2.0787` edge `0.0148` maxDD `-4.182`
- `market_context_high->metal_4h` score `-0.9529` n `88` status `ready` deltaP `0.0139` edge `0.0161` maxDD `-4.0688`
- `market_context_high->index_1h` score `-0.959` n `88` status `ready` deltaP `-6.9066` edge `0.0062` maxDD `-0.9814`
- `market_context_high->fx_1h` score `-1.279` n `88` status `ready` deltaP `-13.4594` edge `-0.0058` maxDD `-0.8088`
- `market_context_high->equity_1h` score `-1.5411` n `88` status `ready` deltaP `-7.0563` edge `0.0341` maxDD `-8.1039`
- `market_context_high->crypto_alt_1h` score `-1.9412` n `88` status `ready` deltaP `0.4831` edge `-0.0542` maxDD `-10.8319`
- `market_context_high->fx_4h` score `-2.1091` n `88` status `ready` deltaP `-6.6103` edge `-0.0082` maxDD `-2.4506`
- `market_context_high->metal_24h` score `-2.1293` n `34` status `ready` deltaP `-4.1667` edge `-0.1899` maxDD `-1.4245`
- `market_context_high->crypto_major_1h` score `-3.1861` n `88` status `ready` deltaP `-5.2599` edge `-0.1111` maxDD `-15.9848`
- `market_context_high->equity_4h` score `-5.9642` n `88` status `ready` deltaP `-0.4573` edge `-0.1128` maxDD `-25.16`
- `market_context_high->crypto_major_24h` score `-6.1742` n `34` status `ready` deltaP `-6.3521` edge `-0.0091` maxDD `-30.3789`
- `market_context_high->crypto_alt_4h` score `-9.018` n `88` status `ready` deltaP `1.7877` edge `-0.2516` maxDD `-34.2787`
- `market_context_high->crypto_alt_24h` score `-10.9942` n `34` status `ready` deltaP `-21.7729` edge `-0.2616` maxDD `-33.4213`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
