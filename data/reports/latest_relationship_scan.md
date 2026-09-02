# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-02T16:52:30.048283+00:00`
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

- `risk_on_high->unknown_4h` score `6.986` n `107` status `ready` deltaP `16.4093` edge `0.5346` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `6.986` n `107` status `ready` deltaP `16.4093` edge `0.5346` maxDD `-2.2797`
- `risk_on_high->equity_24h` score `5.9272` n `107` status `ready` deltaP `26.827` edge `0.7296` maxDD `-19.828`
- `risk_on_and_context->equity_24h` score `5.9272` n `107` status `ready` deltaP `26.827` edge `0.7296` maxDD `-19.828`
- `market_context_high->unknown_4h` score `5.0666` n `147` status `ready` deltaP `12.1433` edge `0.4108` maxDD `-2.563`
- `news_risk_high->equity_24h` score `2.9273` n `59` status `ready` deltaP `12.7766` edge `0.4055` maxDD `-15.4056`
- `market_context_high->equity_24h` score `2.1981` n `147` status `ready` deltaP `22.7962` edge `0.6107` maxDD `-24.4698`
- `risk_on_high->unknown_1h` score `1.0043` n `107` status `ready` deltaP `2.0245` edge `0.1279` maxDD `-1.95`
- `risk_on_and_context->unknown_1h` score `1.0043` n `107` status `ready` deltaP `2.0245` edge `0.1279` maxDD `-1.95`
- `risk_on_high->crypto_alt_24h` score `0.8464` n `107` status `ready` deltaP `16.9166` edge `0.6861` maxDD `-42.8959`
- `risk_on_and_context->crypto_alt_24h` score `0.8464` n `107` status `ready` deltaP `16.9166` edge `0.6861` maxDD `-42.8959`
- `news_risk_high->crypto_alt_24h` score `0.8174` n `59` status `ready` deltaP `16.8374` edge `0.286` maxDD `-19.4761`
- `news_risk_high->unknown_1h` score `0.4715` n `67` status `ready` deltaP `2.6522` edge `0.0563` maxDD `-1.1086`
- `news_risk_high->commodity_4h` score `0.2582` n `65` status `ready` deltaP `5.9123` edge `0.0296` maxDD `-0.8733`
- `risk_on_high->index_4h` score `0.1101` n `107` status `ready` deltaP `20.9355` edge `0.0076` maxDD `-3.6448`
- `risk_on_and_context->index_4h` score `0.1101` n `107` status `ready` deltaP `20.9355` edge `0.0076` maxDD `-3.6448`
- `risk_on_high->index_1h` score `0.0987` n `107` status `ready` deltaP `8.0936` edge `0.0032` maxDD `-0.5605`
- `risk_on_and_context->index_1h` score `0.0987` n `107` status `ready` deltaP `8.0936` edge `0.0032` maxDD `-0.5605`
- `news_risk_high->index_1h` score `-0.0017` n `67` status `ready` deltaP `5.3736` edge `-0.0007` maxDD `-0.8275`
- `risk_on_high->metal_1h` score `-0.0482` n `107` status `ready` deltaP `9.9992` edge `-0.0016` maxDD `-1.699`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
