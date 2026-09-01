# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-01T22:07:29.804582+00:00`
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

- `risk_on_high->unknown_4h` score `7.0547` n `107` status `ready` deltaP `19.1532` edge `0.522` maxDD `-2.2768`
- `risk_on_and_context->unknown_4h` score `7.0547` n `107` status `ready` deltaP `19.1532` edge `0.522` maxDD `-2.2768`
- `market_context_high->unknown_4h` score `5.6013` n `151` status `ready` deltaP `15.4458` edge `0.4333` maxDD `-2.5597`
- `risk_on_high->unknown_1h` score `1.8996` n `107` status `ready` deltaP `3.3718` edge `0.1935` maxDD `-1.9475`
- `risk_on_and_context->unknown_1h` score `1.8996` n `107` status `ready` deltaP `3.3718` edge `0.1935` maxDD `-1.9475`
- `market_context_high->unknown_1h` score `1.7688` n `151` status `ready` deltaP `2.7343` edge `0.1922` maxDD `-2.042`
- `news_risk_high->unknown_1h` score `1.1893` n `59` status `ready` deltaP `0.8373` edge `0.1282` maxDD `-1.1072`
- `news_risk_high->fx_4h` score `0.1391` n `59` status `ready` deltaP `10.4873` edge `0.001` maxDD `-0.7461`
- `risk_on_high->index_1h` score `0.0995` n `107` status `ready` deltaP `8.0936` edge `0.0033` maxDD `-0.5605`
- `risk_on_and_context->index_1h` score `0.0995` n `107` status `ready` deltaP `8.0936` edge `0.0033` maxDD `-0.5605`
- `risk_on_high->metal_1h` score `0.0951` n `107` status `ready` deltaP `12.095` edge `0.0028` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `0.0951` n `107` status `ready` deltaP `12.095` edge `0.0028` maxDD `-1.699`
- `risk_on_high->index_4h` score `0.0294` n `107` status `ready` deltaP `19.5635` edge `0.0064` maxDD `-3.6448`
- `risk_on_and_context->index_4h` score `0.0294` n `107` status `ready` deltaP `19.5635` edge `0.0064` maxDD `-3.6448`
- `risk_on_high->commodity_24h` score `-0.047` n `107` status `ready` deltaP `6.5226` edge `0.0514` maxDD `-0.5706`
- `risk_on_and_context->commodity_24h` score `-0.047` n `107` status `ready` deltaP `6.5226` edge `0.0514` maxDD `-0.5706`
- `risk_on_high->equity_1h` score `-0.1465` n `107` status `ready` deltaP `7.867` edge `0.0117` maxDD `-2.3009`
- `risk_on_and_context->equity_1h` score `-0.1465` n `107` status `ready` deltaP `7.867` edge `0.0117` maxDD `-2.3009`
- `market_context_high->commodity_1h` score `-0.1536` n `151` status `ready` deltaP `6.7762` edge `0.007` maxDD `-1.5315`
- `risk_on_high->commodity_1h` score `-0.1732` n `107` status `ready` deltaP `3.6754` edge `0.0055` maxDD `-0.8428`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
