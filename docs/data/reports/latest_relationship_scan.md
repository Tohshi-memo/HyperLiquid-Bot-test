# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-31T14:37:29.883825+00:00`
- Price records: `672`
- Market context records: `8523`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5898`

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

- `news_risk_high->unknown_24h` score `6279.4161` n `52` status `ready` deltaP `44.7383` edge `523.0285` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `5.5532` n `64` status `ready` deltaP `21.2652` edge `0.3807` maxDD `-3.4427`
- `news_risk_high->index_4h` score `2.0035` n `64` status `ready` deltaP `16.5015` edge `0.076` maxDD `-0.191`
- `news_risk_high->equity_1h` score `1.711` n `64` status `ready` deltaP `15.8028` edge `0.0849` maxDD `-2.4803`
- `news_risk_high->crypto_major_4h` score `0.8338` n `64` status `ready` deltaP `5.6784` edge `0.1466` maxDD `-3.5385`
- `news_risk_high->crypto_alt_4h` score `0.7875` n `64` status `ready` deltaP `14.4817` edge `0.1436` maxDD `-5.8012`
- `market_context_high->crypto_alt_4h` score `0.6076` n `39` status `ready` deltaP `8.392` edge `0.1051` maxDD `-4.6517`
- `news_risk_high->crypto_alt_1h` score `0.5162` n `64` status `ready` deltaP `9.0101` edge `0.0588` maxDD `-1.8813`
- `news_risk_high->crypto_major_1h` score `0.2994` n `64` status `ready` deltaP `6.3155` edge `0.0475` maxDD `-2.0972`
- `market_context_high->crypto_major_4h` score `0.2441` n `39` status `ready` deltaP `4.2762` edge `0.0938` maxDD `-4.2815`
- `news_risk_high->fx_1h` score `0.1158` n `64` status `ready` deltaP `5.7354` edge `0.0047` maxDD `-0.2475`
- `news_risk_high->index_1h` score `0.0519` n `64` status `ready` deltaP `4.3694` edge `0.0092` maxDD `-0.5338`
- `news_risk_high->metal_4h` score `0.0478` n `64` status `ready` deltaP `2.6296` edge `0.0362` maxDD `-0.8085`
- `news_risk_high->fx_4h` score `0.0254` n `64` status `ready` deltaP `11.471` edge `0.0214` maxDD `-0.6604`
- `news_risk_high->metal_1h` score `-0.0832` n `64` status `ready` deltaP `3.7051` edge `0.0087` maxDD `-0.5599`
- `market_context_high->fx_4h` score `-0.2106` n `39` status `ready` deltaP `3.4982` edge `0.0035` maxDD `-0.6389`
- `market_context_high->commodity_1h` score `-0.25` n `51` status `ready` deltaP `3.5253` edge `0.007` maxDD `-2.0038`
- `market_context_high->commodity_4h` score `-0.5` n `39` status `ready` deltaP `6.5197` edge `0.0439` maxDD `-5.4508`
- `market_context_high->index_4h` score `-0.717` n `39` status `ready` deltaP `-1.0866` edge `-0.0281` maxDD `-1.8597`
- `market_context_high->metal_1h` score `-0.7702` n `51` status `ready` deltaP `-3.5253` edge `-0.0258` maxDD `-1.6224`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
