# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-23T05:07:18.958033+00:00`
- Price records: `672`
- Market context records: `1598`
- Flow alert records: `6513`
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

- `market_context_high->metal_24h` score `14.1219` n `182` status `ready` deltaP `30.7616` edge `1.0718` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `12.9037` n `182` status `ready` deltaP `27.171` edge `1.0958` maxDD `-15.1306`
- `market_context_high->crypto_major_24h` score `11.0032` n `182` status `ready` deltaP `26.9135` edge `0.8507` maxDD `-8.0553`
- `market_context_high->equity_24h` score `5.3666` n `182` status `ready` deltaP `21.3599` edge `0.5375` maxDD `-14.2815`
- `market_context_high->index_24h` score `4.3103` n `182` status `ready` deltaP `22.8633` edge `0.3154` maxDD `-5.3574`
- `market_context_high->equity_4h` score `1.1289` n `199` status `ready` deltaP `9.6642` edge `0.1391` maxDD `-5.0894`
- `market_context_high->crypto_alt_4h` score `0.0724` n `199` status `ready` deltaP `12.035` edge `0.261` maxDD `-19.5565`
- `market_context_high->crypto_major_4h` score `0.0109` n `199` status `ready` deltaP `8.5174` edge `0.2155` maxDD `-13.3376`
- `market_context_high->fx_24h` score `-0.1189` n `182` status `ready` deltaP `8.3695` edge `0.0392` maxDD `-1.3925`
- `market_context_high->crypto_alt_1h` score `-0.362` n `199` status `ready` deltaP `0.5183` edge `0.0525` maxDD `-4.1892`
- `market_context_high->equity_1h` score `-0.5348` n `199` status `ready` deltaP `1.063` edge `0.0292` maxDD `-2.8014`
- `market_context_high->fx_1h` score `-0.5946` n `199` status `ready` deltaP `-1.3954` edge `-0.0037` maxDD `-0.3914`
- `market_context_high->index_1h` score `-0.6949` n `199` status `ready` deltaP `0.325` edge `0.0031` maxDD `-1.7205`
- `market_context_high->metal_1h` score `-0.7228` n `199` status `ready` deltaP `5.2975` edge `0.0056` maxDD `-6.3532`
- `market_context_high->commodity_1h` score `-0.8146` n `199` status `ready` deltaP `-1.5451` edge `-0.002` maxDD `-4.7041`
- `market_context_high->crypto_major_1h` score `-0.8786` n `199` status `ready` deltaP `-0.5935` edge `0.027` maxDD `-6.1883`
- `market_context_high->index_4h` score `-1.0191` n `199` status `ready` deltaP `-0.9338` edge `0.0302` maxDD `-3.7119`
- `market_context_high->metal_4h` score `-1.3445` n `199` status `ready` deltaP `9.9063` edge `0.0911` maxDD `-12.5349`
- `market_context_high->fx_4h` score `-1.3712` n `199` status `ready` deltaP `-10.2448` edge `-0.0146` maxDD `-1.4313`
- `market_context_high->commodity_4h` score `-5.2243` n `199` status `ready` deltaP `-14.5476` edge `-0.1101` maxDD `-24.683`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
