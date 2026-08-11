# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-11T06:52:30.503463+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11760`

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

- `market_context_high->unknown_24h` score `43.509` n `128` status `ready` deltaP `-18.5158` edge `3.9946` maxDD `-9.6329`
- `market_context_high->commodity_24h` score `2.3303` n `128` status `ready` deltaP `14.2643` edge `0.2051` maxDD `-4.4804`
- `risk_on_high->commodity_1h` score `0.9757` n `30` status `ready` deltaP `10.8284` edge `0.0324` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `0.9757` n `30` status `ready` deltaP `10.8284` edge `0.0324` maxDD `-0.1957`
- `market_context_high->commodity_1h` score `0.7117` n `180` status `ready` deltaP `9.7173` edge `0.0288` maxDD `-0.7418`
- `market_context_high->commodity_4h` score `0.6514` n `169` status `ready` deltaP `10.3267` edge `0.0569` maxDD `-2.7169`
- `risk_on_high->index_1h` score `0.5412` n `30` status `ready` deltaP `13.0739` edge `0.0103` maxDD `-0.2457`
- `risk_on_and_context->index_1h` score `0.5412` n `30` status `ready` deltaP `13.0739` edge `0.0103` maxDD `-0.2457`
- `market_context_high->fx_24h` score `0.507` n `128` status `ready` deltaP `17.109` edge `0.0317` maxDD `-1.4613`
- `market_context_high->fx_1h` score `-0.1574` n `180` status `ready` deltaP `3.3101` edge `0.0001` maxDD `-0.3878`
- `risk_on_high->fx_1h` score `-0.1694` n `30` status `ready` deltaP `1.0878` edge `0.0014` maxDD `-0.1547`
- `risk_on_and_context->fx_1h` score `-0.1694` n `30` status `ready` deltaP `1.0878` edge `0.0014` maxDD `-0.1547`
- `market_context_high->fx_4h` score `-0.2681` n `169` status `ready` deltaP `3.3288` edge `0.0039` maxDD `-0.504`
- `risk_on_high->equity_1h` score `-0.4674` n `30` status `ready` deltaP `-1.7165` edge `-0.0074` maxDD `-1.2867`
- `risk_on_and_context->equity_1h` score `-0.4674` n `30` status `ready` deltaP `-1.7165` edge `-0.0074` maxDD `-1.2867`
- `market_context_high->metal_1h` score `-1.0413` n `180` status `ready` deltaP `-7.6547` edge `-0.0147` maxDD `-2.0884`
- `risk_on_high->crypto_major_1h` score `-1.0667` n `30` status `ready` deltaP `4.4212` edge `-0.0602` maxDD `-2.6536`
- `risk_on_and_context->crypto_major_1h` score `-1.0667` n `30` status `ready` deltaP `4.4212` edge `-0.0602` maxDD `-2.6536`
- `market_context_high->index_1h` score `-1.3267` n `180` status `ready` deltaP `-7.4817` edge `-0.003` maxDD `-0.948`
- `market_context_high->index_4h` score `-1.3693` n `169` status `ready` deltaP `-2.6226` edge `-0.0072` maxDD `-1.4875`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
