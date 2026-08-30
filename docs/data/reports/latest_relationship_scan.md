# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-30T18:07:30.802353+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11662`

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

- `risk_on_high->crypto_alt_24h` score `26.1838` n `32` status `ready` deltaP `52.2569` edge `1.8336` maxDD `0.0`
- `risk_on_and_context->crypto_alt_24h` score `26.1838` n `32` status `ready` deltaP `52.2569` edge `1.8336` maxDD `0.0`
- `risk_on_high->crypto_major_24h` score `16.7108` n `32` status `ready` deltaP `46.1806` edge `1.0847` maxDD `0.0`
- `risk_on_and_context->crypto_major_24h` score `16.7108` n `32` status `ready` deltaP `46.1806` edge `1.0847` maxDD `0.0`
- `risk_on_high->unknown_4h` score `9.5984` n `63` status `ready` deltaP `26.6575` edge `0.665` maxDD `-1.0945`
- `risk_on_and_context->unknown_4h` score `9.5984` n `63` status `ready` deltaP `26.6575` edge `0.665` maxDD `-1.0945`
- `risk_on_high->equity_24h` score `6.8915` n `32` status `ready` deltaP `40.7986` edge `0.3023` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `6.8915` n `32` status `ready` deltaP `40.7986` edge `0.3023` maxDD `0.0`
- `risk_on_high->fx_24h` score `6.4494` n `32` status `ready` deltaP `72.7431` edge `0.0525` maxDD `0.0`
- `risk_on_and_context->fx_24h` score `6.4494` n `32` status `ready` deltaP `72.7431` edge `0.0525` maxDD `0.0`
- `risk_on_high->metal_24h` score `6.2506` n `32` status `ready` deltaP `53.4722` edge `0.1644` maxDD `0.0`
- `risk_on_and_context->metal_24h` score `6.2506` n `32` status `ready` deltaP `53.4722` edge `0.1644` maxDD `0.0`
- `market_context_high->unknown_4h` score `6.0761` n `149` status `ready` deltaP `21.054` edge `0.413` maxDD `-1.0945`
- `risk_on_high->crypto_major_4h` score `5.1571` n `63` status `ready` deltaP `25.7961` edge `0.2861` maxDD `-0.5985`
- `risk_on_and_context->crypto_major_4h` score `5.1571` n `63` status `ready` deltaP `25.7961` edge `0.2861` maxDD `-0.5985`
- `market_context_high->metal_24h` score `4.4952` n `117` status `ready` deltaP `36.3782` edge `0.234` maxDD `-3.1535`
- `risk_on_high->crypto_alt_4h` score `3.9709` n `63` status `ready` deltaP `14.7745` edge `0.2807` maxDD `-1.5298`
- `risk_on_and_context->crypto_alt_4h` score `3.9709` n `63` status `ready` deltaP `14.7745` edge `0.2807` maxDD `-1.5298`
- `risk_on_high->unknown_1h` score `3.7061` n `74` status `ready` deltaP `10.382` edge `0.2599` maxDD `-0.2885`
- `risk_on_and_context->unknown_1h` score `3.7061` n `74` status `ready` deltaP `10.382` edge `0.2599` maxDD `-0.2885`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
