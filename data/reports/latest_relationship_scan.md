# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-19T16:52:15.209028+00:00`
- Price records: `672`
- Market context records: `1238`
- Flow alert records: `5470`
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

- `market_context_high->crypto_major_24h` score `18.7309` n `128` status `ready` deltaP `44.0104` edge `1.3807` maxDD `-8.0553`
- `market_context_high->unknown_4h` score `7.9967` n `128` status `ready` deltaP `4.6113` edge `0.7573` maxDD `-6.7322`
- `market_context_high->crypto_alt_24h` score `7.8169` n `128` status `ready` deltaP `22.6562` edge `0.702` maxDD `-15.1306`
- `market_context_high->metal_24h` score `6.9432` n `128` status `ready` deltaP `0.3472` edge `0.743` maxDD `-6.3373`
- `market_context_high->commodity_24h` score `4.2258` n `128` status `ready` deltaP `-6.5972` edge `0.5443` maxDD `-6.8535`
- `market_context_high->index_24h` score `3.6915` n `128` status `ready` deltaP `22.5694` edge `0.2658` maxDD `-5.3574`
- `market_context_high->equity_4h` score `3.5108` n `128` status `ready` deltaP `17.5495` edge `0.2419` maxDD `-3.6396`
- `market_context_high->equity_24h` score `3.1841` n `128` status `ready` deltaP `22.3958` edge `0.4916` maxDD `-14.2815`
- `market_context_high->index_4h` score `1.6479` n `128` status `ready` deltaP `14.0434` edge `0.112` maxDD `-2.1308`
- `market_context_high->unknown_24h` score `1.6139` n `128` status `ready` deltaP `1.3889` edge `0.3982` maxDD `-10.1706`
- `market_context_high->index_1h` score `0.732` n `128` status `ready` deltaP `10.1984` edge `0.0247` maxDD `-0.5353`
- `market_context_high->equity_1h` score `0.5931` n `128` status `ready` deltaP `5.3096` edge `0.0509` maxDD `-1.2834`
- `market_context_high->fx_24h` score `0.464` n `128` status `ready` deltaP `6.8577` edge `0.0394` maxDD `-0.3831`
- `market_context_high->metal_1h` score `0.1706` n `128` status `ready` deltaP `10.2685` edge `0.0068` maxDD `-2.2164`
- `market_context_high->metal_4h` score `0.1211` n `128` status `ready` deltaP `15.1487` edge `0.0522` maxDD `-6.4478`
- `market_context_high->crypto_major_4h` score `-0.0346` n `128` status `ready` deltaP `6.6121` edge `0.1436` maxDD `-8.3693`
- `market_context_high->fx_1h` score `-0.0617` n `128` status `ready` deltaP `6.0489` edge `0.0001` maxDD `-0.3124`
- `market_context_high->crypto_alt_1h` score `-0.3102` n `128` status `ready` deltaP `0.6456` edge `0.0402` maxDD `-3.4088`
- `market_context_high->crypto_major_1h` score `-0.444` n `128` status `ready` deltaP `1.9274` edge `0.0068` maxDD `-4.1256`
- `market_context_high->crypto_alt_4h` score `-0.7006` n `128` status `ready` deltaP `7.9458` edge `0.1537` maxDD `-16.7194`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
