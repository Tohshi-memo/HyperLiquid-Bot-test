# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-02T18:22:32.771775+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11557`

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

- `risk_on_high->unknown_4h` score `6.7766` n `107` status `ready` deltaP `16.8666` edge `0.5141` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `6.7766` n `107` status `ready` deltaP `16.8666` edge `0.5141` maxDD `-2.2797`
- `risk_on_high->equity_24h` score `6.1433` n `107` status `ready` deltaP `27.1742` edge `0.7453` maxDD `-19.828`
- `risk_on_and_context->equity_24h` score `6.1433` n `107` status `ready` deltaP `27.1742` edge `0.7453` maxDD `-19.828`
- `market_context_high->unknown_4h` score `4.8572` n `147` status `ready` deltaP `12.6006` edge `0.3903` maxDD `-2.563`
- `news_risk_high->equity_24h` score `3.1435` n `59` status `ready` deltaP `13.1238` edge `0.4212` maxDD `-15.4056`
- `market_context_high->equity_24h` score `2.3386` n `147` status `ready` deltaP `23.1434` edge `0.6264` maxDD `-24.4698`
- `risk_on_high->crypto_alt_24h` score `1.2573` n `107` status `ready` deltaP `17.7846` edge `0.733` maxDD `-42.8959`
- `risk_on_and_context->crypto_alt_24h` score `1.2573` n `107` status `ready` deltaP `17.7846` edge `0.733` maxDD `-42.8959`
- `news_risk_high->crypto_alt_24h` score `1.2284` n `59` status `ready` deltaP `17.7054` edge `0.3329` maxDD `-19.4761`
- `news_risk_high->commodity_4h` score `0.2358` n `66` status `ready` deltaP `5.5571` edge `0.0291` maxDD `-0.8733`
- `risk_on_high->index_4h` score `0.1179` n `107` status `ready` deltaP `20.9355` edge `0.0086` maxDD `-3.6448`
- `risk_on_and_context->index_4h` score `0.1179` n `107` status `ready` deltaP `20.9355` edge `0.0086` maxDD `-3.6448`
- `risk_on_high->index_1h` score `0.1072` n `107` status `ready` deltaP `8.2433` edge `0.0033` maxDD `-0.5605`
- `risk_on_and_context->index_1h` score `0.1072` n `107` status `ready` deltaP `8.2433` edge `0.0033` maxDD `-0.5605`
- `risk_on_high->unknown_1h` score `0.0899` n `107` status `ready` deltaP `1.5754` edge `0.0547` maxDD `-1.95`
- `risk_on_and_context->unknown_1h` score `0.0899` n `107` status `ready` deltaP `1.5754` edge `0.0547` maxDD `-1.95`
- `news_risk_high->index_1h` score `0.0069` n `67` status `ready` deltaP `5.5233` edge `-0.0006` maxDD `-0.8275`
- `risk_on_high->metal_1h` score `-0.0334` n `107` status `ready` deltaP `10.2986` edge `-0.0017` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `-0.0334` n `107` status `ready` deltaP `10.2986` edge `-0.0017` maxDD `-1.699`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
