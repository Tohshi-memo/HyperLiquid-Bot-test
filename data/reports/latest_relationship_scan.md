# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-19T21:52:31.020431+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8212`

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

- `market_context_high->commodity_24h` score `2.8382` n `76` status `ready` deltaP `23.0354` edge `0.1681` maxDD `-1.8119`
- `risk_on_high->commodity_24h` score `0.9875` n `43` status `ready` deltaP `18.4149` edge `0.0393` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `0.9875` n `43` status `ready` deltaP `18.4149` edge `0.0393` maxDD `-1.7154`
- `risk_on_high->equity_1h` score `0.4924` n `43` status `ready` deltaP `13.4487` edge `0.0092` maxDD `-1.9591`
- `risk_on_and_context->equity_1h` score `0.4924` n `43` status `ready` deltaP `13.4487` edge `0.0092` maxDD `-1.9591`
- `risk_on_high->index_1h` score `0.4459` n `43` status `ready` deltaP `10.1553` edge `-0.0002` maxDD `-0.4273`
- `risk_on_and_context->index_1h` score `0.4459` n `43` status `ready` deltaP `10.1553` edge `-0.0002` maxDD `-0.4273`
- `risk_on_high->fx_4h` score `-0.2384` n `43` status `ready` deltaP `0.0957` edge `0.0059` maxDD `-0.1126`
- `risk_on_and_context->fx_4h` score `-0.2384` n `43` status `ready` deltaP `0.0957` edge `0.0059` maxDD `-0.1126`
- `risk_on_high->fx_1h` score `-0.2956` n `43` status `ready` deltaP `-0.3342` edge `-0.001` maxDD `-0.1065`
- `risk_on_and_context->fx_1h` score `-0.2956` n `43` status `ready` deltaP `-0.3342` edge `-0.001` maxDD `-0.1065`
- `market_context_high->metal_1h` score `-0.388` n `95` status `ready` deltaP `-2.047` edge `0.0014` maxDD `-0.6669`
- `market_context_high->crypto_major_1h` score `-0.3911` n `95` status `ready` deltaP `0.5452` edge `0.0479` maxDD `-4.8007`
- `market_context_high->fx_4h` score `-0.5664` n `95` status `ready` deltaP `-1.5934` edge `0.0021` maxDD `-0.7936`
- `market_context_high->commodity_1h` score `-0.6774` n `95` status `ready` deltaP `-1.289` edge `-0.0048` maxDD `-1.5434`
- `risk_on_high->index_4h` score `-0.6898` n `43` status `ready` deltaP `4.1726` edge `0.0014` maxDD `-0.9359`
- `risk_on_and_context->index_4h` score `-0.6898` n `43` status `ready` deltaP `4.1726` edge `0.0014` maxDD `-0.9359`
- `market_context_high->fx_1h` score `-0.7533` n `95` status `ready` deltaP `-6.2338` edge `-0.0021` maxDD `-0.5667`
- `market_context_high->metal_4h` score `-0.7657` n `95` status `ready` deltaP `-0.7734` edge `0.0381` maxDD `-1.4893`
- `market_context_high->index_1h` score `-0.8081` n `95` status `ready` deltaP `0.6571` edge `-0.0046` maxDD `-1.0365`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
