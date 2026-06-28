# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-28T14:55:54.101563+00:00`
- Price records: `672`
- Market context records: `5051`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10292`

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

- `market_context_high->unknown_1h` score `11.728` n `101` status `ready` deltaP `3.6491` edge `1.0031` maxDD `-1.674`
- `market_context_high->unknown_4h` score `8.3218` n `96` status `ready` deltaP `20.3252` edge `0.6602` maxDD `-5.5109`
- `market_context_high->crypto_major_4h` score `5.5315` n `96` status `ready` deltaP `18.0894` edge `0.4988` maxDD `-8.3416`
- `market_context_high->crypto_alt_4h` score `5.3223` n `96` status `ready` deltaP `14.8374` edge `0.484` maxDD `-7.8181`
- `market_context_high->metal_4h` score `1.0291` n `96` status `ready` deltaP `11.1534` edge `0.1193` maxDD `-1.9651`
- `market_context_high->crypto_major_1h` score `0.7655` n `101` status `ready` deltaP `7.1159` edge `0.1081` maxDD `-4.6734`
- `market_context_high->equity_1h` score `0.6954` n `101` status `ready` deltaP `7.0344` edge `0.0684` maxDD `-2.5875`
- `market_context_high->equity_4h` score `0.4123` n `96` status `ready` deltaP `3.4807` edge `0.1678` maxDD `-6.3852`
- `market_context_high->metal_1h` score `0.3358` n `101` status `ready` deltaP `6.2755` edge `0.0358` maxDD `-1.3057`
- `market_context_high->crypto_alt_1h` score `0.1579` n `101` status `ready` deltaP `5.112` edge `0.0884` maxDD `-5.5126`
- `market_context_high->fx_24h` score `-0.1051` n `77` status `ready` deltaP `8.1778` edge `0.0082` maxDD `-1.7626`
- `market_context_high->index_4h` score `-0.1933` n `96` status `ready` deltaP `3.2266` edge `0.0385` maxDD `-1.0893`
- `market_context_high->commodity_1h` score `-0.3151` n `101` status `ready` deltaP `1.6008` edge `0.0149` maxDD `-1.278`
- `market_context_high->index_1h` score `-0.4438` n `101` status `ready` deltaP `0.7944` edge `0.0119` maxDD `-0.5946`
- `market_context_high->commodity_4h` score `-0.6313` n `96` status `ready` deltaP `5.8689` edge `0.0052` maxDD `-5.021`
- `market_context_high->fx_4h` score `-1.0203` n `96` status `ready` deltaP `-4.3445` edge `-0.0029` maxDD `-1.2484`
- `market_context_high->fx_1h` score `-1.472` n `101` status `ready` deltaP `-8.5418` edge `-0.0047` maxDD `-0.5482`
- `market_context_high->unknown_24h` score `-2.0317` n `77` status `ready` deltaP `27.4576` edge `-0.3181` maxDD `-1.4072`
- `market_context_high->metal_24h` score `-3.5051` n `77` status `ready` deltaP `6.2116` edge `0.0547` maxDD `-32.9721`
- `market_context_high->commodity_24h` score `-4.6217` n `77` status `ready` deltaP `0.6831` edge `-0.0862` maxDD `-27.5371`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
