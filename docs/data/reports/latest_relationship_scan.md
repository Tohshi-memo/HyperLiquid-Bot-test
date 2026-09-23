# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-23T02:22:25.415442+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9740`

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

- `market_context_high->unknown_4h` score `46.0398` n `46` status `ready` deltaP `7.0122` edge `3.7899` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `29.6967` n `46` status `ready` deltaP `13.5341` edge `2.4001` maxDD `-0.5817`
- `market_context_high->equity_24h` score `16.5325` n `46` status `ready` deltaP `12.1453` edge `1.3068` maxDD `-0.1382`
- `market_context_high->crypto_alt_24h` score `12.9852` n `46` status `ready` deltaP `10.5903` edge `1.0115` maxDD `0.0`
- `market_context_high->index_24h` score `5.5812` n `46` status `ready` deltaP `20.1314` edge `0.3396` maxDD `-0.03`
- `news_risk_high->crypto_major_24h` score `5.0031` n `96` status `ready` deltaP `-9.2014` edge `1.1641` maxDD `-46.1999`
- `news_risk_high->commodity_24h` score `4.5426` n `96` status `ready` deltaP `34.8958` edge `0.2638` maxDD `-2.431`
- `news_risk_high->crypto_major_4h` score `2.9192` n `97` status `ready` deltaP `14.3701` edge `0.2052` maxDD `-2.619`
- `news_risk_high->crypto_alt_4h` score `2.3278` n `97` status `ready` deltaP `9.4921` edge `0.2305` maxDD `-5.9838`
- `market_context_high->index_4h` score `1.9993` n `46` status `ready` deltaP `23.6214` edge `0.0225` maxDD `-0.0692`
- `news_risk_high->crypto_alt_1h` score `1.6391` n `98` status `ready` deltaP `10.1736` edge `0.1178` maxDD `-1.5895`
- `news_risk_high->fx_4h` score `1.3839` n `97` status `ready` deltaP `20.5086` edge `0.0422` maxDD `-0.421`
- `news_risk_high->crypto_major_1h` score `1.2754` n `98` status `ready` deltaP `12.4191` edge `0.067` maxDD `-1.8141`
- `news_risk_high->fx_24h` score `0.8463` n `96` status `ready` deltaP `23.4375` edge `0.1112` maxDD `-1.7159`
- `market_context_high->equity_1h` score `0.737` n `46` status `ready` deltaP `6.3135` edge `0.0436` maxDD `-0.2751`
- `market_context_high->index_1h` score `0.6663` n `46` status `ready` deltaP `10.5051` edge `0.0108` maxDD `-0.0249`
- `news_risk_high->metal_1h` score `0.6385` n `98` status `ready` deltaP `15.1564` edge `0.0115` maxDD `-0.7468`
- `market_context_high->metal_24h` score `0.5021` n `46` status `ready` deltaP `18.2745` edge `-0.0566` maxDD `-0.2042`
- `market_context_high->equity_4h` score `0.4649` n `46` status `ready` deltaP `3.8707` edge `0.0436` maxDD `-0.4529`
- `news_risk_high->metal_4h` score `0.3463` n `97` status `ready` deltaP `13.0831` edge `0.0374` maxDD `-1.9941`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
