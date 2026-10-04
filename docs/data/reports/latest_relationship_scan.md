# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-04T22:52:26.791812+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5036`

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

- `market_context_high->unknown_1h` score `97.37` n `97` status `ready` deltaP `-0.1605` edge `8.1567` maxDD `-0.9839`
- `market_context_high->unknown_4h` score `79.643` n `97` status `ready` deltaP `2.7564` edge `6.6497` maxDD `-0.4928`
- `news_risk_high->crypto_major_4h` score `10.0518` n `65` status `ready` deltaP `34.9906` edge `0.6247` maxDD `-0.6258`
- `market_context_high->crypto_major_24h` score `7.8066` n `46` status `ready` deltaP `27.6721` edge `0.5313` maxDD `-4.5519`
- `news_risk_high->crypto_alt_4h` score `7.1595` n `65` status `ready` deltaP `22.8354` edge `0.5788` maxDD `-6.4195`
- `market_context_high->crypto_alt_24h` score `7.0807` n `46` status `ready` deltaP `21.2334` edge `0.5758` maxDD `-8.1838`
- `news_risk_high->equity_24h` score `5.7728` n `65` status `ready` deltaP `18.6726` edge `0.3666` maxDD `-0.1344`
- `market_context_high->crypto_major_4h` score `4.3852` n `97` status `ready` deltaP `18.9716` edge `0.3093` maxDD `-3.294`
- `news_risk_high->index_24h` score `3.7004` n `65` status `ready` deltaP `26.2153` edge `0.1336` maxDD `0.0`
- `news_risk_high->equity_4h` score `3.4041` n `65` status `ready` deltaP `23.4732` edge `0.1882` maxDD `-2.881`
- `news_risk_high->index_4h` score `3.109` n `65` status `ready` deltaP `34.0479` edge `0.0583` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.6655` n `65` status `ready` deltaP `10.9143` edge `0.1849` maxDD `-1.5096`
- `news_risk_high->metal_4h` score `2.3872` n `65` status `ready` deltaP `21.2125` edge `0.0991` maxDD `-0.993`
- `news_risk_high->index_1h` score `2.1393` n `65` status `ready` deltaP `26.3657` edge `0.0175` maxDD `-0.1997`
- `market_context_high->crypto_major_1h` score `1.927` n `97` status `ready` deltaP `13.8327` edge `0.1134` maxDD `-2.2692`
- `news_risk_high->crypto_alt_1h` score `1.5402` n `65` status `ready` deltaP `5.3178` edge `0.1448` maxDD `-2.4854`
- `market_context_high->fx_4h` score `1.4346` n `97` status `ready` deltaP `25.2782` edge `0.0267` maxDD `-0.3868`
- `market_context_high->fx_24h` score `1.3732` n `46` status `ready` deltaP `25.536` edge `0.1076` maxDD `-1.8102`
- `market_context_high->crypto_alt_4h` score `1.2727` n `97` status `ready` deltaP `4.6911` edge `0.2537` maxDD `-7.6465`
- `market_context_high->fx_1h` score `0.9252` n `97` status `ready` deltaP `14.5672` edge `0.0064` maxDD `-0.113`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
