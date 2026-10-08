# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-08T11:37:30.869728+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8574`

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

- `market_context_high->unknown_4h` score `40.6879` n `90` status `ready` deltaP `-2.7981` edge `3.4632` maxDD `-2.3109`
- `news_risk_high->crypto_major_4h` score `11.664` n `54` status `ready` deltaP `40.0011` edge `0.7185` maxDD `-0.3872`
- `news_risk_high->crypto_alt_4h` score `10.2284` n `54` status `ready` deltaP `33.4236` edge `0.6897` maxDD `-3.1456`
- `news_risk_high->equity_24h` score `7.1824` n `54` status `ready` deltaP `20.0537` edge `0.4748` maxDD `-0.1298`
- `market_context_high->crypto_major_24h` score `5.9842` n `90` status `ready` deltaP `15.8376` edge `0.959` maxDD `-16.7906`
- `news_risk_high->index_24h` score `5.3943` n `54` status `ready` deltaP `39.3782` edge `0.187` maxDD `0.0`
- `market_context_high->equity_24h` score `3.6543` n `90` status `ready` deltaP `18.5722` edge `0.2236` maxDD `-1.0977`
- `news_risk_high->index_4h` score `3.2602` n `54` status `ready` deltaP `35.3828` edge `0.062` maxDD `-0.4296`
- `news_risk_high->equity_4h` score `3.181` n `54` status `ready` deltaP `21.2906` edge `0.1769` maxDD `-2.6335`
- `news_risk_high->crypto_major_1h` score `2.8029` n `54` status `ready` deltaP `11.0723` edge `0.1953` maxDD `-1.5096`
- `market_context_high->crypto_major_4h` score `2.6668` n `90` status `ready` deltaP `17.4085` edge `0.2026` maxDD `-4.047`
- `news_risk_high->index_1h` score `2.472` n `54` status `ready` deltaP `30.2839` edge `0.0181` maxDD `-0.1194`
- `news_risk_high->crypto_alt_1h` score `1.8795` n `54` status `ready` deltaP `4.7128` edge `0.16` maxDD `-1.4503`
- `market_context_high->metal_24h` score `1.372` n `90` status `ready` deltaP `22.9188` edge `0.1716` maxDD `-3.5466`
- `news_risk_high->metal_4h` score `1.2406` n `54` status `ready` deltaP `19.2355` edge `0.0724` maxDD `-0.993`
- `news_risk_high->commodity_24h` score `1.0234` n `54` status `ready` deltaP `28.1424` edge `0.0066` maxDD `-3.3738`
- `market_context_high->fx_4h` score `0.7906` n `90` status `ready` deltaP `18.6246` edge `0.0164` maxDD `-0.3077`
- `market_context_high->crypto_alt_24h` score `0.5919` n `90` status `ready` deltaP `9.2689` edge `0.6079` maxDD `-34.5048`
- `market_context_high->fx_1h` score `0.5729` n `90` status `ready` deltaP `10.2994` edge `0.0033` maxDD `-0.271`
- `news_risk_high->metal_1h` score `0.3181` n `54` status `ready` deltaP `10.0078` edge `0.0159` maxDD `-1.0132`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
