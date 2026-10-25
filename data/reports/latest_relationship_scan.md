# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-25T00:37:24.244614+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7158`

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

- `market_context_high->unknown_4h` score `22.7709` n `95` status `ready` deltaP `1.741` edge `1.9195` maxDD `-1.016`
- `market_context_high->commodity_24h` score `1.7035` n `56` status `ready` deltaP `22.5694` edge `0.0824` maxDD `-3.6055`
- `market_context_high->commodity_4h` score `0.9972` n `95` status `ready` deltaP `12.8899` edge `0.0534` maxDD `-1.165`
- `market_context_high->commodity_1h` score `-0.2278` n `107` status `ready` deltaP `3.1171` edge `0.0103` maxDD `-1.0053`
- `market_context_high->fx_1h` score `-0.2891` n `107` status `ready` deltaP `-0.6128` edge `0.0025` maxDD `-0.1712`
- `market_context_high->metal_1h` score `-0.922` n `107` status `ready` deltaP `1.1836` edge `-0.0053` maxDD `-1.6873`
- `market_context_high->fx_4h` score `-0.9649` n `95` status `ready` deltaP `-3.5976` edge `0.0042` maxDD `-0.5168`
- `market_context_high->index_1h` score `-1.154` n `107` status `ready` deltaP `-3.5662` edge `-0.0072` maxDD `-1.2155`
- `market_context_high->fx_24h` score `-1.7432` n `56` status `ready` deltaP `-5.2083` edge `-0.0027` maxDD `-1.6275`
- `market_context_high->crypto_major_24h` score `-2.3051` n `56` status `ready` deltaP `-1.1657` edge `-0.0453` maxDD `-14.7298`
- `market_context_high->crypto_major_1h` score `-2.4272` n `107` status `ready` deltaP `0.6897` edge `-0.0348` maxDD `-10.432`
- `market_context_high->crypto_alt_1h` score `-3.277` n `107` status `ready` deltaP `0.5079` edge `-0.0548` maxDD `-14.4004`
- `market_context_high->metal_24h` score `-3.4011` n `56` status `ready` deltaP `-11.2351` edge `0.0098` maxDD `-7.1326`
- `market_context_high->metal_4h` score `-3.4097` n `95` status `ready` deltaP `-11.0029` edge `-0.0326` maxDD `-5.9219`
- `market_context_high->equity_1h` score `-4.0171` n `107` status `ready` deltaP `-1.1347` edge `-0.0943` maxDD `-12.6316`
- `market_context_high->index_4h` score `-4.9792` n `95` status `ready` deltaP `-24.3742` edge `-0.0535` maxDD `-5.2481`
- `market_context_high->index_24h` score `-7.7226` n `56` status `ready` deltaP `-37.5` edge `-0.1756` maxDD `-6.7695`
- `market_context_high->crypto_alt_24h` score `-7.8858` n `56` status `ready` deltaP `1.7361` edge `-0.2866` maxDD `-51.2117`
- `market_context_high->unknown_1h` score `-8.2057` n `107` status `ready` deltaP `-0.1973` edge `-0.6336` maxDD `-1.5781`
- `market_context_high->crypto_major_4h` score `-13.754` n `95` status `ready` deltaP `-24.5267` edge `-0.3522` maxDD `-43.1034`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
