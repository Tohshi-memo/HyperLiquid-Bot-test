# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-02T14:37:35.896444+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11514`

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

- `risk_on_high->unknown_4h` score `7.091` n `107` status `ready` deltaP `16.8666` edge `0.5403` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `7.091` n `107` status `ready` deltaP `16.8666` edge `0.5403` maxDD `-2.2797`
- `risk_on_high->equity_24h` score `5.4224` n `107` status `ready` deltaP `25.4381` edge `0.6968` maxDD `-19.828`
- `risk_on_and_context->equity_24h` score `5.4224` n `107` status `ready` deltaP `25.4381` edge `0.6968` maxDD `-19.828`
- `market_context_high->unknown_4h` score `5.1716` n `147` status `ready` deltaP `12.6006` edge `0.4165` maxDD `-2.563`
- `news_risk_high->equity_24h` score `2.4226` n `59` status `ready` deltaP `11.3877` edge `0.3727` maxDD `-15.4056`
- `market_context_high->equity_24h` score `1.87` n `147` status `ready` deltaP `21.4073` edge `0.5779` maxDD `-24.4698`
- `risk_on_high->unknown_1h` score `1.6714` n `107` status `ready` deltaP `2.6233` edge `0.1795` maxDD `-1.95`
- `risk_on_and_context->unknown_1h` score `1.6714` n `107` status `ready` deltaP `2.6233` edge `0.1795` maxDD `-1.95`
- `news_risk_high->unknown_1h` score `1.094` n `66` status `ready` deltaP `2.7083` edge `0.1078` maxDD `-1.1086`
- `market_context_high->unknown_1h` score `0.3414` n `147` status `ready` deltaP `0.9767` edge `0.085` maxDD `-2.0446`
- `news_risk_high->fx_4h` score `0.3172` n `59` status `ready` deltaP `11.8593` edge `0.0067` maxDD `-0.7461`
- `risk_on_high->crypto_alt_24h` score `0.2449` n `107` status `ready` deltaP `15.3541` edge `0.6194` maxDD `-42.8959`
- `risk_on_and_context->crypto_alt_24h` score `0.2449` n `107` status `ready` deltaP `15.3541` edge `0.6194` maxDD `-42.8959`
- `news_risk_high->crypto_alt_24h` score `0.2159` n `59` status `ready` deltaP `15.2749` edge `0.2193` maxDD `-19.4761`
- `risk_on_high->index_4h` score `0.1328` n `107` status `ready` deltaP `21.0879` edge `0.0095` maxDD `-3.6448`
- `risk_on_and_context->index_4h` score `0.1328` n `107` status `ready` deltaP `21.0879` edge `0.0095` maxDD `-3.6448`
- `risk_on_high->index_1h` score `0.0925` n `107` status `ready` deltaP `7.9439` edge `0.0034` maxDD `-0.5605`
- `risk_on_and_context->index_1h` score `0.0925` n `107` status `ready` deltaP `7.9439` edge `0.0034` maxDD `-0.5605`
- `news_risk_high->index_1h` score `-0.0448` n `66` status `ready` deltaP `4.5455` edge `-0.0007` maxDD `-0.8275`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
