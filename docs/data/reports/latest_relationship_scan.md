# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-02T23:22:27.016849+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4818`

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

- `market_context_high->unknown_1h` score `364.0294` n `50` status `ready` deltaP `10.5749` edge `30.2702` maxDD `-0.0597`
- `market_context_high->unknown_4h` score `291.8705` n `50` status `ready` deltaP `10.6707` edge `24.2514` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `16.9253` n `70` status `ready` deltaP `41.7212` edge `1.1532` maxDD `-1.005`
- `market_context_high->crypto_alt_24h` score `10.6337` n `50` status `ready` deltaP `20.0069` edge `0.9231` maxDD `-11.6271`
- `news_risk_high->equity_24h` score `9.0854` n `70` status `ready` deltaP `33.7351` edge `0.5807` maxDD `-2.8784`
- `market_context_high->crypto_major_24h` score `9.0498` n `50` status `ready` deltaP `31.8264` edge `0.6836` maxDD `-9.3299`
- `market_context_high->crypto_major_4h` score `7.8577` n `50` status `ready` deltaP `19.372` edge `0.596` maxDD `-3.294`
- `news_risk_high->crypto_alt_4h` score `6.7333` n `112` status `ready` deltaP `26.1324` edge `0.5213` maxDD `-6.4195`
- `market_context_high->crypto_alt_4h` score `6.3367` n `50` status `ready` deltaP `17.561` edge `0.5399` maxDD `-7.6465`
- `market_context_high->crypto_alt_1h` score `3.3669` n `50` status `ready` deltaP `15.4012` edge `0.2442` maxDD `-3.6376`
- `market_context_high->crypto_major_1h` score `3.096` n `50` status `ready` deltaP `14.0` edge `0.2097` maxDD `-2.2692`
- `news_risk_high->equity_4h` score `2.8008` n `112` status `ready` deltaP `23.6498` edge `0.137` maxDD `-2.9013`
- `market_context_high->fx_4h` score `2.7775` n `50` status `ready` deltaP `31.0122` edge `0.0382` maxDD `-0.0791`
- `news_risk_high->crypto_major_24h` score `2.628` n `70` status `ready` deltaP `8.3978` edge `0.5343` maxDD `-12.2694`
- `news_risk_high->crypto_major_4h` score `2.2354` n `112` status `ready` deltaP `18.3363` edge `0.3612` maxDD `-9.0817`
- `news_risk_high->metal_24h` score `1.4768` n `70` status `ready` deltaP `14.6528` edge `0.2179` maxDD `-2.0999`
- `market_context_high->fx_1h` score `1.4603` n `50` status `ready` deltaP `20.491` edge `0.0115` maxDD `-0.113`
- `market_context_high->equity_24h` score `1.3146` n `50` status `ready` deltaP `6.0208` edge `0.3146` maxDD `-11.8957`
- `news_risk_high->crypto_alt_1h` score `1.0939` n `112` status `ready` deltaP `4.7583` edge `0.1155` maxDD `-2.4854`
- `market_context_high->fx_24h` score `1.004` n `50` status `ready` deltaP `20.5069` edge `0.0938` maxDD `-1.8102`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
