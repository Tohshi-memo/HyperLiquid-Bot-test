# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-04T04:37:29.762573+00:00`
- Price records: `672`
- Market context records: `5627`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `8743`

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

- `market_context_high->equity_24h` score `2.9863` n `174` status `ready` deltaP `15.0084` edge `0.6567` maxDD `-31.6316`
- `market_context_high->fx_24h` score `1.3484` n `174` status `ready` deltaP `22.1325` edge `0.0622` maxDD `-1.457`
- `market_context_high->crypto_major_4h` score `0.849` n `237` status `ready` deltaP `11.3094` edge `0.2246` maxDD `-14.0065`
- `market_context_high->equity_4h` score `0.4673` n `237` status `ready` deltaP `7.3814` edge `0.1536` maxDD `-7.4425`
- `market_context_high->crypto_alt_4h` score `-0.1474` n `237` status `ready` deltaP `5.7644` edge `0.1342` maxDD `-9.46`
- `market_context_high->fx_1h` score `-0.2883` n `237` status `ready` deltaP `1.4496` edge `0.001` maxDD `-0.4764`
- `market_context_high->equity_1h` score `-0.4074` n `237` status `ready` deltaP `5.0166` edge `0.0333` maxDD `-5.0555`
- `market_context_high->metal_1h` score `-0.5402` n `237` status `ready` deltaP `-0.3064` edge `0.0003` maxDD `-2.0682`
- `market_context_high->crypto_major_1h` score `-0.6349` n `237` status `ready` deltaP `4.2807` edge `0.0431` maxDD `-6.9639`
- `market_context_high->crypto_alt_1h` score `-0.6669` n `237` status `ready` deltaP `0.9873` edge `0.034` maxDD `-5.0257`
- `market_context_high->index_1h` score `-0.9549` n `237` status `ready` deltaP `0.2792` edge `0.0054` maxDD `-0.9472`
- `market_context_high->commodity_1h` score `-1.0584` n `237` status `ready` deltaP `-0.878` edge `-0.0058` maxDD `-3.7906`
- `market_context_high->fx_4h` score `-1.3256` n `237` status `ready` deltaP `1.0658` edge `0.0063` maxDD `-1.335`
- `market_context_high->index_4h` score `-1.9442` n `237` status `ready` deltaP `-0.6219` edge `0.0093` maxDD `-3.04`
- `market_context_high->index_24h` score `-2.3707` n `174` status `ready` deltaP `10.0874` edge `0.0275` maxDD `-16.8946`
- `market_context_high->metal_4h` score `-2.9007` n `237` status `ready` deltaP `-11.9301` edge `-0.054` maxDD `-11.7351`
- `market_context_high->crypto_major_24h` score `-3.3473` n `174` status `ready` deltaP `6.5075` edge `0.1317` maxDD `-29.6555`
- `market_context_high->commodity_4h` score `-4.0246` n `237` status `ready` deltaP `-4.4741` edge `-0.038` maxDD `-14.071`
- `market_context_high->metal_24h` score `-8.2639` n `174` status `ready` deltaP `-10.9315` edge `-0.2505` maxDD `-32.8874`
- `market_context_high->crypto_alt_24h` score `-12.9758` n `174` status `ready` deltaP `-3.7057` edge `-0.1869` maxDD `-54.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
