# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-04T08:22:32.323722+00:00`
- Price records: `672`
- Market context records: `5644`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `8684`

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

- `market_context_high->equity_24h` score `2.6993` n `176` status `ready` deltaP `14.0151` edge `0.6394` maxDD `-31.6316`
- `market_context_high->fx_24h` score `1.283` n `176` status `ready` deltaP `21.3226` edge `0.0626` maxDD `-1.4933`
- `market_context_high->crypto_major_4h` score `0.6192` n `237` status `ready` deltaP `9.9374` edge `0.2146` maxDD `-14.0065`
- `market_context_high->equity_4h` score `0.4625` n `237` status `ready` deltaP `7.3814` edge `0.1532` maxDD `-7.4425`
- `market_context_high->crypto_alt_4h` score `-0.2284` n `237` status `ready` deltaP `5.3071` edge `0.1305` maxDD `-9.46`
- `market_context_high->fx_1h` score `-0.2719` n `237` status `ready` deltaP `1.749` edge `0.0011` maxDD `-0.4764`
- `market_context_high->equity_1h` score `-0.3475` n `237` status `ready` deltaP `5.6154` edge `0.0343` maxDD `-5.0555`
- `market_context_high->metal_1h` score `-0.5652` n `237` status `ready` deltaP `-0.7555` edge `0.0001` maxDD `-2.0682`
- `market_context_high->crypto_alt_1h` score `-0.5986` n `237` status `ready` deltaP `1.5861` edge `0.0357` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `-0.6445` n `237` status `ready` deltaP `3.9813` edge `0.0443` maxDD `-6.9639`
- `market_context_high->index_1h` score `-0.9657` n `237` status `ready` deltaP `0.1295` edge `0.0055` maxDD `-0.9472`
- `market_context_high->commodity_1h` score `-1.0548` n `237` status `ready` deltaP `-0.878` edge `-0.0055` maxDD `-3.7906`
- `market_context_high->fx_4h` score `-1.3256` n `237` status `ready` deltaP `1.0658` edge `0.0063` maxDD `-1.335`
- `market_context_high->index_4h` score `-1.9977` n `237` status `ready` deltaP `-1.2317` edge `0.0089` maxDD `-3.04`
- `market_context_high->index_24h` score `-2.2839` n `176` status `ready` deltaP `10.827` edge `0.0337` maxDD `-16.8946`
- `market_context_high->metal_4h` score `-3.0274` n `237` status `ready` deltaP `-14.2167` edge `-0.055` maxDD `-11.7351`
- `market_context_high->commodity_4h` score `-3.8116` n `237` status `ready` deltaP `-2.1875` edge `-0.0355` maxDD `-14.071`
- `market_context_high->crypto_major_24h` score `-4.5627` n `176` status `ready` deltaP `4.2298` edge `0.0456` maxDD `-29.6555`
- `market_context_high->metal_24h` score `-8.2872` n `176` status `ready` deltaP `-11.3952` edge `-0.2504` maxDD `-32.8874`
- `market_context_high->commodity_24h` score `-13.1641` n `176` status `ready` deltaP `-17.2822` edge `-0.1209` maxDD `-45.8715`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
