# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-18T08:07:29.720022+00:00`
- Price records: `672`
- Market context records: `7118`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11667`

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

- `market_context_high->fx_4h` score `0.3442` n `146` status `ready` deltaP `15.0037` edge `0.0141` maxDD `-0.9333`
- `market_context_high->fx_1h` score `-0.0914` n `149` status `ready` deltaP `4.5895` edge `0.0028` maxDD `-0.276`
- `market_context_high->unknown_1h` score `-0.2506` n `149` status `ready` deltaP `-1.2187` edge `0.0431` maxDD `-1.4688`
- `market_context_high->index_1h` score `-0.5569` n `149` status `ready` deltaP `0.2059` edge `-0.0063` maxDD `-2.3175`
- `market_context_high->crypto_alt_1h` score `-0.6485` n `149` status `ready` deltaP `0.7073` edge `0.03` maxDD `-4.7674`
- `market_context_high->crypto_major_1h` score `-0.837` n `149` status `ready` deltaP `4.063` edge `0.0384` maxDD `-7.1523`
- `market_context_high->commodity_1h` score `-0.8879` n `149` status `ready` deltaP `-4.8216` edge `-0.0196` maxDD `-1.9668`
- `market_context_high->commodity_4h` score `-1.3827` n `146` status `ready` deltaP `-4.5794` edge `-0.0432` maxDD `-2.9494`
- `market_context_high->metal_1h` score `-1.4383` n `149` status `ready` deltaP `-5.6846` edge `-0.0054` maxDD `-2.1249`
- `market_context_high->unknown_4h` score `-1.5479` n `146` status `ready` deltaP `-6.8326` edge `0.0073` maxDD `-4.4825`
- `market_context_high->equity_1h` score `-2.0508` n `149` status `ready` deltaP `3.4893` edge `-0.0439` maxDD `-14.716`
- `market_context_high->crypto_major_4h` score `-3.0171` n `146` status `ready` deltaP `4.3414` edge `0.0127` maxDD `-24.6094`
- `market_context_high->commodity_24h` score `-3.7268` n `146` status `ready` deltaP `-9.5082` edge `-0.1163` maxDD `-4.4704`
- `market_context_high->index_4h` score `-4.0586` n `146` status `ready` deltaP `-2.8817` edge `-0.0491` maxDD `-12.2591`
- `market_context_high->metal_4h` score `-4.4614` n `146` status `ready` deltaP `-9.4115` edge `-0.0122` maxDD `-5.414`
- `market_context_high->crypto_alt_4h` score `-4.649` n `146` status `ready` deltaP `0.7684` edge `-0.014` maxDD `-22.2831`
- `market_context_high->fx_24h` score `-4.6833` n `146` status `ready` deltaP `-12.714` edge `-0.0228` maxDD `-3.9503`
- `market_context_high->unknown_24h` score `-9.4181` n `146` status `ready` deltaP `-27.8039` edge `-0.0848` maxDD `-23.5076`
- `market_context_high->equity_4h` score `-13.671` n `146` status `ready` deltaP `-2.0423` edge `-0.2386` maxDD `-63.963`
- `market_context_high->metal_24h` score `-14.8149` n `146` status `ready` deltaP `-27.5447` edge `-0.1606` maxDD `-42.2274`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
