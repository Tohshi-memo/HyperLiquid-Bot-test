# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-04T14:37:25.535613+00:00`
- Price records: `672`
- Market context records: `2875`
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

- `market_context_high->crypto_alt_24h` score `7.3579` n `142` status `ready` deltaP `6.6951` edge `0.9602` maxDD `-22.6673`
- `market_context_high->unknown_24h` score `4.4326` n `142` status `ready` deltaP `8.6781` edge `0.358` maxDD `-1.7175`
- `market_context_high->equity_24h` score `4.1907` n `142` status `ready` deltaP `8.0399` edge `0.496` maxDD `-12.6963`
- `market_context_high->index_24h` score `2.1178` n `142` status `ready` deltaP `10.2382` edge `0.2063` maxDD `-2.5127`
- `market_context_high->commodity_24h` score `1.6992` n `142` status `ready` deltaP `15.5516` edge `0.3473` maxDD `-12.4171`
- `market_context_high->unknown_4h` score `0.8578` n `142` status `ready` deltaP `6.0331` edge `0.1366` maxDD `-3.7602`
- `market_context_high->index_4h` score `0.7547` n `142` status `ready` deltaP `15.435` edge `0.078` maxDD `-2.3986`
- `market_context_high->index_1h` score `-0.0064` n `142` status `ready` deltaP `4.6471` edge `0.0176` maxDD `-1.2855`
- `market_context_high->unknown_1h` score `-0.0433` n `142` status `ready` deltaP `4.1811` edge `0.0416` maxDD `-3.1801`
- `market_context_high->equity_4h` score `-0.0434` n `142` status `ready` deltaP `4.4014` edge `0.105` maxDD `-5.7037`
- `market_context_high->crypto_alt_4h` score `-0.4905` n `142` status `ready` deltaP `14.4903` edge `0.2966` maxDD `-28.7261`
- `market_context_high->commodity_1h` score `-0.5937` n `142` status `ready` deltaP `-0.5819` edge `0.0031` maxDD `-4.3601`
- `market_context_high->fx_1h` score `-0.6904` n `142` status `ready` deltaP `-2.334` edge `0.0024` maxDD `-0.2164`
- `market_context_high->crypto_alt_1h` score `-0.7131` n `142` status `ready` deltaP `4.6471` edge `0.0536` maxDD `-10.747`
- `market_context_high->metal_1h` score `-0.7346` n `142` status `ready` deltaP `-0.7654` edge `-0.0045` maxDD `-3.0996`
- `market_context_high->equity_1h` score `-0.7564` n `142` status `ready` deltaP `-2.0009` edge `0.0336` maxDD `-2.6634`
- `market_context_high->crypto_major_1h` score `-0.8453` n `142` status `ready` deltaP `4.5248` edge `0.0484` maxDD `-9.622`
- `market_context_high->commodity_4h` score `-1.1213` n `142` status `ready` deltaP `3.8195` edge `0.0228` maxDD `-10.0279`
- `market_context_high->fx_4h` score `-1.3039` n `142` status `ready` deltaP `-5.2774` edge `0.0044` maxDD `-0.5631`
- `market_context_high->fx_24h` score `-1.3915` n `142` status `ready` deltaP `-1.8852` edge `-0.0162` maxDD `-0.6418`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
