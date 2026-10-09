# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-09T04:52:28.813789+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8902`

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

- `market_context_high->unknown_4h` score `40.2184` n `91` status `ready` deltaP `-3.5965` edge `3.4294` maxDD `-2.3109`
- `news_risk_high->crypto_alt_4h` score `12.5284` n `36` status `ready` deltaP `43.4451` edge `0.7544` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `11.1443` n `36` status `ready` deltaP `43.0724` edge `0.6483` maxDD `-0.2073`
- `news_risk_high->equity_24h` score `10.6354` n `36` status `ready` deltaP `27.9514` edge `0.7099` maxDD `-0.1298`
- `market_context_high->crypto_major_24h` score `9.8997` n `90` status `ready` deltaP `22.3611` edge `1.4175` maxDD `-16.7906`
- `market_context_high->equity_24h` score `9.302` n `90` status `ready` deltaP `30.1736` edge `0.6169` maxDD `-1.0977`
- `news_risk_high->index_24h` score `6.8361` n `36` status `ready` deltaP `51.0417` edge `0.2294` maxDD `0.0`
- `news_risk_high->equity_4h` score `6.1021` n `36` status `ready` deltaP `31.9106` edge `0.3163` maxDD `-0.6421`
- `news_risk_high->index_4h` score `4.6039` n `36` status `ready` deltaP `44.6307` edge `0.0906` maxDD `-0.025`
- `market_context_high->crypto_alt_24h` score `3.5618` n `90` status `ready` deltaP `14.0625` edge `0.9567` maxDD `-34.5048`
- `news_risk_high->crypto_major_1h` score `3.1995` n `36` status `ready` deltaP `12.7745` edge `0.217` maxDD `-1.5096`
- `news_risk_high->index_1h` score `2.5754` n `36` status `ready` deltaP `31.0878` edge `0.0163` maxDD `-0.0484`
- `news_risk_high->commodity_24h` score `2.4436` n `36` status `ready` deltaP `27.7777` edge `0.0269` maxDD `-0.0096`
- `news_risk_high->crypto_alt_1h` score `1.8858` n `36` status `ready` deltaP `-0.3659` edge `0.1913` maxDD `-1.2034`
- `market_context_high->crypto_major_4h` score `1.8363` n `91` status `ready` deltaP `17.8588` edge `0.2494` maxDD `-6.9761`
- `market_context_high->metal_24h` score `1.0677` n `90` status `ready` deltaP `19.0625` edge `0.1583` maxDD `-3.5466`
- `news_risk_high->metal_4h` score `0.7416` n `36` status `ready` deltaP `12.2967` edge `0.0214` maxDD `-0.993`
- `market_context_high->fx_1h` score `0.3889` n `91` status `ready` deltaP `8.1941` edge `0.002` maxDD `-0.271`
- `market_context_high->fx_4h` score `0.3348` n `91` status `ready` deltaP `13.8569` edge `0.0102` maxDD `-0.3077`
- `news_risk_high->metal_1h` score `0.2891` n `36` status `ready` deltaP `7.7345` edge `0.016` maxDD `-0.44`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
