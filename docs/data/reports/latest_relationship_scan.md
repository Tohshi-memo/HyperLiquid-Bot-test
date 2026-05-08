# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-08T01:52:14.461391+00:00`
- Price records: `603`
- Market context records: `707`
- Flow alert records: `1997`
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

- `market_context_high->crypto_major_24h` score `10.9073` n `146` status `ready` deltaP `26.4948` edge `0.7657` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `6.5196` n `146` status `ready` deltaP `8.1908` edge `0.4935` maxDD `-0.0508`
- `market_context_high->fx_4h` score `-0.2296` n `149` status `ready` deltaP `6.9462` edge `0.0114` maxDD `-1.6381`
- `market_context_high->fx_1h` score `-0.2822` n `149` status `ready` deltaP `2.9282` edge `0.0021` maxDD `-0.291`
- `market_context_high->commodity_1h` score `-0.4643` n `149` status `ready` deltaP `2.4387` edge `0.0425` maxDD `-3.7959`
- `market_context_high->index_1h` score `-0.6341` n `149` status `ready` deltaP `0.2346` edge `0.0025` maxDD `-2.8282`
- `market_context_high->index_24h` score `-1.038` n `146` status `ready` deltaP `-2.8337` edge `0.1319` maxDD `-5.9609`
- `market_context_high->crypto_major_4h` score `-1.1291` n `149` status `ready` deltaP `16.296` edge `0.1172` maxDD `-22.648`
- `market_context_high->unknown_1h` score `-1.1913` n `149` status `ready` deltaP `-4.2655` edge `-0.0105` maxDD `-2.1602`
- `market_context_high->equity_1h` score `-1.2087` n `149` status `ready` deltaP `-1.9492` edge `-0.0067` maxDD `-4.4826`
- `market_context_high->crypto_alt_1h` score `-1.3659` n `149` status `ready` deltaP `4.6565` edge `-0.0134` maxDD `-8.1842`
- `market_context_high->crypto_major_1h` score `-1.6056` n `149` status `ready` deltaP `6.1355` edge `-0.0024` maxDD `-11.4508`
- `market_context_high->index_4h` score `-1.708` n `149` status `ready` deltaP `2.1804` edge `-0.0046` maxDD `-6.5149`
- `market_context_high->crypto_alt_4h` score `-1.9934` n `149` status `ready` deltaP `3.8496` edge `0.0652` maxDD `-15.2248`
- `market_context_high->equity_24h` score `-2.1386` n `146` status `ready` deltaP `-4.7768` edge `0.1141` maxDD `-10.5047`
- `market_context_high->equity_4h` score `-2.6166` n `149` status `ready` deltaP `-0.9071` edge `0.0032` maxDD `-10.5498`
- `market_context_high->metal_1h` score `-3.3952` n `149` status `ready` deltaP `-5.2503` edge `-0.052` maxDD `-9.0076`
- `market_context_high->commodity_4h` score `-3.8078` n `149` status `ready` deltaP `-6.4535` edge `0.0758` maxDD `-13.0076`
- `market_context_high->unknown_4h` score `-4.2677` n `149` status `ready` deltaP `3.1316` edge `-0.1887` maxDD `-8.3588`
- `market_context_high->fx_24h` score `-5.0474` n `146` status `ready` deltaP `-11.9884` edge `-0.05` maxDD `-21.0414`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
