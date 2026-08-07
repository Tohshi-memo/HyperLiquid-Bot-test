# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-07T19:52:30.163016+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11773`

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

- `market_context_high->equity_24h` score `4.8235` n `91` status `ready` deltaP `-0.098` edge `0.7086` maxDD `-21.1456`
- `market_context_high->metal_24h` score `3.5049` n `91` status `ready` deltaP `15.1151` edge `0.2489` maxDD `-2.2743`
- `market_context_high->fx_24h` score `1.7273` n `91` status `ready` deltaP `26.9976` edge `0.0604` maxDD `-2.3821`
- `market_context_high->commodity_4h` score `1.5203` n `109` status `ready` deltaP `15.5977` edge `0.09` maxDD `-2.7169`
- `market_context_high->index_24h` score `1.2701` n `91` status `ready` deltaP `11.7373` edge `0.1789` maxDD `-5.7715`
- `market_context_high->commodity_1h` score `0.8668` n `113` status `ready` deltaP `11.8104` edge `0.0304` maxDD `-0.9524`
- `market_context_high->fx_1h` score `-0.1297` n `113` status `ready` deltaP `6.0516` edge `-0.0016` maxDD `-0.9639`
- `market_context_high->fx_4h` score `-0.1706` n `109` status `ready` deltaP `7.0163` edge `0.006` maxDD `-1.6928`
- `market_context_high->equity_1h` score `-0.2234` n `113` status `ready` deltaP `5.6463` edge `0.0266` maxDD `-4.6286`
- `market_context_high->index_1h` score `-0.3428` n `113` status `ready` deltaP `-0.9578` edge `-0.0028` maxDD `-0.7809`
- `market_context_high->index_4h` score `-0.3568` n `109` status `ready` deltaP `2.1551` edge `0.0004` maxDD `-1.1743`
- `market_context_high->equity_4h` score `-0.8123` n `109` status `ready` deltaP `8.5855` edge `0.0088` maxDD `-7.6983`
- `market_context_high->metal_1h` score `-0.8887` n `113` status `ready` deltaP `-3.1768` edge `-0.0033` maxDD `-0.9664`
- `market_context_high->metal_4h` score `-0.9118` n `109` status `ready` deltaP `3.7047` edge `0.0002` maxDD `-2.7373`
- `market_context_high->crypto_alt_1h` score `-1.3491` n `113` status `ready` deltaP `-5.6555` edge `-0.0118` maxDD `-2.3669`
- `market_context_high->crypto_major_1h` score `-2.3964` n `113` status `ready` deltaP `-6.7869` edge `-0.0477` maxDD `-5.2071`
- `market_context_high->crypto_alt_4h` score `-2.7253` n `109` status `ready` deltaP `-2.4376` edge `-0.0552` maxDD `-5.7857`
- `market_context_high->crypto_major_24h` score `-3.8598` n `91` status `ready` deltaP `4.2863` edge `-0.1008` maxDD `-14.2873`
- `market_context_high->crypto_alt_24h` score `-4.716` n `91` status `ready` deltaP `-17.3694` edge `-0.1329` maxDD `-4.5445`
- `market_context_high->crypto_major_4h` score `-6.7817` n `109` status `ready` deltaP `-8.4135` edge `-0.1802` maxDD `-18.3083`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
