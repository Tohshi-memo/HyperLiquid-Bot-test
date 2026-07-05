# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-05T08:07:29.578669+00:00`
- Price records: `672`
- Market context records: `5751`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `8664`

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

- `market_context_high->equity_24h` score `0.8333` n `220` status `ready` deltaP `14.7948` edge `0.5161` maxDD `-31.6316`
- `market_context_high->equity_4h` score `0.175` n `285` status `ready` deltaP `7.6728` edge `0.1273` maxDD `-7.4425`
- `market_context_high->fx_1h` score `-0.208` n `289` status `ready` deltaP `3.0344` edge `0.0012` maxDD `-0.5144`
- `market_context_high->metal_1h` score `-0.4602` n `289` status `ready` deltaP `1.3976` edge `-0.0008` maxDD `-2.0682`
- `market_context_high->equity_1h` score `-0.6283` n `289` status `ready` deltaP `3.1251` edge `0.0275` maxDD `-5.0555`
- `market_context_high->index_1h` score `-0.6373` n `289` status `ready` deltaP `0.2` edge `0.0038` maxDD `-0.9472`
- `market_context_high->crypto_major_1h` score `-0.7616` n `289` status `ready` deltaP `3.4369` edge `0.0371` maxDD `-5.5448`
- `market_context_high->commodity_1h` score `-0.7733` n `289` status `ready` deltaP `-1.8933` edge `-0.0058` maxDD `-3.7906`
- `market_context_high->crypto_alt_1h` score `-0.8287` n `289` status `ready` deltaP `2.2859` edge `0.0361` maxDD `-5.6318`
- `market_context_high->fx_24h` score `-0.9723` n `220` status `ready` deltaP `13.4975` edge `0.0437` maxDD `-3.6674`
- `market_context_high->index_4h` score `-1.1536` n `285` status `ready` deltaP `1.4752` edge `0.011` maxDD `-3.165`
- `market_context_high->fx_4h` score `-1.2207` n `285` status `ready` deltaP `3.3189` edge `0.0059` maxDD `-1.4288`
- `market_context_high->metal_4h` score `-2.5964` n `285` status `ready` deltaP `-6.9314` edge `-0.0491` maxDD `-11.6719`
- `market_context_high->crypto_major_4h` score `-2.6527` n `285` status `ready` deltaP `8.2168` edge `0.1547` maxDD `-25.1094`
- `market_context_high->index_24h` score `-3.0189` n `220` status `ready` deltaP `-0.1011` edge `0.0281` maxDD `-18.1572`
- `market_context_high->commodity_4h` score `-3.7163` n `285` status `ready` deltaP `-2.2111` edge `-0.0274` maxDD `-14.071`
- `market_context_high->crypto_alt_4h` score `-3.7982` n `285` status `ready` deltaP `6.5543` edge `0.1088` maxDD `-26.1874`
- `market_context_high->crypto_major_24h` score `-3.961` n `220` status `ready` deltaP `8.8511` edge `0.0566` maxDD `-29.6555`
- `market_context_high->metal_24h` score `-7.8625` n `220` status `ready` deltaP `-10.2935` edge `-0.2509` maxDD `-31.412`
- `market_context_high->commodity_24h` score `-11.9087` n `220` status `ready` deltaP `-13.6364` edge `-0.0875` maxDD `-44.1188`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
