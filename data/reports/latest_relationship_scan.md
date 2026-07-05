# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-05T16:37:30.268388+00:00`
- Price records: `672`
- Market context records: `5790`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `8104`

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

- `market_context_high->equity_24h` score `0.6713` n `246` status `ready` deltaP `15.2905` edge `0.4619` maxDD `-31.6316`
- `market_context_high->equity_4h` score `-0.0255` n `303` status `ready` deltaP `6.6057` edge `0.1177` maxDD `-7.4425`
- `market_context_high->fx_1h` score `-0.2474` n `305` status `ready` deltaP `2.3736` edge `0.001` maxDD `-0.5499`
- `market_context_high->equity_1h` score `-0.627` n `305` status `ready` deltaP `3.292` edge `0.0265` maxDD `-5.0555`
- `market_context_high->metal_1h` score `-0.6335` n `305` status `ready` deltaP `2.3589` edge `-0.001` maxDD `-2.0682`
- `market_context_high->commodity_1h` score `-0.7423` n `305` status `ready` deltaP `-1.4965` edge `-0.0047` maxDD `-3.7721`
- `market_context_high->index_1h` score `-0.9892` n `305` status `ready` deltaP `0.1208` edge `0.0036` maxDD `-0.9472`
- `market_context_high->crypto_major_1h` score `-0.9954` n `305` status `ready` deltaP `2.7226` edge `0.031` maxDD `-6.2348`
- `market_context_high->fx_24h` score `-1.0496` n `246` status `ready` deltaP `13.9101` edge `0.0391` maxDD `-4.3118`
- `market_context_high->crypto_alt_1h` score `-1.1107` n `305` status `ready` deltaP `1.6178` edge `0.0301` maxDD `-6.6758`
- `market_context_high->index_4h` score `-1.1934` n `303` status `ready` deltaP `0.7702` edge `0.0106` maxDD `-3.165`
- `market_context_high->fx_4h` score `-1.4834` n `303` status `ready` deltaP `0.1131` edge `0.0031` maxDD `-2.1895`
- `market_context_high->commodity_4h` score `-2.4698` n `303` status `ready` deltaP `-3.5081` edge `-0.0257` maxDD `-14.071`
- `market_context_high->index_24h` score `-2.8178` n `246` status `ready` deltaP `3.3918` edge `0.0306` maxDD `-18.1572`
- `market_context_high->crypto_major_4h` score `-2.9978` n `303` status `ready` deltaP `7.473` edge `0.1376` maxDD `-25.6458`
- `market_context_high->metal_4h` score `-3.8208` n `303` status `ready` deltaP `-5.2725` edge `-0.0473` maxDD `-11.5426`
- `market_context_high->crypto_alt_4h` score `-4.5942` n `303` status `ready` deltaP `5.2649` edge `0.0829` maxDD `-28.7346`
- `market_context_high->metal_24h` score `-7.1207` n `246` status `ready` deltaP `-7.948` edge `-0.253` maxDD `-27.5543`
- `market_context_high->crypto_major_24h` score `-7.7687` n `246` status `ready` deltaP `1.2406` edge `-0.1308` maxDD `-29.6555`
- `market_context_high->commodity_24h` score `-11.0528` n `246` status `ready` deltaP `-14.9178` edge `-0.084` maxDD `-40.676`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
