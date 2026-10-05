# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-05T17:22:28.573103+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `8176`

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

- `market_context_high->crypto_major_24h` score `11.0308` n `78` status `ready` deltaP `30.2484` edge `0.7312` maxDD `-0.423`
- `news_risk_high->crypto_major_4h` score `9.66` n `65` status `ready` deltaP `33.6187` edge `0.6012` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `6.1504` n `65` status `ready` deltaP `21.0061` edge `0.5069` maxDD `-6.4195`
- `market_context_high->crypto_alt_24h` score `5.5919` n `78` status `ready` deltaP `26.7228` edge `0.3498` maxDD `-2.9571`
- `news_risk_high->index_24h` score `3.3807` n `65` status `ready` deltaP `23.9583` edge `0.122` maxDD `0.0`
- `news_risk_high->equity_24h` score `3.2189` n `65` status `ready` deltaP `9.8184` edge `0.2128` maxDD `-0.1344`
- `news_risk_high->index_4h` score `2.8273` n `65` status `ready` deltaP `31.4564` edge `0.0521` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.6296` n `65` status `ready` deltaP `10.4652` edge `0.1849` maxDD `-1.5096`
- `market_context_high->crypto_major_4h` score `2.5506` n `117` status `ready` deltaP `13.1059` edge `0.2216` maxDD `-4.047`
- `news_risk_high->equity_4h` score `2.366` n `65` status `ready` deltaP `19.6623` edge `0.1271` maxDD `-2.881`
- `news_risk_high->index_1h` score `1.9896` n `65` status `ready` deltaP `24.719` edge `0.016` maxDD `-0.1997`
- `news_risk_high->metal_4h` score `1.9093` n `65` status `ready` deltaP `18.1637` edge `0.0796` maxDD `-0.993`
- `market_context_high->fx_4h` score `1.6616` n `117` status `ready` deltaP `28.0397` edge `0.0272` maxDD `-0.3868`
- `news_risk_high->crypto_alt_1h` score `1.3124` n `65` status `ready` deltaP `4.2699` edge `0.1328` maxDD `-2.4854`
- `market_context_high->fx_1h` score `1.0833` n `117` status `ready` deltaP `16.7345` edge `0.0071` maxDD `-0.271`
- `market_context_high->commodity_4h` score `1.0283` n `117` status `ready` deltaP `14.9247` edge `0.0562` maxDD `-1.6002`
- `market_context_high->metal_24h` score `0.8394` n `78` status `ready` deltaP `25.9215` edge `0.0723` maxDD `-5.6663`
- `market_context_high->commodity_1h` score `0.6495` n `117` status `ready` deltaP `11.3069` edge `0.0184` maxDD `-0.5059`
- `market_context_high->equity_24h` score `0.618` n `78` status `ready` deltaP `13.4081` edge `-0.0318` maxDD `-0.1536`
- `news_risk_high->commodity_24h` score `0.3498` n `65` status `ready` deltaP `24.9119` edge `0.0819` maxDD `-10.9169`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
