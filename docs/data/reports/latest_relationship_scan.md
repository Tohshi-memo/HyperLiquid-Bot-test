# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-28T20:37:25.256235+00:00`
- Price records: `672`
- Market context records: `5076`
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

- `market_context_high->unknown_24h` score `12.3966` n `79` status `ready` deltaP `27.7206` edge `0.8825` maxDD `-1.4072`
- `market_context_high->unknown_1h` score `12.0687` n `103` status `ready` deltaP `3.8428` edge `1.0302` maxDD `-1.674`
- `market_context_high->unknown_4h` score `9.3891` n `93` status `ready` deltaP `20.5268` edge `0.7478` maxDD `-5.5109`
- `market_context_high->crypto_alt_4h` score `7.199` n `93` status `ready` deltaP `21.248` edge `0.5802` maxDD `-6.4213`
- `market_context_high->crypto_major_4h` score `6.4529` n `93` status `ready` deltaP `19.7073` edge `0.5648` maxDD `-8.3416`
- `market_context_high->equity_4h` score `1.7623` n `93` status `ready` deltaP `8.0563` edge `0.2063` maxDD `-6.3852`
- `market_context_high->metal_4h` score `0.9724` n `93` status `ready` deltaP `10.1741` edge `0.1211` maxDD `-1.9651`
- `market_context_high->crypto_major_1h` score `0.9675` n `103` status `ready` deltaP `7.8164` edge `0.131` maxDD `-5.1989`
- `market_context_high->crypto_alt_1h` score `0.9621` n `103` status `ready` deltaP `6.6144` edge `0.1171` maxDD `-3.8153`
- `market_context_high->metal_1h` score `0.6692` n `103` status `ready` deltaP `10.2029` edge `0.0374` maxDD `-1.3057`
- `market_context_high->equity_1h` score `0.598` n `103` status `ready` deltaP `9.0009` edge `0.074` maxDD `-2.5875`
- `market_context_high->index_4h` score `0.2533` n `93` status `ready` deltaP `7.8793` edge `0.0447` maxDD `-1.0893`
- `market_context_high->index_1h` score `-0.0837` n `103` status `ready` deltaP `3.026` edge `0.0128` maxDD `-0.4963`
- `market_context_high->commodity_1h` score `-0.4112` n `103` status `ready` deltaP `2.5812` edge `0.0145` maxDD `-1.278`
- `market_context_high->fx_24h` score `-0.5077` n `79` status `ready` deltaP `1.501` edge `0.0011` maxDD `-1.7626`
- `market_context_high->commodity_4h` score `-0.5731` n `93` status `ready` deltaP `8.9217` edge `0.0101` maxDD `-4.3872`
- `market_context_high->fx_4h` score `-0.978` n `93` status `ready` deltaP `-3.9077` edge `-0.0004` maxDD `-1.2484`
- `market_context_high->fx_1h` score `-0.9886` n `103` status `ready` deltaP `-9.2189` edge `-0.0034` maxDD `-0.6178`
- `market_context_high->commodity_24h` score `-2.5379` n `79` status `ready` deltaP `8.3949` edge `0.0068` maxDD `-20.3848`
- `market_context_high->metal_24h` score `-3.9406` n `79` status `ready` deltaP `-0.3934` edge `0.0429` maxDD `-32.9721`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
