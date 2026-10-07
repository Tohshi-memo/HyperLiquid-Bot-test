# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-07T13:07:33.985282+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8718`

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

- `market_context_high->unknown_4h` score `36.2308` n `90` status `ready` deltaP `-5.8468` edge `3.1121` maxDD `-2.3109`
- `news_risk_high->crypto_major_4h` score `10.6063` n `62` status `ready` deltaP `36.4477` edge `0.6612` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `7.4076` n `62` status `ready` deltaP `24.0018` edge `0.5917` maxDD `-6.4195`
- `news_risk_high->index_24h` score `3.8235` n `62` status `ready` deltaP `27.6042` edge `0.1346` maxDD `0.0`
- `news_risk_high->equity_24h` score `3.3068` n `62` status `ready` deltaP `8.479` edge `0.229` maxDD `-0.1298`
- `news_risk_high->index_4h` score `3.0569` n `62` status `ready` deltaP `33.8317` edge `0.0554` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.394` n `62` status `ready` deltaP `9.7257` edge `0.1702` maxDD `-1.5096`
- `news_risk_high->equity_4h` score `2.3125` n `62` status `ready` deltaP `19.6057` edge `0.1218` maxDD `-2.7837`
- `market_context_high->crypto_major_4h` score `2.1015` n `90` status `ready` deltaP `14.5122` edge `0.1748` maxDD `-4.047`
- `news_risk_high->index_1h` score `2.0355` n `62` status `ready` deltaP `25.623` edge `0.0138` maxDD `-0.1997`
- `market_context_high->crypto_major_24h` score `1.7852` n `90` status `ready` deltaP `6.5625` edge `0.4825` maxDD `-16.7906`
- `news_risk_high->metal_4h` score `1.4617` n `62` status `ready` deltaP `20.4858` edge `0.0924` maxDD `-0.993`
- `news_risk_high->crypto_alt_1h` score `1.2426` n `62` status `ready` deltaP `3.757` edge `0.1304` maxDD `-2.4854`
- `market_context_high->fx_4h` score `0.792` n `90` status `ready` deltaP `18.7771` edge `0.0155` maxDD `-0.3077`
- `market_context_high->fx_1h` score `0.7777` n `90` status `ready` deltaP `12.8443` edge `0.0034` maxDD `-0.271`
- `market_context_high->metal_24h` score `0.6908` n `90` status `ready` deltaP `18.7152` edge `0.1123` maxDD `-3.5466`
- `news_risk_high->metal_1h` score `0.1988` n `62` status `ready` deltaP `7.3498` edge `0.0094` maxDD `-1.0132`
- `news_risk_high->commodity_24h` score `0.1195` n `62` status `ready` deltaP `24.5912` edge `0.008` maxDD `-8.196`
- `market_context_high->crypto_major_1h` score `0.091` n `90` status `ready` deltaP `9.654` edge `0.0362` maxDD `-3.7778`
- `market_context_high->commodity_1h` score `-0.0419` n `90` status `ready` deltaP `4.2315` edge `0.0059` maxDD `-0.3417`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
