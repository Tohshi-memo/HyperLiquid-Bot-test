# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-02T15:52:33.462527+00:00`
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

- `risk_on_high->unknown_4h` score `7.0114` n `107` status `ready` deltaP `16.5617` edge `0.5357` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `7.0114` n `107` status `ready` deltaP `16.5617` edge `0.5357` maxDD `-2.2797`
- `risk_on_high->equity_24h` score `5.7199` n `107` status `ready` deltaP `26.3062` edge `0.7158` maxDD `-19.828`
- `risk_on_and_context->equity_24h` score `5.7199` n `107` status `ready` deltaP `26.3062` edge `0.7158` maxDD `-19.828`
- `market_context_high->unknown_4h` score `5.092` n `147` status `ready` deltaP `12.2957` edge `0.4119` maxDD `-2.563`
- `news_risk_high->equity_24h` score `2.72` n `59` status `ready` deltaP `12.2558` edge `0.3917` maxDD `-15.4056`
- `market_context_high->equity_24h` score `2.0633` n `147` status `ready` deltaP `22.2754` edge `0.5969` maxDD `-24.4698`
- `risk_on_high->unknown_1h` score `1.6102` n `107` status `ready` deltaP `2.1742` edge `0.1774` maxDD `-1.95`
- `risk_on_and_context->unknown_1h` score `1.6102` n `107` status `ready` deltaP `2.1742` edge `0.1774` maxDD `-1.95`
- `news_risk_high->unknown_1h` score `1.0775` n `67` status `ready` deltaP `2.8019` edge `0.1058` maxDD `-1.1086`
- `risk_on_high->crypto_alt_24h` score `0.563` n `107` status `ready` deltaP `16.2221` edge `0.6544` maxDD `-42.8959`
- `risk_on_and_context->crypto_alt_24h` score `0.563` n `107` status `ready` deltaP `16.2221` edge `0.6544` maxDD `-42.8959`
- `news_risk_high->crypto_alt_24h` score `0.5341` n `59` status `ready` deltaP `16.1429` edge `0.2543` maxDD `-19.4761`
- `market_context_high->unknown_1h` score `0.2803` n `147` status `ready` deltaP `0.5276` edge `0.0829` maxDD `-2.0446`
- `news_risk_high->commodity_4h` score `0.1821` n `63` status `ready` deltaP `5.3499` edge `0.0236` maxDD `-0.8733`
- `risk_on_high->index_4h` score `0.114` n `107` status `ready` deltaP `20.9355` edge `0.0081` maxDD `-3.6448`
- `risk_on_and_context->index_4h` score `0.114` n `107` status `ready` deltaP `20.9355` edge `0.0081` maxDD `-3.6448`
- `risk_on_high->index_1h` score `0.0909` n `107` status `ready` deltaP `7.9439` edge `0.0032` maxDD `-0.5605`
- `risk_on_and_context->index_1h` score `0.0909` n `107` status `ready` deltaP `7.9439` edge `0.0032` maxDD `-0.5605`
- `news_risk_high->index_1h` score `-0.0095` n `67` status `ready` deltaP `5.2239` edge `-0.0007` maxDD `-0.8275`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
