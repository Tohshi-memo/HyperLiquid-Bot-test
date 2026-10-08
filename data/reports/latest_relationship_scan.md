# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-08T19:52:32.845912+00:00`
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

- `market_context_high->unknown_4h` score `40.1782` n `91` status `ready` deltaP `-2.2246` edge `3.4169` maxDD `-2.3109`
- `news_risk_high->crypto_alt_4h` score `14.7754` n `49` status `ready` deltaP `44.8171` edge `0.9325` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `14.22` n `49` status `ready` deltaP `46.2233` edge `0.8836` maxDD `-0.2073`
- `news_risk_high->equity_24h` score `9.1482` n `49` status `ready` deltaP `24.7656` edge `0.6072` maxDD `-0.1298`
- `market_context_high->crypto_major_24h` score `8.5764` n `90` status `ready` deltaP `21.3922` edge `1.2543` maxDD `-16.7906`
- `market_context_high->equity_24h` score `6.4797` n `90` status `ready` deltaP `24.04` edge `0.4226` maxDD `-1.0977`
- `news_risk_high->index_24h` score `6.2382` n `49` status `ready` deltaP `44.8873` edge `0.2206` maxDD `0.0`
- `news_risk_high->equity_4h` score `5.9311` n `49` status `ready` deltaP `32.233` edge `0.2999` maxDD `-0.6421`
- `news_risk_high->index_4h` score `4.5769` n `49` status `ready` deltaP `45.6726` edge `0.0814` maxDD `-0.025`
- `news_risk_high->crypto_major_1h` score `3.1996` n `49` status `ready` deltaP `12.9109` edge `0.2161` maxDD `-1.5096`
- `news_risk_high->crypto_alt_1h` score `2.7222` n `49` status `ready` deltaP `6.7885` edge `0.2133` maxDD `-1.2034`
- `market_context_high->crypto_alt_24h` score `2.6574` n `90` status `ready` deltaP `13.0946` edge `0.8472` maxDD `-34.5048`
- `news_risk_high->commodity_24h` score `2.6039` n `49` status `ready` deltaP `31.447` edge `0.0158` maxDD `-0.0096`
- `news_risk_high->index_1h` score `2.4541` n `49` status `ready` deltaP `30.2854` edge `0.0166` maxDD `-0.1194`
- `market_context_high->crypto_major_4h` score `2.0436` n `91` status `ready` deltaP `19.5357` edge `0.2648` maxDD `-6.9761`
- `market_context_high->metal_24h` score `1.4519` n `90` status `ready` deltaP `23.9919` edge `0.1747` maxDD `-3.5466`
- `news_risk_high->metal_4h` score `1.2527` n `49` status `ready` deltaP `19.3629` edge `0.0731` maxDD `-0.993`
- `market_context_high->fx_4h` score `0.6185` n `91` status `ready` deltaP `17.0581` edge `0.0125` maxDD `-0.3077`
- `market_context_high->fx_1h` score `0.4512` n `91` status `ready` deltaP `8.9426` edge `0.0022` maxDD `-0.271`
- `market_context_high->crypto_major_1h` score `0.3683` n `91` status `ready` deltaP `11.3411` edge `0.0605` maxDD `-3.7778`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
