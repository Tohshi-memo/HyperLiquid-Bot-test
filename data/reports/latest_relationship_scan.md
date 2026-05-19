# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-19T17:07:19.826443+00:00`
- Price records: `672`
- Market context records: `1239`
- Flow alert records: `5473`
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

- `market_context_high->crypto_major_24h` score `18.6918` n `128` status `ready` deltaP `43.8368` edge `1.3786` maxDD `-8.0553`
- `market_context_high->unknown_4h` score `8.0173` n `128` status `ready` deltaP `4.7637` edge `0.758` maxDD `-6.7322`
- `market_context_high->crypto_alt_24h` score `7.8229` n `128` status `ready` deltaP `22.6562` edge `0.7025` maxDD `-15.1306`
- `market_context_high->metal_24h` score `7.0471` n `128` status `ready` deltaP `0.5208` edge `0.7505` maxDD `-6.3373`
- `market_context_high->commodity_24h` score `4.1603` n `128` status `ready` deltaP `-6.7708` edge `0.54` maxDD `-6.8535`
- `market_context_high->index_24h` score `3.727` n `128` status `ready` deltaP `22.7431` edge `0.2676` maxDD `-5.3574`
- `market_context_high->equity_4h` score `3.4964` n `128` status `ready` deltaP `17.5495` edge `0.2407` maxDD `-3.6396`
- `market_context_high->equity_24h` score `3.1927` n `128` status `ready` deltaP `22.3958` edge `0.4927` maxDD `-14.2815`
- `market_context_high->unknown_24h` score `1.6986` n `128` status `ready` deltaP `1.5625` edge `0.4041` maxDD `-10.1706`
- `market_context_high->index_4h` score `1.6443` n `128` status `ready` deltaP `14.0434` edge `0.1117` maxDD `-2.1308`
- `market_context_high->index_1h` score `0.7212` n `128` status `ready` deltaP `10.1984` edge `0.0238` maxDD `-0.5353`
- `market_context_high->equity_1h` score `0.5775` n `128` status `ready` deltaP `5.3096` edge `0.0496` maxDD `-1.2834`
- `market_context_high->fx_24h` score `0.4592` n `128` status `ready` deltaP `6.8577` edge `0.039` maxDD `-0.3831`
- `market_context_high->metal_1h` score `0.1742` n `128` status `ready` deltaP `10.2685` edge `0.0071` maxDD `-2.2164`
- `market_context_high->metal_4h` score `0.1573` n `128` status `ready` deltaP `15.3011` edge `0.0542` maxDD `-6.4478`
- `market_context_high->crypto_major_4h` score `-0.033` n `128` status `ready` deltaP `6.6121` edge `0.1438` maxDD `-8.3693`
- `market_context_high->fx_1h` score `-0.0617` n `128` status `ready` deltaP `6.0489` edge `0.0001` maxDD `-0.3124`
- `market_context_high->crypto_alt_1h` score `-0.3063` n `128` status `ready` deltaP `0.6456` edge `0.0407` maxDD `-3.4088`
- `market_context_high->crypto_major_1h` score `-0.444` n `128` status `ready` deltaP `1.9274` edge `0.0068` maxDD `-4.1256`
- `market_context_high->crypto_alt_4h` score `-0.6936` n `128` status `ready` deltaP `7.9458` edge `0.1546` maxDD `-16.7194`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
