# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-06T08:17:51.498320+00:00`
- Price records: `672`
- Market context records: `3054`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6969`

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

- `market_context_high->crypto_alt_24h` score `25.7641` n `99` status `ready` deltaP `14.457` edge `2.4423` maxDD `-22.6673`
- `market_context_high->commodity_24h` score `13.6159` n `99` status `ready` deltaP `45.1547` edge `0.8577` maxDD `-1.2589`
- `market_context_high->unknown_24h` score `13.5371` n `99` status `ready` deltaP `24.6686` edge `1.0101` maxDD `-1.7175`
- `market_context_high->equity_24h` score `10.3294` n `99` status `ready` deltaP `25.6313` edge `1.4286` maxDD `-18.3486`
- `market_context_high->index_24h` score `9.7264` n `99` status `ready` deltaP `23.8321` edge `0.7772` maxDD `-4.7103`
- `market_context_high->commodity_4h` score `2.5166` n `132` status `ready` deltaP `17.2395` edge `0.1595` maxDD `-2.8438`
- `market_context_high->commodity_1h` score `-0.1661` n `136` status `ready` deltaP `1.0083` edge `0.0217` maxDD `-1.7142`
- `market_context_high->unknown_4h` score `-0.3458` n `132` status `ready` deltaP `2.7023` edge `0.0585` maxDD `-3.7602`
- `market_context_high->index_1h` score `-0.5428` n `136` status `ready` deltaP `2.9676` edge `0.0169` maxDD `-4.5023`
- `market_context_high->fx_1h` score `-0.5436` n `136` status `ready` deltaP `-4.8345` edge `-0.0002` maxDD `-0.3147`
- `market_context_high->crypto_alt_1h` score `-0.5956` n `136` status `ready` deltaP `5.7591` edge `0.0982` maxDD `-14.7034`
- `market_context_high->equity_1h` score `-0.7837` n `136` status `ready` deltaP `2.7783` edge `0.0264` maxDD `-8.6319`
- `market_context_high->unknown_1h` score `-0.9264` n `136` status `ready` deltaP `4.4822` edge `-0.034` maxDD `-3.1801`
- `market_context_high->crypto_major_1h` score `-0.934` n `136` status `ready` deltaP `4.491` edge `0.0766` maxDD `-15.1032`
- `market_context_high->fx_4h` score `-1.0933` n `132` status `ready` deltaP `-7.8622` edge `-0.0037` maxDD `-1.0574`
- `market_context_high->metal_1h` score `-1.1278` n `136` status `ready` deltaP `-0.9423` edge `-0.0015` maxDD `-7.278`
- `market_context_high->fx_24h` score `-1.1338` n `99` status `ready` deltaP `0.6313` edge `-0.0115` maxDD `-0.6418`
- `market_context_high->index_4h` score `-1.2538` n `132` status `ready` deltaP `10.9341` edge `0.0579` maxDD `-17.6562`
- `market_context_high->crypto_alt_4h` score `-2.8879` n `132` status `ready` deltaP `19.1612` edge `0.3065` maxDD `-58.6918`
- `market_context_high->equity_4h` score `-3.1791` n `132` status `ready` deltaP `8.9431` edge `0.0503` maxDD `-35.3997`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
