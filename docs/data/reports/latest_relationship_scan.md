# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-30T21:52:33.046870+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11706`

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

- `risk_on_high->crypto_alt_24h` score `24.5282` n `47` status `ready` deltaP `49.6528` edge `1.713` maxDD `0.0`
- `risk_on_and_context->crypto_alt_24h` score `24.5282` n `47` status `ready` deltaP `49.6528` edge `1.713` maxDD `0.0`
- `risk_on_high->crypto_major_24h` score `13.5759` n `47` status `ready` deltaP `37.7142` edge `0.895` maxDD `-0.5414`
- `risk_on_and_context->crypto_major_24h` score `13.5759` n `47` status `ready` deltaP `37.7142` edge `0.895` maxDD `-0.5414`
- `risk_on_high->unknown_4h` score `8.7133` n `77` status `ready` deltaP `29.5435` edge `0.572` maxDD `-1.0945`
- `risk_on_and_context->unknown_4h` score `8.7133` n `77` status `ready` deltaP `29.5435` edge `0.572` maxDD `-1.0945`
- `risk_on_high->fx_24h` score `6.2483` n `47` status `ready` deltaP `70.1389` edge `0.0531` maxDD `0.0`
- `risk_on_and_context->fx_24h` score `6.2483` n `47` status `ready` deltaP `70.1389` edge `0.0531` maxDD `0.0`
- `risk_on_high->metal_24h` score `5.8844` n `47` status `ready` deltaP `51.3445` edge `0.1525` maxDD `-0.0211`
- `risk_on_and_context->metal_24h` score `5.8844` n `47` status `ready` deltaP `51.3445` edge `0.1525` maxDD `-0.0211`
- `market_context_high->unknown_4h` score `5.0033` n `149` status `ready` deltaP `21.054` edge `0.3236` maxDD `-1.0945`
- `risk_on_high->equity_24h` score `4.7008` n `47` status `ready` deltaP `32.3323` edge `0.1889` maxDD `-0.0173`
- `risk_on_and_context->equity_24h` score `4.7008` n `47` status `ready` deltaP `32.3323` edge `0.1889` maxDD `-0.0173`
- `market_context_high->metal_24h` score `4.4892` n `117` status `ready` deltaP `36.3782` edge `0.2335` maxDD `-3.1535`
- `market_context_high->crypto_major_24h` score `3.899` n `117` status `ready` deltaP `16.7468` edge `0.4832` maxDD `-17.2607`
- `risk_on_high->unknown_1h` score `3.1603` n `87` status `ready` deltaP `10.2296` edge `0.2196` maxDD `-0.2885`
- `risk_on_and_context->unknown_1h` score `3.1603` n `87` status `ready` deltaP `10.2296` edge `0.2196` maxDD `-0.2885`
- `market_context_high->crypto_alt_24h` score `2.817` n `117` status `ready` deltaP `14.6101` edge `0.696` maxDD `-28.5798`
- `risk_on_high->crypto_alt_4h` score `2.8081` n `77` status `ready` deltaP `13.484` edge `0.2298` maxDD `-4.5216`
- `risk_on_and_context->crypto_alt_4h` score `2.8081` n `77` status `ready` deltaP `13.484` edge `0.2298` maxDD `-4.5216`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
