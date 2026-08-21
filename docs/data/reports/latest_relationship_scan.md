# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-21T11:52:26.484466+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `13758`

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

- `market_context_high->equity_1h` score `0.4389` n `116` status `ready` deltaP `9.4157` edge `0.0553` maxDD `-3.1861`
- `market_context_high->index_1h` score `0.413` n `116` status `ready` deltaP `11.3205` edge `0.0067` maxDD `-0.4869`
- `market_context_high->fx_4h` score `0.15` n `105` status `ready` deltaP `9.1623` edge `0.0084` maxDD `-0.3539`
- `market_context_high->fx_1h` score `-0.0846` n `116` status `ready` deltaP `3.0353` edge `0.0048` maxDD `-0.2043`
- `market_context_high->equity_4h` score `-0.1` n `105` status `ready` deltaP `3.8255` edge `0.1291` maxDD `-8.3685`
- `market_context_high->index_4h` score `-0.2307` n `105` status `ready` deltaP `7.7527` edge `0.0173` maxDD `-1.3899`
- `market_context_high->metal_4h` score `-0.2848` n `105` status `ready` deltaP `6.5302` edge `-0.0207` maxDD `-1.4145`
- `market_context_high->metal_1h` score `-0.3913` n `116` status `ready` deltaP `1.6519` edge `-0.0033` maxDD `-0.5589`
- `market_context_high->unknown_1h` score `-0.4192` n `116` status `ready` deltaP `9.8338` edge `-0.0778` maxDD `-0.4818`
- `market_context_high->commodity_24h` score `-0.4444` n `105` status `ready` deltaP `4.5883` edge `0.1157` maxDD `-4.666`
- `market_context_high->commodity_1h` score `-0.6938` n `116` status `ready` deltaP `-5.0175` edge `0.0011` maxDD `-1.1941`
- `market_context_high->commodity_4h` score `-0.7813` n `105` status `ready` deltaP `-3.1098` edge `0.0056` maxDD `-2.4692`
- `market_context_high->crypto_alt_1h` score `-1.2296` n `116` status `ready` deltaP `-2.0854` edge `-0.0084` maxDD `-2.413`
- `market_context_high->crypto_major_1h` score `-1.2848` n `116` status `ready` deltaP `-3.5154` edge `-0.0568` maxDD `-2.7581`
- `market_context_high->fx_24h` score `-3.1411` n `105` status `ready` deltaP `-13.6905` edge `-0.0095` maxDD `-2.2121`
- `market_context_high->index_24h` score `-3.552` n `105` status `ready` deltaP `-4.0476` edge `-0.0337` maxDD `-15.5764`
- `market_context_high->crypto_alt_4h` score `-3.7346` n `105` status `ready` deltaP `-1.9686` edge `-0.1711` maxDD `-5.4926`
- `market_context_high->crypto_major_4h` score `-4.0163` n `105` status `ready` deltaP `-0.3296` edge `-0.2304` maxDD `-3.1677`
- `market_context_high->unknown_24h` score `-4.5822` n `105` status `ready` deltaP `8.9038` edge `-0.3902` maxDD `-1.0805`
- `market_context_high->metal_24h` score `-4.6269` n `105` status `ready` deltaP `-16.7212` edge `-0.135` maxDD `-12.7373`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
