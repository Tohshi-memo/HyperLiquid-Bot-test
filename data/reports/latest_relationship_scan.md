# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-22T11:07:14.759961+00:00`
- Price records: `672`
- Market context records: `1520`
- Flow alert records: `6288`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8791`

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

- `market_context_high->metal_24h` score `14.1191` n `161` status `ready` deltaP `24.0511` edge `1.1163` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `11.3161` n `161` status `ready` deltaP `28.8658` edge `0.9522` maxDD `-15.1306`
- `market_context_high->crypto_major_24h` score `10.6531` n `161` status `ready` deltaP `28.1175` edge `0.8135` maxDD `-8.0553`
- `market_context_high->index_24h` score `3.7345` n `161` status `ready` deltaP `19.7765` edge `0.288` maxDD `-5.3574`
- `market_context_high->equity_24h` score `2.4329` n `161` status `ready` deltaP `12.9788` edge `0.3489` maxDD `-14.2815`
- `market_context_high->fx_24h` score `1.0113` n `161` status `ready` deltaP `19.0476` edge `0.0622` maxDD `-1.3925`
- `market_context_high->equity_4h` score `0.7099` n `186` status `ready` deltaP `5.1386` edge `0.1079` maxDD `-3.6396`
- `market_context_high->fx_1h` score `-0.5775` n `198` status `ready` deltaP `-1.1416` edge `-0.0032` maxDD `-0.3914`
- `market_context_high->crypto_alt_1h` score `-0.5966` n `198` status `ready` deltaP `-0.319` edge `0.028` maxDD `-4.1892`
- `market_context_high->index_1h` score `-0.6431` n `198` status `ready` deltaP `0.4824` edge `0.0022` maxDD `-1.7205`
- `market_context_high->commodity_1h` score `-0.7911` n `198` status `ready` deltaP `-0.8982` edge `-0.0033` maxDD `-4.7041`
- `market_context_high->crypto_alt_4h` score `-0.8052` n `186` status `ready` deltaP `9.2447` edge `0.1671` maxDD `-19.5565`
- `market_context_high->equity_1h` score `-0.8479` n `198` status `ready` deltaP `-1.6315` edge `0.0169` maxDD `-2.8014`
- `market_context_high->crypto_major_4h` score `-0.8594` n `186` status `ready` deltaP `4.7108` edge `0.1293` maxDD `-13.3376`
- `market_context_high->crypto_major_1h` score `-1.0693` n `198` status `ready` deltaP `-1.5907` edge `0.0092` maxDD `-6.1883`
- `market_context_high->metal_1h` score `-1.1304` n `198` status `ready` deltaP `5.2925` edge `0.0041` maxDD `-6.3532`
- `market_context_high->metal_4h` score `-1.1818` n `186` status `ready` deltaP `10.9051` edge `0.098` maxDD `-12.5349`
- `market_context_high->index_4h` score `-1.3764` n `186` status `ready` deltaP `-4.6354` edge `0.0251` maxDD `-3.7119`
- `market_context_high->fx_4h` score `-1.7329` n `186` status `ready` deltaP `-6.1221` edge `-0.0107` maxDD `-1.4313`
- `market_context_high->unknown_24h` score `-2.2658` n `161` status `ready` deltaP `-2.3173` edge `0.0996` maxDD `-10.1706`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
