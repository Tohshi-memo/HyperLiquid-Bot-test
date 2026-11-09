# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-09T15:52:39.362840+00:00`
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

- `market_context_high->equity_24h` score `6.4381` n `34` status `ready` deltaP `10.5699` edge `0.7065` maxDD `-16.9034`
- `market_context_high->commodity_24h` score `1.9416` n `34` status `ready` deltaP `4.1463` edge `0.1929` maxDD `-1.6995`
- `market_context_high->index_24h` score `0.882` n `34` status `ready` deltaP `9.8448` edge `0.0937` maxDD `-2.3671`
- `market_context_high->fx_24h` score `0.6909` n `34` status `ready` deltaP `10.6822` edge `-0.003` maxDD `-0.1843`
- `market_context_high->metal_1h` score `-0.3029` n `88` status `ready` deltaP `4.2461` edge `0.0141` maxDD `-1.4122`
- `market_context_high->commodity_1h` score `-0.5382` n `88` status `ready` deltaP `-0.1565` edge `0.0003` maxDD `-1.7935`
- `market_context_high->index_4h` score `-0.58` n `88` status `ready` deltaP `3.0903` edge `0.0028` maxDD `-2.4871`
- `market_context_high->commodity_4h` score `-0.8397` n `88` status `ready` deltaP `-1.9263` edge `0.0158` maxDD `-4.182`
- `market_context_high->metal_4h` score `-0.9419` n `88` status `ready` deltaP `0.1663` edge `0.0165` maxDD `-4.0688`
- `market_context_high->index_1h` score `-0.9582` n `88` status `ready` deltaP `-6.9066` edge `0.0063` maxDD `-0.9814`
- `market_context_high->fx_1h` score `-1.279` n `88` status `ready` deltaP `-13.4594` edge `-0.0058` maxDD `-0.8088`
- `market_context_high->equity_1h` score `-1.5231` n `88` status `ready` deltaP `-7.0563` edge `0.0364` maxDD `-8.1039`
- `market_context_high->crypto_alt_1h` score `-1.9241` n `88` status `ready` deltaP `0.6328` edge `-0.053` maxDD `-10.8319`
- `market_context_high->fx_4h` score `-2.1012` n `88` status `ready` deltaP `-6.4579` edge `-0.0082` maxDD `-2.4506`
- `market_context_high->metal_24h` score `-2.1062` n `34` status `ready` deltaP `-3.9931` edge `-0.1881` maxDD `-1.4245`
- `market_context_high->crypto_major_1h` score `-3.1682` n `88` status `ready` deltaP `-5.1102` edge `-0.1098` maxDD `-15.9848`
- `market_context_high->equity_4h` score `-5.8344` n `88` status `ready` deltaP `-0.3049` edge `-0.103` maxDD `-25.16`
- `market_context_high->crypto_major_24h` score `-6.2174` n `34` status `ready` deltaP `-6.3521` edge `-0.0127` maxDD `-30.3789`
- `market_context_high->crypto_alt_4h` score `-8.9434` n `88` status `ready` deltaP `1.9402` edge `-0.2464` maxDD `-34.2787`
- `market_context_high->crypto_alt_24h` score `-10.9515` n `34` status `ready` deltaP `-21.5993` edge `-0.2592` maxDD `-33.4213`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
