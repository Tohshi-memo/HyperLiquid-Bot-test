# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-27T15:07:25.306409+00:00`
- Price records: `672`
- Market context records: `2050`
- Flow alert records: `7796`
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

- `market_context_high->crypto_major_4h` score `9.3119` n `205` status `ready` deltaP `32.6377` edge `0.6114` maxDD `-1.9063`
- `market_context_high->crypto_alt_4h` score `8.6301` n `205` status `ready` deltaP `25.1613` edge `0.6659` maxDD `-5.1574`
- `market_context_high->unknown_4h` score `6.2555` n `205` status `ready` deltaP `19.7709` edge `0.4644` maxDD `-2.6599`
- `market_context_high->unknown_24h` score `3.2121` n `205` status `ready` deltaP `17.6876` edge `0.6818` maxDD `-35.8966`
- `market_context_high->equity_4h` score `3.1888` n `205` status `ready` deltaP `18.0577` edge `0.2548` maxDD `-5.0894`
- `market_context_high->index_4h` score `1.7414` n `205` status `ready` deltaP `14.1871` edge `0.1189` maxDD `-1.8022`
- `market_context_high->crypto_major_1h` score `1.7107` n `206` status `ready` deltaP `13.4062` edge `0.1518` maxDD `-3.2225`
- `market_context_high->crypto_alt_1h` score `1.3421` n `206` status `ready` deltaP `10.4122` edge `0.1538` maxDD `-4.9097`
- `market_context_high->equity_24h` score `0.9764` n `205` status `ready` deltaP `17.7019` edge `0.4532` maxDD `-33.1875`
- `market_context_high->index_24h` score `0.8607` n `205` status `ready` deltaP `6.2039` edge `0.1532` maxDD `-4.1604`
- `market_context_high->equity_1h` score `0.3901` n `206` status `ready` deltaP `8.1217` edge `0.0572` maxDD `-2.6402`
- `market_context_high->unknown_1h` score `0.2305` n `206` status `ready` deltaP `4.5099` edge `0.0611` maxDD `-3.0902`
- `market_context_high->index_1h` score `-0.1367` n `206` status `ready` deltaP `3.7571` edge `0.0226` maxDD `-1.3898`
- `market_context_high->fx_24h` score `-0.4595` n `205` status `ready` deltaP `11.6415` edge `0.0234` maxDD `-2.811`
- `market_context_high->fx_1h` score `-0.7927` n `206` status `ready` deltaP `-0.5988` edge `0.0007` maxDD `-0.3548`
- `market_context_high->metal_4h` score `-0.7934` n `205` status `ready` deltaP `10.5368` edge `0.1259` maxDD `-11.9812`
- `market_context_high->metal_1h` score `-0.798` n `206` status `ready` deltaP `4.1466` edge `0.0246` maxDD `-5.166`
- `market_context_high->crypto_major_24h` score `-0.8634` n `205` status `ready` deltaP `17.9154` edge `0.6672` maxDD `-62.3533`
- `market_context_high->fx_4h` score `-1.4562` n `205` status `ready` deltaP `-4.8914` edge `-0.0006` maxDD `-1.0513`
- `market_context_high->commodity_1h` score `-1.9332` n `206` status `ready` deltaP `1.792` edge `-0.004` maxDD `-15.7972`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
