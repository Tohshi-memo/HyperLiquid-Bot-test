# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-07T21:52:24.917711+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10273`

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

- `risk_on_high->unknown_24h` score `4412.0419` n `116` status `ready` deltaP `21.3542` edge `367.5278` maxDD `0.0`
- `risk_on_and_context->unknown_24h` score `4412.0419` n `116` status `ready` deltaP `21.3542` edge `367.5278` maxDD `0.0`
- `market_context_high->unknown_24h` score `1469.1228` n `231` status `ready` deltaP `20.4884` edge `122.2955` maxDD `-0.0819`
- `risk_on_high->crypto_alt_24h` score `10.0107` n `116` status `ready` deltaP `26.5864` edge `0.6688` maxDD `-0.2789`
- `risk_on_and_context->crypto_alt_24h` score `10.0107` n `116` status `ready` deltaP `26.5864` edge `0.6688` maxDD `-0.2789`
- `market_context_high->crypto_alt_24h` score `5.9774` n `231` status `ready` deltaP `21.3767` edge `0.4131` maxDD `-2.5998`
- `risk_on_high->crypto_major_24h` score `5.8071` n `116` status `ready` deltaP `21.7194` edge `0.9841` maxDD `-23.0855`
- `risk_on_and_context->crypto_major_24h` score `5.8071` n `116` status `ready` deltaP `21.7194` edge `0.9841` maxDD `-23.0855`
- `risk_on_high->crypto_alt_4h` score `5.7788` n `117` status `ready` deltaP `30.635` edge `0.3145` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `5.7788` n `117` status `ready` deltaP `30.635` edge `0.3145` maxDD `-1.9733`
- `risk_on_high->crypto_major_4h` score `4.8493` n `117` status `ready` deltaP `25.6762` edge `0.3188` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `4.8493` n `117` status `ready` deltaP `25.6762` edge `0.3188` maxDD `-3.8693`
- `market_context_high->equity_24h` score `2.993` n `231` status `ready` deltaP `13.3681` edge `0.1603` maxDD `0.0`
- `risk_on_high->equity_24h` score `2.1626` n `116` status `ready` deltaP `13.3681` edge `0.0911` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `2.1626` n `116` status `ready` deltaP `13.3681` edge `0.0911` maxDD `0.0`
- `risk_on_high->index_24h` score `1.6517` n `116` status `ready` deltaP `15.2957` edge `0.0399` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `1.6517` n `116` status `ready` deltaP `15.2957` edge `0.0399` maxDD `-0.0051`
- `risk_on_high->crypto_alt_1h` score `0.9441` n `117` status `ready` deltaP `4.2467` edge `0.0856` maxDD `-1.1521`
- `risk_on_and_context->crypto_alt_1h` score `0.9441` n `117` status `ready` deltaP `4.2467` edge `0.0856` maxDD `-1.1521`
- `market_context_high->index_24h` score `0.9253` n `231` status `ready` deltaP `10.0897` edge `0.0492` maxDD `-0.1483`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
