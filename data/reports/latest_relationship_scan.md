# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-08T11:07:29.104693+00:00`
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

- `market_context_high->unknown_4h` score `40.6255` n `90` status `ready` deltaP `-2.7981` edge `3.458` maxDD `-2.3109`
- `news_risk_high->crypto_major_4h` score `11.1371` n `56` status `ready` deltaP `38.3275` edge `0.6929` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `9.0329` n `56` status `ready` deltaP `30.1829` edge `0.6395` maxDD `-4.7051`
- `news_risk_high->equity_24h` score `7.3884` n `56` status `ready` deltaP `19.9728` edge `0.4925` maxDD `-0.1298`
- `market_context_high->crypto_major_24h` score `5.8516` n `90` status `ready` deltaP `15.4922` edge `0.9443` maxDD `-16.7906`
- `news_risk_high->index_24h` score `5.3666` n `56` status `ready` deltaP `39.0328` edge `0.187` maxDD `0.0`
- `market_context_high->equity_24h` score `3.5151` n `90` status `ready` deltaP `18.2268` edge `0.2143` maxDD `-1.0977`
- `news_risk_high->index_4h` score `3.2603` n `56` status `ready` deltaP `35.4747` edge `0.0614` maxDD `-0.4296`
- `news_risk_high->equity_4h` score `2.8895` n `56` status `ready` deltaP `19.9478` edge `0.1676` maxDD `-2.7837`
- `news_risk_high->crypto_major_1h` score `2.6382` n `56` status `ready` deltaP `10.3935` edge `0.1861` maxDD `-1.5096`
- `market_context_high->crypto_major_4h` score `2.6102` n `90` status `ready` deltaP `17.2561` edge `0.1989` maxDD `-4.047`
- `news_risk_high->index_1h` score `2.3821` n `56` status `ready` deltaP `29.1595` edge `0.0181` maxDD `-0.1194`
- `market_context_high->metal_24h` score `1.3431` n `90` status `ready` deltaP `22.5734` edge `0.1702` maxDD `-3.5466`
- `news_risk_high->metal_4h` score `1.3393` n `56` status `ready` deltaP `20.1873` edge `0.0787` maxDD `-0.993`
- `news_risk_high->crypto_alt_1h` score `1.2728` n `56` status `ready` deltaP `2.6625` edge `0.1385` maxDD `-2.3482`
- `market_context_high->fx_4h` score `0.8174` n `90` status `ready` deltaP `18.9295` edge `0.0166` maxDD `-0.3077`
- `market_context_high->fx_1h` score `0.5729` n `90` status `ready` deltaP `10.2994` edge `0.0033` maxDD `-0.271`
- `market_context_high->crypto_alt_24h` score `0.5568` n `90` status `ready` deltaP `9.2689` edge `0.6034` maxDD `-34.5048`
- `news_risk_high->commodity_24h` score `0.4579` n `56` status `ready` deltaP `25.3794` edge `-0.0201` maxDD `-4.8981`
- `news_risk_high->metal_1h` score `0.3041` n `56` status `ready` deltaP `9.6771` edge `0.0163` maxDD `-1.0132`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
