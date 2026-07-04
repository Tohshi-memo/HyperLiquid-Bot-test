# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-04T02:07:27.108721+00:00`
- Price records: `672`
- Market context records: `5617`
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

- `market_context_high->equity_24h` score `3.1471` n `174` status `ready` deltaP `15.0084` edge `0.6701` maxDD `-31.6316`
- `market_context_high->fx_24h` score `1.3173` n `174` status `ready` deltaP `22.1325` edge `0.0596` maxDD `-1.457`
- `market_context_high->crypto_major_4h` score `1.2208` n `229` status `ready` deltaP `12.9726` edge `0.2445` maxDD `-14.0065`
- `market_context_high->crypto_alt_4h` score `0.5146` n `229` status `ready` deltaP `7.7198` edge `0.1555` maxDD `-9.46`
- `market_context_high->equity_4h` score `0.3962` n `229` status `ready` deltaP `6.2367` edge `0.1553` maxDD `-7.4425`
- `market_context_high->fx_1h` score `-0.2875` n `237` status `ready` deltaP `1.4496` edge `0.0011` maxDD `-0.4764`
- `market_context_high->equity_1h` score `-0.3235` n `237` status `ready` deltaP `5.9148` edge `0.0343` maxDD `-5.0555`
- `market_context_high->metal_1h` score `-0.5005` n `237` status `ready` deltaP `0.4421` edge `0.0004` maxDD `-2.0682`
- `market_context_high->crypto_major_1h` score `-0.5234` n `237` status `ready` deltaP `4.8795` edge `0.0484` maxDD `-6.9639`
- `market_context_high->crypto_alt_1h` score `-0.5721` n `237` status `ready` deltaP `1.4364` edge `0.0389` maxDD `-5.0257`
- `market_context_high->index_1h` score `-0.9046` n `237` status `ready` deltaP `0.878` edge `0.0056` maxDD `-0.9472`
- `market_context_high->commodity_1h` score `-1.1231` n `237` status `ready` deltaP `-1.6265` edge `-0.0062` maxDD `-3.7906`
- `market_context_high->fx_4h` score `-1.3012` n `229` status `ready` deltaP `1.2522` edge `0.0068` maxDD `-1.2246`
- `market_context_high->index_4h` score `-1.7622` n `229` status `ready` deltaP `0.5518` edge `0.0104` maxDD `-2.874`
- `market_context_high->crypto_major_24h` score `-2.312` n `174` status `ready` deltaP `8.2436` edge `0.2064` maxDD `-29.6555`
- `market_context_high->index_24h` score `-2.3863` n `174` status `ready` deltaP `10.0874` edge `0.0255` maxDD `-16.8946`
- `market_context_high->metal_4h` score `-2.8538` n `229` status `ready` deltaP `-11.0116` edge `-0.0541` maxDD `-11.7351`
- `market_context_high->commodity_4h` score `-4.1241` n `229` status `ready` deltaP `-5.3427` edge `-0.0405` maxDD `-14.071`
- `market_context_high->metal_24h` score `-8.2787` n `174` status `ready` deltaP `-10.9315` edge `-0.2524` maxDD `-32.8874`
- `market_context_high->crypto_alt_24h` score `-12.1925` n `174` status `ready` deltaP `-1.9696` edge `-0.1332` maxDD `-54.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
