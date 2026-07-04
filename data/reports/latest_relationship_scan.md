# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-04T02:22:30.291235+00:00`
- Price records: `672`
- Market context records: `5618`
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

- `market_context_high->equity_24h` score `3.1315` n `174` status `ready` deltaP `15.0084` edge `0.6688` maxDD `-31.6316`
- `market_context_high->fx_24h` score `1.3196` n `174` status `ready` deltaP `22.1325` edge `0.0598` maxDD `-1.457`
- `market_context_high->crypto_major_4h` score `1.1541` n `230` status `ready` deltaP `12.6935` edge `0.2408` maxDD `-14.0065`
- `market_context_high->crypto_alt_4h` score `0.4449` n `230` status `ready` deltaP `7.4483` edge `0.1515` maxDD `-9.46`
- `market_context_high->equity_4h` score `0.3889` n `230` status `ready` deltaP `6.2513` edge `0.1546` maxDD `-7.4425`
- `market_context_high->fx_1h` score `-0.2797` n `237` status `ready` deltaP `1.5993` edge `0.0011` maxDD `-0.4764`
- `market_context_high->equity_1h` score `-0.3235` n `237` status `ready` deltaP `5.9148` edge `0.0343` maxDD `-5.0555`
- `market_context_high->metal_1h` score `-0.5005` n `237` status `ready` deltaP `0.4421` edge `0.0004` maxDD `-2.0682`
- `market_context_high->crypto_major_1h` score `-0.5198` n `237` status `ready` deltaP `4.8795` edge `0.0487` maxDD `-6.9639`
- `market_context_high->crypto_alt_1h` score `-0.5697` n `237` status `ready` deltaP `1.4364` edge `0.0391` maxDD `-5.0257`
- `market_context_high->index_1h` score `-0.9046` n `237` status `ready` deltaP `0.878` edge `0.0056` maxDD `-0.9472`
- `market_context_high->commodity_1h` score `-1.1087` n `237` status `ready` deltaP `-1.4768` edge `-0.006` maxDD `-3.7906`
- `market_context_high->fx_4h` score `-1.3077` n `230` status `ready` deltaP `1.1691` edge `0.0068` maxDD `-1.2461`
- `market_context_high->index_4h` score `-1.7829` n `230` status `ready` deltaP `0.3221` edge `0.0102` maxDD `-2.874`
- `market_context_high->index_24h` score `-2.3847` n `174` status `ready` deltaP `10.0874` edge `0.0257` maxDD `-16.8946`
- `market_context_high->crypto_major_24h` score `-2.4039` n `174` status `ready` deltaP `8.07` edge `0.1999` maxDD `-29.6555`
- `market_context_high->metal_4h` score `-2.8619` n `230` status `ready` deltaP `-11.1691` edge `-0.0541` maxDD `-11.7351`
- `market_context_high->commodity_4h` score `-4.1206` n `230` status `ready` deltaP `-5.3592` edge `-0.0401` maxDD `-14.071`
- `market_context_high->metal_24h` score `-8.2771` n `174` status `ready` deltaP `-10.9315` edge `-0.2522` maxDD `-32.8874`
- `market_context_high->crypto_alt_24h` score `-12.2664` n `174` status `ready` deltaP `-2.1432` edge `-0.1382` maxDD `-54.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
