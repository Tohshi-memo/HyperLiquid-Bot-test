# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-17T02:52:26.923579+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11831`

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

- `market_context_high->commodity_24h` score `3.9355` n `70` status `ready` deltaP `34.1915` edge `0.1349` maxDD `-0.4576`
- `market_context_high->index_24h` score `1.4625` n `70` status `ready` deltaP `21.7014` edge `-0.0228` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `1.3983` n `70` status `ready` deltaP `2.1627` edge `0.2449` maxDD `-6.0904`
- `market_context_high->commodity_4h` score `1.298` n `100` status `ready` deltaP `14.3415` edge `0.0597` maxDD `-0.7718`
- `market_context_high->equity_24h` score `1.2493` n `70` status `ready` deltaP `15.6944` edge `0.0376` maxDD `-1.7163`
- `market_context_high->commodity_1h` score `-0.2374` n `108` status `ready` deltaP `0.3826` edge `0.0116` maxDD `-0.8998`
- `market_context_high->metal_4h` score `-0.3771` n `100` status `ready` deltaP `15.1037` edge `0.0086` maxDD `-4.5909`
- `market_context_high->fx_1h` score `-0.4172` n `108` status `ready` deltaP `-2.1513` edge `-0.0021` maxDD `-0.2968`
- `market_context_high->metal_1h` score `-0.5413` n `108` status `ready` deltaP `3.6095` edge `0.0024` maxDD `-1.7257`
- `market_context_high->fx_4h` score `-0.6519` n `100` status `ready` deltaP `-2.5061` edge `-0.0064` maxDD `-0.504`
- `market_context_high->index_1h` score `-1.0024` n `108` status `ready` deltaP `-4.4355` edge `-0.0018` maxDD `-0.5064`
- `market_context_high->equity_1h` score `-1.1987` n `108` status `ready` deltaP `-6.2042` edge `-0.0292` maxDD `-3.3165`
- `market_context_high->crypto_major_4h` score `-1.5674` n `100` status `ready` deltaP `1.1524` edge `-0.0175` maxDD `-4.6638`
- `market_context_high->crypto_alt_1h` score `-1.8386` n `108` status `ready` deltaP `-5.2284` edge `-0.0174` maxDD `-4.4101`
- `market_context_high->crypto_major_1h` score `-1.9206` n `108` status `ready` deltaP `-5.2284` edge `-0.0248` maxDD `-4.0312`
- `market_context_high->index_4h` score `-1.9531` n `100` status `ready` deltaP `-11.5` edge `-0.0052` maxDD `-0.8045`
- `market_context_high->fx_24h` score `-3.1295` n `70` status `ready` deltaP `-29.9355` edge `-0.0409` maxDD `-1.8596`
- `market_context_high->equity_4h` score `-3.5971` n `100` status `ready` deltaP `-19.4817` edge `-0.1506` maxDD `-8.1221`
- `market_context_high->metal_24h` score `-5.3416` n `70` status `ready` deltaP `-22.3264` edge `-0.0451` maxDD `-7.0954`
- `market_context_high->crypto_alt_4h` score `-6.0225` n `100` status `ready` deltaP `-9.9329` edge `-0.0675` maxDD `-16.786`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
