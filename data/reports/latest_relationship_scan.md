# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-25T20:22:31.127554+00:00`
- Price records: `672`
- Market context records: `4756`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7476`

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

- `market_context_high->unknown_1h` score `82.6274` n `136` status `ready` deltaP `13.046` edge `6.8404` maxDD `-1.674`
- `market_context_high->unknown_4h` score `6.2478` n `133` status `ready` deltaP `14.1734` edge `0.5472` maxDD `-4.6834`
- `market_context_high->unknown_24h` score `3.0847` n `121` status `ready` deltaP `15.0884` edge `0.2488` maxDD `-4.7201`
- `market_context_high->index_4h` score `-0.3887` n `133` status `ready` deltaP `7.4478` edge `0.0074` maxDD `-5.5505`
- `market_context_high->equity_4h` score `-0.4904` n `133` status `ready` deltaP `6.8276` edge `0.0602` maxDD `-8.8203`
- `market_context_high->commodity_1h` score `-0.5528` n `136` status `ready` deltaP `1.8492` edge `0.0212` maxDD `-2.0345`
- `market_context_high->fx_4h` score `-0.7584` n `133` status `ready` deltaP `-0.6602` edge `-0.0017` maxDD `-1.6242`
- `market_context_high->equity_1h` score `-0.9472` n `136` status `ready` deltaP `-1.4838` edge `-0.0166` maxDD `-5.262`
- `market_context_high->fx_1h` score `-1.146` n `136` status `ready` deltaP `-3.923` edge `-0.0043` maxDD `-0.8704`
- `market_context_high->commodity_4h` score `-1.1834` n `133` status `ready` deltaP `8.0185` edge `0.0239` maxDD `-8.4112`
- `market_context_high->index_1h` score `-1.5237` n `136` status `ready` deltaP `-2.8443` edge `-0.0076` maxDD `-2.6999`
- `market_context_high->metal_1h` score `-2.5348` n `136` status `ready` deltaP `-3.311` edge `-0.0699` maxDD `-15.3067`
- `market_context_high->commodity_24h` score `-2.5446` n `121` status `ready` deltaP `17.2119` edge `0.0699` maxDD `-27.5371`
- `market_context_high->crypto_alt_1h` score `-2.7899` n `136` status `ready` deltaP `-0.7221` edge `-0.055` maxDD `-19.8288`
- `market_context_high->crypto_major_1h` score `-3.2654` n `136` status `ready` deltaP `-0.1101` edge `-0.0748` maxDD `-24.7815`
- `market_context_high->fx_24h` score `-4.1955` n `121` status `ready` deltaP `-15.4284` edge `-0.0215` maxDD `-4.3546`
- `market_context_high->crypto_alt_4h` score `-5.4858` n `133` status `ready` deltaP `2.0527` edge `-0.0407` maxDD `-48.7701`
- `market_context_high->index_24h` score `-7.0465` n `121` status `ready` deltaP `-11.4828` edge `-0.1149` maxDD `-22.6608`
- `market_context_high->crypto_major_4h` score `-8.1575` n `133` status `ready` deltaP `2.8149` edge `-0.1415` maxDD `-68.5143`
- `market_context_high->metal_4h` score `-8.3231` n `133` status `ready` deltaP `4.5021` edge `-0.273` maxDD `-61.2596`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
