# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-19T17:52:21.075810+00:00`
- Price records: `672`
- Market context records: `1242`
- Flow alert records: `5483`
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

- `market_context_high->crypto_major_24h` score `18.5494` n `128` status `ready` deltaP `43.3159` edge `1.3702` maxDD `-8.0553`
- `market_context_high->unknown_4h` score `8.0707` n `128` status `ready` deltaP `5.221` edge `0.7594` maxDD `-6.7322`
- `market_context_high->crypto_alt_24h` score `7.8097` n `128` status `ready` deltaP `22.6562` edge `0.7014` maxDD `-15.1306`
- `market_context_high->metal_24h` score `7.3659` n `128` status `ready` deltaP `1.0417` edge `0.7736` maxDD `-6.3373`
- `market_context_high->commodity_24h` score `3.9686` n `128` status `ready` deltaP `-7.2917` edge `0.5275` maxDD `-6.8535`
- `market_context_high->index_24h` score `3.7997` n `128` status `ready` deltaP `22.9167` edge `0.2725` maxDD `-5.3574`
- `market_context_high->equity_4h` score `3.4676` n `128` status `ready` deltaP `17.5495` edge `0.2383` maxDD `-3.6396`
- `market_context_high->equity_24h` score `3.2091` n `128` status `ready` deltaP `22.3958` edge `0.4948` maxDD `-14.2815`
- `market_context_high->unknown_24h` score `1.9314` n `128` status `ready` deltaP `1.5625` edge `0.4235` maxDD `-10.1706`
- `market_context_high->index_4h` score `1.6335` n `128` status `ready` deltaP `14.0434` edge `0.1108` maxDD `-2.1308`
- `market_context_high->index_1h` score `0.6612` n `128` status `ready` deltaP `9.7493` edge `0.0218` maxDD `-0.5353`
- `market_context_high->equity_1h` score `0.5391` n `128` status `ready` deltaP `5.3096` edge `0.0464` maxDD `-1.2834`
- `market_context_high->fx_24h` score `0.4424` n `128` status `ready` deltaP `6.8577` edge `0.0376` maxDD `-0.3831`
- `market_context_high->metal_4h` score `0.2213` n `128` status `ready` deltaP `15.606` edge `0.0575` maxDD `-6.4478`
- `market_context_high->metal_1h` score `0.1934` n `128` status `ready` deltaP `10.4182` edge `0.0077` maxDD `-2.2164`
- `market_context_high->crypto_major_4h` score `-0.0117` n `128` status `ready` deltaP `6.917` edge `0.1445` maxDD `-8.3693`
- `market_context_high->fx_1h` score `-0.0629` n `128` status `ready` deltaP `6.0489` edge `0.0` maxDD `-0.3124`
- `market_context_high->crypto_alt_1h` score `-0.3102` n `128` status `ready` deltaP `0.6456` edge `0.0402` maxDD `-3.4088`
- `market_context_high->crypto_major_1h` score `-0.4627` n `128` status `ready` deltaP `1.7777` edge `0.0054` maxDD `-4.1256`
- `market_context_high->crypto_alt_4h` score `-0.6574` n `128` status `ready` deltaP `8.2507` edge `0.1572` maxDD `-16.7194`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
