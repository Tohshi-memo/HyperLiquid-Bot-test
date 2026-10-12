# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-12T01:37:31.109624+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `9488`

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

- `market_context_high->unknown_24h` score `993.4813` n `46` status `ready` deltaP `-19.3085` edge `82.9552` maxDD `-1.2425`
- `market_context_high->unknown_4h` score `38.0176` n `111` status `ready` deltaP `-8.7618` edge `3.2971` maxDD `-2.3109`
- `market_context_high->equity_24h` score `9.3776` n `46` status `ready` deltaP `30.6084` edge `0.6203` maxDD `-1.0977`
- `market_context_high->index_24h` score `6.0526` n `46` status `ready` deltaP `50.4303` edge `0.1725` maxDD `-0.012`
- `risk_on_high->crypto_alt_4h` score `5.4435` n `32` status `ready` deltaP `24.314` edge `0.3363` maxDD `-1.9151`
- `risk_on_and_context->crypto_alt_4h` score `5.4435` n `32` status `ready` deltaP `24.314` edge `0.3363` maxDD `-1.9151`
- `risk_on_high->crypto_major_4h` score `4.9538` n `32` status `ready` deltaP `27.0579` edge `0.3177` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `4.9538` n `32` status `ready` deltaP `27.0579` edge `0.3177` maxDD `-4.1548`
- `market_context_high->crypto_major_24h` score `4.377` n `46` status `ready` deltaP `-10.0241` edge `0.7464` maxDD `-17.8526`
- `risk_on_high->metal_4h` score `2.9468` n `32` status `ready` deltaP `26.9055` edge `0.0894` maxDD `-0.1896`
- `risk_on_and_context->metal_4h` score `2.9468` n `32` status `ready` deltaP `26.9055` edge `0.0894` maxDD `-0.1896`
- `market_context_high->fx_24h` score `1.7014` n `46` status `ready` deltaP `21.5806` edge `0.0254` maxDD `-0.1993`
- `risk_on_high->crypto_major_1h` score `1.4019` n `44` status `ready` deltaP `13.0376` edge `0.0952` maxDD `-3.2233`
- `risk_on_and_context->crypto_major_1h` score `1.4019` n `44` status `ready` deltaP `13.0376` edge `0.0952` maxDD `-3.2233`
- `risk_on_high->metal_1h` score `1.2652` n `44` status `ready` deltaP `15.6369` edge `0.0251` maxDD `-0.2466`
- `risk_on_and_context->metal_1h` score `1.2652` n `44` status `ready` deltaP `15.6369` edge `0.0251` maxDD `-0.2466`
- `market_context_high->unknown_1h` score `0.9604` n `123` status `ready` deltaP `-3.8167` edge `0.1391` maxDD `-1.0231`
- `risk_on_high->crypto_alt_1h` score `0.8872` n `44` status `ready` deltaP `9.4448` edge `0.1063` maxDD `-2.4421`
- `risk_on_and_context->crypto_alt_1h` score `0.8872` n `44` status `ready` deltaP `9.4448` edge `0.1063` maxDD `-2.4421`
- `risk_on_high->equity_4h` score `0.7286` n `32` status `ready` deltaP `6.8598` edge `0.0858` maxDD `-1.0501`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
