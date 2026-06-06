# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-06T07:37:24.046238+00:00`
- Price records: `672`
- Market context records: `3051`
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

- `market_context_high->crypto_alt_24h` score `25.4812` n `99` status `ready` deltaP `13.9362` edge `2.4222` maxDD `-22.6673`
- `market_context_high->unknown_24h` score `13.4807` n `99` status `ready` deltaP `24.6686` edge `1.0054` maxDD `-1.7175`
- `market_context_high->commodity_24h` score `13.4795` n `99` status `ready` deltaP `44.6338` edge `0.8498` maxDD `-1.2589`
- `market_context_high->equity_24h` score `9.9771` n `99` status `ready` deltaP `25.1105` edge `1.3869` maxDD `-18.3486`
- `market_context_high->index_24h` score `9.4648` n `99` status `ready` deltaP `23.8321` edge `0.7554` maxDD `-4.7103`
- `market_context_high->commodity_4h` score `2.7485` n `129` status `ready` deltaP `18.4735` edge `0.1706` maxDD `-2.8438`
- `market_context_high->commodity_1h` score `-0.1812` n `135` status `ready` deltaP `0.804` edge `0.0218` maxDD `-1.7142`
- `market_context_high->unknown_4h` score `-0.4392` n `129` status `ready` deltaP `1.8506` edge `0.0564` maxDD `-3.7602`
- `market_context_high->index_1h` score `-0.5183` n `135` status `ready` deltaP `3.3489` edge `0.0175` maxDD `-4.5023`
- `market_context_high->fx_1h` score `-0.5589` n `135` status `ready` deltaP `-5.0987` edge `-0.0004` maxDD `-0.3147`
- `market_context_high->crypto_alt_1h` score `-0.6257` n `135` status `ready` deltaP `5.7208` edge `0.0946` maxDD `-14.7034`
- `market_context_high->equity_1h` score `-0.7391` n `135` status `ready` deltaP `2.8765` edge `0.0274` maxDD `-8.3065`
- `market_context_high->unknown_1h` score `-0.9041` n `135` status `ready` deltaP `4.4766` edge `-0.0321` maxDD `-3.1801`
- `market_context_high->crypto_major_1h` score `-0.9713` n `135` status `ready` deltaP `4.2703` edge `0.0733` maxDD `-15.1032`
- `market_context_high->index_4h` score `-0.9811` n `129` status `ready` deltaP `12.2554` edge `0.0618` maxDD `-16.8761`
- `market_context_high->fx_4h` score `-1.0959` n `129` status `ready` deltaP `-8.0261` edge `-0.0035` maxDD `-1.0127`
- `market_context_high->metal_1h` score `-1.161` n `135` status `ready` deltaP `-1.5059` edge `-0.002` maxDD `-7.278`
- `market_context_high->fx_24h` score `-1.1934` n `99` status `ready` deltaP `0.1105` edge `-0.013` maxDD `-0.6418`
- `market_context_high->equity_4h` score `-2.9298` n `129` status `ready` deltaP `9.8423` edge `0.0515` maxDD `-34.4188`
- `market_context_high->crypto_alt_4h` score `-3.1662` n `129` status `ready` deltaP `18.1745` edge `0.2774` maxDD `-58.6918`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
