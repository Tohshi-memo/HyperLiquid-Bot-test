# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-05T14:07:32.888621+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `8444`

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

- `market_context_high->crypto_major_24h` score `10.94` n `82` status `ready` deltaP `29.8484` edge `0.7263` maxDD `-0.423`
- `news_risk_high->crypto_major_4h` score `9.3804` n `65` status `ready` deltaP `32.704` edge `0.584` maxDD `-0.6258`
- `market_context_high->crypto_alt_24h` score `6.189` n `82` status `ready` deltaP `25.487` edge `0.4078` maxDD `-2.9571`
- `news_risk_high->crypto_alt_4h` score `5.7094` n `65` status `ready` deltaP `19.6341` edge `0.4793` maxDD `-6.4195`
- `news_risk_high->index_24h` score `3.4585` n `65` status `ready` deltaP `24.8264` edge `0.1227` maxDD `0.0`
- `news_risk_high->equity_24h` score `3.0257` n `65` status `ready` deltaP `9.8184` edge `0.1967` maxDD `-0.1344`
- `news_risk_high->index_4h` score `2.8819` n `65` status `ready` deltaP `31.9137` edge `0.0536` maxDD `-0.4296`
- `market_context_high->crypto_major_4h` score `2.7876` n `118` status `ready` deltaP `13.2777` edge `0.2402` maxDD `-4.047`
- `news_risk_high->crypto_major_1h` score `2.4425` n `65` status `ready` deltaP `9.567` edge `0.1753` maxDD `-1.5096`
- `news_risk_high->equity_4h` score `2.4224` n `65` status `ready` deltaP `20.5769` edge `0.1257` maxDD `-2.881`
- `news_risk_high->index_1h` score `2.0279` n `65` status `ready` deltaP `25.1681` edge `0.0162` maxDD `-0.1997`
- `news_risk_high->metal_4h` score `1.7976` n `65` status `ready` deltaP `17.0967` edge `0.0774` maxDD `-0.993`
- `market_context_high->fx_4h` score `1.522` n `118` status `ready` deltaP `26.4004` edge `0.0265` maxDD `-0.3868`
- `news_risk_high->crypto_alt_1h` score `1.1085` n `65` status `ready` deltaP `3.3717` edge `0.1218` maxDD `-2.4854`
- `market_context_high->equity_24h` score `1.0588` n `82` status `ready` deltaP `13.5332` edge `0.0041` maxDD `-0.1536`
- `market_context_high->fx_1h` score `0.9377` n `121` status `ready` deltaP `15.0492` edge `0.0062` maxDD `-0.271`
- `market_context_high->metal_24h` score `0.8855` n `82` status `ready` deltaP `26.6429` edge `0.075` maxDD `-5.7943`
- `market_context_high->commodity_4h` score `0.7747` n `118` status `ready` deltaP `12.6937` edge `0.047` maxDD `-1.3656`
- `news_risk_high->commodity_24h` score `0.4294` n `65` status `ready` deltaP `24.9119` edge `0.0921` maxDD `-10.9169`
- `market_context_high->crypto_alt_4h` score `0.3748` n `118` status `ready` deltaP `-0.1964` edge `0.2049` maxDD `-7.1222`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
