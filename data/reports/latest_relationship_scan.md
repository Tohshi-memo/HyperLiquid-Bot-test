# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-06T20:52:25.435190+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10329`

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

- `risk_on_high->unknown_24h` score `271.8316` n `105` status `ready` deltaP `26.4782` edge `22.4808` maxDD `-0.0416`
- `risk_on_and_context->unknown_24h` score `271.8316` n `105` status `ready` deltaP `26.4782` edge `22.4808` maxDD `-0.0416`
- `risk_on_high->crypto_major_24h` score `19.7566` n `105` status `ready` deltaP `33.0109` edge `1.478` maxDD `-1.4687`
- `risk_on_and_context->crypto_major_24h` score `19.7566` n `105` status `ready` deltaP `33.0109` edge `1.478` maxDD `-1.4687`
- `risk_on_high->crypto_alt_24h` score `12.9526` n `105` status `ready` deltaP `27.0933` edge `0.9194` maxDD `-0.6512`
- `risk_on_and_context->crypto_alt_24h` score `12.9526` n `105` status `ready` deltaP `27.0933` edge `0.9194` maxDD `-0.6512`
- `market_context_high->crypto_alt_24h` score `8.2116` n `196` status `ready` deltaP `22.2293` edge `0.5936` maxDD `-2.5998`
- `market_context_high->equity_24h` score `6.7732` n `196` status `ready` deltaP `23.0903` edge `0.4105` maxDD `0.0`
- `risk_on_high->equity_24h` score `5.9404` n `105` status `ready` deltaP `23.0903` edge `0.3411` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `5.9404` n `105` status `ready` deltaP `23.0903` edge `0.3411` maxDD `0.0`
- `risk_on_high->crypto_alt_4h` score `3.8695` n `119` status `ready` deltaP `27.1188` edge `0.2768` maxDD `-9.1438`
- `risk_on_and_context->crypto_alt_4h` score `3.8695` n `119` status `ready` deltaP `27.1188` edge `0.2768` maxDD `-9.1438`
- `risk_on_high->index_24h` score `2.2235` n `105` status `ready` deltaP `20.0694` edge `0.0787` maxDD `-0.5094`
- `risk_on_and_context->index_24h` score `2.2235` n `105` status `ready` deltaP `20.0694` edge `0.0787` maxDD `-0.5094`
- `risk_on_high->crypto_major_4h` score `2.2207` n `119` status `ready` deltaP `21.2915` edge `0.2151` maxDD `-10.759`
- `risk_on_and_context->crypto_major_4h` score `2.2207` n `119` status `ready` deltaP `21.2915` edge `0.2151` maxDD `-10.759`
- `market_context_high->index_24h` score `2.2075` n `196` status `ready` deltaP `20.6137` edge `0.0933` maxDD `-0.7414`
- `risk_on_high->crypto_alt_1h` score `0.7321` n `129` status `ready` deltaP `4.1777` edge `0.0817` maxDD `-2.2169`
- `risk_on_and_context->crypto_alt_1h` score `0.7321` n `129` status `ready` deltaP `4.1777` edge `0.0817` maxDD `-2.2169`
- `risk_on_high->metal_24h` score `0.6533` n `105` status `ready` deltaP `13.4623` edge `0.0981` maxDD `-2.6605`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
