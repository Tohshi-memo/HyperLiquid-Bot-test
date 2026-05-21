# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-21T23:07:23.954134+00:00`
- Price records: `672`
- Market context records: `1470`
- Flow alert records: `6141`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8809`

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

- `market_context_high->crypto_alt_24h` score `13.3004` n `170` status `ready` deltaP `28.9645` edge `1.1169` maxDD `-15.1306`
- `market_context_high->crypto_major_24h` score `12.1166` n `170` status `ready` deltaP `27.7206` edge `0.9381` maxDD `-8.0553`
- `market_context_high->metal_24h` score `11.0338` n `170` status `ready` deltaP `15.1654` edge `0.9851` maxDD `-6.3373`
- `market_context_high->equity_24h` score `4.4994` n `170` status `ready` deltaP `13.5049` edge `0.5176` maxDD `-14.2815`
- `market_context_high->index_24h` score `4.2921` n `170` status `ready` deltaP `20.2369` edge `0.3314` maxDD `-5.3574`
- `market_context_high->equity_4h` score `1.5794` n `221` status `ready` deltaP `7.3819` edge `0.1654` maxDD `-3.6396`
- `market_context_high->fx_24h` score `0.2883` n `170` status `ready` deltaP `12.3795` edge `0.0464` maxDD `-1.3925`
- `market_context_high->equity_1h` score `-0.1244` n `221` status `ready` deltaP `1.9881` edge `0.0364` maxDD `-2.8014`
- `market_context_high->index_1h` score `-0.137` n `221` status `ready` deltaP `3.179` edge `0.0139` maxDD `-1.7205`
- `market_context_high->crypto_alt_4h` score `-0.1436` n `221` status `ready` deltaP `11.6233` edge `0.2425` maxDD `-19.5565`
- `market_context_high->index_4h` score `-0.3922` n `221` status `ready` deltaP `1.5479` edge `0.0659` maxDD `-3.7119`
- `market_context_high->crypto_alt_1h` score `-0.4832` n `221` status `ready` deltaP `2.2198` edge `0.0473` maxDD `-4.1892`
- `market_context_high->fx_1h` score `-0.494` n `221` status `ready` deltaP `0.3895` edge `-0.0027` maxDD `-0.3914`
- `market_context_high->crypto_major_4h` score `-1.0248` n `221` status `ready` deltaP `5.5934` edge `0.1482` maxDD `-13.3376`
- `market_context_high->fx_4h` score `-1.0459` n `221` status `ready` deltaP `-4.1607` edge `-0.0093` maxDD `-1.4313`
- `market_context_high->commodity_1h` score `-1.1944` n `221` status `ready` deltaP `-1.1244` edge `0.0001` maxDD `-4.7041`
- `market_context_high->metal_1h` score `-1.2525` n `221` status `ready` deltaP `4.4856` edge `-0.0007` maxDD `-6.3532`
- `market_context_high->crypto_major_1h` score `-1.5349` n `221` status `ready` deltaP `-0.3488` edge `0.0101` maxDD `-6.1883`
- `market_context_high->metal_4h` score `-1.7975` n `221` status `ready` deltaP `7.904` edge `0.0667` maxDD `-12.5349`
- `market_context_high->commodity_4h` score `-4.0413` n `221` status `ready` deltaP `-11.5337` edge `-0.0696` maxDD `-17.3969`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
