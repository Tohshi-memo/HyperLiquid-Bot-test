# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-23T03:08:04.267478+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9748`

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

- `market_context_high->unknown_4h` score `46.0278` n `46` status `ready` deltaP `7.0122` edge `3.7889` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `29.6571` n `46` status `ready` deltaP `13.5341` edge `2.3968` maxDD `-0.5817`
- `market_context_high->equity_24h` score `16.6021` n `46` status `ready` deltaP `12.1453` edge `1.3126` maxDD `-0.1382`
- `market_context_high->crypto_alt_24h` score `12.9108` n `46` status `ready` deltaP `10.5903` edge `1.0053` maxDD `0.0`
- `market_context_high->index_24h` score `5.6174` n `46` status `ready` deltaP `20.4786` edge `0.3403` maxDD `-0.03`
- `news_risk_high->crypto_major_24h` score `4.9635` n `96` status `ready` deltaP `-9.2014` edge `1.1608` maxDD `-46.1999`
- `news_risk_high->commodity_24h` score `4.5174` n `96` status `ready` deltaP `34.8958` edge `0.2617` maxDD `-2.431`
- `news_risk_high->crypto_major_4h` score `2.872` n `97` status `ready` deltaP `14.0653` edge `0.2033` maxDD `-2.619`
- `news_risk_high->crypto_alt_4h` score `2.2806` n `97` status `ready` deltaP `9.1872` edge `0.2286` maxDD `-5.9838`
- `market_context_high->index_4h` score `2.0467` n `46` status `ready` deltaP `24.0787` edge `0.0234` maxDD `-0.0692`
- `news_risk_high->crypto_alt_1h` score `1.7598` n `101` status `ready` deltaP `10.6924` edge `0.1244` maxDD `-1.5895`
- `news_risk_high->fx_4h` score `1.3997` n `97` status `ready` deltaP `20.661` edge `0.0425` maxDD `-0.421`
- `news_risk_high->crypto_major_1h` score `1.3781` n `101` status `ready` deltaP `12.938` edge `0.0721` maxDD `-1.8141`
- `news_risk_high->fx_24h` score `0.8722` n `96` status `ready` deltaP `23.7847` edge `0.1122` maxDD `-1.7159`
- `market_context_high->equity_1h` score `0.7826` n `46` status `ready` deltaP `6.6129` edge `0.0454` maxDD `-0.2751`
- `market_context_high->index_1h` score `0.6938` n `46` status `ready` deltaP `10.8045` edge `0.0111` maxDD `-0.0249`
- `market_context_high->equity_4h` score `0.5507` n `46` status `ready` deltaP `4.328` edge `0.0477` maxDD `-0.4529`
- `news_risk_high->metal_1h` score `0.494` n `101` status `ready` deltaP `13.6657` edge `0.0094` maxDD `-0.7468`
- `market_context_high->metal_24h` score `0.4552` n `46` status `ready` deltaP `17.9273` edge `-0.0582` maxDD `-0.2042`
- `news_risk_high->metal_4h` score `0.4033` n `97` status `ready` deltaP `13.5404` edge `0.0391` maxDD `-1.9941`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
