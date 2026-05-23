# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-23T04:52:17.390867+00:00`
- Price records: `672`
- Market context records: `1596`
- Flow alert records: `6510`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8814`

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

- `market_context_high->metal_24h` score `14.0756` n `182` status `ready` deltaP `30.5879` edge `1.0691` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `12.8221` n `182` status `ready` deltaP `27.171` edge `1.089` maxDD `-15.1306`
- `market_context_high->crypto_major_24h` score `10.9504` n `182` status `ready` deltaP `26.9135` edge `0.8463` maxDD `-8.0553`
- `market_context_high->equity_24h` score `5.2903` n `182` status `ready` deltaP `21.1863` edge `0.5323` maxDD `-14.2815`
- `market_context_high->index_24h` score `4.288` n `182` status `ready` deltaP `22.6896` edge `0.3147` maxDD `-5.3574`
- `market_context_high->equity_4h` score `1.1277` n `199` status `ready` deltaP `9.6642` edge `0.139` maxDD `-5.0894`
- `market_context_high->crypto_alt_4h` score `0.0842` n `199` status `ready` deltaP `12.1875` edge `0.2615` maxDD `-19.5565`
- `market_context_high->crypto_major_4h` score `0.0109` n `199` status `ready` deltaP `8.5174` edge `0.2155` maxDD `-13.3376`
- `market_context_high->fx_24h` score `-0.1038` n `182` status `ready` deltaP `8.5432` edge `0.0393` maxDD `-1.3925`
- `market_context_high->crypto_alt_1h` score `-0.3612` n `199` status `ready` deltaP `0.5183` edge `0.0526` maxDD `-4.1892`
- `market_context_high->equity_1h` score `-0.5372` n `199` status `ready` deltaP `1.063` edge `0.029` maxDD `-2.8014`
- `market_context_high->fx_1h` score `-0.5946` n `199` status `ready` deltaP `-1.3954` edge `-0.0037` maxDD `-0.3914`
- `market_context_high->index_1h` score `-0.7081` n `199` status `ready` deltaP `0.1753` edge `0.003` maxDD `-1.7205`
- `market_context_high->metal_1h` score `-0.7228` n `199` status `ready` deltaP `5.2975` edge `0.0056` maxDD `-6.3532`
- `market_context_high->commodity_1h` score `-0.8154` n `199` status `ready` deltaP `-1.5451` edge `-0.0021` maxDD `-4.7041`
- `market_context_high->crypto_major_1h` score `-0.881` n `199` status `ready` deltaP `-0.5935` edge `0.0267` maxDD `-6.1883`
- `market_context_high->index_4h` score `-1.0313` n `199` status `ready` deltaP `-1.0862` edge `0.0302` maxDD `-3.7119`
- `market_context_high->metal_4h` score `-1.3311` n `199` status `ready` deltaP `10.0587` edge `0.0912` maxDD `-12.5349`
- `market_context_high->fx_4h` score `-1.3712` n `199` status `ready` deltaP `-10.2448` edge `-0.0146` maxDD `-1.4313`
- `market_context_high->commodity_4h` score `-5.2282` n `199` status `ready` deltaP `-14.5476` edge `-0.1106` maxDD `-24.683`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
