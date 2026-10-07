# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-07T09:52:30.534684+00:00`
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

- `market_context_high->unknown_24h` score `297.3434` n `99` status `ready` deltaP `8.2702` edge `24.7615` maxDD `-1.3748`
- `market_context_high->unknown_4h` score `35.6946` n `99` status `ready` deltaP `-3.6246` edge `3.0526` maxDD `-2.3109`
- `news_risk_high->crypto_major_4h` score `10.0696` n `62` status `ready` deltaP `35.2282` edge `0.6246` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `6.8083` n `62` status `ready` deltaP `22.6299` edge `0.5509` maxDD `-6.4195`
- `news_risk_high->index_24h` score `3.5496` n `62` status `ready` deltaP `25.6944` edge `0.1245` maxDD `0.0`
- `market_context_high->crypto_major_4h` score `2.9465` n `99` status `ready` deltaP `15.0099` edge `0.2419` maxDD `-4.047`
- `news_risk_high->index_4h` score `2.8566` n `62` status `ready` deltaP `32.0024` edge `0.0509` maxDD `-0.4296`
- `news_risk_high->equity_24h` score `2.6374` n `62` status `ready` deltaP `6.3956` edge `0.1871` maxDD `-0.1298`
- `news_risk_high->crypto_major_1h` score `2.1423` n `62` status `ready` deltaP `8.079` edge `0.1602` maxDD `-1.5096`
- `news_risk_high->index_1h` score `2.0079` n `62` status `ready` deltaP `25.3236` edge `0.0135` maxDD `-0.1997`
- `news_risk_high->equity_4h` score `1.9383` n `62` status `ready` deltaP `17.9288` edge `0.1018` maxDD `-2.7837`
- `news_risk_high->metal_4h` score `1.4177` n `62` status `ready` deltaP `20.1809` edge `0.0888` maxDD `-0.993`
- `news_risk_high->crypto_alt_1h` score `1.0651` n `62` status `ready` deltaP `2.8588` edge `0.1216` maxDD `-2.4854`
- `market_context_high->fx_1h` score `1.0076` n `99` status `ready` deltaP `15.4328` edge `0.0053` maxDD `-0.271`
- `market_context_high->crypto_major_24h` score `0.9606` n `99` status `ready` deltaP `6.1396` edge `0.3796` maxDD `-16.7906`
- `market_context_high->fx_4h` score `0.6501` n `99` status `ready` deltaP `17.2564` edge `0.0148` maxDD `-0.3868`
- `market_context_high->crypto_alt_4h` score `0.5727` n `99` status `ready` deltaP `-2.867` edge `0.2392` maxDD `-7.1222`
- `news_risk_high->commodity_24h` score `0.4488` n `62` status `ready` deltaP `26.1537` edge `0.0398` maxDD `-8.196`
- `market_context_high->crypto_major_1h` score `0.3544` n `99` status `ready` deltaP `11.2397` edge `0.0594` maxDD `-3.7778`
- `market_context_high->commodity_1h` score `0.2491` n `99` status `ready` deltaP `7.1645` edge `0.0106` maxDD `-0.3417`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
