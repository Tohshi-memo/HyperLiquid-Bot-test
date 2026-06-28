# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-28T19:52:25.653065+00:00`
- Price records: `672`
- Market context records: `5073`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10324`

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

- `market_context_high->unknown_24h` score `12.4298` n `82` status `ready` deltaP `28.0911` edge `0.8828` maxDD `-1.4072`
- `market_context_high->unknown_1h` score `11.1099` n `103` status `ready` deltaP `3.8428` edge `0.9503` maxDD `-1.674`
- `market_context_high->unknown_4h` score `9.3591` n `96` status `ready` deltaP `21.3668` edge `0.7397` maxDD `-5.5109`
- `market_context_high->crypto_alt_4h` score `6.4945` n `96` status `ready` deltaP `19.1311` edge `0.5356` maxDD `-6.4213`
- `market_context_high->crypto_major_4h` score `5.8198` n `96` status `ready` deltaP `17.6576` edge `0.5257` maxDD `-8.3416`
- `market_context_high->metal_4h` score `1.0093` n `96` status `ready` deltaP `10.6961` edge `0.1207` maxDD `-1.9651`
- `market_context_high->equity_4h` score `0.8093` n `96` status `ready` deltaP `6.5803` edge `0.1772` maxDD `-6.3852`
- `market_context_high->equity_1h` score `0.6485` n `103` status `ready` deltaP `6.5374` edge `0.0678` maxDD `-2.5875`
- `market_context_high->crypto_major_1h` score `0.6373` n `103` status `ready` deltaP `6.174` edge `0.1081` maxDD `-5.0256`
- `market_context_high->metal_1h` score `0.5246` n `103` status `ready` deltaP `8.5605` edge `0.0363` maxDD `-1.3057`
- `market_context_high->crypto_alt_1h` score `0.2836` n `103` status `ready` deltaP `4.9721` edge `0.0914` maxDD `-4.3889`
- `market_context_high->index_4h` score `0.0783` n `96` status `ready` deltaP `6.3516` edge `0.0403` maxDD `-1.0893`
- `market_context_high->index_1h` score `-0.2786` n `103` status `ready` deltaP `1.3836` edge `0.0119` maxDD `-0.5475`
- `market_context_high->commodity_1h` score `-0.398` n `103` status `ready` deltaP `2.5812` edge `0.0156` maxDD `-1.278`
- `market_context_high->fx_24h` score `-0.4144` n `82` status `ready` deltaP `2.7862` edge `0.0045` maxDD `-1.7626`
- `market_context_high->commodity_4h` score `-0.8114` n `96` status `ready` deltaP `7.3424` edge `0.0063` maxDD `-4.829`
- `market_context_high->fx_4h` score `-0.9131` n `96` status `ready` deltaP `-2.7185` edge `0.0` maxDD `-1.2484`
- `market_context_high->fx_1h` score `-1.5963` n `103` status `ready` deltaP `-10.0401` edge `-0.0045` maxDD `-0.594`
- `market_context_high->commodity_24h` score `-3.1727` n `82` status `ready` deltaP `7.1096` edge `-0.0171` maxDD `-23.2975`
- `market_context_high->metal_24h` score `-3.6749` n `82` status `ready` deltaP `1.7022` edge `0.063` maxDD `-32.9721`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
