# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-05T02:52:26.423247+00:00`
- Price records: `672`
- Market context records: `2929`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6927`

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

- `market_context_high->crypto_alt_24h` score `14.6626` n `142` status `ready` deltaP `14.334` edge `1.518` maxDD `-22.6673`
- `market_context_high->equity_24h` score `7.1933` n `142` status `ready` deltaP `16.5468` edge `0.6895` maxDD `-12.6963`
- `market_context_high->unknown_24h` score `6.2734` n `142` status `ready` deltaP `14.4072` edge `0.4732` maxDD `-1.7175`
- `market_context_high->index_24h` score `2.4932` n `142` status `ready` deltaP `12.3215` edge `0.2237` maxDD `-2.5127`
- `market_context_high->commodity_24h` score `1.8276` n `142` status `ready` deltaP `15.5516` edge `0.358` maxDD `-12.4171`
- `market_context_high->equity_4h` score `0.798` n `142` status `ready` deltaP `8.3648` edge `0.1487` maxDD `-5.7037`
- `market_context_high->index_4h` score `0.6947` n `142` status `ready` deltaP `14.6728` edge `0.0754` maxDD `-2.3986`
- `market_context_high->crypto_alt_4h` score `0.0351` n `142` status `ready` deltaP `15.4049` edge `0.3343` maxDD `-28.7261`
- `market_context_high->unknown_4h` score `0.0221` n `142` status `ready` deltaP `3.7465` edge `0.0822` maxDD `-3.7602`
- `market_context_high->index_1h` score `-0.0482` n `143` status `ready` deltaP `3.9488` edge `0.0169` maxDD `-1.2855`
- `market_context_high->equity_1h` score `-0.4472` n `143` status `ready` deltaP `0.4544` edge `0.043` maxDD `-2.6634`
- `market_context_high->unknown_1h` score `-0.4703` n `143` status `ready` deltaP `3.4484` edge `0.0109` maxDD `-3.1801`
- `market_context_high->crypto_alt_1h` score `-0.5132` n `143` status `ready` deltaP `5.5955` edge `0.0729` maxDD `-10.747`
- `market_context_high->fx_1h` score `-0.559` n `143` status `ready` deltaP `-0.7966` edge `0.0031` maxDD `-0.2164`
- `market_context_high->metal_1h` score `-0.6645` n `143` status `ready` deltaP `0.0973` edge `0.0029` maxDD `-3.4325`
- `market_context_high->crypto_major_1h` score `-0.6686` n `143` status `ready` deltaP `5.6426` edge `0.0636` maxDD `-9.622`
- `market_context_high->commodity_1h` score `-0.6976` n `143` status `ready` deltaP `-1.8445` edge `-0.0018` maxDD `-4.3601`
- `market_context_high->fx_4h` score `-1.0152` n `142` status `ready` deltaP `-1.9237` edge `0.0061` maxDD `-0.5631`
- `market_context_high->fx_24h` score `-1.2924` n `142` status `ready` deltaP `-1.7116` edge `-0.0091` maxDD `-0.6418`
- `market_context_high->commodity_4h` score `-1.2946` n `142` status `ready` deltaP `1.6854` edge `0.0148` maxDD `-10.0279`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
