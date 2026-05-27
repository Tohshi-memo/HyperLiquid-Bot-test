# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-27T14:52:24.293960+00:00`
- Price records: `672`
- Market context records: `2049`
- Flow alert records: `7793`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9125`

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

- `market_context_high->crypto_major_4h` score `9.2649` n `205` status `ready` deltaP `32.4858` edge `0.6085` maxDD `-1.9063`
- `market_context_high->crypto_alt_4h` score `8.5855` n `205` status `ready` deltaP `25.0093` edge `0.6632` maxDD `-5.1574`
- `market_context_high->unknown_4h` score `6.2459` n `205` status `ready` deltaP `19.7709` edge `0.4636` maxDD `-2.6599`
- `market_context_high->equity_4h` score `3.143` n `205` status `ready` deltaP `17.9057` edge `0.252` maxDD `-5.0894`
- `market_context_high->unknown_24h` score `3.0813` n `205` status `ready` deltaP `17.6876` edge `0.6709` maxDD `-35.8966`
- `market_context_high->crypto_major_1h` score `1.7083` n `206` status `ready` deltaP `13.4062` edge `0.1516` maxDD `-3.2225`
- `market_context_high->index_4h` score `1.6957` n `205` status `ready` deltaP `14.0352` edge `0.1161` maxDD `-1.8022`
- `market_context_high->crypto_alt_1h` score `1.3361` n `206` status `ready` deltaP `10.4122` edge `0.1533` maxDD `-4.9097`
- `market_context_high->equity_24h` score `0.9326` n `205` status `ready` deltaP `17.5289` edge `0.4507` maxDD `-33.1875`
- `market_context_high->index_24h` score `0.8144` n `205` status `ready` deltaP `6.0309` edge `0.1505` maxDD `-4.1604`
- `market_context_high->equity_1h` score `0.3697` n `206` status `ready` deltaP `7.972` edge `0.0565` maxDD `-2.6402`
- `market_context_high->unknown_1h` score `0.2077` n `206` status `ready` deltaP `4.5099` edge `0.0592` maxDD `-3.0902`
- `market_context_high->index_1h` score `-0.1559` n `206` status `ready` deltaP `3.6074` edge `0.022` maxDD `-1.3898`
- `market_context_high->fx_24h` score `-0.4758` n `205` status `ready` deltaP `11.4685` edge `0.0232` maxDD `-2.811`
- `market_context_high->fx_1h` score `-0.7927` n `206` status `ready` deltaP `-0.5988` edge `0.0007` maxDD `-0.3548`
- `market_context_high->metal_1h` score `-0.7968` n `206` status `ready` deltaP `4.1466` edge `0.0247` maxDD `-5.166`
- `market_context_high->metal_4h` score `-0.8212` n `205` status `ready` deltaP `10.3848` edge `0.1246` maxDD `-11.9812`
- `market_context_high->crypto_major_24h` score `-0.9504` n `205` status `ready` deltaP `17.7424` edge `0.6611` maxDD `-62.3533`
- `market_context_high->fx_4h` score `-1.4562` n `205` status `ready` deltaP `-4.8914` edge `-0.0006` maxDD `-1.0513`
- `market_context_high->commodity_1h` score `-1.9169` n `206` status `ready` deltaP `1.9417` edge `-0.0029` maxDD `-15.7972`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
