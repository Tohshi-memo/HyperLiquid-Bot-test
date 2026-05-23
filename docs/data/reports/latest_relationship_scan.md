# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-23T05:22:20.325999+00:00`
- Price records: `672`
- Market context records: `1599`
- Flow alert records: `6516`
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

- `market_context_high->metal_24h` score `14.1706` n `182` status `ready` deltaP `30.9352` edge `1.0747` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `13.0208` n `182` status `ready` deltaP `27.3447` edge `1.1044` maxDD `-15.1306`
- `market_context_high->crypto_major_24h` score `11.0771` n `182` status `ready` deltaP `27.0872` edge `0.8557` maxDD `-8.0553`
- `market_context_high->equity_24h` score `5.4429` n `182` status `ready` deltaP `21.5335` edge `0.5427` maxDD `-14.2815`
- `market_context_high->index_24h` score `4.3325` n `182` status `ready` deltaP `23.0369` edge `0.3161` maxDD `-5.3574`
- `market_context_high->equity_4h` score `1.1435` n `199` status `ready` deltaP `9.8166` edge `0.1393` maxDD `-5.0894`
- `market_context_high->crypto_alt_4h` score `0.085` n `199` status `ready` deltaP `12.1875` edge `0.2616` maxDD `-19.5565`
- `market_context_high->crypto_major_4h` score `0.0204` n `199` status `ready` deltaP `8.6699` edge `0.2157` maxDD `-13.3376`
- `market_context_high->fx_24h` score `-0.1352` n `182` status `ready` deltaP `8.1959` edge `0.039` maxDD `-1.3925`
- `market_context_high->crypto_alt_1h` score `-0.3581` n `199` status `ready` deltaP `0.5183` edge `0.053` maxDD `-4.1892`
- `market_context_high->equity_1h` score `-0.5348` n `199` status `ready` deltaP `1.063` edge `0.0292` maxDD `-2.8014`
- `market_context_high->fx_1h` score `-0.6024` n `199` status `ready` deltaP `-1.5451` edge `-0.0037` maxDD `-0.3914`
- `market_context_high->index_1h` score `-0.6805` n `199` status `ready` deltaP `0.4747` edge `0.0033` maxDD `-1.7205`
- `market_context_high->metal_1h` score `-0.7228` n `199` status `ready` deltaP `5.2975` edge `0.0056` maxDD `-6.3532`
- `market_context_high->commodity_1h` score `-0.813` n `199` status `ready` deltaP `-1.5451` edge `-0.0018` maxDD `-4.7041`
- `market_context_high->crypto_major_1h` score `-0.8763` n `199` status `ready` deltaP `-0.5935` edge `0.0273` maxDD `-6.1883`
- `market_context_high->index_4h` score `-1.0057` n `199` status `ready` deltaP `-0.7814` edge `0.0303` maxDD `-3.7119`
- `market_context_high->metal_4h` score `-1.3579` n `199` status `ready` deltaP `9.7538` edge `0.091` maxDD `-12.5349`
- `market_context_high->fx_4h` score `-1.3799` n `199` status `ready` deltaP `-10.3973` edge `-0.0147` maxDD `-1.4313`
- `market_context_high->commodity_4h` score `-5.222` n `199` status `ready` deltaP `-14.5476` edge `-0.1098` maxDD `-24.683`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
