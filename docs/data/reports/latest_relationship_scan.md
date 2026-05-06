# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-06T19:37:21.751954+00:00`
- Price records: `482`
- Market context records: `574`
- Flow alert records: `1621`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `807`

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

- `market_context_high->crypto_alt_24h` score `4.8201` n `146` status `ready` deltaP `7.3462` edge `0.3575` maxDD `-0.0508`
- `market_context_high->crypto_major_24h` score `2.9026` n `146` status `ready` deltaP `9.6564` edge `0.2109` maxDD `-1.3382`
- `market_context_high->fx_4h` score `0.0275` n `146` status `ready` deltaP `10.6002` edge `0.02` maxDD `-1.6381`
- `market_context_high->fx_1h` score `-0.268` n `146` status `ready` deltaP `2.8409` edge `0.0045` maxDD `-0.291`
- `market_context_high->commodity_1h` score `-0.5222` n `146` status `ready` deltaP `2.1646` edge `0.0395` maxDD `-3.7959`
- `market_context_high->index_1h` score `-0.6819` n `146` status `ready` deltaP `0.1994` edge `-0.0034` maxDD `-2.8282`
- `market_context_high->unknown_1h` score `-1.1391` n `146` status `ready` deltaP `-3.823` edge `-0.0091` maxDD `-2.1602`
- `market_context_high->crypto_alt_1h` score `-1.2784` n `146` status `ready` deltaP `4.7602` edge `-0.0068` maxDD `-8.1842`
- `market_context_high->equity_1h` score `-1.2825` n `146` status `ready` deltaP `-2.1213` edge `-0.0117` maxDD `-4.4826`
- `market_context_high->index_24h` score `-1.8089` n `146` status `ready` deltaP `-5.5691` edge `0.0859` maxDD `-5.9609`
- `market_context_high->crypto_major_1h` score `-1.9156` n `146` status `ready` deltaP `4.1497` edge `-0.015` maxDD `-11.4508`
- `market_context_high->index_4h` score `-2.1594` n `146` status `ready` deltaP `0.7828` edge `-0.0329` maxDD `-6.5149`
- `market_context_high->crypto_alt_4h` score `-2.2246` n `146` status `ready` deltaP `2.8191` edge `0.0528` maxDD `-15.2248`
- `market_context_high->crypto_major_4h` score `-3.0581` n `146` status `ready` deltaP `10.9736` edge `0.0426` maxDD `-22.648`
- `market_context_high->equity_4h` score `-3.2455` n `146` status `ready` deltaP `-3.1133` edge `-0.0345` maxDD `-10.5498`
- `market_context_high->metal_1h` score `-3.2961` n `146` status `ready` deltaP `-4.5825` edge `-0.0482` maxDD `-9.0076`
- `market_context_high->commodity_4h` score `-3.5208` n `146` status `ready` deltaP `-5.5802` edge `0.0939` maxDD `-13.0076`
- `market_context_high->equity_24h` score `-3.6514` n `146` status `ready` deltaP `-9.736` edge `0.0211` maxDD `-10.5047`
- `market_context_high->fx_24h` score `-4.6143` n `146` status `ready` deltaP `-5.2643` edge `-0.0393` maxDD `-21.0414`
- `market_context_high->unknown_4h` score `-5.2171` n `146` status `ready` deltaP `0.6085` edge `-0.251` maxDD `-8.3588`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
