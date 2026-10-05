# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-05T14:22:37.229782+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `8492`

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

- `market_context_high->crypto_major_24h` score `10.928` n `82` status `ready` deltaP `29.8484` edge `0.7253` maxDD `-0.423`
- `news_risk_high->crypto_major_4h` score `9.3852` n `65` status `ready` deltaP `32.704` edge `0.5844` maxDD `-0.6258`
- `market_context_high->crypto_alt_24h` score `6.2022` n `82` status `ready` deltaP `25.487` edge `0.4089` maxDD `-2.9571`
- `news_risk_high->crypto_alt_4h` score `5.7312` n `65` status `ready` deltaP `19.7866` edge `0.4801` maxDD `-6.4195`
- `news_risk_high->index_24h` score `3.4422` n `65` status `ready` deltaP `24.6528` edge `0.1225` maxDD `0.0`
- `news_risk_high->equity_24h` score `3.0269` n `65` status `ready` deltaP `9.8184` edge `0.1968` maxDD `-0.1344`
- `news_risk_high->index_4h` score `2.8795` n `65` status `ready` deltaP `31.9137` edge `0.0534` maxDD `-0.4296`
- `market_context_high->crypto_major_4h` score `2.7866` n `119` status `ready` deltaP `13.5055` edge `0.2386` maxDD `-4.047`
- `news_risk_high->crypto_major_1h` score `2.4089` n `65` status `ready` deltaP `9.4173` edge `0.1735` maxDD `-1.5096`
- `news_risk_high->equity_4h` score `2.4066` n `65` status `ready` deltaP `20.4245` edge `0.1254` maxDD `-2.881`
- `news_risk_high->index_1h` score `2.0123` n `65` status `ready` deltaP `25.0184` edge `0.0159` maxDD `-0.1997`
- `news_risk_high->metal_4h` score `1.7976` n `65` status `ready` deltaP `17.0967` edge `0.0774` maxDD `-0.993`
- `market_context_high->fx_4h` score `1.482` n `119` status `ready` deltaP `25.9903` edge `0.0259` maxDD `-0.3868`
- `news_risk_high->crypto_alt_1h` score `1.0821` n `65` status `ready` deltaP `3.3717` edge `0.1196` maxDD `-2.4854`
- `market_context_high->equity_24h` score `1.06` n `82` status `ready` deltaP `13.5332` edge `0.0042` maxDD `-0.1536`
- `market_context_high->fx_1h` score `0.9521` n `121` status `ready` deltaP `15.1989` edge `0.0064` maxDD `-0.271`
- `market_context_high->metal_24h` score `0.8718` n `82` status `ready` deltaP `26.4693` edge `0.0744` maxDD `-5.7943`
- `market_context_high->commodity_4h` score `0.666` n `119` status `ready` deltaP `12.181` edge `0.0443` maxDD `-1.6002`
- `news_risk_high->commodity_24h` score `0.4263` n `65` status `ready` deltaP `24.9119` edge `0.0917` maxDD `-10.9169`
- `market_context_high->crypto_alt_4h` score `0.3069` n `119` status `ready` deltaP `-0.5495` edge `0.2016` maxDD `-7.1222`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
