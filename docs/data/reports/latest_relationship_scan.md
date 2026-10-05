# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-05T06:37:29.232942+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `64`

- Symbol pattern count: `6958`

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

- `market_context_high->unknown_1h` score `90.438` n `113` status `ready` deltaP `1.2996` edge `7.5693` maxDD `-0.9839`
- `market_context_high->unknown_4h` score `63.7903` n `101` status `ready` deltaP `3.2872` edge `5.3251` maxDD `-0.4928`
- `market_context_high->crypto_major_24h` score `10.369` n `70` status `ready` deltaP `29.2212` edge `0.6829` maxDD `-0.423`
- `news_risk_high->crypto_major_4h` score `9.2961` n `65` status `ready` deltaP `32.3992` edge `0.579` maxDD `-0.6258`
- `market_context_high->crypto_alt_24h` score `7.2758` n `70` status `ready` deltaP `24.1617` edge `0.5072` maxDD `-2.9571`
- `news_risk_high->crypto_alt_4h` score `5.8938` n `65` status `ready` deltaP `20.2439` edge `0.4906` maxDD `-6.4195`
- `news_risk_high->equity_24h` score `3.5339` n `65` status `ready` deltaP `13.2906` edge `0.2159` maxDD `-0.1344`
- `news_risk_high->index_24h` score `3.3457` n `65` status `ready` deltaP `23.6111` edge `0.1214` maxDD `0.0`
- `market_context_high->crypto_major_4h` score `3.0402` n `101` status `ready` deltaP `13.3588` edge `0.2409` maxDD `-3.7955`
- `news_risk_high->index_4h` score `2.8853` n `65` status `ready` deltaP `31.7613` edge `0.0549` maxDD `-0.4296`
- `news_risk_high->equity_4h` score `2.5458` n `65` status `ready` deltaP `20.4245` edge `0.137` maxDD `-2.881`
- `news_risk_high->crypto_major_1h` score `2.4988` n `65` status `ready` deltaP `10.1658` edge `0.176` maxDD `-1.5096`
- `news_risk_high->index_1h` score `2.0722` n `65` status `ready` deltaP `25.6172` edge `0.0169` maxDD `-0.1997`
- `news_risk_high->metal_4h` score `1.9609` n `65` status `ready` deltaP `18.1637` edge `0.0839` maxDD `-0.993`
- `market_context_high->fx_4h` score `1.2465` n `101` status `ready` deltaP `23.0469` edge `0.0259` maxDD `-0.3868`
- `news_risk_high->crypto_alt_1h` score `1.2069` n `65` status `ready` deltaP `3.8208` edge `0.127` maxDD `-2.4854`
- `market_context_high->crypto_major_1h` score `0.796` n `113` status `ready` deltaP `10.3837` edge `0.086` maxDD `-3.7778`
- `news_risk_high->commodity_24h` score `0.526` n `65` status `ready` deltaP `24.5646` edge `0.1068` maxDD `-10.9169`
- `market_context_high->fx_1h` score `0.4875` n `113` status `ready` deltaP `12.8981` edge `0.0049` maxDD `-0.271`
- `market_context_high->equity_24h` score `0.4638` n `70` status `ready` deltaP `5.1587` edge `0.0245` maxDD `-0.6196`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
