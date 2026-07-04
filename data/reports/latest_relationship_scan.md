# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-04T06:37:28.441279+00:00`
- Price records: `672`
- Market context records: `5636`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `8683`

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

- `market_context_high->equity_24h` score `2.8932` n `174` status `ready` deltaP `14.8348` edge `0.6501` maxDD `-31.6316`
- `market_context_high->fx_24h` score `1.3664` n `174` status `ready` deltaP `22.1325` edge `0.0637` maxDD `-1.457`
- `market_context_high->crypto_major_4h` score `0.6894` n `237` status `ready` deltaP `10.3948` edge `0.2174` maxDD `-14.0065`
- `market_context_high->equity_4h` score `0.4661` n `237` status `ready` deltaP `7.3814` edge `0.1535` maxDD `-7.4425`
- `market_context_high->crypto_alt_4h` score `-0.2538` n `237` status `ready` deltaP `5.1547` edge `0.1294` maxDD `-9.46`
- `market_context_high->fx_1h` score `-0.2797` n `237` status `ready` deltaP `1.5993` edge `0.0011` maxDD `-0.4764`
- `market_context_high->equity_1h` score `-0.4014` n `237` status `ready` deltaP `5.0166` edge `0.0338` maxDD `-5.0555`
- `market_context_high->metal_1h` score `-0.5488` n `237` status `ready` deltaP `-0.4561` edge `0.0002` maxDD `-2.0682`
- `market_context_high->crypto_alt_1h` score `-0.6105` n `237` status `ready` deltaP `1.4364` edge `0.0357` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `-0.6193` n `237` status `ready` deltaP `4.2807` edge `0.0444` maxDD `-6.9639`
- `market_context_high->index_1h` score `-0.9418` n `237` status `ready` deltaP `0.4289` edge `0.0055` maxDD `-0.9472`
- `market_context_high->commodity_1h` score `-1.0572` n `237` status `ready` deltaP `-0.878` edge `-0.0057` maxDD `-3.7906`
- `market_context_high->fx_4h` score `-1.3335` n `237` status `ready` deltaP `0.9133` edge `0.0063` maxDD `-1.335`
- `market_context_high->index_4h` score `-1.9466` n `237` status `ready` deltaP `-0.6219` edge `0.0091` maxDD `-3.04`
- `market_context_high->index_24h` score `-2.3155` n `174` status `ready` deltaP `10.6082` edge `0.0311` maxDD `-16.8946`
- `market_context_high->metal_4h` score `-2.9688` n `237` status `ready` deltaP `-13.1496` edge `-0.0546` maxDD `-11.7351`
- `market_context_high->commodity_4h` score `-3.9102` n `237` status `ready` deltaP `-3.2546` edge `-0.0366` maxDD `-14.071`
- `market_context_high->crypto_major_24h` score `-4.1424` n `174` status `ready` deltaP `5.1186` edge `0.0747` maxDD `-29.6555`
- `market_context_high->metal_24h` score `-8.2607` n `174` status `ready` deltaP `-10.9315` edge `-0.2501` maxDD `-32.8874`
- `market_context_high->commodity_24h` score `-13.314` n `174` status `ready` deltaP `-18.1513` edge `-0.1276` maxDD `-45.8715`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
