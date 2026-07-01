# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-01T11:47:43.938142+00:00`
- Price records: `672`
- Market context records: `5348`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11468`

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

- `market_context_high->unknown_24h` score `16.4738` n `158` status `ready` deltaP `20.6707` edge `1.244` maxDD `-0.3859`
- `market_context_high->crypto_major_24h` score `5.879` n `158` status `ready` deltaP `22.431` edge `0.7853` maxDD `-28.9274`
- `market_context_high->equity_24h` score `4.6423` n `158` status `ready` deltaP `17.8863` edge `0.8305` maxDD `-40.0306`
- `market_context_high->crypto_major_4h` score `2.8531` n `194` status `ready` deltaP `13.3361` edge `0.3781` maxDD `-14.0065`
- `market_context_high->crypto_alt_4h` score `2.62` n `194` status `ready` deltaP `10.8169` edge `0.3103` maxDD `-9.46`
- `market_context_high->equity_4h` score `1.8086` n `194` status `ready` deltaP `10.0924` edge `0.2473` maxDD `-7.4425`
- `market_context_high->index_24h` score `0.843` n `158` status `ready` deltaP `25.255` edge `0.1032` maxDD `-7.413`
- `market_context_high->equity_1h` score `0.4644` n `194` status `ready` deltaP `7.7135` edge `0.0838` maxDD `-5.0555`
- `market_context_high->fx_24h` score `0.1434` n `158` status `ready` deltaP `9.4629` edge `0.0384` maxDD `-0.8294`
- `market_context_high->crypto_major_1h` score `0.1054` n `194` status `ready` deltaP `4.7904` edge `0.1014` maxDD `-6.9639`
- `market_context_high->crypto_alt_1h` score `0.0722` n `194` status `ready` deltaP `2.0958` edge `0.0882` maxDD `-5.0257`
- `market_context_high->index_1h` score `0.0538` n `194` status `ready` deltaP `6.3677` edge `0.0124` maxDD `-1.0296`
- `market_context_high->fx_1h` score `-0.3797` n `194` status `ready` deltaP `0.1158` edge `-0.0005` maxDD `-0.5823`
- `market_context_high->index_4h` score `-0.3951` n `194` status `ready` deltaP `5.9168` edge `0.0258` maxDD `-2.9391`
- `market_context_high->metal_1h` score `-0.4737` n `194` status `ready` deltaP `0.7485` edge `0.0018` maxDD `-2.0682`
- `market_context_high->fx_4h` score `-0.7016` n `194` status `ready` deltaP `1.5259` edge `0.0028` maxDD `-1.567`
- `market_context_high->unknown_4h` score `-1.2809` n `194` status `ready` deltaP `7.7555` edge `-0.0402` maxDD `-6.126`
- `market_context_high->commodity_1h` score `-1.4682` n `194` status `ready` deltaP `-3.6252` edge `-0.0064` maxDD `-3.3428`
- `market_context_high->metal_4h` score `-2.5991` n `194` status `ready` deltaP `-7.2243` edge `-0.0326` maxDD `-12.8631`
- `market_context_high->commodity_4h` score `-3.8286` n `194` status `ready` deltaP `-7.1662` edge `-0.0429` maxDD `-11.937`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
