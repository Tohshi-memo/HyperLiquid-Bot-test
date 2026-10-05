# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-05T00:07:32.856642+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5040`

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

- `market_context_high->unknown_1h` score `99.7231` n `97` status `ready` deltaP `0.1389` edge `8.3508` maxDD `-0.9839`
- `market_context_high->unknown_4h` score `91.5962` n `97` status `ready` deltaP `2.7564` edge `7.6458` maxDD `-0.4928`
- `news_risk_high->crypto_major_4h` score `9.8324` n `65` status `ready` deltaP `34.2284` edge `0.6115` maxDD `-0.6258`
- `market_context_high->crypto_major_24h` score `7.3879` n `46` status `ready` deltaP `26.804` edge `0.5022` maxDD `-4.5519`
- `news_risk_high->crypto_alt_4h` score `6.9173` n `65` status `ready` deltaP `22.0732` edge `0.5637` maxDD `-6.4195`
- `market_context_high->crypto_alt_24h` score `6.5709` n `46` status `ready` deltaP `20.3654` edge `0.5391` maxDD `-8.1838`
- `news_risk_high->equity_24h` score `5.365` n `65` status `ready` deltaP `17.8045` edge `0.3384` maxDD `-0.1344`
- `market_context_high->crypto_major_4h` score `4.1659` n `97` status `ready` deltaP `18.2094` edge `0.2961` maxDD `-3.294`
- `news_risk_high->index_24h` score `3.6221` n `65` status `ready` deltaP `25.5208` edge `0.1317` maxDD `0.0`
- `news_risk_high->equity_4h` score `3.1991` n `65` status `ready` deltaP `22.711` edge `0.1762` maxDD `-2.881`
- `news_risk_high->index_4h` score `3.0372` n `65` status `ready` deltaP `33.2857` edge `0.0574` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.7362` n `65` status `ready` deltaP `11.3634` edge `0.1878` maxDD `-1.5096`
- `news_risk_high->metal_4h` score `2.2723` n `65` status `ready` deltaP `20.4503` edge `0.0946` maxDD `-0.993`
- `news_risk_high->index_1h` score `2.18` n `65` status `ready` deltaP `26.8148` edge `0.0179` maxDD `-0.1997`
- `market_context_high->crypto_major_1h` score `1.9978` n `97` status `ready` deltaP `14.2818` edge `0.1163` maxDD `-2.2692`
- `news_risk_high->crypto_alt_1h` score `1.5726` n `65` status `ready` deltaP `5.3178` edge `0.1475` maxDD `-2.4854`
- `market_context_high->fx_4h` score `1.4796` n `97` status `ready` deltaP `25.7355` edge `0.0274` maxDD `-0.3868`
- `market_context_high->fx_24h` score `1.3853` n `46` status `ready` deltaP `25.7096` edge `0.108` maxDD `-1.8102`
- `market_context_high->crypto_alt_4h` score `1.0305` n `97` status `ready` deltaP `3.9289` edge `0.2386` maxDD `-7.6465`
- `market_context_high->fx_1h` score `0.9791` n `97` status `ready` deltaP `15.166` edge `0.0069` maxDD `-0.113`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
