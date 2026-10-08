# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-08T19:22:32.294347+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8924`

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

- `market_context_high->unknown_4h` score `40.201` n `91` status `ready` deltaP `-2.2246` edge `3.4188` maxDD `-2.3109`
- `news_risk_high->crypto_alt_4h` score `14.808` n `49` status `ready` deltaP `44.9695` edge `0.9342` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `14.255` n `49` status `ready` deltaP `46.3757` edge `0.8855` maxDD `-0.2073`
- `news_risk_high->equity_24h` score `8.9512` n `49` status `ready` deltaP `24.419` edge `0.5931` maxDD `-0.1298`
- `market_context_high->crypto_major_24h` score `8.4398` n `90` status `ready` deltaP `21.0456` edge `1.2391` maxDD `-16.7906`
- `market_context_high->equity_24h` score `6.2828` n `90` status `ready` deltaP `23.6934` edge `0.4085` maxDD `-1.0977`
- `news_risk_high->index_24h` score `6.1781` n `49` status `ready` deltaP `44.5407` edge `0.2179` maxDD `0.0`
- `news_risk_high->equity_4h` score `5.8599` n `49` status `ready` deltaP `31.9282` edge `0.296` maxDD `-0.6421`
- `news_risk_high->index_4h` score `4.5441` n `49` status `ready` deltaP `45.3677` edge `0.0807` maxDD `-0.025`
- `news_risk_high->crypto_major_1h` score `3.2176` n `49` status `ready` deltaP `12.9109` edge `0.2176` maxDD `-1.5096`
- `news_risk_high->crypto_alt_1h` score `2.733` n `49` status `ready` deltaP `6.7885` edge `0.2142` maxDD `-1.2034`
- `news_risk_high->commodity_24h` score `2.6652` n `49` status `ready` deltaP `31.7936` edge `0.0186` maxDD `-0.0096`
- `market_context_high->crypto_alt_24h` score `2.52` n `90` status `ready` deltaP `12.748` edge `0.8319` maxDD `-34.5048`
- `news_risk_high->index_1h` score `2.4409` n `49` status `ready` deltaP `30.1357` edge `0.0165` maxDD `-0.1194`
- `market_context_high->crypto_major_4h` score `2.0664` n `91` status `ready` deltaP `19.6881` edge `0.2667` maxDD `-6.9761`
- `market_context_high->metal_24h` score `1.4778` n `90` status `ready` deltaP `24.3385` edge `0.1757` maxDD `-3.5466`
- `news_risk_high->metal_4h` score `1.2535` n `49` status `ready` deltaP `19.3629` edge `0.0732` maxDD `-0.993`
- `market_context_high->fx_4h` score `0.6051` n `91` status `ready` deltaP `16.9057` edge `0.0124` maxDD `-0.3077`
- `market_context_high->fx_1h` score `0.45` n `91` status `ready` deltaP `8.9426` edge `0.0021` maxDD `-0.271`
- `market_context_high->crypto_major_1h` score `0.38` n `91` status `ready` deltaP `11.3411` edge `0.062` maxDD `-3.7778`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
