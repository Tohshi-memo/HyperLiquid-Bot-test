# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-31T14:07:25.882912+00:00`
- Price records: `672`
- Market context records: `8521`
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

- `news_risk_high->unknown_24h` score `6278.9241` n `52` status `ready` deltaP `44.7383` edge `522.9875` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `5.4762` n `64` status `ready` deltaP `21.1128` edge `0.3753` maxDD `-3.4427`
- `news_risk_high->index_4h` score `1.9769` n `64` status `ready` deltaP `16.3491` edge `0.0748` maxDD `-0.191`
- `news_risk_high->equity_1h` score `1.6738` n `64` status `ready` deltaP `15.8028` edge `0.0818` maxDD `-2.4803`
- `market_context_high->crypto_alt_4h` score `0.8569` n `37` status `ready` deltaP `11.1363` edge `0.1141` maxDD `-4.279`
- `news_risk_high->crypto_major_4h` score `0.8015` n `64` status `ready` deltaP `5.3735` edge `0.1445` maxDD `-3.5385`
- `news_risk_high->crypto_alt_4h` score `0.7576` n `64` status `ready` deltaP `14.1768` edge `0.1418` maxDD `-5.8012`
- `market_context_high->crypto_major_4h` score `0.7048` n `37` status `ready` deltaP `7.0205` edge `0.1225` maxDD `-3.3158`
- `news_risk_high->crypto_alt_1h` score `0.5131` n `64` status `ready` deltaP `9.0101` edge `0.0584` maxDD `-1.8813`
- `news_risk_high->crypto_major_1h` score `0.2799` n `64` status `ready` deltaP `6.1658` edge `0.046` maxDD `-2.0972`
- `news_risk_high->fx_1h` score `0.115` n `64` status `ready` deltaP `5.7354` edge `0.0046` maxDD `-0.2475`
- `news_risk_high->index_1h` score `0.0457` n `64` status `ready` deltaP `4.3694` edge `0.0084` maxDD `-0.5338`
- `news_risk_high->metal_4h` score `0.0241` n `64` status `ready` deltaP `2.3247` edge `0.0352` maxDD `-0.8085`
- `news_risk_high->fx_4h` score `0.0218` n `64` status `ready` deltaP `11.471` edge `0.0211` maxDD `-0.6604`
- `market_context_high->fx_4h` score `-0.0188` n `37` status `ready` deltaP `5.8544` edge `0.0094` maxDD `-0.4004`
- `news_risk_high->metal_1h` score `-0.0964` n `64` status `ready` deltaP `3.5554` edge `0.0086` maxDD `-0.5599`
- `market_context_high->commodity_1h` score `-0.1269` n `49` status `ready` deltaP `5.4564` edge `0.0099` maxDD `-2.0038`
- `market_context_high->equity_4h` score `-0.2387` n `37` status `ready` deltaP `18.6635` edge `-0.0411` maxDD `-6.4471`
- `market_context_high->index_4h` score `-0.348` n `37` status `ready` deltaP `1.9488` edge `-0.0105` maxDD `-1.1016`
- `market_context_high->metal_4h` score `-0.5988` n `37` status `ready` deltaP `6.6744` edge `-0.0346` maxDD `-2.2668`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
