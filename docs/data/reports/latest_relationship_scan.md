# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-24T22:37:15.863000+00:00`
- Price records: `672`
- Market context records: `1784`
- Flow alert records: `7031`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8882`

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

- `market_context_high->metal_24h` score `7.1446` n `185` status `ready` deltaP `28.2282` edge `0.6498` maxDD `-12.7414`
- `news_risk_high->commodity_4h` score `6.0372` n `30` status `ready` deltaP `27.5813` edge `0.3847` maxDD `-3.5713`
- `market_context_high->crypto_alt_4h` score `5.8668` n `194` status `ready` deltaP `21.7076` edge `0.5208` maxDD `-9.1295`
- `market_context_high->crypto_major_4h` score `4.4716` n `194` status `ready` deltaP `22.935` edge `0.4603` maxDD `-10.9117`
- `market_context_high->unknown_4h` score `3.7152` n `194` status `ready` deltaP `15.6022` edge `0.4327` maxDD `-11.1695`
- `market_context_high->index_24h` score `3.1421` n `185` status `ready` deltaP `16.0164` edge `0.2779` maxDD `-4.1604`
- `news_risk_high->commodity_1h` score `3.1187` n `30` status `ready` deltaP `24.1218` edge `0.1308` maxDD `-1.2043`
- `market_context_high->equity_4h` score `3.0563` n `194` status `ready` deltaP `16.6269` edge `0.2533` maxDD `-5.0894`
- `market_context_high->equity_24h` score `1.9304` n `185` status `ready` deltaP `16.036` edge `0.5438` maxDD `-33.1875`
- `market_context_high->unknown_24h` score `1.4512` n `185` status `ready` deltaP `13.3014` edge `0.5643` maxDD `-35.8966`
- `market_context_high->index_4h` score `0.9295` n `194` status `ready` deltaP `12.4591` edge `0.1033` maxDD `-3.7119`
- `news_risk_high->fx_4h` score `0.8079` n `30` status `ready` deltaP `20.2643` edge `-0.0043` maxDD `-0.1774`
- `market_context_high->crypto_alt_1h` score `0.5663` n `197` status `ready` deltaP `7.653` edge `0.1064` maxDD `-4.8183`
- `news_risk_high->unknown_4h` score `0.5242` n `30` status `ready` deltaP `10.8943` edge `0.0669` maxDD `-2.7857`
- `market_context_high->crypto_major_1h` score `0.1533` n `197` status `ready` deltaP `4.6985` edge `0.0888` maxDD `-3.9211`
- `market_context_high->equity_1h` score `0.0668` n `197` status `ready` deltaP `5.0427` edge `0.0528` maxDD `-2.8014`
- `market_context_high->index_1h` score `-0.1704` n `197` status `ready` deltaP `4.1514` edge `0.0213` maxDD `-1.7205`
- `market_context_high->metal_4h` score `-0.2255` n `194` status `ready` deltaP `13.017` edge `0.1535` maxDD `-12.5349`
- `news_risk_high->unknown_1h` score `-0.4216` n `30` status `ready` deltaP `17.1557` edge `-0.1212` maxDD `-2.1115`
- `market_context_high->fx_24h` score `-0.4253` n `185` status `ready` deltaP `8.5745` edge `0.0123` maxDD `-1.3925`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
