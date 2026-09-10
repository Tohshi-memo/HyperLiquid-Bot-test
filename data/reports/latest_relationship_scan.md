# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-10T06:22:31.634449+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `104`

- Symbol pattern count: `10918`

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

- `risk_on_high->crypto_alt_24h` score `13.901` n `93` status `ready` deltaP `30.7348` edge `0.9765` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `13.901` n `93` status `ready` deltaP `30.7348` edge `0.9765` maxDD `-0.8386`
- `market_context_high->crypto_alt_24h` score `10.075` n `215` status `ready` deltaP `23.0878` edge `0.7684` maxDD `-3.9523`
- `risk_on_high->crypto_alt_4h` score `7.2795` n `93` status `ready` deltaP `37.1542` edge `0.3961` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `7.2795` n `93` status `ready` deltaP `37.1542` edge `0.3961` maxDD `-1.9733`
- `risk_on_high->crypto_major_4h` score `5.2457` n `93` status `ready` deltaP `26.0556` edge `0.3493` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `5.2457` n `93` status `ready` deltaP `26.0556` edge `0.3493` maxDD `-3.8693`
- `risk_on_high->crypto_major_24h` score `4.169` n `93` status `ready` deltaP `20.2453` edge `0.8063` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `4.169` n `93` status `ready` deltaP `20.2453` edge `0.8063` maxDD `-24.5429`
- `risk_on_high->index_24h` score `2.8817` n `93` status `ready` deltaP `31.4964` edge `0.0344` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `2.8817` n `93` status `ready` deltaP `31.4964` edge `0.0344` maxDD `-0.0051`
- `market_context_high->equity_24h` score `2.6768` n `215` status `ready` deltaP `15.625` edge `0.1189` maxDD `0.0`
- `market_context_high->index_24h` score `2.387` n `215` status `ready` deltaP `26.3501` edge `0.0626` maxDD `-0.1483`
- `risk_on_high->commodity_24h` score `1.7196` n `93` status `ready` deltaP `16.157` edge `0.045` maxDD `-0.0866`
- `risk_on_and_context->commodity_24h` score `1.7196` n `93` status `ready` deltaP `16.157` edge `0.045` maxDD `-0.0866`
- `risk_on_high->equity_4h` score `1.6451` n `93` status `ready` deltaP `24.3246` edge `-0.0104` maxDD `-0.5072`
- `risk_on_and_context->equity_4h` score `1.6451` n `93` status `ready` deltaP `24.3246` edge `-0.0104` maxDD `-0.5072`
- `risk_on_high->equity_1h` score `1.1135` n `93` status `ready` deltaP `17.6615` edge `0.0029` maxDD `-0.228`
- `risk_on_and_context->equity_1h` score `1.1135` n `93` status `ready` deltaP `17.6615` edge `0.0029` maxDD `-0.228`
- `risk_on_high->crypto_alt_1h` score `1.0292` n `93` status `ready` deltaP `4.05` edge `0.094` maxDD `-1.1521`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
