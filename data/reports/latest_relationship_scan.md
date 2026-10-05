# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-05T07:37:27.757904+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `64`

- Symbol pattern count: `6964`

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

- `market_context_high->unknown_1h` score `83.7436` n `117` status `ready` deltaP `1.1695` edge `7.0123` maxDD `-0.9839`
- `market_context_high->unknown_4h` score `57.8551` n `105` status `ready` deltaP `2.1777` edge `4.8379` maxDD `-0.4928`
- `market_context_high->crypto_major_24h` score `10.5676` n `74` status `ready` deltaP `29.4528` edge `0.6979` maxDD `-0.423`
- `news_risk_high->crypto_major_4h` score `9.3191` n `65` status `ready` deltaP `32.5516` edge `0.5799` maxDD `-0.6258`
- `market_context_high->crypto_alt_24h` score `7.1126` n `74` status `ready` deltaP `24.4323` edge `0.4918` maxDD `-2.9571`
- `news_risk_high->crypto_alt_4h` score `5.8104` n `65` status `ready` deltaP `19.7866` edge `0.4867` maxDD `-6.4195`
- `news_risk_high->equity_24h` score `3.3763` n `65` status `ready` deltaP `12.5962` edge `0.2074` maxDD `-0.1344`
- `news_risk_high->index_24h` score `3.3433` n `65` status `ready` deltaP `23.6111` edge `0.1212` maxDD `0.0`
- `market_context_high->crypto_major_4h` score `2.9563` n `105` status `ready` deltaP `13.5772` edge `0.2356` maxDD `-4.047`
- `news_risk_high->index_4h` score `2.8731` n `65` status `ready` deltaP `31.6088` edge `0.0549` maxDD `-0.4296`
- `news_risk_high->equity_4h` score `2.5048` n `65` status `ready` deltaP `20.272` edge `0.1346` maxDD `-2.881`
- `news_risk_high->crypto_major_1h` score `2.4209` n `65` status `ready` deltaP `9.7167` edge `0.1725` maxDD `-1.5096`
- `news_risk_high->index_1h` score `2.0602` n `65` status `ready` deltaP `25.4675` edge `0.0169` maxDD `-0.1997`
- `news_risk_high->metal_4h` score `1.927` n `65` status `ready` deltaP `17.8588` edge `0.0831` maxDD `-0.993`
- `market_context_high->fx_4h` score `1.2376` n `105` status `ready` deltaP `23.0705` edge `0.025` maxDD `-0.3868`
- `news_risk_high->crypto_alt_1h` score `1.0762` n `65` status `ready` deltaP `3.222` edge `0.1201` maxDD `-2.4854`
- `market_context_high->crypto_major_1h` score `0.9517` n `117` status `ready` deltaP `11.0843` edge `0.0943` maxDD `-3.7778`
- `news_risk_high->commodity_24h` score `0.5695` n `65` status `ready` deltaP `25.0855` edge `0.1089` maxDD `-10.9169`
- `market_context_high->fx_1h` score `0.4999` n `117` status `ready` deltaP `13.166` edge `0.0047` maxDD `-0.271`
- `market_context_high->equity_24h` score `0.2672` n `74` status `ready` deltaP `5.2365` edge `0.0076` maxDD `-0.6196`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
