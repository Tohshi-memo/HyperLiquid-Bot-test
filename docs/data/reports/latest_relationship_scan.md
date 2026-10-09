# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-09T04:07:32.554737+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8896`

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

- `market_context_high->unknown_4h` score `40.0672` n `91` status `ready` deltaP `-3.5965` edge `3.4168` maxDD `-2.3109`
- `news_risk_high->crypto_alt_4h` score `13.0372` n `39` status `ready` deltaP `43.4451` edge `0.7968` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `11.9177` n `39` status `ready` deltaP `43.4998` edge `0.7099` maxDD `-0.2073`
- `news_risk_high->equity_24h` score `10.8554` n `39` status `ready` deltaP `28.2853` edge `0.726` maxDD `-0.1298`
- `market_context_high->crypto_major_24h` score `9.8357` n `90` status `ready` deltaP `22.3611` edge `1.4093` maxDD `-16.7906`
- `market_context_high->equity_24h` score `9.1104` n `90` status `ready` deltaP `29.6528` edge `0.6044` maxDD `-1.0977`
- `news_risk_high->index_24h` score `6.8617` n `39` status `ready` deltaP `50.5208` edge `0.235` maxDD `0.0`
- `news_risk_high->equity_4h` score `6.0898` n `39` status `ready` deltaP `32.5516` edge `0.311` maxDD `-0.6421`
- `news_risk_high->index_4h` score `4.5718` n `39` status `ready` deltaP `44.8444` edge `0.0865` maxDD `-0.025`
- `market_context_high->crypto_alt_24h` score `3.5384` n `90` status `ready` deltaP `14.0625` edge `0.9537` maxDD `-34.5048`
- `news_risk_high->crypto_major_1h` score `3.5163` n `39` status `ready` deltaP `15.1889` edge `0.2273` maxDD `-1.5096`
- `news_risk_high->index_1h` score `2.6791` n `39` status `ready` deltaP `32.3699` edge `0.0164` maxDD `-0.0484`
- `news_risk_high->commodity_24h` score `2.2942` n `39` status `ready` deltaP `28.2051` edge `0.0116` maxDD `-0.0096`
- `news_risk_high->crypto_alt_1h` score `2.2664` n `39` status `ready` deltaP `3.1169` edge `0.1998` maxDD `-1.2034`
- `market_context_high->crypto_major_4h` score `1.8145` n `91` status `ready` deltaP `17.8588` edge `0.2466` maxDD `-6.9761`
- `news_risk_high->metal_4h` score `1.2716` n `39` status `ready` deltaP `15.5019` edge `0.0442` maxDD `-0.993`
- `market_context_high->metal_24h` score `1.1041` n `90` status `ready` deltaP `19.5833` edge `0.1595` maxDD `-3.5466`
- `news_risk_high->metal_1h` score `0.7984` n `39` status `ready` deltaP `10.79` edge `0.0251` maxDD `-0.44`
- `market_context_high->fx_1h` score `0.4009` n `91` status `ready` deltaP `8.3438` edge `0.002` maxDD `-0.271`
- `market_context_high->fx_4h` score `0.3506` n `91` status `ready` deltaP `14.0094` edge `0.0105` maxDD `-0.3077`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
