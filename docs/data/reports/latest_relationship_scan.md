# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-07T17:22:27.341369+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8742`

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

- `market_context_high->unknown_4h` score `37.621` n `90` status `ready` deltaP `-5.5994` edge `3.2263` maxDD `-2.3109`
- `news_risk_high->crypto_major_4h` score `10.8345` n `62` status `ready` deltaP `37.6802` edge `0.672` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `7.4603` n `62` status `ready` deltaP `23.8651` edge `0.597` maxDD `-6.4195`
- `news_risk_high->index_24h` score `4.1212` n `62` status `ready` deltaP `29.5848` edge `0.1462` maxDD `0.0`
- `news_risk_high->equity_24h` score `4.0404` n `62` status `ready` deltaP `9.6384` edge `0.2824` maxDD `-0.1298`
- `news_risk_high->index_4h` score `3.036` n `62` status `ready` deltaP `33.3906` edge `0.0566` maxDD `-0.4296`
- `market_context_high->crypto_major_24h` score `2.668` n `90` status `ready` deltaP `7.97` edge `0.5863` maxDD `-16.7906`
- `news_risk_high->crypto_major_1h` score `2.4365` n `62` status `ready` deltaP `9.9571` edge `0.1722` maxDD `-1.5096`
- `market_context_high->crypto_major_4h` score `2.3297` n `90` status `ready` deltaP `15.7447` edge `0.1856` maxDD `-4.047`
- `news_risk_high->equity_4h` score `2.2779` n `62` status `ready` deltaP `19.1882` edge `0.1217` maxDD `-2.7837`
- `news_risk_high->index_1h` score `2.0357` n `62` status `ready` deltaP `25.5509` edge `0.0143` maxDD `-0.1997`
- `news_risk_high->metal_4h` score `1.429` n `62` status `ready` deltaP `20.1735` edge `0.0903` maxDD `-0.993`
- `news_risk_high->crypto_alt_1h` score `1.28` n `62` status `ready` deltaP `3.9852` edge `0.132` maxDD `-2.4854`
- `market_context_high->fx_4h` score `0.856` n `90` status `ready` deltaP `19.517` edge `0.0159` maxDD `-0.3077`
- `market_context_high->metal_24h` score `0.8124` n `90` status `ready` deltaP `19.0426` edge `0.1257` maxDD `-3.5466`
- `market_context_high->fx_1h` score `0.7833` n `90` status `ready` deltaP `12.9148` edge `0.0034` maxDD `-0.271`
- `news_risk_high->unknown_4h` score `0.4006` n `62` status `ready` deltaP `-8.5744` edge `0.2151` maxDD `-5.6309`
- `market_context_high->crypto_major_1h` score `0.1187` n `90` status `ready` deltaP `9.8854` edge `0.0382` maxDD `-3.7778`
- `news_risk_high->metal_1h` score `0.0862` n `62` status `ready` deltaP `6.2274` edge `0.0075` maxDD `-1.0132`
- `market_context_high->commodity_1h` score `0.0238` n `90` status `ready` deltaP `4.7533` edge `0.0079` maxDD `-0.3417`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
