# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-07T20:37:28.930275+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10305`

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

- `risk_on_high->unknown_24h` score `1340.8878` n `111` status `ready` deltaP `22.2222` edge `111.5925` maxDD `0.0`
- `risk_on_and_context->unknown_24h` score `1340.8878` n `111` status `ready` deltaP `22.2222` edge `111.5925` maxDD `0.0`
- `market_context_high->unknown_24h` score `309.1519` n `226` status `ready` deltaP `21.3372` edge `25.6256` maxDD `-0.0819`
- `risk_on_high->crypto_major_24h` score `12.0128` n `111` status `ready` deltaP `24.9813` edge `1.1213` maxDD `-16.9418`
- `risk_on_and_context->crypto_major_24h` score `12.0128` n `111` status `ready` deltaP `24.9813` edge `1.1213` maxDD `-16.9418`
- `risk_on_high->crypto_alt_24h` score `11.1931` n `111` status `ready` deltaP `28.7538` edge `0.7472` maxDD `-0.1572`
- `risk_on_and_context->crypto_alt_24h` score `11.1931` n `111` status `ready` deltaP `28.7538` edge `0.7472` maxDD `-0.1572`
- `market_context_high->crypto_alt_24h` score `6.5029` n `226` status `ready` deltaP `22.591` edge `0.4488` maxDD `-2.5998`
- `risk_on_high->crypto_alt_4h` score `5.7572` n `117` status `ready` deltaP `30.635` edge `0.3127` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `5.7572` n `117` status `ready` deltaP `30.635` edge `0.3127` maxDD `-1.9733`
- `risk_on_high->crypto_major_4h` score `4.9317` n `117` status `ready` deltaP `26.286` edge `0.3216` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `4.9317` n `117` status `ready` deltaP `26.286` edge `0.3216` maxDD `-3.8693`
- `market_context_high->equity_24h` score `3.3865` n `226` status `ready` deltaP `14.2361` edge `0.1873` maxDD `0.0`
- `risk_on_high->equity_24h` score `2.5909` n `111` status `ready` deltaP `14.2361` edge `0.121` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `2.5909` n `111` status `ready` deltaP `14.2361` edge `0.121` maxDD `0.0`
- `risk_on_high->index_24h` score `1.767` n `111` status `ready` deltaP `16.0473` edge `0.0445` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `1.767` n `111` status `ready` deltaP `16.0473` edge `0.0445` maxDD `-0.0051`
- `market_context_high->index_24h` score `1.0338` n `226` status `ready` deltaP `10.7854` edge `0.0536` maxDD `-0.1483`
- `risk_on_high->crypto_alt_1h` score `0.9489` n `117` status `ready` deltaP `4.2467` edge `0.086` maxDD `-1.1521`
- `risk_on_and_context->crypto_alt_1h` score `0.9489` n `117` status `ready` deltaP `4.2467` edge `0.086` maxDD `-1.1521`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
