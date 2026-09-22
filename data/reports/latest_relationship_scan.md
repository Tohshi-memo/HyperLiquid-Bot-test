# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-22T06:07:33.368915+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10002`

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

- `market_context_high->unknown_4h` score `48.355` n `46` status `ready` deltaP `7.3171` edge `3.9808` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `34.7396` n `46` status `ready` deltaP `21.5203` edge `2.7671` maxDD `-0.5817`
- `market_context_high->crypto_alt_24h` score `19.3814` n `46` status `ready` deltaP `20.3125` edge `1.4797` maxDD `0.0`
- `market_context_high->equity_24h` score `17.0768` n `46` status `ready` deltaP `14.7494` edge `1.3348` maxDD `-0.1382`
- `news_risk_high->crypto_major_24h` score `7.0224` n `101` status `ready` deltaP `-3.8349` edge `1.2966` maxDD `-46.1999`
- `market_context_high->index_24h` score `5.634` n `46` status `ready` deltaP `20.1314` edge `0.344` maxDD `-0.03`
- `news_risk_high->crypto_alt_24h` score `2.9004` n `101` status `ready` deltaP `-3.4499` edge `0.7528` maxDD `-32.7147`
- `news_risk_high->commodity_24h` score `2.846` n `101` status `ready` deltaP `35.0024` edge `0.2621` maxDD `-3.4467`
- `news_risk_high->crypto_alt_4h` score `2.6613` n `101` status `ready` deltaP `13.1263` edge `0.2552` maxDD `-7.675`
- `news_risk_high->crypto_alt_1h` score `2.2906` n `101` status `ready` deltaP `13.9859` edge `0.1442` maxDD `-2.058`
- `news_risk_high->crypto_major_4h` score `2.1378` n `101` status `ready` deltaP `16.1751` edge `0.1961` maxDD `-8.0625`
- `market_context_high->index_4h` score `1.9773` n `46` status `ready` deltaP `23.3165` edge `0.0227` maxDD `-0.0692`
- `news_risk_high->crypto_major_1h` score `1.6132` n `101` status `ready` deltaP `15.6326` edge `0.0825` maxDD `-2.8494`
- `market_context_high->equity_4h` score `1.1208` n `46` status `ready` deltaP `8.1389` edge `0.0698` maxDD `-0.4529`
- `market_context_high->crypto_alt_4h` score `1.1057` n `46` status `ready` deltaP `8.8215` edge `0.0928` maxDD `-2.7574`
- `market_context_high->equity_1h` score `0.954` n `46` status `ready` deltaP `7.5111` edge `0.0537` maxDD `-0.2751`
- `news_risk_high->fx_4h` score `0.8715` n `101` status `ready` deltaP `15.348` edge `0.0339` maxDD `-0.421`
- `market_context_high->index_1h` score `0.6591` n `46` status `ready` deltaP `10.3554` edge `0.0112` maxDD `-0.0249`
- `news_risk_high->metal_1h` score `0.5478` n `101` status `ready` deltaP `13.8495` edge `0.0135` maxDD `-0.8144`
- `market_context_high->crypto_major_1h` score `0.5253` n `46` status `ready` deltaP `1.061` edge `0.089` maxDD `-2.1836`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
