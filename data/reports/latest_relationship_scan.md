# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-11T08:22:29.070666+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `5970`

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

- `market_context_high->unknown_4h` score `42.5931` n `85` status `ready` deltaP `-12.9484` edge `3.6938` maxDD `-2.3109`
- `market_context_high->equity_24h` score `9.5405` n `68` status `ready` deltaP `37.4591` edge `0.5882` maxDD `-1.0977`
- `market_context_high->crypto_major_24h` score `7.2527` n `68` status `ready` deltaP `10.7639` edge `1.1729` maxDD `-17.8526`
- `market_context_high->fx_4h` score `1.7036` n `85` status `ready` deltaP `23.75` edge `0.012` maxDD `-0.2692`
- `market_context_high->index_24h` score `0.508` n `68` status `ready` deltaP `13.8582` edge `0.1075` maxDD `-1.4474`
- `market_context_high->fx_1h` score `0.2103` n `97` status `ready` deltaP `7.3477` edge `0.0022` maxDD `-0.271`
- `market_context_high->commodity_4h` score `-0.0685` n `85` status `ready` deltaP `6.1693` edge `0.0065` maxDD `-1.6002`
- `market_context_high->commodity_1h` score `-0.1894` n `97` status `ready` deltaP `1.6282` edge `0.0068` maxDD `-0.3417`
- `market_context_high->crypto_major_1h` score `-0.3743` n `97` status `ready` deltaP `1.3797` edge `0.0317` maxDD `-3.7778`
- `market_context_high->crypto_major_4h` score `-0.4378` n `85` status `ready` deltaP `3.4845` edge `0.123` maxDD `-10.5224`
- `market_context_high->metal_1h` score `-0.4742` n `97` status `ready` deltaP `-0.3997` edge `0.0014` maxDD `-0.7626`
- `market_context_high->fx_24h` score `-0.7716` n `68` status `ready` deltaP `4.759` edge `0.0059` maxDD `-1.5905`
- `market_context_high->metal_24h` score `-0.9143` n `68` status `ready` deltaP `-2.5225` edge `0.0481` maxDD `-3.5466`
- `market_context_high->crypto_alt_1h` score `-0.9749` n `97` status `ready` deltaP `-4.3907` edge `0.0202` maxDD `-4.9401`
- `market_context_high->index_4h` score `-1.2606` n `85` status `ready` deltaP `-10.3049` edge `0.0003` maxDD `-1.1242`
- `market_context_high->index_1h` score `-1.64` n `97` status `ready` deltaP `-7.1501` edge `-0.0028` maxDD `-0.5627`
- `market_context_high->equity_1h` score `-1.6945` n `97` status `ready` deltaP `-7.1023` edge `-0.0069` maxDD `-2.2898`
- `market_context_high->crypto_alt_24h` score `-1.834` n `68` status `ready` deltaP `-3.6152` edge `0.4002` maxDD `-35.5652`
- `market_context_high->metal_4h` score `-1.8865` n `85` status `ready` deltaP `-11.7001` edge `0.0139` maxDD `-1.1153`
- `market_context_high->equity_4h` score `-2.7278` n `85` status `ready` deltaP `-9.1912` edge `-0.0068` maxDD `-6.4057`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
