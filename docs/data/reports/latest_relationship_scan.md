# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-07T23:37:24.389754+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8574`

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

- `market_context_high->unknown_4h` score `38.4222` n `90` status `ready` deltaP `-4.7798` edge `3.2876` maxDD `-2.3109`
- `news_risk_high->crypto_major_4h` score `10.9779` n `62` status `ready` deltaP `38.8867` edge `0.6759` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `7.0227` n `62` status `ready` deltaP `22.325` edge `0.5708` maxDD `-6.4195`
- `news_risk_high->equity_24h` score `5.384` n `62` status `ready` deltaP `13.0986` edge `0.3713` maxDD `-0.1298`
- `news_risk_high->index_24h` score `4.5125` n `62` status `ready` deltaP `32.526` edge `0.1592` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `3.9038` n `90` status `ready` deltaP `10.0461` edge `0.7309` maxDD `-16.7906`
- `news_risk_high->index_4h` score `2.828` n `62` status `ready` deltaP `31.2402` edge `0.0536` maxDD `-0.4296`
- `market_context_high->crypto_major_4h` score `2.473` n `90` status `ready` deltaP `16.9512` edge `0.1895` maxDD `-4.047`
- `news_risk_high->crypto_major_1h` score `2.4635` n `62` status `ready` deltaP `10.1748` edge `0.173` maxDD `-1.5096`
- `news_risk_high->equity_4h` score `2.0298` n `62` status `ready` deltaP `17.1666` edge `0.1145` maxDD `-2.7837`
- `news_risk_high->index_1h` score `1.8858` n `62` status `ready` deltaP `23.8266` edge `0.0133` maxDD `-0.1997`
- `news_risk_high->metal_4h` score `1.4912` n `62` status `ready` deltaP `21.248` edge `0.0911` maxDD `-0.993`
- `news_risk_high->unknown_4h` score `1.2018` n `62` status `ready` deltaP `-7.7548` edge `0.2764` maxDD `-5.6309`
- `market_context_high->metal_24h` score `1.0863` n `90` status `ready` deltaP `20.0807` edge `0.1539` maxDD `-3.5466`
- `news_risk_high->crypto_alt_1h` score `1.0375` n `62` status `ready` deltaP `2.7091` edge `0.1203` maxDD `-2.4854`
- `market_context_high->fx_4h` score `0.9284` n `90` status `ready` deltaP `20.3015` edge `0.0167` maxDD `-0.3077`
- `market_context_high->equity_24h` score `0.8794` n `90` status `ready` deltaP `10.6613` edge `0.0451` maxDD `-1.0977`
- `market_context_high->fx_1h` score `0.6795` n `90` status `ready` deltaP `11.6467` edge `0.0032` maxDD `-0.271`
- `market_context_high->crypto_major_1h` score `0.1362` n `90` status `ready` deltaP `10.1031` edge `0.039` maxDD `-3.7778`
- `news_risk_high->metal_1h` score `0.1137` n `62` status `ready` deltaP `6.4516` edge `0.0083` maxDD `-1.0132`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
