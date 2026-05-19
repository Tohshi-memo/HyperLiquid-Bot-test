# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-19T15:22:19.631495+00:00`
- Price records: `672`
- Market context records: `1232`
- Flow alert records: `5452`
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

- `market_context_high->crypto_major_24h` score `18.8276` n `128` status `ready` deltaP `44.184` edge `1.3876` maxDD `-8.0553`
- `market_context_high->unknown_4h` score `7.8671` n `128` status `ready` deltaP `3.6966` edge `0.7526` maxDD `-6.7322`
- `market_context_high->crypto_alt_24h` score `7.6393` n `128` status `ready` deltaP `22.6562` edge `0.6872` maxDD `-15.1306`
- `market_context_high->metal_24h` score `6.2875` n `128` status `ready` deltaP `-0.6944` edge `0.6953` maxDD `-6.3373`
- `market_context_high->commodity_24h` score `4.6055` n `128` status `ready` deltaP `-5.5556` edge `0.569` maxDD `-6.8535`
- `market_context_high->equity_4h` score `3.4674` n `128` status `ready` deltaP `17.3971` edge `0.2393` maxDD `-3.6396`
- `market_context_high->index_24h` score `3.3586` n `128` status `ready` deltaP `21.5278` edge `0.245` maxDD `-5.3574`
- `market_context_high->equity_24h` score `2.9982` n `128` status `ready` deltaP `21.7014` edge `0.4724` maxDD `-14.2815`
- `market_context_high->index_4h` score `1.5089` n `128` status `ready` deltaP `13.2812` edge `0.1055` maxDD `-2.1308`
- `market_context_high->unknown_24h` score `1.0681` n `128` status `ready` deltaP `0.5208` edge `0.3585` maxDD `-10.1706`
- `market_context_high->index_1h` score `0.7368` n `128` status `ready` deltaP `10.1984` edge `0.0251` maxDD `-0.5353`
- `market_context_high->equity_1h` score `0.7022` n `128` status `ready` deltaP `5.7587` edge `0.057` maxDD `-1.2834`
- `market_context_high->fx_24h` score `0.5572` n `128` status `ready` deltaP `7.3785` edge `0.0437` maxDD `-0.3831`
- `market_context_high->metal_1h` score `0.149` n `128` status `ready` deltaP `10.2685` edge `0.005` maxDD `-2.2164`
- `market_context_high->fx_1h` score `-0.0414` n `128` status `ready` deltaP `6.1986` edge `0.0008` maxDD `-0.3124`
- `market_context_high->crypto_major_4h` score `-0.1304` n `128` status `ready` deltaP `5.8499` edge `0.1364` maxDD `-8.3693`
- `market_context_high->metal_4h` score `-0.2209` n `128` status `ready` deltaP `14.234` edge `0.0298` maxDD `-6.4478`
- `market_context_high->crypto_alt_1h` score `-0.3398` n `128` status `ready` deltaP `0.3462` edge `0.0384` maxDD `-3.4088`
- `market_context_high->crypto_major_1h` score `-0.4159` n `128` status `ready` deltaP `2.3765` edge `0.0074` maxDD `-4.1256`
- `market_context_high->commodity_1h` score `-0.8554` n `128` status `ready` deltaP `-2.7601` edge `0.0086` maxDD `-2.252`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
