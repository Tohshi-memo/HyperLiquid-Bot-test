# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-04T23:22:24.262032+00:00`
- Price records: `672`
- Market context records: `2913`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6912`

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

- `market_context_high->crypto_alt_24h` score `12.7066` n `142` status `ready` deltaP `11.9034` edge `1.3712` maxDD `-22.6673`
- `market_context_high->equity_24h` score `6.4241` n `142` status `ready` deltaP `14.1163` edge `0.6416` maxDD `-12.6963`
- `market_context_high->unknown_24h` score `5.6843` n `142` status `ready` deltaP `12.3239` edge `0.438` maxDD `-1.7175`
- `market_context_high->index_24h` score `2.1838` n `142` status `ready` deltaP `10.2382` edge `0.2118` maxDD `-2.5127`
- `market_context_high->commodity_24h` score `1.7868` n `142` status `ready` deltaP `15.5516` edge `0.3546` maxDD `-12.4171`
- `market_context_high->index_4h` score `0.486` n `142` status `ready` deltaP `13.1484` edge `0.0588` maxDD `-2.3986`
- `market_context_high->equity_4h` score `0.3013` n `142` status `ready` deltaP `6.5355` edge `0.1195` maxDD `-5.7037`
- `market_context_high->unknown_4h` score `0.1311` n `142` status `ready` deltaP `4.5087` edge `0.0862` maxDD `-3.7602`
- `market_context_high->index_1h` score `-0.0368` n `142` status `ready` deltaP `4.198` edge `0.0167` maxDD `-1.2855`
- `market_context_high->crypto_alt_4h` score `-0.1581` n `142` status `ready` deltaP `15.4049` edge `0.3182` maxDD `-28.7261`
- `market_context_high->unknown_1h` score `-0.2893` n `142` status `ready` deltaP `4.1811` edge `0.0211` maxDD `-3.1801`
- `market_context_high->equity_1h` score `-0.398` n `142` status `ready` deltaP `0.6937` edge `0.0455` maxDD `-2.6634`
- `market_context_high->crypto_alt_1h` score `-0.4621` n `142` status `ready` deltaP `6.1441` edge `0.0758` maxDD `-10.747`
- `market_context_high->fx_1h` score `-0.5514` n `142` status `ready` deltaP `-0.6873` edge `0.003` maxDD `-0.2164`
- `market_context_high->commodity_1h` score `-0.603` n `142` status `ready` deltaP `-0.5819` edge `0.0019` maxDD `-4.3601`
- `market_context_high->crypto_major_1h` score `-0.6193` n `142` status `ready` deltaP `6.0218` edge `0.0674` maxDD `-9.622`
- `market_context_high->metal_1h` score `-0.6614` n `142` status `ready` deltaP `-0.1666` edge `0.0009` maxDD `-3.0996`
- `market_context_high->fx_4h` score `-0.9862` n `142` status `ready` deltaP `-1.7713` edge `0.0075` maxDD `-0.5631`
- `market_context_high->commodity_4h` score `-1.2441` n `142` status `ready` deltaP `2.4476` edge `0.0162` maxDD `-10.0279`
- `market_context_high->fx_24h` score `-1.2768` n `142` status `ready` deltaP `-1.7116` edge `-0.0078` maxDD `-0.6418`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
