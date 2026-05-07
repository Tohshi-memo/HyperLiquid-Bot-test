# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-07T19:37:14.754389+00:00`
- Price records: `578`
- Market context records: `677`
- Flow alert records: `1919`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `901`

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

- `market_context_high->crypto_major_24h` score `9.2132` n `146` status `ready` deltaP `23.1086` edge `0.6471` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `6.5133` n `146` status `ready` deltaP `8.6512` edge `0.4899` maxDD `-0.0508`
- `market_context_high->fx_4h` score `-0.2177` n `147` status `ready` deltaP `7.0697` edge `0.0121` maxDD `-1.6381`
- `market_context_high->fx_1h` score `-0.3022` n `149` status `ready` deltaP `2.4549` edge `0.0027` maxDD `-0.291`
- `market_context_high->commodity_1h` score `-0.4613` n `149` status `ready` deltaP `2.3266` edge `0.0435` maxDD `-3.7959`
- `market_context_high->index_1h` score `-0.5816` n `149` status `ready` deltaP `0.929` edge `0.0046` maxDD `-2.8282`
- `market_context_high->equity_1h` score `-1.1449` n `149` status `ready` deltaP `-1.4966` edge `-0.0044` maxDD `-4.4826`
- `market_context_high->unknown_1h` score `-1.3374` n `149` status `ready` deltaP `-5.1622` edge `-0.0167` maxDD `-2.1602`
- `market_context_high->crypto_alt_1h` score `-1.4087` n `149` status `ready` deltaP `4.3764` edge `-0.0151` maxDD `-8.1842`
- `market_context_high->index_4h` score `-1.6633` n `147` status `ready` deltaP `2.6187` edge `-0.0038` maxDD `-6.5149`
- `market_context_high->crypto_major_1h` score `-1.6843` n `149` status `ready` deltaP `5.6018` edge `-0.0054` maxDD `-11.4508`
- `market_context_high->crypto_alt_4h` score `-1.7171` n `147` status `ready` deltaP `5.3828` edge `0.078` maxDD `-15.2248`
- `market_context_high->crypto_major_4h` score `-1.7332` n `147` status `ready` deltaP `16.0905` edge `0.1189` maxDD `-22.648`
- `market_context_high->index_24h` score `-2.2112` n `146` status `ready` deltaP `-6.7433` edge `0.0602` maxDD `-5.9609`
- `market_context_high->equity_4h` score `-2.6595` n `147` status `ready` deltaP `-1.5031` edge `0.0036` maxDD `-10.5498`
- `market_context_high->metal_1h` score `-3.3441` n `149` status `ready` deltaP `-4.9423` edge `-0.0498` maxDD `-9.0076`
- `market_context_high->commodity_4h` score `-3.6507` n `147` status `ready` deltaP `-5.4495` edge `0.0822` maxDD `-13.0076`
- `market_context_high->equity_24h` score `-3.7771` n `146` status `ready` deltaP `-8.9671` edge `0.0055` maxDD `-10.5047`
- `market_context_high->unknown_4h` score `-4.5852` n `147` status `ready` deltaP `1.8774` edge `-0.2068` maxDD `-8.3588`
- `market_context_high->fx_24h` score `-4.788` n `146` status `ready` deltaP `-8.8898` edge `-0.0374` maxDD `-21.0414`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
