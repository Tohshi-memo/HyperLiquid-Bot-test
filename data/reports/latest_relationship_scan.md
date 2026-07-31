# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-31T13:52:36.856216+00:00`
- Price records: `672`
- Market context records: `8520`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5882`

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

- `news_risk_high->unknown_24h` score `6278.6721` n `52` status `ready` deltaP `44.7383` edge `522.9665` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `5.4642` n `64` status `ready` deltaP `21.1128` edge `0.3743` maxDD `-3.4427`
- `news_risk_high->index_4h` score `1.9721` n `64` status `ready` deltaP `16.3491` edge `0.0744` maxDD `-0.191`
- `news_risk_high->equity_1h` score `1.6678` n `64` status `ready` deltaP `15.8028` edge `0.0813` maxDD `-2.4803`
- `market_context_high->crypto_alt_4h` score `1.0961` n `36` status `ready` deltaP `12.6355` edge `0.1311` maxDD `-3.9846`
- `market_context_high->crypto_major_4h` score `1.005` n `36` status `ready` deltaP `8.6721` edge `0.1444` maxDD `-2.8692`
- `news_risk_high->crypto_major_4h` score `0.7968` n `64` status `ready` deltaP `5.3735` edge `0.1439` maxDD `-3.5385`
- `news_risk_high->crypto_alt_4h` score `0.7411` n `64` status `ready` deltaP `14.0244` edge `0.1407` maxDD `-5.8012`
- `market_context_high->equity_4h` score `0.6812` n `36` status `ready` deltaP `20.7656` edge `0.0272` maxDD `-3.9308`
- `news_risk_high->crypto_alt_1h` score `0.5077` n `64` status `ready` deltaP `9.0101` edge `0.0577` maxDD `-1.8813`
- `news_risk_high->crypto_major_1h` score `0.276` n `64` status `ready` deltaP `6.1658` edge `0.0455` maxDD `-2.0972`
- `news_risk_high->fx_1h` score `0.1049` n `64` status `ready` deltaP `5.5857` edge `0.0043` maxDD `-0.2475`
- `market_context_high->fx_4h` score `0.0939` n `36` status `ready` deltaP `7.1307` edge `0.014` maxDD `-0.2932`
- `news_risk_high->index_1h` score `0.0441` n `64` status `ready` deltaP `4.3694` edge `0.0082` maxDD `-0.5338`
- `news_risk_high->fx_4h` score `0.0194` n `64` status `ready` deltaP `11.471` edge `0.0209` maxDD `-0.6604`
- `news_risk_high->metal_4h` score `0.01` n `64` status `ready` deltaP `2.1723` edge `0.0344` maxDD `-0.8085`
- `market_context_high->commodity_1h` score `-0.0484` n `48` status `ready` deltaP `6.5619` edge `0.0126` maxDD `-2.0038`
- `news_risk_high->metal_1h` score `-0.1131` n `64` status `ready` deltaP `3.4057` edge `0.0082` maxDD `-0.5599`
- `market_context_high->index_4h` score `-0.1461` n `36` status `ready` deltaP `3.6755` edge `-0.0008` maxDD `-0.7282`
- `market_context_high->crypto_major_1h` score `-0.3248` n `48` status `ready` deltaP `2.52` edge `-0.0087` maxDD `-1.9791`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
