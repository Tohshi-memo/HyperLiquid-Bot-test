# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-30T21:07:25.041835+00:00`
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

- `risk_on_high->crypto_alt_24h` score `25.1711` n `44` status `ready` deltaP `50.1736` edge `1.7631` maxDD `0.0`
- `risk_on_and_context->crypto_alt_24h` score `25.1711` n `44` status `ready` deltaP `50.1736` edge `1.7631` maxDD `0.0`
- `risk_on_high->crypto_major_24h` score `14.8929` n `44` status `ready` deltaP `41.9981` edge `0.968` maxDD `-0.2195`
- `risk_on_and_context->crypto_major_24h` score `14.8929` n `44` status `ready` deltaP `41.9981` edge `0.968` maxDD `-0.2195`
- `risk_on_high->unknown_4h` score `9.012` n `74` status `ready` deltaP `29.017` edge `0.6004` maxDD `-1.0945`
- `risk_on_and_context->unknown_4h` score `9.012` n `74` status `ready` deltaP `29.017` edge `0.6004` maxDD `-1.0945`
- `risk_on_high->fx_24h` score `6.284` n `44` status `ready` deltaP `70.6597` edge `0.0526` maxDD `0.0`
- `risk_on_and_context->fx_24h` score `6.284` n `44` status `ready` deltaP `70.6597` edge `0.0526` maxDD `0.0`
- `risk_on_high->metal_24h` score `6.1659` n `44` status `ready` deltaP `53.2986` edge `0.1585` maxDD `0.0`
- `risk_on_and_context->metal_24h` score `6.1659` n `44` status `ready` deltaP `53.2986` edge `0.1585` maxDD `0.0`
- `risk_on_high->equity_24h` score `5.541` n `44` status `ready` deltaP `36.6162` edge `0.2219` maxDD `-0.0076`
- `risk_on_and_context->equity_24h` score `5.541` n `44` status `ready` deltaP `36.6162` edge `0.2219` maxDD `-0.0076`
- `market_context_high->unknown_4h` score `5.0741` n `149` status `ready` deltaP `21.054` edge `0.3295` maxDD `-1.0945`
- `market_context_high->metal_24h` score `4.5653` n `117` status `ready` deltaP `37.0593` edge `0.2353` maxDD `-3.1535`
- `risk_on_high->crypto_major_4h` score `3.9665` n `74` status `ready` deltaP `24.3037` edge `0.2349` maxDD `-3.6443`
- `risk_on_and_context->crypto_major_4h` score `3.9665` n `74` status `ready` deltaP `24.3037` edge `0.2349` maxDD `-3.6443`
- `risk_on_high->crypto_alt_4h` score `3.8253` n `74` status `ready` deltaP `16.0638` edge `0.2683` maxDD `-2.1958`
- `risk_on_and_context->crypto_alt_4h` score `3.8253` n `74` status `ready` deltaP `16.0638` edge `0.2683` maxDD `-2.1958`
- `market_context_high->crypto_major_24h` score `3.5734` n `117` status `ready` deltaP `16.0657` edge `0.4731` maxDD `-17.2607`
- `risk_on_high->equity_4h` score `3.1799` n `74` status `ready` deltaP `29.8204` edge `0.0901` maxDD `-0.5794`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
