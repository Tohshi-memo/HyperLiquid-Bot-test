# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-12T22:07:26.745573+00:00`
- Price records: `672`
- Market context records: `6545`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9854`

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

- `market_context_high->unknown_24h` score `6.4135` n `144` status `ready` deltaP `11.8934` edge `0.7852` maxDD `-15.0689`
- `news_risk_high->fx_4h` score `3.7068` n `34` status `ready` deltaP `39.1499` edge `0.0525` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.2697` n `34` status `ready` deltaP `28.0204` edge `0.0204` maxDD `-0.1113`
- `market_context_high->unknown_1h` score `2.0257` n `198` status `ready` deltaP `-5.8928` edge `0.2982` maxDD `-3.2083`
- `market_context_high->commodity_24h` score `1.3249` n `144` status `ready` deltaP `12.784` edge `0.212` maxDD `-5.2791`
- `market_context_high->index_4h` score `0.5073` n `190` status `ready` deltaP `12.4069` edge `0.0272` maxDD `-0.4108`
- `news_risk_high->crypto_major_1h` score `0.4651` n `34` status `ready` deltaP `4.2357` edge `0.0851` maxDD `-2.6299`
- `market_context_high->crypto_alt_4h` score `0.2668` n `190` status `ready` deltaP `9.3758` edge `0.1151` maxDD `-6.7632`
- `news_risk_high->crypto_alt_1h` score `-0.2656` n `34` status `ready` deltaP `-2.7915` edge `0.0355` maxDD `-2.0756`
- `market_context_high->equity_4h` score `-0.2663` n `190` status `ready` deltaP `11.1361` edge `0.0615` maxDD `-8.2573`
- `market_context_high->crypto_major_4h` score `-0.4354` n `190` status `ready` deltaP `11.8694` edge `0.0941` maxDD `-12.6576`
- `market_context_high->fx_1h` score `-0.438` n `198` status `ready` deltaP `-0.5595` edge `-0.0017` maxDD `-0.7249`
- `market_context_high->commodity_1h` score `-0.494` n `198` status `ready` deltaP `1.0464` edge `-0.002` maxDD `-2.1314`
- `market_context_high->crypto_alt_1h` score `-0.5654` n `198` status `ready` deltaP `6.2103` edge `0.0174` maxDD `-5.8368`
- `market_context_high->crypto_major_1h` score `-0.5839` n `198` status `ready` deltaP `5.9291` edge `0.0122` maxDD `-6.7936`
- `market_context_high->equity_1h` score `-0.6887` n `198` status `ready` deltaP `2.8988` edge `0.0034` maxDD `-4.2147`
- `market_context_high->index_1h` score `-0.7759` n `198` status `ready` deltaP `0.4491` edge `0.0043` maxDD `-0.7564`
- `news_risk_high->metal_1h` score `-0.9348` n `34` status `ready` deltaP `-5.2307` edge `-0.0226` maxDD `-1.6568`
- `market_context_high->metal_4h` score `-0.9829` n `190` status `ready` deltaP `0.9323` edge `0.0386` maxDD `-2.6662`
- `market_context_high->unknown_4h` score `-1.0947` n `190` status `ready` deltaP `-19.5683` edge `0.2798` maxDD `-10.5788`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
