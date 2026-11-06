# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-06T23:37:27.443975+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4148`

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

- `news_risk_high->equity_4h` score `1.0396` n `76` status `ready` deltaP `8.9618` edge `0.1641` maxDD `-4.2454`
- `news_risk_high->index_4h` score `0.2705` n `76` status `ready` deltaP `9.6678` edge `0.018` maxDD `-0.4888`
- `news_risk_high->index_1h` score `0.1591` n `76` status `ready` deltaP `9.2735` edge `0.0039` maxDD `-0.2931`
- `news_risk_high->equity_1h` score `0.1472` n `76` status `ready` deltaP `3.1989` edge `0.0525` maxDD `-1.396`
- `news_risk_high->fx_4h` score `0.0354` n `76` status `ready` deltaP `6.948` edge `0.0028` maxDD `-0.2336`
- `news_risk_high->index_24h` score `0.0243` n `76` status `ready` deltaP `4.2489` edge `0.1416` maxDD `-6.6786`
- `news_risk_high->fx_24h` score `-0.1966` n `76` status `ready` deltaP `-1.8641` edge `0.0403` maxDD `-0.2073`
- `news_risk_high->fx_1h` score `-0.2855` n `76` status `ready` deltaP `1.9382` edge `0.0019` maxDD `-0.0888`
- `news_risk_high->metal_1h` score `-0.45` n `76` status `ready` deltaP `-2.3637` edge `-0.0062` maxDD `-0.5256`
- `news_risk_high->crypto_major_1h` score `-1.0013` n `76` status `ready` deltaP `-3.8843` edge `-0.0086` maxDD `-4.1772`
- `news_risk_high->crypto_alt_1h` score `-1.2715` n `76` status `ready` deltaP `-2.1195` edge `-0.0261` maxDD `-5.8225`
- `news_risk_high->metal_4h` score `-1.3053` n `76` status `ready` deltaP `-5.6402` edge `-0.0392` maxDD `-1.5773`
- `news_risk_high->crypto_major_4h` score `-2.487` n `76` status `ready` deltaP `-5.8568` edge `0.0004` maxDD `-9.1553`
- `news_risk_high->equity_24h` score `-2.8061` n `76` status `ready` deltaP `22.5878` edge `0.6483` maxDD `-86.0244`
- `news_risk_high->commodity_1h` score `-2.9583` n `76` status `ready` deltaP `-18.3029` edge `-0.0076` maxDD `-1.6855`
- `news_risk_high->metal_24h` score `-3.2445` n `76` status `ready` deltaP `0.7859` edge `-0.2316` maxDD `-8.5019`
- `news_risk_high->commodity_4h` score `-3.992` n `76` status `ready` deltaP `-25.706` edge `-0.0015` maxDD `-4.1171`
- `news_risk_high->crypto_alt_4h` score `-4.6955` n `76` status `ready` deltaP `-9.3068` edge `-0.0656` maxDD `-14.0916`
- `news_risk_high->commodity_24h` score `-9.5801` n `76` status `ready` deltaP `-26.3798` edge `-0.0544` maxDD `-28.1127`
- `news_risk_high->crypto_major_24h` score `-12.9879` n `76` status `ready` deltaP `-29.9707` edge `-0.0322` maxDD `-50.6925`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
