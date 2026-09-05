# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-05T18:22:54.485864+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10591`

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

- `risk_on_high->unknown_4h` score `20.3261` n `140` status `ready` deltaP `-1.054` edge `1.8798` maxDD `-6.6476`
- `risk_on_and_context->unknown_4h` score `20.3261` n `140` status `ready` deltaP `-1.054` edge `1.8798` maxDD `-6.6476`
- `market_context_high->unknown_4h` score `8.4335` n `228` status `ready` deltaP `2.0913` edge `0.9042` maxDD `-7.895`
- `news_risk_high->crypto_alt_24h` score `6.9959` n `37` status `ready` deltaP `25.1783` edge `0.4421` maxDD `-0.8236`
- `news_risk_high->commodity_24h` score `3.7709` n `37` status `ready` deltaP `19.7917` edge `0.1823` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `3.4324` n `37` status `ready` deltaP `17.0279` edge `0.2138` maxDD `-0.9693`
- `news_risk_high->metal_4h` score `2.3783` n `37` status `ready` deltaP `24.1513` edge `0.0593` maxDD `-0.7692`
- `news_risk_high->commodity_4h` score `1.7779` n `37` status `ready` deltaP `10.0569` edge `0.1012` maxDD `-0.2737`
- `news_risk_high->equity_1h` score `1.532` n `37` status `ready` deltaP `12.4859` edge `0.0835` maxDD `-0.7924`
- `news_risk_high->metal_1h` score `1.2586` n `37` status `ready` deltaP `15.0146` edge `0.0241` maxDD `-0.2118`
- `news_risk_high->index_1h` score `1.1131` n `37` status `ready` deltaP `13.9748` edge `0.013` maxDD `-0.0724`
- `news_risk_high->crypto_major_1h` score `1.1019` n `37` status `ready` deltaP `5.8667` edge `0.071` maxDD `-0.4628`
- `news_risk_high->crypto_alt_1h` score `0.9501` n `37` status `ready` deltaP `9.1763` edge `0.0445` maxDD `-0.7867`
- `news_risk_high->crypto_major_24h` score `0.7667` n `37` status `ready` deltaP `16.5776` edge `0.2654` maxDD `-18.2098`
- `news_risk_high->fx_24h` score `0.6752` n `37` status `ready` deltaP `17.1781` edge `0.0433` maxDD `-3.1244`
- `market_context_high->equity_24h` score `0.5625` n `175` status `ready` deltaP `13.5218` edge `0.3913` maxDD `-20.7654`
- `news_risk_high->crypto_alt_4h` score `0.5185` n `37` status `ready` deltaP `5.6362` edge `0.0385` maxDD `-1.296`
- `risk_on_high->index_1h` score `0.0446` n `148` status `ready` deltaP `7.8937` edge `-0.0022` maxDD `-0.5764`
- `risk_on_and_context->index_1h` score `0.0446` n `148` status `ready` deltaP `7.8937` edge `-0.0022` maxDD `-0.5764`
- `news_risk_high->commodity_1h` score `-0.0091` n `37` status `ready` deltaP `6.0245` edge `0.0033` maxDD `-0.9036`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
