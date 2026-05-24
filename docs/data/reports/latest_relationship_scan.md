# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-24T01:22:18.434961+00:00`
- Price records: `672`
- Market context records: `1687`
- Flow alert records: `6763`
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

- `market_context_high->metal_24h` score `7.6742` n `148` status `ready` deltaP `26.5828` edge `0.7049` maxDD `-12.7414`
- `market_context_high->crypto_alt_4h` score `5.4704` n `192` status `ready` deltaP `23.9076` edge `0.5629` maxDD `-16.3135`
- `market_context_high->unknown_24h` score `4.3374` n `148` status `ready` deltaP `16.0783` edge `0.7863` maxDD `-35.8966`
- `market_context_high->index_24h` score `3.8817` n `148` status `ready` deltaP `17.9814` edge `0.3414` maxDD `-5.3574`
- `market_context_high->crypto_major_4h` score `3.7551` n `192` status `ready` deltaP `21.062` edge `0.4434` maxDD `-13.3376`
- `market_context_high->equity_4h` score `2.9103` n `192` status `ready` deltaP `15.7012` edge `0.2473` maxDD `-5.0894`
- `market_context_high->equity_24h` score `1.9002` n `148` status `ready` deltaP `17.0088` edge `0.5348` maxDD `-33.1875`
- `market_context_high->crypto_alt_1h` score `0.54` n `204` status `ready` deltaP `5.6798` edge `0.1095` maxDD `-4.1892`
- `market_context_high->crypto_alt_24h` score `0.372` n `148` status `ready` deltaP `24.7218` edge `1.0471` maxDD `-88.8062`
- `market_context_high->index_4h` score `0.1575` n `192` status `ready` deltaP `5.8689` edge `0.0829` maxDD `-3.7119`
- `market_context_high->equity_1h` score `-0.0201` n `204` status `ready` deltaP `4.3619` edge `0.0501` maxDD `-2.8014`
- `market_context_high->crypto_major_24h` score `-0.3125` n `148` status `ready` deltaP `23.312` edge `0.6631` maxDD `-62.3533`
- `market_context_high->crypto_major_1h` score `-0.349` n `204` status `ready` deltaP `3.2553` edge `0.0766` maxDD `-5.5244`
- `market_context_high->index_1h` score `-0.4839` n `204` status `ready` deltaP `1.0127` edge `0.0161` maxDD `-1.7205`
- `market_context_high->metal_1h` score `-0.5402` n `204` status `ready` deltaP `7.0682` edge `0.0172` maxDD `-6.3532`
- `market_context_high->metal_4h` score `-0.625` n `192` status `ready` deltaP `12.0299` edge `0.1369` maxDD `-12.5349`
- `market_context_high->fx_24h` score `-0.6953` n `148` status `ready` deltaP `5.4101` edge `0.0109` maxDD `-1.3925`
- `market_context_high->fx_1h` score `-1.0228` n `204` status `ready` deltaP `-2.9265` edge `-0.0025` maxDD `-0.3914`
- `market_context_high->fx_4h` score `-1.1684` n `192` status `ready` deltaP `-6.9613` edge `-0.0105` maxDD `-1.4313`
- `market_context_high->commodity_1h` score `-2.0557` n `204` status `ready` deltaP `1.4853` edge `-0.028` maxDD `-14.9691`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
