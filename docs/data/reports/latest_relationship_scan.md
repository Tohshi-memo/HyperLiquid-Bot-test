# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-08T09:37:25.531663+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4807`

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

- `market_context_high->unknown_4h` score `125.233` n `37` status `ready` deltaP `-3.9387` edge `10.5071` maxDD `-0.9139`
- `market_context_high->equity_1h` score `3.2856` n `37` status `ready` deltaP `10.6571` edge `0.2487` maxDD `-2.3425`
- `market_context_high->fx_4h` score `3.1449` n `37` status `ready` deltaP `33.9239` edge `0.0449` maxDD `-0.0521`
- `market_context_high->index_4h` score `2.0426` n `37` status `ready` deltaP `26.6604` edge `0.0395` maxDD `-2.4279`
- `market_context_high->equity_24h` score `1.9258` n `30` status `ready` deltaP `4.0625` edge `0.6493` maxDD `-31.3588`
- `news_risk_high->fx_4h` score `1.4455` n `45` status `ready` deltaP `19.3293` edge `0.013` maxDD `-0.0455`
- `news_risk_high->fx_24h` score `1.2941` n `42` status `ready` deltaP `6.0516` edge `0.0896` maxDD `-0.1014`
- `market_context_high->crypto_major_1h` score `0.8274` n `37` status `ready` deltaP `10.0502` edge `0.0605` maxDD `-3.0172`
- `market_context_high->crypto_alt_1h` score `0.548` n `37` status `ready` deltaP `12.146` edge `0.0708` maxDD `-3.1881`
- `market_context_high->fx_1h` score `0.3846` n `37` status `ready` deltaP `6.6233` edge `0.015` maxDD `-0.1681`
- `news_risk_high->equity_4h` score `0.3812` n `45` status `ready` deltaP `1.4804` edge `0.1129` maxDD `-4.2454`
- `market_context_high->index_1h` score `0.3476` n `37` status `ready` deltaP `2.549` edge `0.039` maxDD `-0.1621`
- `news_risk_high->fx_1h` score `0.335` n `45` status `ready` deltaP `6.6833` edge `0.0049` maxDD `-0.0567`
- `market_context_high->index_24h` score `0.2987` n `30` status `ready` deltaP `2.5` edge `0.0847` maxDD `-2.7123`
- `market_context_high->fx_24h` score `0.2567` n `30` status `ready` deltaP `6.5278` edge `-0.0133` maxDD `-0.0397`
- `market_context_high->commodity_1h` score `0.1436` n `37` status `ready` deltaP `9.4676` edge `0.0099` maxDD `-1.7019`
- `news_risk_high->index_4h` score `0.0734` n `45` status `ready` deltaP `5.5793` edge `0.0201` maxDD `-0.4975`
- `market_context_high->commodity_4h` score `-0.0243` n `37` status `ready` deltaP `2.8346` edge `0.0234` maxDD `-1.633`
- `market_context_high->commodity_24h` score `-0.0331` n `30` status `ready` deltaP `-2.3611` edge `0.131` maxDD `-6.5601`
- `market_context_high->metal_1h` score `-0.0723` n `37` status `ready` deltaP `1.052` edge `0.0165` maxDD `-0.6226`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
