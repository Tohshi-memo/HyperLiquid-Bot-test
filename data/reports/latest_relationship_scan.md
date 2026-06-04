# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-04T22:52:25.478222+00:00`
- Price records: `672`
- Market context records: `2911`
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

- `market_context_high->crypto_alt_24h` score `12.3824` n `142` status `ready` deltaP `11.5562` edge `1.3465` maxDD `-22.6673`
- `market_context_high->equity_24h` score `6.3519` n `142` status `ready` deltaP `13.769` edge `0.6379` maxDD `-12.6963`
- `market_context_high->unknown_24h` score `5.5725` n `142` status `ready` deltaP `11.9767` edge `0.431` maxDD `-1.7175`
- `market_context_high->index_24h` score `2.1886` n `142` status `ready` deltaP `10.2382` edge `0.2122` maxDD `-2.5127`
- `market_context_high->commodity_24h` score `1.7796` n `142` status `ready` deltaP `15.5516` edge `0.354` maxDD `-12.4171`
- `market_context_high->index_4h` score `0.479` n `142` status `ready` deltaP `13.1484` edge `0.0579` maxDD `-2.3986`
- `market_context_high->equity_4h` score `0.2507` n `142` status `ready` deltaP `6.3831` edge `0.1163` maxDD `-5.7037`
- `market_context_high->unknown_4h` score `0.1059` n `142` status `ready` deltaP `4.5087` edge `0.0841` maxDD `-3.7602`
- `market_context_high->index_1h` score `-0.0469` n `142` status `ready` deltaP `4.0483` edge `0.0164` maxDD `-1.2855`
- `market_context_high->crypto_alt_4h` score `-0.2507` n `142` status `ready` deltaP `15.2525` edge `0.3115` maxDD `-28.7261`
- `market_context_high->unknown_1h` score `-0.3157` n `142` status `ready` deltaP `4.0314` edge `0.0199` maxDD `-3.1801`
- `market_context_high->equity_1h` score `-0.4328` n `142` status `ready` deltaP `0.3943` edge `0.0446` maxDD `-2.6634`
- `market_context_high->crypto_alt_1h` score `-0.4668` n `142` status `ready` deltaP `5.9944` edge `0.0762` maxDD `-10.747`
- `market_context_high->fx_1h` score `-0.5538` n `142` status `ready` deltaP `-0.6873` edge `0.0028` maxDD `-0.2164`
- `market_context_high->commodity_1h` score `-0.5914` n `142` status `ready` deltaP `-0.4322` edge `0.0024` maxDD `-4.3601`
- `market_context_high->crypto_major_1h` score `-0.6138` n `142` status `ready` deltaP `6.0218` edge `0.0681` maxDD `-9.622`
- `market_context_high->metal_1h` score `-0.68` n `142` status `ready` deltaP `-0.466` edge `0.0005` maxDD `-3.0996`
- `market_context_high->fx_4h` score `-1.0008` n `142` status `ready` deltaP `-1.9237` edge `0.0073` maxDD `-0.5631`
- `market_context_high->commodity_4h` score `-1.2394` n `142` status `ready` deltaP `2.4476` edge `0.0168` maxDD `-10.0279`
- `market_context_high->fx_24h` score `-1.2816` n `142` status `ready` deltaP `-1.7116` edge `-0.0082` maxDD `-0.6418`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
