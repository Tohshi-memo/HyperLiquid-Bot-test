# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-06T05:22:25.243274+00:00`
- Price records: `672`
- Market context records: `5848`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `10128`

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

- `news_risk_high->fx_1h` score `1.9747` n `30` status `ready` deltaP `23.9321` edge `0.0189` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `0.8464` n `30` status `ready` deltaP `11.3872` edge `0.0793` maxDD `-2.0691`
- `market_context_high->equity_4h` score `0.7531` n `256` status `ready` deltaP `7.9554` edge `0.1555` maxDD `-6.9958`
- `news_risk_high->crypto_alt_1h` score `0.2177` n `30` status `ready` deltaP `5.02` edge `0.0406` maxDD `-1.6923`
- `market_context_high->fx_1h` score `-0.3061` n `256` status `ready` deltaP `1.38` edge `0.0001` maxDD `-0.5499`
- `news_risk_high->metal_1h` score `-0.4001` n `30` status `ready` deltaP `1.8363` edge `-0.0269` maxDD `-1.2643`
- `market_context_high->equity_1h` score `-0.4399` n `256` status `ready` deltaP `4.1753` edge `0.0362` maxDD `-5.0555`
- `market_context_high->metal_1h` score `-0.4706` n `256` status `ready` deltaP `3.5811` edge `0.004` maxDD `-2.0339`
- `market_context_high->commodity_1h` score `-0.5145` n `256` status `ready` deltaP `-0.7298` edge `-0.001` maxDD `-2.1412`
- `market_context_high->index_1h` score `-0.589` n `256` status `ready` deltaP `0.7298` edge `0.0044` maxDD `-0.7819`
- `market_context_high->crypto_major_1h` score `-0.8318` n `256` status `ready` deltaP `3.5227` edge `0.0393` maxDD `-6.2348`
- `market_context_high->equity_24h` score `-0.8518` n `228` status `ready` deltaP `17.0413` edge `0.3233` maxDD `-31.6316`
- `market_context_high->crypto_alt_1h` score `-0.9922` n `256` status `ready` deltaP `2.2595` edge `0.0357` maxDD `-6.6758`
- `market_context_high->index_4h` score `-1.1849` n `256` status `ready` deltaP `0.4383` edge `0.0139` maxDD `-3.165`
- `news_risk_high->index_1h` score `-1.2323` n `30` status `ready` deltaP `-12.3952` edge `-0.0239` maxDD `-1.1161`
- `market_context_high->fx_4h` score `-1.7428` n `256` status `ready` deltaP `-3.9348` edge `-0.0023` maxDD `-2.2593`
- `market_context_high->fx_24h` score `-1.8132` n `228` status `ready` deltaP `4.8794` edge `0.0168` maxDD `-5.5435`
- `market_context_high->metal_4h` score `-2.0934` n `256` status `ready` deltaP `-4.3826` edge `-0.0388` maxDD `-8.6964`
- `market_context_high->commodity_4h` score `-2.3055` n `256` status `ready` deltaP `-0.0286` edge `-0.0127` maxDD `-7.0053`
- `market_context_high->crypto_major_4h` score `-2.8` n `256` status `ready` deltaP `7.3361` edge `0.155` maxDD `-25.6458`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
