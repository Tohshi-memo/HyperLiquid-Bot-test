# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-02T03:52:25.405175+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11475`

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

- `risk_on_high->unknown_4h` score `7.6917` n `107` status `ready` deltaP `19.9154` edge `0.57` maxDD `-2.2768`
- `risk_on_and_context->unknown_4h` score `7.6917` n `107` status `ready` deltaP `19.9154` edge `0.57` maxDD `-2.2768`
- `market_context_high->unknown_4h` score `5.6345` n `150` status `ready` deltaP `16.0711` edge `0.4319` maxDD `-2.5597`
- `risk_on_high->equity_24h` score `1.8491` n `107` status `ready` deltaP `17.9728` edge `0.4507` maxDD `-19.9806`
- `risk_on_and_context->equity_24h` score `1.8491` n `107` status `ready` deltaP `17.9728` edge `0.4507` maxDD `-19.9806`
- `risk_on_high->unknown_1h` score `1.4965` n `107` status `ready` deltaP `3.0724` edge `0.1619` maxDD `-1.9475`
- `risk_on_and_context->unknown_1h` score `1.4965` n `107` status `ready` deltaP `3.0724` edge `0.1619` maxDD `-1.9475`
- `market_context_high->unknown_1h` score `1.3375` n `150` status `ready` deltaP `2.1877` edge `0.1599` maxDD `-2.042`
- `news_risk_high->unknown_1h` score `0.7862` n `59` status `ready` deltaP `0.5379` edge `0.0966` maxDD `-1.1072`
- `news_risk_high->fx_4h` score `0.1987` n `59` status `ready` deltaP `11.0971` edge `0.0019` maxDD `-0.7461`
- `risk_on_high->metal_1h` score `0.1442` n `107` status `ready` deltaP `12.6938` edge `0.0051` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `0.1442` n `107` status `ready` deltaP `12.6938` edge `0.0051` maxDD `-1.699`
- `risk_on_high->index_1h` score `0.1026` n `107` status `ready` deltaP `8.0936` edge `0.0037` maxDD `-0.5605`
- `risk_on_and_context->index_1h` score `0.1026` n `107` status `ready` deltaP `8.0936` edge `0.0037` maxDD `-0.5605`
- `risk_on_high->index_4h` score `0.0807` n `107` status `ready` deltaP `20.3257` edge `0.0079` maxDD `-3.6448`
- `risk_on_and_context->index_4h` score `0.0807` n `107` status `ready` deltaP `20.3257` edge `0.0079` maxDD `-3.6448`
- `risk_on_high->equity_1h` score `-0.1332` n `107` status `ready` deltaP `7.867` edge `0.0134` maxDD `-2.3009`
- `risk_on_and_context->equity_1h` score `-0.1332` n `107` status `ready` deltaP `7.867` edge `0.0134` maxDD `-2.3009`
- `news_risk_high->index_1h` score `-0.1887` n `59` status `ready` deltaP `2.6921` edge `-0.0068` maxDD `-0.8275`
- `market_context_high->commodity_1h` score `-0.2027` n `150` status `ready` deltaP `6.2974` edge `0.0061` maxDD `-1.5315`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
