# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-03T17:37:30.926963+00:00`
- Price records: `672`
- Market context records: `5580`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11413`

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

- `market_context_high->equity_24h` score `4.1515` n `174` status `ready` deltaP `15.0084` edge `0.7538` maxDD `-31.6316`
- `market_context_high->crypto_major_4h` score `1.1995` n `195` status `ready` deltaP `11.3861` edge `0.2533` maxDD `-14.0065`
- `market_context_high->fx_24h` score `0.8836` n `174` status `ready` deltaP `17.7922` edge `0.0524` maxDD `-1.457`
- `market_context_high->crypto_major_24h` score `0.6918` n `174` status `ready` deltaP `13.4519` edge `0.422` maxDD `-29.6555`
- `market_context_high->crypto_alt_4h` score `0.6145` n `195` status `ready` deltaP `6.8543` edge `0.1696` maxDD `-9.46`
- `market_context_high->equity_4h` score `0.5654` n `195` status `ready` deltaP `5.6074` edge `0.1736` maxDD `-7.4425`
- `market_context_high->index_1h` score `-0.2007` n `207` status `ready` deltaP `3.6774` edge `0.0081` maxDD `-0.9472`
- `market_context_high->equity_1h` score `-0.2833` n `207` status `ready` deltaP `5.8477` edge `0.0381` maxDD `-5.0555`
- `market_context_high->fx_4h` score `-0.3496` n `195` status `ready` deltaP `5.2885` edge `0.009` maxDD `-0.8712`
- `market_context_high->metal_1h` score `-0.5133` n `207` status `ready` deltaP `0.0918` edge `0.0011` maxDD `-2.0682`
- `market_context_high->fx_1h` score `-0.5155` n `207` status `ready` deltaP `0.4592` edge `0.0008` maxDD `-0.4122`
- `market_context_high->crypto_alt_1h` score `-0.6004` n `207` status `ready` deltaP `0.9626` edge `0.0397` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `-0.7511` n `207` status `ready` deltaP `2.589` edge `0.0447` maxDD `-6.9639`
- `market_context_high->commodity_1h` score `-1.201` n `207` status `ready` deltaP `-2.2556` edge `-0.0085` maxDD `-3.7906`
- `market_context_high->index_4h` score `-1.5181` n `195` status `ready` deltaP `2.8072` edge `0.0157` maxDD `-2.874`
- `market_context_high->index_24h` score `-2.0738` n `174` status `ready` deltaP `12.6916` edge `0.0482` maxDD `-16.8946`
- `market_context_high->metal_4h` score `-3.0556` n `195` status `ready` deltaP `-13.7977` edge `-0.0614` maxDD `-11.7351`
- `market_context_high->commodity_4h` score `-4.3234` n `195` status `ready` deltaP `-6.2445` edge `-0.0511` maxDD `-14.071`
- `market_context_high->metal_24h` score `-7.9268` n `174` status `ready` deltaP `-8.1537` edge `-0.2258` maxDD `-32.8874`
- `market_context_high->crypto_alt_24h` score `-9.356` n `174` status `ready` deltaP `3.4124` edge `0.0673` maxDD `-54.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
