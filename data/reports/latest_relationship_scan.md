# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-18T19:07:26.150350+00:00`
- Price records: `672`
- Market context records: `7171`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11810`

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

- `risk_on_high->commodity_1h` score `1.9008` n `32` status `ready` deltaP `20.509` edge `0.0367` maxDD `-0.2021`
- `risk_on_and_context->commodity_1h` score `1.9008` n `32` status `ready` deltaP `20.509` edge `0.0367` maxDD `-0.2021`
- `risk_on_high->equity_1h` score `0.3415` n `32` status `ready` deltaP `3.7612` edge `0.0334` maxDD `-0.7345`
- `risk_on_and_context->equity_1h` score `0.3415` n `32` status `ready` deltaP `3.7612` edge `0.0334` maxDD `-0.7345`
- `risk_on_high->crypto_major_1h` score `0.2772` n `32` status `ready` deltaP `6.6991` edge `0.0199` maxDD `-0.9888`
- `risk_on_and_context->crypto_major_1h` score `0.2772` n `32` status `ready` deltaP `6.6991` edge `0.0199` maxDD `-0.9888`
- `market_context_high->fx_4h` score `-0.3501` n `159` status `ready` deltaP `9.9757` edge `0.0101` maxDD `-1.1291`
- `market_context_high->fx_1h` score `-0.4466` n `171` status `ready` deltaP `1.6257` edge `0.0008` maxDD `-0.5752`
- `market_context_high->crypto_major_1h` score `-0.5773` n `171` status `ready` deltaP `4.2503` edge `0.0387` maxDD `-7.6171`
- `market_context_high->unknown_1h` score `-0.6142` n `171` status `ready` deltaP `-1.2283` edge `0.0212` maxDD `-1.4688`
- `market_context_high->index_1h` score `-0.8375` n `171` status `ready` deltaP `0.147` edge `-0.0043` maxDD `-2.3175`
- `market_context_high->commodity_1h` score `-0.9034` n `171` status `ready` deltaP `-0.105` edge `-0.0125` maxDD `-1.9668`
- `market_context_high->crypto_alt_1h` score `-0.9439` n `171` status `ready` deltaP `-0.2504` edge `0.0269` maxDD `-5.9775`
- `risk_on_high->fx_1h` score `-1.0554` n `32` status `ready` deltaP `-8.6265` edge `-0.0027` maxDD `-0.2195`
- `risk_on_and_context->fx_1h` score `-1.0554` n `32` status `ready` deltaP `-8.6265` edge `-0.0027` maxDD `-0.2195`
- `risk_on_high->crypto_alt_1h` score `-1.3614` n `32` status `ready` deltaP `-10.7036` edge `0.0001` maxDD `-1.3755`
- `risk_on_and_context->crypto_alt_1h` score `-1.3614` n `32` status `ready` deltaP `-10.7036` edge `0.0001` maxDD `-1.3755`
- `market_context_high->metal_1h` score `-1.3921` n `171` status `ready` deltaP `-8.3255` edge `-0.0052` maxDD `-2.0882`
- `risk_on_high->index_1h` score `-1.6547` n `32` status `ready` deltaP `-15.5876` edge `-0.001` maxDD `-0.3045`
- `risk_on_and_context->index_1h` score `-1.6547` n `32` status `ready` deltaP `-15.5876` edge `-0.001` maxDD `-0.3045`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
