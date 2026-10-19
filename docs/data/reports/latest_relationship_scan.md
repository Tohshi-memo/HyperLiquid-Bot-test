# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-19T20:07:38.059957+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8114`

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

- `market_context_high->commodity_24h` score `2.5634` n `76` status `ready` deltaP `21.8201` edge `0.1533` maxDD `-1.8119`
- `risk_on_high->commodity_24h` score `0.7127` n `43` status `ready` deltaP `17.1996` edge `0.0245` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `0.7127` n `43` status `ready` deltaP `17.1996` edge `0.0245` maxDD `-1.7154`
- `risk_on_high->equity_1h` score `0.5439` n `43` status `ready` deltaP `14.0475` edge `0.0095` maxDD `-1.9591`
- `risk_on_and_context->equity_1h` score `0.5439` n `43` status `ready` deltaP `14.0475` edge `0.0095` maxDD `-1.9591`
- `risk_on_high->index_1h` score `0.4447` n `43` status `ready` deltaP `10.1553` edge `-0.0003` maxDD `-0.4273`
- `risk_on_and_context->index_1h` score `0.4447` n `43` status `ready` deltaP `10.1553` edge `-0.0003` maxDD `-0.4273`
- `risk_on_high->fx_4h` score `-0.2408` n `43` status `ready` deltaP `0.0957` edge `0.0057` maxDD `-0.1126`
- `risk_on_and_context->fx_4h` score `-0.2408` n `43` status `ready` deltaP `0.0957` edge `0.0057` maxDD `-0.1126`
- `market_context_high->crypto_major_1h` score `-0.2773` n `95` status `ready` deltaP `1.5931` edge `0.0555` maxDD `-4.8007`
- `risk_on_high->fx_1h` score `-0.2878` n `43` status `ready` deltaP `-0.1845` edge `-0.001` maxDD `-0.1065`
- `risk_on_and_context->fx_1h` score `-0.2878` n `43` status `ready` deltaP `-0.1845` edge `-0.001` maxDD `-0.1065`
- `market_context_high->metal_1h` score `-0.4215` n `95` status `ready` deltaP `-2.6458` edge `0.0011` maxDD `-0.6669`
- `market_context_high->fx_4h` score `-0.6229` n `93` status `ready` deltaP `-2.68` edge `0.0021` maxDD `-0.7936`
- `risk_on_high->index_4h` score `-0.6426` n `43` status `ready` deltaP `4.4774` edge `0.0033` maxDD `-0.9359`
- `risk_on_and_context->index_4h` score `-0.6426` n `43` status `ready` deltaP `4.4774` edge `0.0033` maxDD `-0.9359`
- `risk_on_high->equity_4h` score `-0.6743` n `43` status `ready` deltaP `3.6762` edge `0.0546` maxDD `-4.824`
- `risk_on_and_context->equity_4h` score `-0.6743` n `43` status `ready` deltaP `3.6762` edge `0.0546` maxDD `-4.824`
- `market_context_high->metal_4h` score `-0.698` n `93` status `ready` deltaP `0.2` edge `0.0403` maxDD `-1.4893`
- `market_context_high->commodity_1h` score `-0.7234` n `95` status `ready` deltaP `-2.0375` edge `-0.0057` maxDD `-1.5434`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
