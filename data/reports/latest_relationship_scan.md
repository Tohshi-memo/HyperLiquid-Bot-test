# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-07T22:07:31.819397+00:00`
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

- `risk_on_high->unknown_24h` score `4249.4988` n `116` status `ready` deltaP `21.1806` edge `353.9837` maxDD `0.0`
- `risk_on_and_context->unknown_24h` score `4249.4988` n `116` status `ready` deltaP `21.1806` edge `353.9837` maxDD `0.0`
- `market_context_high->unknown_24h` score `1690.9208` n `232` status `ready` deltaP `20.3185` edge `140.7798` maxDD `-0.0819`
- `risk_on_high->crypto_alt_24h` score `9.9812` n `116` status `ready` deltaP `26.4128` edge `0.6675` maxDD `-0.2789`
- `risk_on_and_context->crypto_alt_24h` score `9.9812` n `116` status `ready` deltaP `26.4128` edge `0.6675` maxDD `-0.2789`
- `market_context_high->crypto_alt_24h` score `5.8813` n `232` status `ready` deltaP `21.2404` edge `0.406` maxDD `-2.5998`
- `risk_on_high->crypto_major_24h` score `5.7899` n `116` status `ready` deltaP `21.7194` edge `0.9819` maxDD `-23.0855`
- `risk_on_and_context->crypto_major_24h` score `5.7899` n `116` status `ready` deltaP `21.7194` edge `0.9819` maxDD `-23.0855`
- `risk_on_high->crypto_alt_4h` score `5.78` n `117` status `ready` deltaP `30.635` edge `0.3146` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `5.78` n `117` status `ready` deltaP `30.635` edge `0.3146` maxDD `-1.9733`
- `risk_on_high->crypto_major_4h` score `4.8397` n `117` status `ready` deltaP `25.6762` edge `0.318` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `4.8397` n `117` status `ready` deltaP `25.6762` edge `0.318` maxDD `-3.8693`
- `market_context_high->equity_24h` score `2.9096` n `232` status `ready` deltaP `13.1944` edge `0.1545` maxDD `0.0`
- `risk_on_high->equity_24h` score `2.0948` n `116` status `ready` deltaP `13.1944` edge `0.0866` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `2.0948` n `116` status `ready` deltaP `13.1944` edge `0.0866` maxDD `0.0`
- `risk_on_high->index_24h` score `1.6294` n `116` status `ready` deltaP `15.1221` edge `0.0392` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `1.6294` n `116` status `ready` deltaP `15.1221` edge `0.0392` maxDD `-0.0051`
- `risk_on_high->crypto_alt_1h` score `0.9429` n `117` status `ready` deltaP `4.2467` edge `0.0855` maxDD `-1.1521`
- `risk_on_and_context->crypto_alt_1h` score `0.9429` n `117` status `ready` deltaP `4.2467` edge `0.0855` maxDD `-1.1521`
- `market_context_high->index_24h` score `0.9033` n `232` status `ready` deltaP `9.9497` edge `0.0483` maxDD `-0.1483`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
