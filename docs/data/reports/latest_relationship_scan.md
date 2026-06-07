# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-07T07:52:20.440962+00:00`
- Price records: `672`
- Market context records: `3158`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `8852`

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

- `market_context_high->commodity_24h` score `13.9721` n `107` status `ready` deltaP `47.425` edge `0.891` maxDD `-2.0927`
- `market_context_high->crypto_alt_24h` score `12.1066` n `107` status `ready` deltaP `14.9613` edge `2.45` maxDD `-71.142`
- `market_context_high->unknown_24h` score `11.8346` n `107` status `ready` deltaP `21.7078` edge `0.8903` maxDD `-1.9039`
- `market_context_high->index_24h` score `6.4446` n `107` status `ready` deltaP `30.7762` edge `0.8765` maxDD `-16.1026`
- `market_context_high->equity_24h` score `4.899` n `107` status `ready` deltaP `12.9154` edge `1.3836` maxDD `-53.663`
- `market_context_high->commodity_4h` score `2.9069` n `140` status `ready` deltaP `18.7412` edge `0.1631` maxDD `-1.9973`
- `market_context_high->fx_24h` score `0.2158` n `107` status `ready` deltaP `9.607` edge `0.0017` maxDD `-0.4876`
- `market_context_high->commodity_1h` score `0.1706` n `140` status `ready` deltaP `4.136` edge `0.0289` maxDD `-1.7142`
- `market_context_high->crypto_alt_1h` score `-0.4127` n `140` status `ready` deltaP `5.633` edge `0.1225` maxDD `-14.7034`
- `market_context_high->index_1h` score `-0.4941` n `140` status `ready` deltaP `4.0547` edge `0.0159` maxDD `-4.5023`
- `market_context_high->equity_1h` score `-0.9181` n `140` status `ready` deltaP `2.7417` edge `0.0126` maxDD `-8.8863`
- `market_context_high->crypto_major_1h` score `-1.0799` n `140` status `ready` deltaP `2.0017` edge `0.0745` maxDD `-15.1032`
- `market_context_high->index_4h` score `-1.0873` n `140` status `ready` deltaP `13.1707` edge `0.0637` maxDD `-17.6057`
- `market_context_high->unknown_4h` score `-1.0875` n `140` status `ready` deltaP `8.5497` edge `0.0746` maxDD `-14.7778`
- `market_context_high->fx_1h` score `-1.1092` n `140` status `ready` deltaP `-10.3122` edge `-0.0052` maxDD `-0.7941`
- `market_context_high->fx_4h` score `-1.4159` n `140` status `ready` deltaP `-12.818` edge `-0.0076` maxDD `-1.4115`
- `market_context_high->metal_1h` score `-2.1246` n `140` status `ready` deltaP `-4.6322` edge `-0.0068` maxDD `-7.4828`
- `market_context_high->equity_4h` score `-2.9179` n `140` status `ready` deltaP `13.4669` edge `0.0667` maxDD `-36.7784`
- `market_context_high->crypto_alt_4h` score `-2.975` n `140` status `ready` deltaP `19.0897` edge `0.4293` maxDD `-58.6918`
- `market_context_high->unknown_1h` score `-3.2762` n `140` status `ready` deltaP `1.6382` edge `-0.0813` maxDD `-14.2111`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
