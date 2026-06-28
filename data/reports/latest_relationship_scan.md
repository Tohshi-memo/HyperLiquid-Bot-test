# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-28T21:22:26.686372+00:00`
- Price records: `672`
- Market context records: `5079`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10338`

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

- `market_context_high->unknown_24h` score `12.4906` n `76` status `ready` deltaP `27.3209` edge `0.893` maxDD `-1.4072`
- `market_context_high->unknown_1h` score `12.2322` n `103` status `ready` deltaP `3.0216` edge `1.0493` maxDD `-1.674`
- `market_context_high->unknown_4h` score `9.4464` n `91` status `ready` deltaP `20.8825` edge `0.7502` maxDD `-5.5109`
- `market_context_high->crypto_alt_4h` score `7.0647` n `91` status `ready` deltaP `20.844` edge `0.5717` maxDD `-6.4213`
- `market_context_high->crypto_major_4h` score `6.3532` n `91` status `ready` deltaP `19.2559` edge `0.5595` maxDD `-8.3416`
- `market_context_high->equity_4h` score `2.0975` n `91` status `ready` deltaP `9.9505` edge `0.2216` maxDD `-6.3852`
- `market_context_high->equity_1h` score `1.074` n `103` status `ready` deltaP `9.8221` edge `0.0772` maxDD `-2.5875`
- `market_context_high->crypto_major_1h` score `0.9927` n `103` status `ready` deltaP `7.8164` edge `0.1331` maxDD `-5.1989`
- `market_context_high->crypto_alt_1h` score `0.9801` n `103` status `ready` deltaP `6.6144` edge `0.1186` maxDD `-3.8153`
- `market_context_high->metal_1h` score `0.8855` n `103` status `ready` deltaP `12.6664` edge `0.039` maxDD `-1.3057`
- `market_context_high->metal_4h` score `0.6878` n `91` status `ready` deltaP `9.1816` edge `0.104` maxDD `-1.9651`
- `market_context_high->index_1h` score `0.2735` n `103` status `ready` deltaP `5.4895` edge `0.016` maxDD `-0.3843`
- `market_context_high->index_4h` score `0.2526` n `91` status `ready` deltaP `7.8096` edge `0.0451` maxDD `-1.0893`
- `market_context_high->commodity_4h` score `-0.3285` n `91` status `ready` deltaP `10.0325` edge `0.0141` maxDD `-3.6686`
- `market_context_high->fx_24h` score `-0.6186` n `76` status `ready` deltaP `0.0731` edge `-0.0036` maxDD `-1.7626`
- `market_context_high->commodity_1h` score `-0.7163` n `103` status `ready` deltaP `0.1177` edge `0.0055` maxDD `-1.278`
- `market_context_high->fx_4h` score `-1.1041` n `91` status `ready` deltaP `-5.7073` edge `-0.0039` maxDD `-1.3012`
- `market_context_high->fx_1h` score `-1.7538` n `103` status `ready` deltaP `-11.6825` edge `-0.0051` maxDD `-0.7201`
- `market_context_high->commodity_24h` score `-1.9061` n `76` status `ready` deltaP `9.8227` edge `0.0317` maxDD `-17.6575`
- `market_context_high->metal_24h` score `-4.2536` n `76` status `ready` deltaP `-2.8418` edge `0.0191` maxDD `-32.9721`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
