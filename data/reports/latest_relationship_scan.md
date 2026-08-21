# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-21T19:09:48.980486+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `13790`

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

- `market_context_high->unknown_1h` score `1.2756` n `133` status `ready` deltaP `8.5375` edge `0.0721` maxDD `-0.4843`
- `market_context_high->fx_4h` score `0.1896` n `132` status `ready` deltaP `9.7145` edge `0.0098` maxDD `-0.3539`
- `market_context_high->index_1h` score `0.1818` n `133` status `ready` deltaP `10.7559` edge `0.0047` maxDD `-0.9144`
- `market_context_high->unknown_4h` score `-0.0403` n `132` status `ready` deltaP `21.129` edge `-0.1003` maxDD `-0.5133`
- `market_context_high->fx_1h` score `-0.1323` n `133` status `ready` deltaP `2.1791` edge `0.0044` maxDD `-0.2043`
- `market_context_high->equity_1h` score `-0.2217` n `133` status `ready` deltaP `6.5643` edge `0.0348` maxDD `-5.2257`
- `market_context_high->metal_1h` score `-0.3604` n `133` status `ready` deltaP `0.233` edge `-0.0059` maxDD `-0.6822`
- `market_context_high->metal_4h` score `-0.5057` n `132` status `ready` deltaP `2.9795` edge `-0.0231` maxDD `-1.5942`
- `market_context_high->index_4h` score `-0.6316` n `132` status `ready` deltaP `1.9632` edge `0.0095` maxDD `-2.618`
- `market_context_high->commodity_4h` score `-0.6556` n `132` status `ready` deltaP `-0.9932` edge `0.0076` maxDD `-2.4692`
- `market_context_high->crypto_alt_1h` score `-0.6704` n `133` status `ready` deltaP `0.4199` edge `0.0215` maxDD `-2.413`
- `market_context_high->commodity_1h` score `-0.6869` n `133` status `ready` deltaP `-4.7206` edge `0.0` maxDD `-1.1941`
- `market_context_high->commodity_24h` score `-0.8722` n `105` status `ready` deltaP `1.1161` edge `0.1032` maxDD `-4.666`
- `market_context_high->crypto_major_1h` score `-1.1944` n `133` status `ready` deltaP `-1.2505` edge `-0.0423` maxDD `-4.1996`
- `market_context_high->crypto_alt_4h` score `-1.3165` n `132` status `ready` deltaP `3.3721` edge `-0.0052` maxDD `-5.4926`
- `market_context_high->equity_4h` score `-1.8648` n `132` status `ready` deltaP `-2.319` edge `0.0569` maxDD `-16.1079`
- `market_context_high->fx_24h` score `-2.6423` n `105` status `ready` deltaP `-8.6558` edge `-0.0015` maxDD `-2.2121`
- `market_context_high->crypto_major_4h` score `-3.9293` n `132` status `ready` deltaP `-0.3973` edge `-0.2227` maxDD `-3.1677`
- `market_context_high->index_24h` score `-4.2581` n `105` status `ready` deltaP `-6.4633` edge `-0.0526` maxDD `-18.6848`
- `market_context_high->metal_24h` score `-4.7615` n `105` status `ready` deltaP `-18.4574` edge `-0.1566` maxDD `-11.4635`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
