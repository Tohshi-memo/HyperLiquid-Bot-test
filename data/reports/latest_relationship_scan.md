# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-05T03:07:24.580528+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5368`

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

- `market_context_high->unknown_1h` score `117.5394` n `99` status `ready` deltaP `-1.0781` edge `9.8436` maxDD `-0.9839`
- `market_context_high->unknown_4h` score `71.6584` n `95` status `ready` deltaP `2.4743` edge `5.9862` maxDD `-0.4928`
- `market_context_high->crypto_major_24h` score `11.1028` n `56` status `ready` deltaP `30.2332` edge `0.7373` maxDD `-0.423`
- `market_context_high->crypto_alt_24h` score `9.8726` n `56` status `ready` deltaP `25.3472` edge `0.7157` maxDD `-2.9571`
- `news_risk_high->crypto_major_4h` score `9.3465` n `65` status `ready` deltaP `32.3992` edge `0.5832` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `6.1782` n `65` status `ready` deltaP `20.2439` edge `0.5143` maxDD `-6.4195`
- `news_risk_high->equity_24h` score `4.4123` n `65` status `ready` deltaP `15.7212` edge `0.2729` maxDD `-0.1344`
- `market_context_high->crypto_major_4h` score `4.2392` n `95` status `ready` deltaP `17.9862` edge `0.3037` maxDD `-3.294`
- `news_risk_high->index_24h` score `3.3997` n `65` status `ready` deltaP `23.6111` edge `0.1259` maxDD `0.0`
- `news_risk_high->index_4h` score `2.8889` n `65` status `ready` deltaP `31.7613` edge `0.0552` maxDD `-0.4296`
- `news_risk_high->equity_4h` score `2.7924` n `65` status `ready` deltaP `20.8818` edge `0.1545` maxDD `-2.881`
- `news_risk_high->crypto_major_1h` score `2.5204` n `65` status `ready` deltaP `10.1658` edge `0.1778` maxDD `-1.5096`
- `market_context_high->crypto_major_1h` score `2.1263` n `99` status `ready` deltaP `14.7191` edge `0.1241` maxDD `-2.2692`
- `news_risk_high->index_1h` score `2.0722` n `65` status `ready` deltaP `25.6172` edge `0.0169` maxDD `-0.1997`
- `news_risk_high->metal_4h` score `2.0481` n `65` status `ready` deltaP `18.7735` edge `0.0871` maxDD `-0.993`
- `market_context_high->fx_24h` score `1.6104` n `56` status `ready` deltaP `20.2381` edge `0.0914` maxDD `-1.703`
- `market_context_high->equity_24h` score `1.5101` n `56` status `ready` deltaP `4.0179` edge `0.1193` maxDD `-0.6196`
- `market_context_high->fx_4h` score `1.4855` n `95` status `ready` deltaP `25.6291` edge `0.0286` maxDD `-0.3868`
- `news_risk_high->crypto_alt_1h` score `1.2716` n `65` status `ready` deltaP `3.9705` edge `0.1314` maxDD `-2.4854`
- `market_context_high->crypto_alt_4h` score `1.058` n `95` status `ready` deltaP `3.4018` edge `0.2444` maxDD `-7.6465`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
