# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-17T22:07:33.589203+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4053`

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

- `market_context_high->unknown_24h` score `1491.033` n `98` status `ready` deltaP `3.4722` edge `124.2296` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `15.5698` n `98` status `ready` deltaP `46.8856` edge `2.0106` maxDD `-22.8301`
- `market_context_high->crypto_alt_24h` score `14.6831` n `98` status `ready` deltaP `33.1208` edge `1.874` maxDD `-13.3222`
- `market_context_high->metal_1h` score `-0.4852` n `98` status `ready` deltaP `-0.5163` edge `0.0014` maxDD `-2.1461`
- `market_context_high->crypto_alt_4h` score `-0.7517` n `98` status `ready` deltaP `-1.1044` edge `0.192` maxDD `-17.1476`
- `market_context_high->metal_24h` score `-0.8577` n `98` status `ready` deltaP `16.0501` edge `0.144` maxDD `-15.7982`
- `market_context_high->index_1h` score `-1.052` n `98` status `ready` deltaP `-5.0196` edge `-0.0027` maxDD `-1.2295`
- `market_context_high->crypto_alt_1h` score `-1.2531` n `98` status `ready` deltaP `-2.5571` edge `0.0067` maxDD `-7.6911`
- `market_context_high->fx_1h` score `-1.3077` n `98` status `ready` deltaP `-7.9983` edge `-0.001` maxDD `-0.3721`
- `market_context_high->crypto_major_4h` score `-1.3098` n `98` status `ready` deltaP `-3.2977` edge `0.2123` maxDD `-22.3259`
- `market_context_high->metal_4h` score `-1.3982` n `98` status `ready` deltaP `5.3696` edge `-0.0216` maxDD `-6.1238`
- `market_context_high->crypto_major_1h` score `-2.2998` n `98` status `ready` deltaP `-2.4349` edge `0.0113` maxDD `-10.2705`
- `market_context_high->index_4h` score `-2.9107` n `98` status `ready` deltaP `-12.1982` edge `-0.0269` maxDD `-4.7471`
- `market_context_high->commodity_1h` score `-2.9499` n `98` status `ready` deltaP `-15.8224` edge `-0.0356` maxDD `-3.7125`
- `market_context_high->equity_1h` score `-3.5202` n `98` status `ready` deltaP `-1.387` edge `-0.0655` maxDD `-11.1548`
- `market_context_high->fx_4h` score `-4.612` n `98` status `ready` deltaP `-25.4542` edge `-0.0104` maxDD `-2.0058`
- `market_context_high->fx_24h` score `-6.6136` n `98` status `ready` deltaP `-17.5985` edge `-0.0029` maxDD `-5.8059`
- `market_context_high->commodity_4h` score `-7.8329` n `98` status `ready` deltaP `-27.7159` edge `-0.1219` maxDD `-14.6855`
- `market_context_high->index_24h` score `-8.6607` n `98` status `ready` deltaP `-11.0403` edge `-0.1059` maxDD `-20.7114`
- `market_context_high->equity_4h` score `-13.5168` n `98` status `ready` deltaP `-18.8496` edge `-0.3153` maxDD `-44.5018`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
