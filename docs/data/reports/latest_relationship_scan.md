# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-28T20:21:41.251791+00:00`
- Price records: `672`
- Market context records: `5075`
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

- `market_context_high->unknown_24h` score `12.4211` n `80` status `ready` deltaP `27.8472` edge `0.8837` maxDD `-1.4072`
- `market_context_high->unknown_1h` score `11.6151` n `103` status `ready` deltaP `3.8428` edge `0.9924` maxDD `-1.674`
- `market_context_high->unknown_4h` score `9.4036` n `94` status `ready` deltaP `20.8128` edge `0.7471` maxDD `-5.5109`
- `market_context_high->crypto_alt_4h` score `7.0262` n `94` status `ready` deltaP `20.5274` edge `0.5706` maxDD `-6.4213`
- `market_context_high->crypto_major_4h` score `6.3023` n `94` status `ready` deltaP `19.0095` edge `0.5569` maxDD `-8.3416`
- `market_context_high->equity_4h` score `1.624` n `94` status `ready` deltaP `7.6025` edge `0.1978` maxDD `-6.3852`
- `market_context_high->metal_4h` score `1.0216` n `94` status `ready` deltaP `10.6545` edge `0.122` maxDD `-1.9651`
- `market_context_high->crypto_major_1h` score `0.8406` n `103` status `ready` deltaP `6.9952` edge `0.1259` maxDD `-5.1989`
- `market_context_high->crypto_alt_1h` score `0.8196` n `103` status `ready` deltaP `5.7933` edge `0.1107` maxDD `-3.8153`
- `market_context_high->metal_1h` score `0.5987` n `103` status `ready` deltaP `9.3817` edge `0.037` maxDD `-1.3057`
- `market_context_high->equity_1h` score `0.5443` n `103` status `ready` deltaP `8.1798` edge `0.0726` maxDD `-2.5875`
- `market_context_high->index_4h` score `0.2102` n `94` status `ready` deltaP `7.4598` edge `0.0439` maxDD `-1.0893`
- `market_context_high->index_1h` score `-0.1639` n `103` status `ready` deltaP `2.2048` edge `0.0123` maxDD `-0.5074`
- `market_context_high->commodity_1h` score `-0.3119` n `103` status `ready` deltaP `3.4024` edge `0.0173` maxDD `-1.278`
- `market_context_high->fx_24h` score `-0.4761` n `80` status `ready` deltaP `1.9444` edge `0.0022` maxDD `-1.7626`
- `market_context_high->commodity_4h` score `-0.6652` n `94` status `ready` deltaP `8.3841` edge `0.0083` maxDD `-4.5699`
- `market_context_high->fx_4h` score `-0.956` n `94` status `ready` deltaP `-3.4997` edge `-0.0003` maxDD `-1.2484`
- `market_context_high->fx_1h` score `-1.5187` n `103` status `ready` deltaP `-9.2189` edge `-0.0035` maxDD `-0.5945`
- `market_context_high->commodity_24h` score `-2.7608` n `80` status `ready` deltaP `7.9514` edge `-0.0021` maxDD `-21.3882`
- `market_context_high->metal_24h` score `-3.8457` n `80` status `ready` deltaP `0.3819` edge `0.0499` maxDD `-32.9721`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
