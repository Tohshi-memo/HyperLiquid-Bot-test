# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-17T09:22:27.047757+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9372`

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

- `risk_on_high->commodity_24h` score `7.0269` n `54` status `ready` deltaP `38.5017` edge `0.3289` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `7.0269` n `54` status `ready` deltaP `38.5017` edge `0.3289` maxDD `0.0`
- `market_context_high->crypto_alt_4h` score `6.9067` n `137` status `ready` deltaP `16.0862` edge `0.5681` maxDD `-4.9825`
- `risk_on_high->crypto_major_4h` score `6.2877` n `63` status `ready` deltaP `35.436` edge `0.373` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `6.2877` n `63` status `ready` deltaP `35.436` edge `0.373` maxDD `-4.1548`
- `market_context_high->crypto_major_4h` score `6.028` n `137` status `ready` deltaP `23.6992` edge `0.4765` maxDD `-5.906`
- `risk_on_high->crypto_alt_4h` score `3.6173` n `63` status `ready` deltaP `12.425` edge `0.3021` maxDD `-3.679`
- `risk_on_and_context->crypto_alt_4h` score `3.6173` n `63` status `ready` deltaP `12.425` edge `0.3021` maxDD `-3.679`
- `market_context_high->crypto_major_1h` score `1.0009` n `149` status `ready` deltaP `7.6458` edge `0.113` maxDD `-3.7781`
- `market_context_high->crypto_alt_1h` score `0.9651` n `149` status `ready` deltaP `9.5095` edge `0.1318` maxDD `-5.8485`
- `market_context_high->metal_4h` score `0.3725` n `137` status `ready` deltaP `12.806` edge `0.0502` maxDD `-1.6961`
- `risk_on_high->index_1h` score `0.1221` n `75` status `ready` deltaP `6.5226` edge `0.0051` maxDD `-0.7394`
- `risk_on_and_context->index_1h` score `0.1221` n `75` status `ready` deltaP `6.5226` edge `0.0051` maxDD `-0.7394`
- `market_context_high->index_1h` score `-0.1576` n `149` status `ready` deltaP `7.5338` edge `0.0044` maxDD `-1.3195`
- `risk_on_high->crypto_major_1h` score `-0.2379` n `75` status `ready` deltaP `5.2655` edge `0.0173` maxDD `-3.7781`
- `risk_on_and_context->crypto_major_1h` score `-0.2379` n `75` status `ready` deltaP `5.2655` edge `0.0173` maxDD `-3.7781`
- `market_context_high->metal_1h` score `-0.2634` n `149` status `ready` deltaP `8.3993` edge `0.009` maxDD `-0.9556`
- `risk_on_high->metal_1h` score `-0.4331` n `75` status `ready` deltaP `2.0279` edge `0.0041` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.4331` n `75` status `ready` deltaP `2.0279` edge `0.0041` maxDD `-0.8513`
- `market_context_high->equity_1h` score `-0.4494` n `149` status `ready` deltaP `8.6644` edge `0.0356` maxDD `-7.0778`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
