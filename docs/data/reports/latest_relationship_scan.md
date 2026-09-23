# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-23T14:07:46.476576+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9738`

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

- `market_context_high->unknown_4h` score `39.5273` n `46` status `ready` deltaP `7.9268` edge `3.2411` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `30.1308` n `46` status `ready` deltaP `15.2703` edge `2.4247` maxDD `-0.5817`
- `market_context_high->equity_24h` score `17.1058` n `46` status `ready` deltaP `12.6661` edge `1.3511` maxDD `-0.1382`
- `market_context_high->crypto_alt_24h` score `12.45` n `46` status `ready` deltaP `10.5903` edge `0.9669` maxDD `0.0`
- `market_context_high->index_24h` score `5.7734` n `46` status `ready` deltaP `21.6939` edge `0.3452` maxDD `-0.03`
- `news_risk_high->crypto_major_24h` score `5.4372` n `96` status `ready` deltaP `-7.4652` edge `1.1887` maxDD `-46.1999`
- `news_risk_high->commodity_24h` score `3.4027` n `96` status `ready` deltaP `30.3819` edge `0.1989` maxDD `-2.431`
- `news_risk_high->crypto_major_4h` score `3.1723` n `103` status `ready` deltaP `14.3841` edge `0.2262` maxDD `-2.619`
- `market_context_high->index_4h` score `2.5042` n `46` status `ready` deltaP `28.9567` edge `0.029` maxDD `-0.0692`
- `news_risk_high->crypto_alt_4h` score `2.3537` n `103` status `ready` deltaP `9.2011` edge `0.2346` maxDD `-5.9838`
- `news_risk_high->crypto_alt_1h` score `1.9596` n `103` status `ready` deltaP `11.6607` edge `0.1346` maxDD `-1.5895`
- `news_risk_high->crypto_major_1h` score `1.6487` n `103` status `ready` deltaP `14.3553` edge `0.0852` maxDD `-1.8141`
- `market_context_high->equity_4h` score `1.3433` n `46` status `ready` deltaP `9.5109` edge `0.0792` maxDD `-0.4529`
- `news_risk_high->fx_4h` score `1.2141` n `103` status `ready` deltaP `18.9557` edge `0.0384` maxDD `-0.421`
- `news_risk_high->fx_24h` score `1.1575` n `96` status `ready` deltaP `27.9514` edge `0.121` maxDD `-1.7159`
- `market_context_high->equity_1h` score `1.0355` n `46` status `ready` deltaP `8.559` edge `0.0535` maxDD `-0.2751`
- `market_context_high->index_1h` score `0.8663` n `46` status `ready` deltaP `12.7506` edge `0.0125` maxDD `-0.0249`
- `news_risk_high->metal_1h` score `0.653` n `103` status `ready` deltaP `15.2026` edge `0.0124` maxDD `-0.7468`
- `news_risk_high->metal_4h` score `0.26` n `103` status `ready` deltaP `12.8981` edge `0.0431` maxDD `-1.9941`
- `market_context_high->metal_24h` score `0.253` n `46` status `ready` deltaP `15.6703` edge `-0.06` maxDD `-0.2042`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
