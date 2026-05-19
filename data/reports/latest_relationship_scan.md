# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-19T16:37:20.247595+00:00`
- Price records: `672`
- Market context records: `1237`
- Flow alert records: `5467`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8788`

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

- `market_context_high->crypto_major_24h` score `18.7676` n `128` status `ready` deltaP `44.184` edge `1.3826` maxDD `-8.0553`
- `market_context_high->unknown_4h` score `7.9713` n `128` status `ready` deltaP `4.4588` edge `0.7562` maxDD `-6.7322`
- `market_context_high->crypto_alt_24h` score `7.8013` n `128` status `ready` deltaP `22.6562` edge `0.7007` maxDD `-15.1306`
- `market_context_high->metal_24h` score `6.8393` n `128` status `ready` deltaP `0.1736` edge `0.7355` maxDD `-6.3373`
- `market_context_high->commodity_24h` score `4.2889` n `128` status `ready` deltaP `-6.4236` edge `0.5484` maxDD `-6.8535`
- `market_context_high->index_24h` score `3.6513` n `128` status `ready` deltaP `22.3958` edge `0.2636` maxDD `-5.3574`
- `market_context_high->equity_4h` score `3.512` n `128` status `ready` deltaP `17.5495` edge `0.242` maxDD `-3.6396`
- `market_context_high->equity_24h` score `3.1709` n `128` status `ready` deltaP `22.3958` edge `0.4899` maxDD `-14.2815`
- `market_context_high->index_4h` score `1.6431` n `128` status `ready` deltaP `14.0434` edge `0.1116` maxDD `-2.1308`
- `market_context_high->unknown_24h` score `1.5232` n `128` status `ready` deltaP `1.2153` edge `0.3918` maxDD `-10.1706`
- `market_context_high->index_1h` score `0.7392` n `128` status `ready` deltaP `10.1984` edge `0.0253` maxDD `-0.5353`
- `market_context_high->equity_1h` score `0.6063` n `128` status `ready` deltaP `5.3096` edge `0.052` maxDD `-1.2834`
- `market_context_high->fx_24h` score `0.4676` n `128` status `ready` deltaP `6.8577` edge `0.0397` maxDD `-0.3831`
- `market_context_high->metal_1h` score `0.167` n `128` status `ready` deltaP `10.2685` edge `0.0065` maxDD `-2.2164`
- `market_context_high->metal_4h` score `0.0693` n `128` status `ready` deltaP `14.9962` edge `0.0489` maxDD `-6.4478`
- `market_context_high->crypto_major_4h` score `-0.0503` n `128` status `ready` deltaP `6.4597` edge `0.1426` maxDD `-8.3693`
- `market_context_high->fx_1h` score `-0.0629` n `128` status `ready` deltaP `6.0489` edge `0.0` maxDD `-0.3124`
- `market_context_high->crypto_alt_1h` score `-0.3141` n `128` status `ready` deltaP `0.6456` edge `0.0397` maxDD `-3.4088`
- `market_context_high->crypto_major_1h` score `-0.4448` n `128` status `ready` deltaP `1.9274` edge `0.0067` maxDD `-4.1256`
- `market_context_high->crypto_alt_4h` score `-0.7226` n `128` status `ready` deltaP `7.7934` edge `0.1519` maxDD `-16.7194`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
