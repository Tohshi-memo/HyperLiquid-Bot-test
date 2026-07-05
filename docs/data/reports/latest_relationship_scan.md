# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-05T12:52:25.016468+00:00`
- Price records: `672`
- Market context records: `5773`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `8674`

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

- `market_context_high->equity_24h` score `0.6775` n `231` status `ready` deltaP `15.4875` edge `0.4915` maxDD `-31.6316`
- `market_context_high->equity_4h` score `0.1437` n `288` status `ready` deltaP `7.5204` edge `0.1257` maxDD `-7.4425`
- `market_context_high->fx_1h` score `-0.2556` n `300` status `ready` deltaP `2.1497` edge `0.001` maxDD `-0.5144`
- `market_context_high->metal_1h` score `-0.4165` n `300` status `ready` deltaP `2.2375` edge `-0.0008` maxDD `-2.0682`
- `market_context_high->equity_1h` score `-0.6086` n `300` status `ready` deltaP `3.4471` edge `0.027` maxDD `-5.0555`
- `market_context_high->commodity_1h` score `-0.8024` n `300` status `ready` deltaP `-2.503` edge `-0.0057` maxDD `-3.7721`
- `market_context_high->crypto_major_1h` score `-0.8934` n `300` status `ready` deltaP `3.3673` edge `0.0352` maxDD `-6.2348`
- `market_context_high->fx_24h` score `-0.9125` n `231` status `ready` deltaP `14.9486` edge `0.0417` maxDD `-3.6674`
- `market_context_high->index_1h` score `-0.9493` n `300` status `ready` deltaP `0.6048` edge `0.0037` maxDD `-0.9472`
- `market_context_high->crypto_alt_1h` score `-1.1044` n `300` status `ready` deltaP `1.6527` edge `0.0304` maxDD `-6.6758`
- `market_context_high->fx_4h` score `-1.2487` n `288` status `ready` deltaP `2.7947` edge `0.0058` maxDD `-1.4288`
- `market_context_high->index_4h` score `-1.8481` n `288` status `ready` deltaP `0.6182` edge `0.0106` maxDD `-3.165`
- `market_context_high->commodity_4h` score `-2.4505` n `288` status `ready` deltaP `-2.8963` edge `-0.0273` maxDD `-14.071`
- `market_context_high->metal_4h` score `-2.5386` n `288` status `ready` deltaP `-6.1822` edge `-0.0483` maxDD `-11.5426`
- `market_context_high->crypto_major_4h` score `-2.829` n `288` status `ready` deltaP `7.7828` edge `0.1496` maxDD `-25.6458`
- `market_context_high->index_24h` score `-2.8977` n `231` status `ready` deltaP `2.0202` edge `0.0295` maxDD `-18.1572`
- `market_context_high->crypto_alt_4h` score `-4.402` n `288` status `ready` deltaP `5.4624` edge `0.0976` maxDD `-28.7346`
- `market_context_high->crypto_major_24h` score `-5.6613` n `231` status `ready` deltaP `4.4823` edge `-0.0393` maxDD `-29.6555`
- `market_context_high->metal_24h` score `-7.0336` n `231` status `ready` deltaP `-7.8778` edge `-0.2423` maxDD `-27.5543`
- `market_context_high->commodity_24h` score `-10.8728` n `231` status `ready` deltaP `-13.553` edge `-0.0781` maxDD `-40.676`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
