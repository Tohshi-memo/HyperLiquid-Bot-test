# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-30T12:37:29.686893+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7034`

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

- `market_context_high->unknown_24h` score `1812.3242` n `134` status `ready` deltaP `-2.7908` edge `151.0886` maxDD `-1.1049`
- `news_risk_high->unknown_1h` score `211.9537` n `44` status `ready` deltaP `-3.0348` edge `17.6956` maxDD `-0.3382`
- `market_context_high->unknown_4h` score `32.4291` n `134` status `ready` deltaP `2.7029` edge `2.6977` maxDD `-0.3966`
- `news_risk_high->crypto_alt_4h` score `9.3188` n `32` status `ready` deltaP `28.4299` edge `0.6217` maxDD `-1.4402`
- `market_context_high->index_24h` score `3.2656` n `134` status `ready` deltaP `34.2221` edge `0.0623` maxDD `-0.1315`
- `market_context_high->equity_24h` score `2.5504` n `134` status `ready` deltaP `16.3117` edge `0.3795` maxDD `-14.0571`
- `news_risk_high->crypto_alt_1h` score `1.9392` n `44` status `ready` deltaP `11.1595` edge `0.1289` maxDD `-1.669`
- `news_risk_high->commodity_4h` score `0.5031` n `32` status `ready` deltaP `4.3445` edge `0.0693` maxDD `-0.7008`
- `market_context_high->metal_1h` score `0.3813` n `134` status `ready` deltaP `10.9036` edge `0.0141` maxDD `-0.3659`
- `market_context_high->metal_4h` score `0.3169` n `134` status `ready` deltaP `15.6785` edge `0.0257` maxDD `-1.8344`
- `market_context_high->equity_1h` score `0.1178` n `134` status `ready` deltaP `4.3324` edge `0.0685` maxDD `-2.3383`
- `market_context_high->commodity_4h` score `0.0789` n `134` status `ready` deltaP `12.4135` edge `0.0457` maxDD `-1.0837`
- `market_context_high->crypto_major_1h` score `0.024` n `134` status `ready` deltaP `7.1655` edge `0.057` maxDD `-5.2213`
- `market_context_high->fx_1h` score `-0.1119` n `134` status `ready` deltaP `3.4297` edge `-0.0014` maxDD `-0.1986`
- `market_context_high->equity_4h` score `-0.2796` n `134` status `ready` deltaP `1.9339` edge `0.1097` maxDD `-6.008`
- `news_risk_high->index_1h` score `-0.2867` n `44` status `ready` deltaP `4.2733` edge `-0.0045` maxDD `-0.5267`
- `news_risk_high->metal_4h` score `-0.3016` n `32` status `ready` deltaP `7.4695` edge `-0.0061` maxDD `-1.9226`
- `market_context_high->commodity_1h` score `-0.3619` n `134` status `ready` deltaP `1.3451` edge `0.0123` maxDD `-0.4475`
- `news_risk_high->commodity_1h` score `-0.5328` n `44` status `ready` deltaP `-8.4921` edge `0.0185` maxDD `-0.4158`
- `market_context_high->fx_4h` score `-0.5669` n `134` status `ready` deltaP `-1.2354` edge `-0.0046` maxDD `-0.4545`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
