# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-02T12:22:28.912951+00:00`
- Price records: `672`
- Market context records: `5454`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11440`

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

- `market_context_high->crypto_major_24h` score `3.5665` n `191` status `ready` deltaP `17.2248` edge `0.6364` maxDD `-29.6555`
- `market_context_high->crypto_major_4h` score `2.7506` n `197` status `ready` deltaP `15.1301` edge `0.3576` maxDD `-14.0065`
- `market_context_high->equity_4h` score `2.3193` n `197` status `ready` deltaP `12.2307` edge `0.2756` maxDD `-7.4425`
- `market_context_high->crypto_alt_4h` score `2.1041` n `197` status `ready` deltaP `10.2034` edge `0.2714` maxDD `-9.46`
- `market_context_high->equity_24h` score `0.8331` n `191` status `ready` deltaP `9.2714` edge `0.5102` maxDD `-31.5398`
- `market_context_high->equity_1h` score `0.4955` n `199` status `ready` deltaP `8.1628` edge `0.0834` maxDD `-5.0555`
- `market_context_high->index_1h` score `0.1546` n `199` status `ready` deltaP `6.7839` edge `0.017` maxDD `-0.9472`
- `market_context_high->fx_24h` score `0.1526` n `191` status `ready` deltaP `10.4621` edge `0.0325` maxDD `-0.8294`
- `market_context_high->metal_1h` score `-0.2341` n `199` status `ready` deltaP `4.1111` edge `0.0206` maxDD `-2.0682`
- `market_context_high->crypto_alt_1h` score `-0.3249` n `199` status `ready` deltaP `0.9569` edge `0.0627` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `-0.4375` n `199` status `ready` deltaP `2.1439` edge `0.0738` maxDD `-6.9639`
- `market_context_high->fx_1h` score `-0.5524` n `199` status `ready` deltaP `0.4115` edge `0.0001` maxDD `-0.577`
- `market_context_high->index_4h` score `-0.8638` n `197` status `ready` deltaP `7.1608` edge `0.0412` maxDD `-2.874`
- `market_context_high->fx_4h` score `-1.0719` n `197` status `ready` deltaP `1.3634` edge `0.0041` maxDD `-1.5345`
- `market_context_high->commodity_1h` score `-1.3529` n `199` status `ready` deltaP `-1.9724` edge `-0.0048` maxDD `-3.5831`
- `market_context_high->index_24h` score `-1.5266` n `191` status `ready` deltaP `13.9043` edge `0.0742` maxDD `-15.6753`
- `market_context_high->metal_4h` score `-2.59` n `197` status `ready` deltaP `-7.8146` edge `-0.0275` maxDD `-12.8631`
- `market_context_high->commodity_4h` score `-4.2708` n `197` status `ready` deltaP `-6.2337` edge `-0.0429` maxDD `-14.3822`
- `market_context_high->crypto_alt_24h` score `-7.2013` n `191` status `ready` deltaP `8.3106` edge `0.2142` maxDD `-54.2437`
- `market_context_high->metal_24h` score `-7.2137` n `191` status `ready` deltaP `-3.9403` edge `-0.1608` maxDD `-33.021`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
