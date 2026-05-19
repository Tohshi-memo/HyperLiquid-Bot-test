# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-19T18:52:20.939467+00:00`
- Price records: `672`
- Market context records: `1246`
- Flow alert records: `5495`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8798`

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

- `market_context_high->crypto_major_24h` score `18.3198` n `128` status `ready` deltaP `42.6215` edge `1.3557` maxDD `-8.0553`
- `market_context_high->unknown_4h` score `8.0011` n `128` status `ready` deltaP `5.221` edge `0.7536` maxDD `-6.7322`
- `market_context_high->metal_24h` score `7.7503` n `128` status `ready` deltaP `1.7361` edge `0.801` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `7.6962` n `128` status `ready` deltaP `22.4826` edge `0.6931` maxDD `-15.1306`
- `market_context_high->index_24h` score `3.8741` n `128` status `ready` deltaP `22.9167` edge `0.2787` maxDD `-5.3574`
- `market_context_high->commodity_24h` score `3.7235` n `128` status `ready` deltaP `-7.9861` edge `0.5117` maxDD `-6.8535`
- `market_context_high->equity_4h` score `3.362` n `128` status `ready` deltaP `17.5495` edge `0.2295` maxDD `-3.6396`
- `market_context_high->equity_24h` score `3.2138` n `128` status `ready` deltaP `22.3958` edge `0.4954` maxDD `-14.2815`
- `market_context_high->unknown_24h` score `2.0034` n `128` status `ready` deltaP `1.5625` edge `0.4295` maxDD `-10.1706`
- `market_context_high->index_4h` score `1.5747` n `128` status `ready` deltaP `14.0434` edge `0.1059` maxDD `-2.1308`
- `market_context_high->index_1h` score `0.6588` n `128` status `ready` deltaP `9.7493` edge `0.0216` maxDD `-0.5353`
- `market_context_high->equity_1h` score `0.5942` n `128` status `ready` deltaP `5.7587` edge `0.048` maxDD `-1.2834`
- `market_context_high->fx_24h` score `0.3604` n `128` status `ready` deltaP `6.1632` edge `0.0354` maxDD `-0.3831`
- `market_context_high->metal_1h` score `0.2857` n `128` status `ready` deltaP `11.017` edge `0.0114` maxDD `-2.2164`
- `market_context_high->metal_4h` score `0.2597` n `128` status `ready` deltaP `15.606` edge `0.0607` maxDD `-6.4478`
- `market_context_high->crypto_major_4h` score `-0.0141` n `128` status `ready` deltaP `6.917` edge `0.1442` maxDD `-8.3693`
- `market_context_high->fx_1h` score `-0.0629` n `128` status `ready` deltaP `6.0489` edge `0.0` maxDD `-0.3124`
- `market_context_high->crypto_alt_1h` score `-0.2798` n `128` status `ready` deltaP `0.945` edge `0.0421` maxDD `-3.4088`
- `market_context_high->crypto_major_1h` score `-0.4167` n `128` status `ready` deltaP `2.2268` edge `0.0083` maxDD `-4.1256`
- `market_context_high->crypto_alt_4h` score `-0.67` n `128` status `ready` deltaP `8.0983` edge `0.1566` maxDD `-16.7194`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
