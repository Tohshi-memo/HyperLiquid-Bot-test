# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-30T20:52:25.478781+00:00`
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

- `risk_on_high->crypto_alt_24h` score `25.4586` n `43` status `ready` deltaP `50.3472` edge `1.7859` maxDD `0.0`
- `risk_on_and_context->crypto_alt_24h` score `25.4586` n `43` status `ready` deltaP `50.3472` edge `1.7859` maxDD `0.0`
- `risk_on_high->crypto_major_24h` score `15.5045` n `43` status `ready` deltaP `44.2708` edge `0.9969` maxDD `0.0`
- `risk_on_and_context->crypto_major_24h` score `15.5045` n `43` status `ready` deltaP `44.2708` edge `0.9969` maxDD `0.0`
- `risk_on_high->unknown_4h` score `9.0344` n `73` status `ready` deltaP `28.8319` edge `0.6035` maxDD `-1.0945`
- `risk_on_and_context->unknown_4h` score `9.0344` n `73` status `ready` deltaP `28.8319` edge `0.6035` maxDD `-1.0945`
- `risk_on_high->fx_24h` score `6.2967` n `43` status `ready` deltaP `70.8333` edge `0.0525` maxDD `0.0`
- `risk_on_and_context->fx_24h` score `6.2967` n `43` status `ready` deltaP `70.8333` edge `0.0525` maxDD `0.0`
- `risk_on_high->metal_24h` score `6.1839` n `43` status `ready` deltaP `53.2986` edge `0.16` maxDD `0.0`
- `risk_on_and_context->metal_24h` score `6.1839` n `43` status `ready` deltaP `53.2986` edge `0.16` maxDD `0.0`
- `risk_on_high->equity_24h` score `5.9119` n `43` status `ready` deltaP `38.8889` edge `0.2334` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `5.9119` n `43` status `ready` deltaP `38.8889` edge `0.2334` maxDD `0.0`
- `market_context_high->unknown_4h` score `5.0717` n `149` status `ready` deltaP `21.054` edge `0.3293` maxDD `-1.0945`
- `market_context_high->metal_24h` score `4.5713` n `117` status `ready` deltaP `37.0593` edge `0.2358` maxDD `-3.1535`
- `risk_on_high->crypto_major_4h` score `4.5249` n `73` status `ready` deltaP `25.1879` edge `0.2562` maxDD `-2.0972`
- `risk_on_and_context->crypto_major_4h` score `4.5249` n `73` status `ready` deltaP `25.1879` edge `0.2562` maxDD `-2.0972`
- `risk_on_high->crypto_alt_4h` score `4.221` n `73` status `ready` deltaP `16.9709` edge `0.2869` maxDD `-1.5298`
- `risk_on_and_context->crypto_alt_4h` score `4.221` n `73` status `ready` deltaP `16.9709` edge `0.2869` maxDD `-1.5298`
- `market_context_high->crypto_major_24h` score `3.4982` n `117` status `ready` deltaP `16.0657` edge `0.471` maxDD `-17.2607`
- `risk_on_high->equity_4h` score `3.3496` n `73` status `ready` deltaP `30.9681` edge `0.0937` maxDD `-0.3481`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
