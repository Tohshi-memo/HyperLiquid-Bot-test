# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-07T10:07:30.182654+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8718`

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

- `market_context_high->unknown_24h` score `227.1413` n `98` status `ready` deltaP `8.064` edge `18.9127` maxDD `-1.3748`
- `market_context_high->unknown_4h` score `36.1925` n `98` status `ready` deltaP `-3.8514` edge `3.0956` maxDD `-2.3109`
- `news_risk_high->crypto_major_4h` score `10.1178` n `62` status `ready` deltaP `35.3806` edge `0.6276` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `6.8517` n `62` status `ready` deltaP `22.7823` edge `0.5535` maxDD `-6.4195`
- `news_risk_high->index_24h` score `3.5532` n `62` status `ready` deltaP `25.6944` edge `0.1248` maxDD `0.0`
- `market_context_high->crypto_major_4h` score `2.884` n `98` status `ready` deltaP `14.8737` edge `0.2376` maxDD `-4.047`
- `news_risk_high->index_4h` score `2.8566` n `62` status `ready` deltaP `32.0024` edge `0.0509` maxDD `-0.4296`
- `news_risk_high->equity_24h` score `2.6729` n `62` status `ready` deltaP `6.5692` edge `0.1889` maxDD `-0.1298`
- `news_risk_high->crypto_major_1h` score `2.1723` n `62` status `ready` deltaP `8.2287` edge `0.1617` maxDD `-1.5096`
- `news_risk_high->index_1h` score `2.0079` n `62` status `ready` deltaP `25.3236` edge `0.0135` maxDD `-0.1997`
- `news_risk_high->equity_4h` score `1.9443` n `62` status `ready` deltaP `17.9288` edge `0.1023` maxDD `-2.7837`
- `news_risk_high->metal_4h` score `1.4177` n `62` status `ready` deltaP `20.1809` edge `0.0888` maxDD `-0.993`
- `news_risk_high->crypto_alt_1h` score `1.0963` n `62` status `ready` deltaP `3.0085` edge `0.1232` maxDD `-2.4854`
- `market_context_high->crypto_major_24h` score `1.0031` n `98` status `ready` deltaP `5.9524` edge `0.3863` maxDD `-16.7906`
- `market_context_high->fx_1h` score `0.9887` n `98` status `ready` deltaP `15.2114` edge `0.0052` maxDD `-0.271`
- `market_context_high->fx_4h` score `0.625` n `98` status `ready` deltaP `17.0172` edge `0.0143` maxDD `-0.3868`
- `market_context_high->crypto_alt_4h` score `0.5314` n `98` status `ready` deltaP `-3.1888` edge `0.2379` maxDD `-7.1222`
- `news_risk_high->commodity_24h` score `0.4356` n `62` status `ready` deltaP `26.1537` edge `0.0381` maxDD `-8.196`
- `market_context_high->crypto_major_1h` score `0.3396` n `98` status `ready` deltaP `11.0595` edge `0.0587` maxDD `-3.7778`
- `market_context_high->commodity_1h` score `0.198` n `98` status `ready` deltaP `6.7212` edge `0.0093` maxDD `-0.3417`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
