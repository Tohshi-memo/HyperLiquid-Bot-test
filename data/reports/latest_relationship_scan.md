# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-04T06:07:31.708606+00:00`
- Price records: `672`
- Market context records: `5634`
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

- `market_context_high->equity_24h` score `2.9251` n `174` status `ready` deltaP `15.0084` edge `0.6516` maxDD `-31.6316`
- `market_context_high->fx_24h` score `1.3653` n `174` status `ready` deltaP `22.1325` edge `0.0636` maxDD `-1.457`
- `market_context_high->crypto_major_4h` score `0.7136` n `237` status `ready` deltaP `10.5472` edge `0.2184` maxDD `-14.0065`
- `market_context_high->equity_4h` score `0.4661` n `237` status `ready` deltaP `7.3814` edge `0.1535` maxDD `-7.4425`
- `market_context_high->crypto_alt_4h` score `-0.2514` n `237` status `ready` deltaP `5.1547` edge `0.1296` maxDD `-9.46`
- `market_context_high->fx_1h` score `-0.2883` n `237` status `ready` deltaP `1.4496` edge `0.001` maxDD `-0.4764`
- `market_context_high->equity_1h` score `-0.417` n `237` status `ready` deltaP `4.8669` edge `0.0335` maxDD `-5.0555`
- `market_context_high->metal_1h` score `-0.5325` n `237` status `ready` deltaP `-0.1567` edge `0.0003` maxDD `-2.0682`
- `market_context_high->crypto_major_1h` score `-0.6457` n `237` status `ready` deltaP `4.131` edge `0.0432` maxDD `-6.9639`
- `market_context_high->crypto_alt_1h` score `-0.6477` n `237` status `ready` deltaP `1.137` edge `0.0346` maxDD `-5.0257`
- `market_context_high->index_1h` score `-0.9418` n `237` status `ready` deltaP `0.4289` edge `0.0055` maxDD `-0.9472`
- `market_context_high->commodity_1h` score `-1.0572` n `237` status `ready` deltaP `-0.878` edge `-0.0057` maxDD `-3.7906`
- `market_context_high->fx_4h` score `-1.3335` n `237` status `ready` deltaP `0.9133` edge `0.0063` maxDD `-1.335`
- `market_context_high->index_4h` score `-1.9454` n `237` status `ready` deltaP `-0.6219` edge `0.0092` maxDD `-3.04`
- `market_context_high->index_24h` score `-2.3414` n `174` status `ready` deltaP `10.261` edge `0.0301` maxDD `-16.8946`
- `market_context_high->metal_4h` score `-2.9514` n `237` status `ready` deltaP `-12.8448` edge `-0.0544` maxDD `-11.7351`
- `market_context_high->commodity_4h` score `-3.9394` n `237` status `ready` deltaP `-3.5594` edge `-0.037` maxDD `-14.071`
- `market_context_high->crypto_major_24h` score `-3.9611` n `174` status `ready` deltaP `5.4658` edge `0.0875` maxDD `-29.6555`
- `market_context_high->metal_24h` score `-8.26` n `174` status `ready` deltaP `-10.9315` edge `-0.25` maxDD `-32.8874`
- `market_context_high->commodity_24h` score `-13.3586` n `174` status `ready` deltaP `-18.4985` edge `-0.129` maxDD `-45.8715`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
