# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-29T10:07:31.335888+00:00`
- Price records: `672`
- Market context records: `5134`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5588`

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

- `market_context_high->unknown_24h` score `29.089` n `63` status `ready` deltaP `29.3155` edge `2.2629` maxDD `-1.4072`
- `market_context_high->unknown_1h` score `7.7848` n `130` status `ready` deltaP `8.9521` edge `0.6532` maxDD `-2.7986`
- `market_context_high->unknown_4h` score `7.3189` n `120` status `ready` deltaP `20.2845` edge `0.5769` maxDD `-5.5109`
- `market_context_high->crypto_alt_4h` score `5.022` n `120` status `ready` deltaP `14.8069` edge `0.4797` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `3.568` n `120` status `ready` deltaP `12.6118` edge `0.4425` maxDD `-14.0065`
- `market_context_high->commodity_24h` score `1.5897` n `63` status `ready` deltaP `20.2381` edge `0.1547` maxDD `-4.1987`
- `market_context_high->equity_4h` score `0.8253` n `120` status `ready` deltaP `8.496` edge `0.176` maxDD `-7.4425`
- `market_context_high->crypto_alt_1h` score `0.7527` n `130` status `ready` deltaP `5.3224` edge `0.1234` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `0.6716` n `130` status `ready` deltaP `7.6969` edge `0.1292` maxDD `-6.9639`
- `market_context_high->equity_1h` score `0.6104` n `130` status `ready` deltaP `6.8816` edge `0.0643` maxDD `-2.745`
- `market_context_high->metal_24h` score `0.0636` n `63` status `ready` deltaP `0.9424` edge `0.2` maxDD `-11.4122`
- `market_context_high->metal_1h` score `-0.0283` n `130` status `ready` deltaP `4.9401` edge `0.016` maxDD `-1.5387`
- `market_context_high->index_1h` score `-0.076` n `130` status `ready` deltaP `4.445` edge `0.0144` maxDD `-1.0296`
- `market_context_high->crypto_alt_24h` score `-0.3743` n `63` status `ready` deltaP `15.7986` edge `0.548` maxDD `-50.438`
- `market_context_high->index_4h` score `-0.46` n `120` status `ready` deltaP `5.6402` edge `0.0358` maxDD `-2.9391`
- `market_context_high->commodity_1h` score `-0.4791` n `130` status `ready` deltaP `2.1165` edge `0.0014` maxDD `-2.155`
- `market_context_high->metal_4h` score `-0.5736` n `120` status `ready` deltaP `2.3984` edge `0.0515` maxDD `-4.6157`
- `market_context_high->fx_1h` score `-0.6754` n `130` status `ready` deltaP `-3.1184` edge `-0.0017` maxDD `-0.7944`
- `market_context_high->fx_4h` score `-0.9876` n `120` status `ready` deltaP `-2.9573` edge `0.0004` maxDD `-1.9169`
- `market_context_high->fx_24h` score `-1.0741` n `63` status `ready` deltaP `0.9921` edge `-0.0046` maxDD `-0.9885`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
