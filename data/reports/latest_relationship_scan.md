# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-08T12:37:28.525780+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8747`

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

- `market_context_high->unknown_4h` score `40.6867` n `90` status `ready` deltaP `-2.7981` edge `3.4631` maxDD `-2.3109`
- `news_risk_high->crypto_major_4h` score `12.7508` n `50` status `ready` deltaP `43.7134` edge `0.7779` maxDD `-0.2073`
- `news_risk_high->crypto_alt_4h` score `12.6424` n `50` status `ready` deltaP `40.6829` edge `0.7925` maxDD `-0.4816`
- `news_risk_high->equity_24h` score `6.7355` n `50` status `ready` deltaP `20.152` edge `0.4369` maxDD `-0.1298`
- `market_context_high->crypto_major_24h` score `6.251` n `90` status `ready` deltaP `16.5285` edge `0.9886` maxDD `-16.7906`
- `news_risk_high->index_24h` score `5.4603` n `50` status `ready` deltaP `40.0691` edge `0.1879` maxDD `0.0`
- `news_risk_high->equity_4h` score `4.6417` n `50` status `ready` deltaP `27.9573` edge `0.2242` maxDD `-0.9019`
- `news_risk_high->index_4h` score `4.1699` n `50` status `ready` deltaP `42.4939` edge `0.0711` maxDD `-0.2185`
- `market_context_high->equity_24h` score `3.9088` n `90` status `ready` deltaP `19.2631` edge `0.2402` maxDD `-1.0977`
- `news_risk_high->commodity_24h` score `3.3092` n `50` status `ready` deltaP `34.4145` edge `0.0621` maxDD `-0.5945`
- `news_risk_high->crypto_major_1h` score `3.0381` n `50` status `ready` deltaP `12.5569` edge `0.205` maxDD `-1.5096`
- `market_context_high->crypto_major_4h` score `2.7656` n `90` status `ready` deltaP `17.7134` edge `0.2088` maxDD `-4.047`
- `news_risk_high->crypto_alt_1h` score `2.5535` n `50` status `ready` deltaP `7.4551` edge `0.1948` maxDD `-1.2034`
- `news_risk_high->index_1h` score `2.3211` n `50` status `ready` deltaP `28.8024` edge `0.0154` maxDD `-0.1194`
- `market_context_high->metal_24h` score `1.4122` n `90` status `ready` deltaP `23.4369` edge `0.1733` maxDD `-3.5466`
- `news_risk_high->metal_4h` score `1.0971` n `50` status `ready` deltaP `17.0305` edge `0.0687` maxDD `-0.993`
- `market_context_high->fx_4h` score `0.737` n `90` status `ready` deltaP `18.0149` edge `0.016` maxDD `-0.3077`
- `market_context_high->crypto_alt_24h` score `0.6874` n `90` status `ready` deltaP `9.4416` edge `0.619` maxDD `-34.5048`
- `market_context_high->fx_1h` score `0.5853` n `91` status `ready` deltaP `10.4396` edge `0.0034` maxDD `-0.271`
- `market_context_high->crypto_major_1h` score `0.1898` n `91` status `ready` deltaP `10.2932` edge `0.0446` maxDD `-3.7778`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
