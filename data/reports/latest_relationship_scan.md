# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-19T15:07:22.442190+00:00`
- Price records: `672`
- Market context records: `1231`
- Flow alert records: `5449`
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

- `market_context_high->crypto_major_24h` score `18.8667` n `128` status `ready` deltaP `44.3576` edge `1.3897` maxDD `-8.0553`
- `market_context_high->unknown_4h` score `7.8659` n `128` status `ready` deltaP `3.6966` edge `0.7525` maxDD `-6.7322`
- `market_context_high->crypto_alt_24h` score `7.6129` n `128` status `ready` deltaP `22.6562` edge `0.685` maxDD `-15.1306`
- `market_context_high->metal_24h` score `6.1812` n `128` status `ready` deltaP `-0.8681` edge `0.6876` maxDD `-6.3373`
- `market_context_high->commodity_24h` score `4.6662` n `128` status `ready` deltaP `-5.3819` edge `0.5729` maxDD `-6.8535`
- `market_context_high->equity_4h` score `3.4456` n `128` status `ready` deltaP `17.2446` edge `0.2385` maxDD `-3.6396`
- `market_context_high->index_24h` score `3.2967` n `128` status `ready` deltaP `21.3542` edge `0.241` maxDD `-5.3574`
- `market_context_high->equity_24h` score `2.9557` n `128` status `ready` deltaP `21.5278` edge `0.4681` maxDD `-14.2815`
- `market_context_high->index_4h` score `1.4799` n `128` status `ready` deltaP `13.1288` edge `0.1041` maxDD `-2.1308`
- `market_context_high->unknown_24h` score `0.981` n `128` status `ready` deltaP `0.3472` edge `0.3524` maxDD `-10.1706`
- `market_context_high->index_1h` score `0.756` n `128` status `ready` deltaP `10.3481` edge `0.0257` maxDD `-0.5353`
- `market_context_high->equity_1h` score `0.7154` n `128` status `ready` deltaP `5.7587` edge `0.0581` maxDD `-1.2834`
- `market_context_high->fx_24h` score `0.5879` n `128` status `ready` deltaP `7.5521` edge `0.0451` maxDD `-0.3831`
- `market_context_high->metal_1h` score `0.1646` n `128` status `ready` deltaP `10.4182` edge `0.0053` maxDD `-2.2164`
- `market_context_high->fx_1h` score `-0.0378` n `128` status `ready` deltaP `6.1986` edge `0.0011` maxDD `-0.3124`
- `market_context_high->crypto_major_4h` score `-0.1438` n `128` status `ready` deltaP `5.6975` edge `0.1357` maxDD `-8.3693`
- `market_context_high->metal_4h` score `-0.2822` n `128` status `ready` deltaP `14.0816` edge `0.0257` maxDD `-6.4478`
- `market_context_high->crypto_alt_1h` score `-0.3539` n `128` status `ready` deltaP `0.1965` edge `0.0376` maxDD `-3.4088`
- `market_context_high->crypto_major_1h` score `-0.405` n `128` status `ready` deltaP `2.5262` edge `0.0078` maxDD `-4.1256`
- `market_context_high->commodity_1h` score `-0.8734` n `128` status `ready` deltaP `-2.9098` edge `0.0081` maxDD `-2.252`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
