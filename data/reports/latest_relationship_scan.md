# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-06T20:32:21.101377+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10299`

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

- `risk_on_high->unknown_24h` score `275.1556` n `104` status `ready` deltaP `26.6427` edge `22.7567` maxDD `-0.0416`
- `risk_on_and_context->unknown_24h` score `275.1556` n `104` status `ready` deltaP `26.6427` edge `22.7567` maxDD `-0.0416`
- `risk_on_high->crypto_major_24h` score `19.9863` n `104` status `ready` deltaP `33.0929` edge `1.4966` maxDD `-1.4687`
- `risk_on_and_context->crypto_major_24h` score `19.9863` n `104` status `ready` deltaP `33.0929` edge `1.4966` maxDD `-1.4687`
- `risk_on_high->crypto_alt_24h` score `13.0799` n `104` status `ready` deltaP `27.2302` edge `0.9291` maxDD `-0.6512`
- `risk_on_and_context->crypto_alt_24h` score `13.0799` n `104` status `ready` deltaP `27.2302` edge `0.9291` maxDD `-0.6512`
- `market_context_high->crypto_alt_24h` score `8.1102` n `196` status `ready` deltaP `21.8927` edge `0.5874` maxDD `-2.5998`
- `market_context_high->equity_24h` score `6.7612` n `196` status `ready` deltaP `23.0903` edge `0.4095` maxDD `0.0`
- `risk_on_high->equity_24h` score `6.0016` n `104` status `ready` deltaP `23.0903` edge `0.3462` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `6.0016` n `104` status `ready` deltaP `23.0903` edge `0.3462` maxDD `0.0`
- `risk_on_high->crypto_alt_4h` score `3.9372` n `118` status `ready` deltaP `27.2142` edge `0.2818` maxDD `-9.1438`
- `risk_on_and_context->crypto_alt_4h` score `3.9372` n `118` status `ready` deltaP `27.2142` edge `0.2818` maxDD `-9.1438`
- `risk_on_high->crypto_major_4h` score `2.2589` n `118` status `ready` deltaP `21.2588` edge `0.2185` maxDD `-10.759`
- `risk_on_and_context->crypto_major_4h` score `2.2589` n `118` status `ready` deltaP `21.2588` edge `0.2185` maxDD `-10.759`
- `risk_on_high->index_24h` score `2.2479` n `104` status `ready` deltaP `20.1789` edge `0.08` maxDD `-0.5094`
- `risk_on_and_context->index_24h` score `2.2479` n `104` status `ready` deltaP `20.1789` edge `0.08` maxDD `-0.5094`
- `market_context_high->index_24h` score `2.1057` n `196` status `ready` deltaP `20.277` edge `0.0929` maxDD `-0.875`
- `risk_on_high->crypto_alt_1h` score `0.7549` n `129` status `ready` deltaP `4.3274` edge `0.0826` maxDD `-2.2169`
- `risk_on_and_context->crypto_alt_1h` score `0.7549` n `129` status `ready` deltaP `4.3274` edge `0.0826` maxDD `-2.2169`
- `risk_on_high->metal_24h` score `0.7333` n `104` status `ready` deltaP `14.0759` edge `0.1001` maxDD `-2.6605`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
