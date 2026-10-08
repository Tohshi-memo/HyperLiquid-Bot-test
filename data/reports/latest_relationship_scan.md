# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-08T18:52:29.225492+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8914`

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

- `market_context_high->unknown_4h` score `40.2202` n `91` status `ready` deltaP `-2.2246` edge `3.4204` maxDD `-2.3109`
- `news_risk_high->crypto_alt_4h` score `14.6792` n `49` status `ready` deltaP `44.6646` edge `0.9255` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `14.1562` n `49` status `ready` deltaP `46.0708` edge `0.8793` maxDD `-0.2073`
- `news_risk_high->equity_24h` score `8.7375` n `49` status `ready` deltaP `24.0724` edge `0.5776` maxDD `-0.1298`
- `market_context_high->crypto_major_24h` score `8.2751` n `90` status `ready` deltaP `20.699` edge `1.2203` maxDD `-16.7906`
- `news_risk_high->index_24h` score `6.1155` n `49` status `ready` deltaP `44.1941` edge `0.215` maxDD `0.0`
- `market_context_high->equity_24h` score `6.0691` n `90` status `ready` deltaP `23.3468` edge `0.393` maxDD `-1.0977`
- `news_risk_high->equity_4h` score `5.7623` n `49` status `ready` deltaP `31.6233` edge `0.2899` maxDD `-0.6421`
- `news_risk_high->index_4h` score `4.5089` n `49` status `ready` deltaP `45.0629` edge `0.0798` maxDD `-0.025`
- `news_risk_high->crypto_major_1h` score `3.2212` n `49` status `ready` deltaP `12.9109` edge `0.2179` maxDD `-1.5096`
- `news_risk_high->crypto_alt_1h` score `2.7426` n `49` status `ready` deltaP `6.7885` edge `0.215` maxDD `-1.2034`
- `news_risk_high->commodity_24h` score `2.7338` n `49` status `ready` deltaP `32.1402` edge `0.022` maxDD `-0.0096`
- `news_risk_high->index_1h` score `2.4242` n `49` status `ready` deltaP `29.986` edge `0.0161` maxDD `-0.1194`
- `market_context_high->crypto_alt_24h` score `2.3514` n `90` status `ready` deltaP `12.4014` edge `0.8126` maxDD `-34.5048`
- `market_context_high->crypto_major_4h` score `2.0022` n `91` status `ready` deltaP `19.3832` edge `0.2605` maxDD `-6.9761`
- `market_context_high->metal_24h` score `1.4922` n `90` status `ready` deltaP `24.5118` edge `0.1764` maxDD `-3.5466`
- `news_risk_high->metal_4h` score `1.252` n `49` status `ready` deltaP `19.3629` edge `0.073` maxDD `-0.993`
- `market_context_high->fx_4h` score `0.5917` n `91` status `ready` deltaP `16.7533` edge `0.0123` maxDD `-0.3077`
- `market_context_high->fx_1h` score `0.4763` n `91` status `ready` deltaP `9.242` edge `0.0023` maxDD `-0.271`
- `market_context_high->crypto_major_1h` score `0.3823` n `91` status `ready` deltaP `11.3411` edge `0.0623` maxDD `-3.7778`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
