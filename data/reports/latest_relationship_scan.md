# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-02T15:22:29.479509+00:00`
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

- `risk_on_high->unknown_4h` score `7.0306` n `107` status `ready` deltaP `16.5617` edge `0.5373` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `7.0306` n `107` status `ready` deltaP `16.5617` edge `0.5373` maxDD `-2.2797`
- `risk_on_high->equity_24h` score `5.5901` n `107` status `ready` deltaP `25.9589` edge `0.7073` maxDD `-19.828`
- `risk_on_and_context->equity_24h` score `5.5901` n `107` status `ready` deltaP `25.9589` edge `0.7073` maxDD `-19.828`
- `market_context_high->unknown_4h` score `5.1112` n `147` status `ready` deltaP `12.2957` edge `0.4135` maxDD `-2.563`
- `news_risk_high->equity_24h` score `2.5902` n `59` status `ready` deltaP `11.9085` edge `0.3832` maxDD `-15.4056`
- `market_context_high->equity_24h` score `1.979` n `147` status `ready` deltaP `21.9281` edge `0.5884` maxDD `-24.4698`
- `risk_on_high->unknown_1h` score `1.6342` n `107` status `ready` deltaP `2.3239` edge `0.1784` maxDD `-1.95`
- `risk_on_and_context->unknown_1h` score `1.6342` n `107` status `ready` deltaP `2.3239` edge `0.1784` maxDD `-1.95`
- `news_risk_high->unknown_1h` score `1.0568` n `66` status `ready` deltaP `2.4089` edge `0.1067` maxDD `-1.1086`
- `risk_on_high->crypto_alt_24h` score `0.4202` n `107` status `ready` deltaP `15.8749` edge `0.6384` maxDD `-42.8959`
- `risk_on_and_context->crypto_alt_24h` score `0.4202` n `107` status `ready` deltaP `15.8749` edge `0.6384` maxDD `-42.8959`
- `news_risk_high->crypto_alt_24h` score `0.3912` n `59` status `ready` deltaP `15.7957` edge `0.2383` maxDD `-19.4761`
- `market_context_high->unknown_1h` score `0.3043` n `147` status `ready` deltaP `0.6773` edge `0.0839` maxDD `-2.0446`
- `news_risk_high->fx_4h` score `0.1219` n `61` status `ready` deltaP `10.081` edge `0.0032` maxDD `-0.8196`
- `risk_on_high->index_4h` score `0.1171` n `107` status `ready` deltaP `20.9355` edge `0.0085` maxDD `-3.6448`
- `risk_on_and_context->index_4h` score `0.1171` n `107` status `ready` deltaP `20.9355` edge `0.0085` maxDD `-3.6448`
- `risk_on_high->index_1h` score `0.0909` n `107` status `ready` deltaP `7.9439` edge `0.0032` maxDD `-0.5605`
- `risk_on_and_context->index_1h` score `0.0909` n `107` status `ready` deltaP `7.9439` edge `0.0032` maxDD `-0.5605`
- `news_risk_high->commodity_4h` score `0.062` n `61` status `ready` deltaP `4.4057` edge `0.0145` maxDD `-0.8733`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
