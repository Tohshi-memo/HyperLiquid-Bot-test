# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-29T12:22:30.521060+00:00`
- Price records: `672`
- Market context records: `5143`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5596`

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

- `market_context_high->unknown_24h` score `25.7994` n `68` status `ready` deltaP `31.5462` edge `1.9739` maxDD `-1.4072`
- `market_context_high->unknown_4h` score `6.6393` n `126` status `ready` deltaP `18.9896` edge `0.5289` maxDD `-5.5109`
- `market_context_high->unknown_1h` score `6.0243` n `138` status `ready` deltaP `9.8217` edge `0.5007` maxDD `-2.7986`
- `market_context_high->crypto_alt_4h` score `4.9267` n `126` status `ready` deltaP `15.0116` edge `0.4704` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `3.6311` n `126` status `ready` deltaP `12.9356` edge `0.4456` maxDD `-14.0065`
- `market_context_high->equity_4h` score `0.9887` n `126` status `ready` deltaP `10.1336` edge `0.1787` maxDD `-7.4425`
- `market_context_high->crypto_alt_1h` score `0.8476` n `138` status `ready` deltaP `5.7429` edge `0.1285` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `0.8288` n `138` status `ready` deltaP `8.1619` edge `0.1392` maxDD `-6.9639`
- `market_context_high->commodity_24h` score `0.7644` n `68` status `ready` deltaP `15.6862` edge `0.1167` maxDD `-5.1955`
- `market_context_high->equity_1h` score `0.7069` n `138` status `ready` deltaP `7.5935` edge `0.0676` maxDD `-2.745`
- `market_context_high->crypto_alt_24h` score `0.5087` n `68` status `ready` deltaP `17.1977` edge `0.5729` maxDD `-46.2794`
- `market_context_high->index_1h` score `0.0` n `138` status `ready` deltaP `5.3957` edge `0.0144` maxDD `-1.0296`
- `market_context_high->metal_1h` score `-0.0499` n `138` status `ready` deltaP `5.0659` edge `0.0164` maxDD `-1.8592`
- `market_context_high->crypto_major_24h` score `-0.0943` n `68` status `ready` deltaP `15.5638` edge `0.5723` maxDD `-48.0465`
- `market_context_high->metal_24h` score `-0.3515` n `68` status `ready` deltaP `-1.8587` edge `0.1714` maxDD `-10.0641`
- `market_context_high->index_4h` score `-0.3588` n `126` status `ready` deltaP `6.7702` edge `0.0367` maxDD `-2.9391`
- `market_context_high->fx_24h` score `-0.465` n `68` status `ready` deltaP `4.4015` edge `0.0009` maxDD `-0.8549`
- `market_context_high->fx_1h` score `-0.5694` n `138` status `ready` deltaP `-1.126` edge `-0.0014` maxDD `-0.7944`
- `market_context_high->commodity_1h` score `-0.5895` n `138` status `ready` deltaP `0.3233` edge `-0.0008` maxDD `-2.155`
- `market_context_high->fx_4h` score `-0.8767` n `126` status `ready` deltaP `-1.0356` edge `0.0013` maxDD `-1.8772`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
