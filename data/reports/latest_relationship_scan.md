# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-19T23:42:21.298606+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `10828`

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

- `market_context_high->equity_4h` score `2.1715` n `96` status `ready` deltaP `11.6107` edge `0.1924` maxDD `-2.4411`
- `market_context_high->equity_1h` score `1.7313` n `96` status `ready` deltaP `14.2528` edge `0.0794` maxDD `-0.4112`
- `market_context_high->index_1h` score `0.921` n `96` status `ready` deltaP `15.7622` edge `0.0104` maxDD `-0.0982`
- `market_context_high->metal_4h` score `0.424` n `96` status `ready` deltaP `12.6016` edge `0.0089` maxDD `-1.273`
- `market_context_high->index_4h` score `0.2858` n `96` status `ready` deltaP `9.7815` edge `0.0241` maxDD `-0.5728`
- `market_context_high->commodity_24h` score `0.1895` n `96` status `ready` deltaP `6.4236` edge `0.1648` maxDD `-4.666`
- `market_context_high->fx_4h` score `0.0257` n `96` status `ready` deltaP `7.3424` edge `0.0046` maxDD `-0.3539`
- `market_context_high->metal_1h` score `-0.14` n `96` status `ready` deltaP `3.4244` edge `0.0042` maxDD `-0.4291`
- `market_context_high->unknown_24h` score `-0.1941` n `96` status `ready` deltaP `17.7083` edge `-0.0836` maxDD `-1.0505`
- `market_context_high->unknown_1h` score `-0.204` n `96` status `ready` deltaP `5.7635` edge `-0.0327` maxDD `-0.4843`
- `market_context_high->fx_1h` score `-0.3292` n `96` status `ready` deltaP `-1.3224` edge `0.0025` maxDD `-0.2043`
- `market_context_high->commodity_4h` score `-0.6883` n `96` status `ready` deltaP `-1.3973` edge `0.0061` maxDD `-2.4692`
- `market_context_high->crypto_alt_1h` score `-0.8282` n `96` status `ready` deltaP `-0.1684` edge `-0.0249` maxDD `-2.413`
- `market_context_high->commodity_1h` score `-0.904` n `96` status `ready` deltaP `-8.0402` edge `-0.0057` maxDD `-1.1941`
- `market_context_high->crypto_major_1h` score `-0.9491` n `96` status `ready` deltaP `1.0354` edge `-0.0441` maxDD `-2.7581`
- `market_context_high->crypto_alt_4h` score `-2.0682` n `96` status `ready` deltaP `3.2012` edge `-0.0667` maxDD `-5.4926`
- `market_context_high->crypto_major_4h` score `-2.3227` n `96` status `ready` deltaP `5.3607` edge `-0.1272` maxDD `-3.1677`
- `market_context_high->fx_24h` score `-3.2286` n `96` status `ready` deltaP `-16.1458` edge `-0.0031` maxDD `-1.9981`
- `market_context_high->metal_24h` score `-3.4138` n `96` status `ready` deltaP `-11.1111` edge `-0.0328` maxDD `-11.4635`
- `market_context_high->crypto_major_24h` score `-3.4165` n `96` status `ready` deltaP `2.9514` edge `-0.1836` maxDD `-4.9964`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
