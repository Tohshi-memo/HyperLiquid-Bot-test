# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-24T01:52:13.376456+00:00`
- Price records: `672`
- Market context records: `1689`
- Flow alert records: `6770`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8854`

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

- `market_context_high->metal_24h` score `7.3667` n `146` status `ready` deltaP `26.3236` edge `0.681` maxDD `-12.7414`
- `market_context_high->crypto_alt_4h` score `5.4217` n `192` status `ready` deltaP `23.5391` edge `0.5613` maxDD `-16.3135`
- `market_context_high->unknown_24h` score `5.3035` n `146` status `ready` deltaP `16.8152` edge `0.8619` maxDD `-35.8966`
- `market_context_high->crypto_major_4h` score `3.8921` n `192` status `ready` deltaP `21.7988` edge `0.4499` maxDD `-13.3376`
- `market_context_high->index_24h` score `3.8791` n `146` status `ready` deltaP `17.6944` edge `0.3431` maxDD `-5.3574`
- `market_context_high->equity_4h` score `2.9439` n `192` status `ready` deltaP `15.7012` edge `0.2501` maxDD `-5.0894`
- `market_context_high->equity_24h` score `1.9007` n `146` status `ready` deltaP `16.6848` edge `0.537` maxDD `-33.1875`
- `market_context_high->crypto_alt_1h` score `0.6022` n `202` status `ready` deltaP `5.9628` edge `0.1128` maxDD `-4.1892`
- `market_context_high->crypto_alt_24h` score `0.3872` n `146` status `ready` deltaP `24.5367` edge `1.0496` maxDD `-88.8062`
- `market_context_high->index_4h` score `0.2417` n `192` status `ready` deltaP `6.6057` edge `0.085` maxDD `-3.7119`
- `market_context_high->equity_1h` score `0.0129` n `202` status `ready` deltaP `4.6837` edge `0.0507` maxDD `-2.8014`
- `market_context_high->crypto_major_1h` score `-0.217` n `202` status `ready` deltaP `3.4994` edge `0.0785` maxDD `-4.9264`
- `market_context_high->crypto_major_24h` score `-0.417` n `146` status `ready` deltaP `23.0436` edge `0.6515` maxDD `-62.3533`
- `market_context_high->index_1h` score `-0.5189` n `202` status `ready` deltaP `0.6196` edge `0.0158` maxDD `-1.7205`
- `market_context_high->metal_1h` score `-0.5627` n `202` status `ready` deltaP `6.6654` edge `0.017` maxDD `-6.3532`
- `market_context_high->metal_4h` score `-0.6058` n `192` status `ready` deltaP `12.0299` edge `0.1385` maxDD `-12.5349`
- `market_context_high->fx_24h` score `-0.7358` n `146` status `ready` deltaP `5.1879` edge `0.009` maxDD `-1.3925`
- `market_context_high->fx_1h` score `-1.0236` n `202` status `ready` deltaP `-2.9362` edge `-0.0025` maxDD `-0.3914`
- `market_context_high->fx_4h` score `-1.7351` n `192` status `ready` deltaP `-6.2246` edge `-0.0102` maxDD `-1.4313`
- `market_context_high->commodity_1h` score `-2.0835` n `202` status `ready` deltaP `1.0242` edge `-0.0285` maxDD `-14.9691`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
