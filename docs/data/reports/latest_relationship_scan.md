# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-06T08:52:31.360850+00:00`
- Price records: `672`
- Market context records: `5863`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `10104`

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

- `news_risk_high->fx_4h` score `3.7023` n `30` status `ready` deltaP `38.628` edge `0.0556` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `1.9627` n `30` status `ready` deltaP `23.7824` edge `0.0189` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `0.8807` n `30` status `ready` deltaP `11.6866` edge `0.0817` maxDD `-2.0691`
- `market_context_high->equity_4h` score `0.6102` n `245` status `ready` deltaP `6.7695` edge `0.1515` maxDD `-6.9958`
- `news_risk_high->crypto_alt_1h` score `0.2684` n `30` status `ready` deltaP `5.4691` edge `0.0441` maxDD `-1.6923`
- `market_context_high->fx_1h` score `-0.3462` n `245` status `ready` deltaP `0.6532` edge `-0.0002` maxDD `-0.5499`
- `market_context_high->equity_1h` score `-0.4188` n `245` status `ready` deltaP `4.6646` edge `0.0347` maxDD `-5.0555`
- `news_risk_high->metal_1h` score `-0.4367` n `30` status `ready` deltaP `1.3872` edge `-0.0286` maxDD `-1.2643`
- `market_context_high->metal_1h` score `-0.4696` n `245` status `ready` deltaP `3.5641` edge `0.0042` maxDD `-2.0339`
- `market_context_high->commodity_1h` score `-0.5718` n `245` status `ready` deltaP `-1.5911` edge `-0.0026` maxDD `-2.1412`
- `market_context_high->index_1h` score `-0.6047` n `245` status `ready` deltaP `0.5163` edge `0.0038` maxDD `-0.7819`
- `market_context_high->crypto_major_1h` score `-0.7577` n `245` status `ready` deltaP `3.8635` edge `0.0432` maxDD `-6.2348`
- `market_context_high->crypto_alt_1h` score `-0.9106` n `245` status `ready` deltaP `2.68` edge `0.0397` maxDD `-6.6758`
- `news_risk_high->index_1h` score `-1.2409` n `30` status `ready` deltaP `-12.5449` edge `-0.024` maxDD `-1.1161`
- `market_context_high->index_4h` score `-1.2418` n `245` status `ready` deltaP `-0.3858` edge `0.0121` maxDD `-3.165`
- `market_context_high->equity_24h` score `-1.6926` n `228` status `ready` deltaP `14.6473` edge `0.2692` maxDD `-31.6316`
- `market_context_high->metal_4h` score `-1.7437` n `245` status `ready` deltaP `-3.3904` edge `-0.0331` maxDD `-6.095`
- `news_risk_high->commodity_4h` score `-1.7873` n `30` status `ready` deltaP `-13.4248` edge `-0.0521` maxDD `-2.3372`
- `market_context_high->fx_24h` score `-1.8265` n `228` status `ready` deltaP `4.8794` edge `0.0151` maxDD `-5.5435`
- `market_context_high->fx_4h` score `-1.841` n `245` status `ready` deltaP `-5.6577` edge `-0.0034` maxDD `-2.2593`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
