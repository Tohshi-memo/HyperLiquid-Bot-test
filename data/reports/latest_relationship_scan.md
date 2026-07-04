# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-04T04:22:25.324369+00:00`
- Price records: `672`
- Market context records: `5626`
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

- `market_context_high->equity_24h` score `2.9971` n `174` status `ready` deltaP `15.0084` edge `0.6576` maxDD `-31.6316`
- `market_context_high->fx_24h` score `1.3448` n `174` status `ready` deltaP `22.1325` edge `0.0619` maxDD `-1.457`
- `market_context_high->crypto_major_4h` score `0.8732` n `237` status `ready` deltaP `11.4618` edge `0.2256` maxDD `-14.0065`
- `market_context_high->equity_4h` score `0.4685` n `237` status `ready` deltaP `7.3814` edge `0.1537` maxDD `-7.4425`
- `market_context_high->crypto_alt_4h` score `-0.1414` n `237` status `ready` deltaP `5.7644` edge `0.1347` maxDD `-9.46`
- `market_context_high->fx_1h` score `-0.2883` n `237` status `ready` deltaP `1.4496` edge `0.001` maxDD `-0.4764`
- `market_context_high->equity_1h` score `-0.3942` n `237` status `ready` deltaP `5.1663` edge `0.0334` maxDD `-5.0555`
- `market_context_high->metal_1h` score `-0.5325` n `237` status `ready` deltaP `-0.1567` edge `0.0003` maxDD `-2.0682`
- `market_context_high->crypto_major_1h` score `-0.611` n `237` status `ready` deltaP `4.4304` edge `0.0441` maxDD `-6.9639`
- `market_context_high->crypto_alt_1h` score `-0.6621` n `237` status `ready` deltaP `0.9873` edge `0.0344` maxDD `-5.0257`
- `market_context_high->index_1h` score `-0.9549` n `237` status `ready` deltaP `0.2792` edge `0.0054` maxDD `-0.9472`
- `market_context_high->commodity_1h` score `-1.0716` n `237` status `ready` deltaP `-1.0277` edge `-0.0059` maxDD `-3.7906`
- `market_context_high->fx_4h` score `-1.3335` n `237` status `ready` deltaP `0.9133` edge `0.0063` maxDD `-1.335`
- `market_context_high->index_4h` score `-1.9308` n `237` status `ready` deltaP `-0.4695` edge `0.0094` maxDD `-3.04`
- `market_context_high->index_24h` score `-2.3738` n `174` status `ready` deltaP `10.0874` edge `0.0271` maxDD `-16.8946`
- `market_context_high->metal_4h` score `-2.8928` n `237` status `ready` deltaP `-11.7777` edge `-0.054` maxDD `-11.7351`
- `market_context_high->crypto_major_24h` score `-3.2302` n `174` status `ready` deltaP `6.6811` edge `0.1403` maxDD `-29.6555`
- `market_context_high->commodity_4h` score `-4.0392` n `237` status `ready` deltaP `-4.6265` edge `-0.0382` maxDD `-14.071`
- `market_context_high->metal_24h` score `-8.2654` n `174` status `ready` deltaP `-10.9315` edge `-0.2507` maxDD `-32.8874`
- `market_context_high->crypto_alt_24h` score `-12.8959` n `174` status `ready` deltaP `-3.5321` edge `-0.1814` maxDD `-54.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
