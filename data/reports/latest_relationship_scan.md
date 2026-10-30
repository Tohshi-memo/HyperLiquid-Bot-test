# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-30T11:22:29.405358+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7046`

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

- `market_context_high->unknown_24h` score `1794.5246` n `134` status `ready` deltaP `-2.7908` edge `149.6053` maxDD `-1.1049`
- `news_risk_high->unknown_1h` score `222.642` n `39` status `ready` deltaP `-2.5103` edge `18.5828` maxDD `-0.3382`
- `market_context_high->unknown_4h` score `34.3033` n `134` status `ready` deltaP `3.4651` edge `2.8488` maxDD `-0.3966`
- `market_context_high->index_24h` score `3.1645` n `134` status `ready` deltaP `33.5277` edge `0.0585` maxDD `-0.1315`
- `news_risk_high->crypto_alt_1h` score `2.5785` n `39` status `ready` deltaP `15.7301` edge `0.1517` maxDD `-1.669`
- `market_context_high->equity_24h` score `2.1772` n `134` status `ready` deltaP `16.3117` edge `0.3484` maxDD `-14.0571`
- `market_context_high->metal_1h` score `0.3688` n `134` status `ready` deltaP `10.7539` edge `0.0135` maxDD `-0.3659`
- `market_context_high->metal_4h` score `0.2932` n `134` status `ready` deltaP `15.3736` edge `0.0247` maxDD `-1.8344`
- `news_risk_high->index_1h` score `0.2932` n `39` status `ready` deltaP `11.5577` edge `-0.0013` maxDD `-0.3858`
- `market_context_high->equity_1h` score `0.1118` n `134` status `ready` deltaP `4.3324` edge `0.068` maxDD `-2.3383`
- `market_context_high->commodity_4h` score `0.0741` n `134` status `ready` deltaP `12.4135` edge `0.0453` maxDD `-1.0837`
- `market_context_high->crypto_major_1h` score `-0.0407` n `134` status `ready` deltaP `6.7164` edge `0.0546` maxDD `-5.2213`
- `market_context_high->fx_1h` score `-0.1213` n `134` status `ready` deltaP `3.28` edge `-0.0016` maxDD `-0.1986`
- `news_risk_high->commodity_1h` score `-0.2016` n `39` status `ready` deltaP `-3.5468` edge `0.028` maxDD `-0.4158`
- `market_context_high->commodity_1h` score `-0.3871` n `134` status `ready` deltaP `1.0457` edge `0.0122` maxDD `-0.4475`
- `market_context_high->equity_4h` score `-0.3941` n `134` status `ready` deltaP `1.1717` edge `0.1001` maxDD `-6.008`
- `news_risk_high->fx_1h` score `-0.5355` n `39` status `ready` deltaP `-2.4797` edge `-0.0007` maxDD `-0.1142`
- `market_context_high->fx_4h` score `-0.6097` n `134` status `ready` deltaP `-1.9976` edge `-0.005` maxDD `-0.4545`
- `market_context_high->crypto_alt_1h` score `-0.8719` n `134` status `ready` deltaP `2.6991` edge `0.0567` maxDD `-8.251`
- `market_context_high->index_1h` score `-0.8762` n `134` status `ready` deltaP `-2.5449` edge `-0.0002` maxDD `-1.1344`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
