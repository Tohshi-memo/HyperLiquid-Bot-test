# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-29T20:52:30.943466+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `6816`

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

- `market_context_high->unknown_24h` score `1614.9647` n `134` status `ready` deltaP `-2.2699` edge `134.6385` maxDD `-1.1049`
- `market_context_high->unknown_4h` score `61.9974` n `134` status `ready` deltaP `5.7517` edge `5.1414` maxDD `-0.3966`
- `market_context_high->index_24h` score `2.2976` n `134` status `ready` deltaP `27.9721` edge `0.0233` maxDD `-0.1315`
- `market_context_high->metal_1h` score `0.2855` n `134` status `ready` deltaP `9.706` edge `0.0098` maxDD `-0.3659`
- `market_context_high->metal_4h` score `0.0823` n `134` status `ready` deltaP `13.087` edge `0.0129` maxDD `-1.8344`
- `market_context_high->commodity_4h` score `0.0454` n `134` status `ready` deltaP `11.4989` edge `0.049` maxDD `-1.0837`
- `market_context_high->fx_1h` score `-0.1182` n `134` status `ready` deltaP `3.28` edge `-0.0012` maxDD `-0.1986`
- `market_context_high->crypto_major_1h` score `-0.2865` n `134` status `ready` deltaP `5.6685` edge `0.0411` maxDD `-5.2213`
- `market_context_high->equity_1h` score `-0.3665` n `134` status `ready` deltaP `1.7875` edge `0.0451` maxDD `-2.3383`
- `market_context_high->commodity_1h` score `-0.411` n `134` status `ready` deltaP `0.5966` edge `0.0132` maxDD `-0.4475`
- `market_context_high->fx_4h` score `-0.5211` n `134` status `ready` deltaP `-0.4732` edge `-0.0038` maxDD `-0.4545`
- `market_context_high->index_1h` score `-0.9924` n `134` status `ready` deltaP `-3.7425` edge `-0.0019` maxDD `-1.1344`
- `market_context_high->crypto_alt_1h` score `-1.0426` n `134` status `ready` deltaP `2.3997` edge `0.0368` maxDD `-8.251`
- `market_context_high->fx_24h` score `-1.097` n `134` status `ready` deltaP `4.4932` edge `0.0117` maxDD `-0.9792`
- `market_context_high->equity_4h` score `-1.473` n `134` status `ready` deltaP `-2.7917` edge `-0.0118` maxDD `-6.008`
- `market_context_high->metal_24h` score `-1.6491` n `134` status `ready` deltaP `3.9257` edge `0.0271` maxDD `-10.5088`
- `market_context_high->equity_24h` score `-2.3931` n `134` status `ready` deltaP `10.4089` edge `0.0069` maxDD `-14.0571`
- `market_context_high->index_4h` score `-2.442` n `134` status `ready` deltaP `-7.1965` edge `-0.0235` maxDD `-3.5621`
- `market_context_high->crypto_major_4h` score `-2.5953` n `134` status `ready` deltaP `4.96` edge `-0.0363` maxDD `-19.0267`
- `market_context_high->commodity_24h` score `-4.3878` n `134` status `ready` deltaP `1.946` edge `-0.0165` maxDD `-24.0547`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
