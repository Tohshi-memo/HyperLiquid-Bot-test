# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-25T03:37:15.179847+00:00`
- Price records: `672`
- Market context records: `1805`
- Flow alert records: `7093`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8872`

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

- `market_context_high->metal_24h` score `6.9013` n `182` status `ready` deltaP `27.9609` edge `0.6313` maxDD `-12.7414`
- `market_context_high->crypto_alt_4h` score `6.7994` n `187` status `ready` deltaP `22.4248` edge `0.5384` maxDD `-5.7025`
- `news_risk_high->commodity_4h` score `6.5077` n `30` status `ready` deltaP `29.563` edge `0.4107` maxDD `-3.5713`
- `market_context_high->crypto_major_4h` score `5.9305` n `187` status `ready` deltaP `25.948` edge `0.4836` maxDD `-6.657`
- `market_context_high->unknown_4h` score `4.2598` n `187` status `ready` deltaP `16.5474` edge `0.4603` maxDD `-10.2508`
- `market_context_high->index_24h` score `3.3024` n `182` status `ready` deltaP `16.0409` edge `0.2911` maxDD `-4.1604`
- `news_risk_high->commodity_1h` score `3.2662` n `30` status `ready` deltaP `24.7206` edge `0.1391` maxDD `-1.2043`
- `market_context_high->equity_4h` score `2.9726` n `187` status `ready` deltaP `16.1797` edge `0.2493` maxDD `-5.0894`
- `market_context_high->equity_24h` score `2.5069` n `182` status `ready` deltaP `17.9182` edge `0.5793` maxDD `-33.1875`
- `market_context_high->unknown_24h` score `1.7749` n `182` status `ready` deltaP `12.2768` edge `0.5981` maxDD `-35.8966`
- `news_risk_high->fx_4h` score `0.9058` n `30` status `ready` deltaP `21.6362` edge `-0.0009` maxDD `-0.1774`
- `market_context_high->index_4h` score `0.845` n `187` status `ready` deltaP `12.0468` edge `0.099` maxDD `-3.7119`
- `market_context_high->crypto_major_1h` score `0.4274` n `189` status `ready` deltaP `6.335` edge `0.092` maxDD `-3.2225`
- `news_risk_high->unknown_4h` score `0.3728` n `30` status `ready` deltaP `9.8272` edge `0.0546` maxDD `-2.7857`
- `market_context_high->crypto_alt_1h` score `0.3171` n `189` status `ready` deltaP `6.7944` edge `0.0925` maxDD `-4.9097`
- `market_context_high->equity_1h` score `-0.1381` n `189` status `ready` deltaP `3.9707` edge `0.0414` maxDD `-2.6836`
- `market_context_high->index_1h` score `-0.4422` n `189` status `ready` deltaP `1.8337` edge `0.0141` maxDD `-1.7205`
- `market_context_high->fx_24h` score `-0.447` n `182` status `ready` deltaP `8.9782` edge `0.0078` maxDD `-1.3925`
- `news_risk_high->fx_1h` score `-0.4546` n `30` status `ready` deltaP `-4.8303` edge `0.0001` maxDD `-0.0948`
- `news_risk_high->unknown_1h` score `-0.4738` n `30` status `ready` deltaP `16.5569` edge `-0.1239` maxDD `-2.1115`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
