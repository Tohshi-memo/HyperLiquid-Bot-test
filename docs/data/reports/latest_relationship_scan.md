# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-28T11:22:24.417281+00:00`
- Price records: `672`
- Market context records: `5034`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10200`

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

- `market_context_high->unknown_1h` score `14.063` n `95` status `ready` deltaP `2.4913` edge `1.2054` maxDD `-1.674`
- `market_context_high->unknown_4h` score `9.0787` n `93` status `ready` deltaP `22.2118` edge `0.7107` maxDD `-5.5109`
- `market_context_high->crypto_major_4h` score `5.4503` n `93` status `ready` deltaP `16.4897` edge `0.5027` maxDD `-8.3416`
- `market_context_high->crypto_alt_4h` score `5.2804` n `93` status `ready` deltaP `14.1785` edge `0.4849` maxDD `-7.8181`
- `market_context_high->metal_4h` score `1.2404` n `93` status `ready` deltaP `13.2392` edge `0.123` maxDD `-1.9651`
- `market_context_high->equity_1h` score `0.8203` n `95` status `ready` deltaP `7.89` edge `0.0731` maxDD `-2.5875`
- `market_context_high->crypto_major_1h` score `0.683` n `95` status `ready` deltaP `5.7705` edge `0.1102` maxDD `-4.6734`
- `market_context_high->equity_4h` score `0.3781` n `93` status `ready` deltaP `2.3587` edge `0.1709` maxDD `-6.3852`
- `market_context_high->metal_1h` score `0.3613` n `95` status `ready` deltaP `6.3693` edge `0.0373` maxDD `-1.3057`
- `market_context_high->crypto_alt_1h` score `0.1475` n `95` status `ready` deltaP `4.8818` edge `0.0886` maxDD `-5.5126`
- `market_context_high->fx_24h` score `-0.0216` n `74` status `ready` deltaP `9.9053` edge `0.0074` maxDD `-1.7626`
- `market_context_high->index_4h` score `-0.1788` n `93` status `ready` deltaP `3.2569` edge `0.0395` maxDD `-1.0893`
- `market_context_high->commodity_1h` score `-0.3176` n `95` status `ready` deltaP `1.5695` edge `0.0148` maxDD `-1.278`
- `market_context_high->index_1h` score `-0.6264` n `95` status `ready` deltaP `1.4245` edge `0.0124` maxDD `-0.5946`
- `market_context_high->commodity_4h` score `-0.7759` n `93` status `ready` deltaP `4.0028` edge `-0.0009` maxDD `-5.021`
- `market_context_high->fx_4h` score `-1.0181` n `93` status `ready` deltaP `-4.3732` edge `-0.0025` maxDD `-1.2426`
- `market_context_high->fx_1h` score `-1.7183` n `95` status `ready` deltaP `-11.5159` edge `-0.0054` maxDD `-0.5482`
- `market_context_high->metal_24h` score `-3.6842` n `74` status `ready` deltaP `5.9028` edge `0.0338` maxDD `-32.9721`
- `market_context_high->commodity_24h` score `-4.6291` n `74` status `ready` deltaP `0.5865` edge `-0.0865` maxDD `-27.5371`
- `market_context_high->unknown_24h` score `-4.745` n `74` status `ready` deltaP `27.0364` edge `-0.5414` maxDD `-1.4072`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
