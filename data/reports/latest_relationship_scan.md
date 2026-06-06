# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-06T06:52:26.678254+00:00`
- Price records: `672`
- Market context records: `3048`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6969`

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

- `market_context_high->crypto_alt_24h` score `25.2343` n `99` status `ready` deltaP `13.4154` edge `2.4051` maxDD `-22.6673`
- `market_context_high->unknown_24h` score `13.5131` n `99` status `ready` deltaP `24.6686` edge `1.0081` maxDD `-1.7175`
- `market_context_high->commodity_24h` score `13.3454` n `99` status `ready` deltaP `44.113` edge `0.8421` maxDD `-1.2589`
- `market_context_high->equity_24h` score `9.6544` n `99` status `ready` deltaP `24.5897` edge `1.349` maxDD `-18.3486`
- `market_context_high->index_24h` score `9.2061` n `99` status `ready` deltaP `23.6585` edge `0.735` maxDD `-4.7103`
- `market_context_high->commodity_4h` score `2.6855` n `129` status `ready` deltaP `18.0162` edge `0.1684` maxDD `-2.8438`
- `market_context_high->commodity_1h` score `-0.1032` n `133` status `ready` deltaP `1.5837` edge `0.0231` maxDD `-1.7142`
- `market_context_high->unknown_4h` score `-0.4682` n `129` status `ready` deltaP `1.6981` edge `0.055` maxDD `-3.7602`
- `market_context_high->index_1h` score `-0.4817` n `133` status `ready` deltaP `3.9789` edge `0.018` maxDD `-4.5023`
- `market_context_high->fx_1h` score `-0.5272` n `133` status `ready` deltaP `-4.5912` edge `0.0` maxDD `-0.2921`
- `market_context_high->crypto_alt_1h` score `-0.5967` n `133` status `ready` deltaP `6.0848` edge `0.0959` maxDD `-14.7034`
- `market_context_high->equity_1h` score `-0.6781` n `133` status `ready` deltaP `3.3902` edge `0.0318` maxDD `-8.3065`
- `market_context_high->crypto_major_1h` score `-0.9207` n `133` status `ready` deltaP `4.7172` edge `0.0768` maxDD `-15.1032`
- `market_context_high->index_4h` score `-0.9621` n `129` status `ready` deltaP `12.5602` edge `0.0622` maxDD `-16.8761`
- `market_context_high->unknown_1h` score `-1.0057` n `133` status `ready` deltaP `4.3019` edge `-0.0394` maxDD `-3.1801`
- `market_context_high->fx_4h` score `-1.1125` n `129` status `ready` deltaP `-8.331` edge `-0.0036` maxDD `-1.0127`
- `market_context_high->metal_1h` score `-1.1879` n `133` status `ready` deltaP `-1.9034` edge `-0.0028` maxDD `-7.278`
- `market_context_high->fx_24h` score `-1.2531` n `99` status `ready` deltaP `-0.4103` edge `-0.0145` maxDD `-0.6418`
- `market_context_high->equity_4h` score `-2.9298` n `129` status `ready` deltaP `9.8423` edge `0.0515` maxDD `-34.4188`
- `market_context_high->crypto_alt_4h` score `-3.1889` n `129` status `ready` deltaP `18.022` edge `0.2755` maxDD `-58.6918`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
