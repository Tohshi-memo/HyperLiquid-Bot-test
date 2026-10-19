# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-19T00:07:25.219740+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8526`

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

- `market_context_high->crypto_major_4h` score `1.6463` n `95` status `ready` deltaP `15.2262` edge `0.45` maxDD `-15.2359`
- `risk_on_high->commodity_24h` score `1.457` n `62` status `ready` deltaP `16.1543` edge `0.0935` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `1.457` n `62` status `ready` deltaP `16.1543` edge `0.0935` maxDD `-1.7154`
- `market_context_high->commodity_24h` score `1.2623` n `95` status `ready` deltaP `16.1373` edge `0.1394` maxDD `-1.8119`
- `risk_on_high->crypto_major_4h` score `0.8501` n `62` status `ready` deltaP `13.2228` edge `0.2689` maxDD `-11.1788`
- `risk_on_and_context->crypto_major_4h` score `0.8501` n `62` status `ready` deltaP `13.2228` edge `0.2689` maxDD `-11.1788`
- `market_context_high->crypto_major_1h` score `0.4367` n `95` status `ready` deltaP `4.5871` edge `0.1143` maxDD `-3.7781`
- `risk_on_high->index_1h` score `0.0669` n `62` status `ready` deltaP `6.7568` edge `0.0012` maxDD `-0.6799`
- `risk_on_and_context->index_1h` score `0.0669` n `62` status `ready` deltaP `6.7568` edge `0.0012` maxDD `-0.6799`
- `risk_on_high->fx_1h` score `-0.2243` n `62` status `ready` deltaP `1.3126` edge `-0.0018` maxDD `-0.1904`
- `risk_on_and_context->fx_1h` score `-0.2243` n `62` status `ready` deltaP `1.3126` edge `-0.0018` maxDD `-0.1904`
- `market_context_high->index_1h` score `-0.4931` n `95` status `ready` deltaP `2.02` edge `-0.0026` maxDD `-1.2599`
- `market_context_high->crypto_alt_1h` score `-0.6049` n `95` status `ready` deltaP `-0.8494` edge `0.0781` maxDD `-7.3329`
- `market_context_high->fx_4h` score `-0.6738` n `95` status `ready` deltaP `-3.784` edge `0.0019` maxDD `-0.7115`
- `risk_on_high->fx_4h` score `-0.7387` n `62` status `ready` deltaP `-5.0064` edge `0.0004` maxDD `-0.2866`
- `risk_on_and_context->fx_4h` score `-0.7387` n `62` status `ready` deltaP `-5.0064` edge `0.0004` maxDD `-0.2866`
- `market_context_high->metal_1h` score `-0.7433` n `95` status `ready` deltaP `-1.8973` edge `0.0043` maxDD `-0.9556`
- `risk_on_high->crypto_major_1h` score `-0.8458` n `62` status `ready` deltaP `-3.3755` edge `0.006` maxDD `-4.6876`
- `risk_on_and_context->crypto_major_1h` score `-0.8458` n `62` status `ready` deltaP `-3.3755` edge `0.006` maxDD `-4.6876`
- `market_context_high->fx_1h` score `-0.878` n `95` status `ready` deltaP `-2.9319` edge `-0.0015` maxDD `-0.503`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
