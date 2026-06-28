# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-28T14:37:25.374552+00:00`
- Price records: `672`
- Market context records: `5049`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10276`

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

- `market_context_high->unknown_1h` score `11.7736` n `101` status `ready` deltaP `3.6491` edge `1.0069` maxDD `-1.674`
- `market_context_high->unknown_4h` score `8.2776` n `95` status `ready` deltaP `20.1926` edge `0.6574` maxDD `-5.5109`
- `market_context_high->crypto_major_4h` score `5.5197` n `95` status `ready` deltaP `17.7166` edge `0.5003` maxDD `-8.3416`
- `market_context_high->crypto_alt_4h` score `5.2577` n `95` status `ready` deltaP `14.4207` edge `0.4814` maxDD `-7.8181`
- `market_context_high->metal_4h` score `1.0912` n `95` status `ready` deltaP `11.7346` edge `0.1206` maxDD `-1.9651`
- `market_context_high->crypto_major_1h` score `0.7499` n `101` status `ready` deltaP `6.9662` edge `0.1078` maxDD `-4.6734`
- `market_context_high->equity_1h` score `0.693` n `101` status `ready` deltaP `7.0344` edge `0.0682` maxDD `-2.5875`
- `market_context_high->equity_4h` score `0.3886` n `95` status `ready` deltaP `2.9653` edge `0.1682` maxDD `-6.3852`
- `market_context_high->metal_1h` score `0.3238` n `101` status `ready` deltaP `6.1258` edge `0.0358` maxDD `-1.3057`
- `market_context_high->crypto_alt_1h` score `0.161` n `101` status `ready` deltaP `5.112` edge `0.0888` maxDD `-5.5126`
- `market_context_high->fx_24h` score `-0.0953` n `77` status `ready` deltaP `8.3514` edge `0.0083` maxDD `-1.7626`
- `market_context_high->index_4h` score `-0.2253` n `95` status `ready` deltaP `2.8418` edge `0.0384` maxDD `-1.0893`
- `market_context_high->commodity_1h` score `-0.3144` n `101` status `ready` deltaP `1.6008` edge `0.015` maxDD `-1.278`
- `market_context_high->index_1h` score `-0.4361` n `101` status `ready` deltaP `0.9441` edge `0.0119` maxDD `-0.5946`
- `market_context_high->commodity_4h` score `-0.6752` n `95` status `ready` deltaP `5.3097` edge `0.0033` maxDD `-5.021`
- `market_context_high->fx_4h` score `-1.0422` n `95` status `ready` deltaP `-4.7513` edge `-0.003` maxDD `-1.2484`
- `market_context_high->fx_1h` score `-1.4732` n `101` status `ready` deltaP `-8.5418` edge `-0.0048` maxDD `-0.5482`
- `market_context_high->unknown_24h` score `-1.7101` n `77` status `ready` deltaP `27.4576` edge `-0.2913` maxDD `-1.4072`
- `market_context_high->metal_24h` score `-3.5204` n `77` status `ready` deltaP `6.038` edge `0.0539` maxDD `-32.9721`
- `market_context_high->commodity_24h` score `-4.601` n `77` status `ready` deltaP `0.8567` edge `-0.0847` maxDD `-27.5371`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
