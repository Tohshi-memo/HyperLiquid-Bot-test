# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-02T15:37:27.868874+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11537`

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

- `risk_on_high->unknown_4h` score `7.0258` n `107` status `ready` deltaP `16.5617` edge `0.5369` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `7.0258` n `107` status `ready` deltaP `16.5617` edge `0.5369` maxDD `-2.2797`
- `risk_on_high->equity_24h` score `5.6556` n `107` status `ready` deltaP `26.1325` edge `0.7116` maxDD `-19.828`
- `risk_on_and_context->equity_24h` score `5.6556` n `107` status `ready` deltaP `26.1325` edge `0.7116` maxDD `-19.828`
- `market_context_high->unknown_4h` score `5.1064` n `147` status `ready` deltaP `12.2957` edge `0.4131` maxDD `-2.563`
- `news_risk_high->equity_24h` score `2.6557` n `59` status `ready` deltaP `12.0821` edge `0.3875` maxDD `-15.4056`
- `market_context_high->equity_24h` score `2.0215` n `147` status `ready` deltaP `22.1017` edge `0.5927` maxDD `-24.4698`
- `risk_on_high->unknown_1h` score `1.6174` n `107` status `ready` deltaP `2.1742` edge `0.178` maxDD `-1.95`
- `risk_on_and_context->unknown_1h` score `1.6174` n `107` status `ready` deltaP `2.1742` edge `0.178` maxDD `-1.95`
- `news_risk_high->unknown_1h` score `1.04` n `66` status `ready` deltaP `2.2592` edge `0.1063` maxDD `-1.1086`
- `risk_on_high->crypto_alt_24h` score `0.4885` n `107` status `ready` deltaP `16.0485` edge `0.646` maxDD `-42.8959`
- `risk_on_and_context->crypto_alt_24h` score `0.4885` n `107` status `ready` deltaP `16.0485` edge `0.646` maxDD `-42.8959`
- `news_risk_high->crypto_alt_24h` score `0.4595` n `59` status `ready` deltaP `15.9693` edge `0.2459` maxDD `-19.4761`
- `market_context_high->unknown_1h` score `0.2875` n `147` status `ready` deltaP `0.5276` edge `0.0835` maxDD `-2.0446`
- `news_risk_high->commodity_4h` score `0.123` n `62` status `ready` deltaP `4.8879` edge `0.0191` maxDD `-0.8733`
- `risk_on_high->index_4h` score `0.1155` n `107` status `ready` deltaP `20.9355` edge `0.0083` maxDD `-3.6448`
- `risk_on_and_context->index_4h` score `0.1155` n `107` status `ready` deltaP `20.9355` edge `0.0083` maxDD `-3.6448`
- `risk_on_high->index_1h` score `0.0995` n `107` status `ready` deltaP `8.0936` edge `0.0033` maxDD `-0.5605`
- `risk_on_and_context->index_1h` score `0.0995` n `107` status `ready` deltaP `8.0936` edge `0.0033` maxDD `-0.5605`
- `news_risk_high->fx_4h` score `0.0202` n `62` status `ready` deltaP `9.2349` edge `0.0017` maxDD `-0.9269`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
