# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-02T17:37:31.666189+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11555`

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

- `risk_on_high->unknown_4h` score `7.009` n `107` status `ready` deltaP `16.5617` edge `0.5355` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `7.009` n `107` status `ready` deltaP `16.5617` edge `0.5355` maxDD `-2.2797`
- `risk_on_high->equity_24h` score `6.0713` n `107` status `ready` deltaP `27.1742` edge `0.7393` maxDD `-19.828`
- `risk_on_and_context->equity_24h` score `6.0713` n `107` status `ready` deltaP `27.1742` edge `0.7393` maxDD `-19.828`
- `market_context_high->unknown_4h` score `5.0896` n `147` status `ready` deltaP `12.2957` edge `0.4117` maxDD `-2.563`
- `news_risk_high->equity_24h` score `3.0715` n `59` status `ready` deltaP `13.1238` edge `0.4152` maxDD `-15.4056`
- `market_context_high->equity_24h` score `2.2918` n `147` status `ready` deltaP `23.1434` edge `0.6204` maxDD `-24.4698`
- `risk_on_high->crypto_alt_24h` score `1.0841` n `107` status `ready` deltaP `17.4374` edge `0.7131` maxDD `-42.8959`
- `risk_on_and_context->crypto_alt_24h` score `1.0841` n `107` status `ready` deltaP `17.4374` edge `0.7131` maxDD `-42.8959`
- `news_risk_high->crypto_alt_24h` score `1.0551` n `59` status `ready` deltaP `17.3582` edge `0.313` maxDD `-19.4761`
- `risk_on_high->unknown_1h` score `1.0103` n `107` status `ready` deltaP `2.0245` edge `0.1284` maxDD `-1.95`
- `risk_on_and_context->unknown_1h` score `1.0103` n `107` status `ready` deltaP `2.0245` edge `0.1284` maxDD `-1.95`
- `news_risk_high->unknown_1h` score `0.4775` n `67` status `ready` deltaP `2.6522` edge `0.0568` maxDD `-1.1086`
- `news_risk_high->commodity_4h` score `0.2744` n `66` status `ready` deltaP `6.0144` edge `0.031` maxDD `-0.8733`
- `risk_on_high->index_1h` score `0.1158` n `107` status `ready` deltaP `8.393` edge `0.0034` maxDD `-0.5605`
- `risk_on_and_context->index_1h` score `0.1158` n `107` status `ready` deltaP `8.393` edge `0.0034` maxDD `-0.5605`
- `risk_on_high->index_4h` score `0.1116` n `107` status `ready` deltaP `20.9355` edge `0.0078` maxDD `-3.6448`
- `risk_on_and_context->index_4h` score `0.1116` n `107` status `ready` deltaP `20.9355` edge `0.0078` maxDD `-3.6448`
- `news_risk_high->index_1h` score `0.0154` n `67` status `ready` deltaP `5.673` edge `-0.0005` maxDD `-0.8275`
- `risk_on_high->metal_1h` score `-0.0225` n `107` status `ready` deltaP `10.4483` edge `-0.0013` maxDD `-1.699`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
