# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-03T06:07:37.388448+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5903`

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

- `news_risk_high->unknown_24h` score `1435.4759` n `38` status `ready` deltaP `19.8556` edge `119.5327` maxDD `-2.0332`
- `market_context_high->crypto_alt_24h` score `13.2795` n `40` status `ready` deltaP `51.4583` edge `0.8033` maxDD `-2.1786`
- `market_context_high->commodity_24h` score `11.0358` n `40` status `ready` deltaP `51.3194` edge `0.5903` maxDD `-0.6889`
- `news_risk_high->equity_4h` score `0.8738` n `38` status `ready` deltaP `-5.0706` edge `0.2222` maxDD `-3.4427`
- `news_risk_high->commodity_1h` score `0.8061` n `38` status `ready` deltaP `17.8853` edge `0.0053` maxDD `-0.6947`
- `news_risk_high->index_4h` score `0.4234` n `38` status `ready` deltaP `2.9766` edge `0.0535` maxDD `-0.3783`
- `market_context_high->commodity_1h` score `0.3479` n `47` status `ready` deltaP `7.4149` edge `0.0326` maxDD `-1.3282`
- `market_context_high->commodity_4h` score `0.306` n `47` status `ready` deltaP `5.0338` edge `0.0903` maxDD `-2.7703`
- `market_context_high->fx_4h` score `0.0596` n `47` status `ready` deltaP `14.1801` edge `-0.0039` maxDD `-1.8531`
- `market_context_high->fx_1h` score `0.025` n `47` status `ready` deltaP `7.5646` edge `-0.0083` maxDD `-0.7804`
- `news_risk_high->metal_1h` score `-0.1501` n `38` status `ready` deltaP `1.434` edge `0.0032` maxDD `-0.5599`
- `market_context_high->crypto_alt_4h` score `-0.2283` n `47` status `ready` deltaP `2.1439` edge `0.047` maxDD `-4.9116`
- `news_risk_high->fx_24h` score `-0.3372` n `38` status `ready` deltaP `6.8439` edge `0.0344` maxDD `-2.6504`
- `news_risk_high->fx_1h` score `-0.4` n `38` status `ready` deltaP `-3.0177` edge `0.0011` maxDD `-0.2475`
- `news_risk_high->crypto_alt_1h` score `-0.4073` n `38` status `ready` deltaP `3.9789` edge `-0.0147` maxDD `-3.1233`
- `news_risk_high->fx_4h` score `-0.4581` n `38` status `ready` deltaP `-0.5456` edge `0.0276` maxDD `-0.6158`
- `news_risk_high->commodity_4h` score `-0.6012` n `38` status `ready` deltaP `6.0976` edge `-0.0306` maxDD `-2.4785`
- `news_risk_high->metal_4h` score `-0.6225` n `38` status `ready` deltaP `-0.6098` edge `-0.0127` maxDD `-0.8085`
- `market_context_high->fx_24h` score `-0.6815` n `40` status `ready` deltaP `0.6597` edge `0.0368` maxDD `-2.506`
- `news_risk_high->index_1h` score `-0.7504` n `38` status `ready` deltaP `-4.1286` edge `-0.0027` maxDD `-0.5845`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
