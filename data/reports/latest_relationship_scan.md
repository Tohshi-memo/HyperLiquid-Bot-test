# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-04T02:37:29.368534+00:00`
- Price records: `672`
- Market context records: `5619`
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

- `market_context_high->equity_24h` score `3.1123` n `174` status `ready` deltaP `15.0084` edge `0.6672` maxDD `-31.6316`
- `market_context_high->fx_24h` score `1.322` n `174` status `ready` deltaP `22.1325` edge `0.06` maxDD `-1.457`
- `market_context_high->crypto_major_4h` score `1.096` n `231` status `ready` deltaP `12.4169` edge `0.2378` maxDD `-14.0065`
- `market_context_high->equity_4h` score `0.3962` n `231` status `ready` deltaP `6.417` edge `0.1541` maxDD `-7.4425`
- `market_context_high->crypto_alt_4h` score `0.3861` n `231` status `ready` deltaP `7.1792` edge `0.1484` maxDD `-9.46`
- `market_context_high->fx_1h` score `-0.2797` n `237` status `ready` deltaP `1.5993` edge `0.0011` maxDD `-0.4764`
- `market_context_high->equity_1h` score `-0.3247` n `237` status `ready` deltaP `5.9148` edge `0.0342` maxDD `-5.0555`
- `market_context_high->metal_1h` score `-0.5005` n `237` status `ready` deltaP `0.4421` edge `0.0004` maxDD `-2.0682`
- `market_context_high->crypto_major_1h` score `-0.5078` n `237` status `ready` deltaP `5.0292` edge `0.0487` maxDD `-6.9639`
- `market_context_high->crypto_alt_1h` score `-0.5889` n `237` status `ready` deltaP `1.2867` edge `0.0385` maxDD `-5.0257`
- `market_context_high->index_1h` score `-0.9166` n `237` status `ready` deltaP `0.7283` edge `0.0056` maxDD `-0.9472`
- `market_context_high->commodity_1h` score `-1.0956` n `237` status `ready` deltaP `-1.3271` edge `-0.0059` maxDD `-3.7906`
- `market_context_high->fx_4h` score `-1.3133` n `231` status `ready` deltaP `1.0882` edge `0.0067` maxDD `-1.2528`
- `market_context_high->index_4h` score `-1.8064` n `231` status `ready` deltaP `0.0944` edge `0.01` maxDD `-2.8928`
- `market_context_high->index_24h` score `-2.3839` n `174` status `ready` deltaP `10.0874` edge `0.0258` maxDD `-16.8946`
- `market_context_high->crypto_major_24h` score `-2.5018` n `174` status `ready` deltaP `7.8963` edge `0.1929` maxDD `-29.6555`
- `market_context_high->metal_4h` score `-2.8614` n `231` status `ready` deltaP `-11.173` edge `-0.054` maxDD `-11.7351`
- `market_context_high->commodity_4h` score `-4.1182` n `231` status `ready` deltaP `-5.3743` edge `-0.0398` maxDD `-14.071`
- `market_context_high->metal_24h` score `-8.2748` n `174` status `ready` deltaP `-10.9315` edge `-0.2519` maxDD `-32.8874`
- `market_context_high->crypto_alt_24h` score `-12.3451` n `174` status `ready` deltaP `-2.3168` edge `-0.1436` maxDD `-54.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
