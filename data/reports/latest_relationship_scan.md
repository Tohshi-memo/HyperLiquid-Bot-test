# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-19T09:37:20.763192+00:00`
- Price records: `672`
- Market context records: `1207`
- Flow alert records: `5381`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8776`

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

- `market_context_high->crypto_major_24h` score `18.6318` n `131` status `ready` deltaP `44.1357` edge `1.3716` maxDD `-8.0553`
- `market_context_high->crypto_alt_24h` score `7.2137` n `131` status `ready` deltaP `22.0155` edge `0.656` maxDD `-15.1306`
- `market_context_high->unknown_4h` score `6.6493` n `131` status `ready` deltaP `3.1291` edge `0.6549` maxDD `-6.7322`
- `market_context_high->commodity_24h` score `4.8294` n `131` status `ready` deltaP `-3.1011` edge `0.6232` maxDD `-11.0064`
- `market_context_high->metal_24h` score `4.3659` n `131` status `ready` deltaP `-3.5942` edge `0.5545` maxDD `-6.3373`
- `market_context_high->equity_4h` score `2.8068` n `131` status `ready` deltaP `14.4642` edge `0.2038` maxDD `-3.6396`
- `market_context_high->index_24h` score `2.1292` n `131` status `ready` deltaP `17.7852` edge `0.1675` maxDD `-5.3574`
- `market_context_high->equity_24h` score `1.7712` n `131` status `ready` deltaP `17.9946` edge `0.3398` maxDD `-14.2815`
- `market_context_high->index_4h` score `0.9315` n `131` status `ready` deltaP `10.339` edge `0.077` maxDD `-2.1308`
- `market_context_high->fx_24h` score `0.7496` n `131` status `ready` deltaP `9.4572` edge `0.0588` maxDD `-1.417`
- `market_context_high->index_1h` score `0.5582` n `131` status `ready` deltaP `9.0311` edge `0.018` maxDD `-0.5353`
- `market_context_high->equity_1h` score `0.3866` n `131` status `ready` deltaP `3.8819` edge `0.0441` maxDD `-1.3546`
- `market_context_high->metal_1h` score `-0.0999` n `131` status `ready` deltaP `9.3615` edge `-0.0097` maxDD `-2.2164`
- `market_context_high->fx_1h` score `-0.126` n `131` status `ready` deltaP `5.1858` edge `0.0005` maxDD `-0.3124`
- `market_context_high->crypto_major_4h` score `-0.2035` n `131` status `ready` deltaP `5.5692` edge `0.1289` maxDD `-8.3693`
- `market_context_high->crypto_alt_1h` score `-0.3755` n `131` status `ready` deltaP `0.4857` edge `0.0329` maxDD `-3.4088`
- `market_context_high->crypto_major_1h` score `-0.3858` n `131` status `ready` deltaP `3.1506` edge `0.0061` maxDD `-4.1256`
- `market_context_high->unknown_24h` score `-0.6619` n `131` status `ready` deltaP `0.4811` edge `0.2146` maxDD `-10.1706`
- `market_context_high->commodity_1h` score `-0.8016` n `131` status `ready` deltaP `-2.6569` edge `0.0124` maxDD `-2.252`
- `market_context_high->metal_4h` score `-0.8366` n `131` status `ready` deltaP `9.8619` edge `-0.0299` maxDD `-6.4478`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
