# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-29T08:07:24.239980+00:00`
- Price records: `672`
- Market context records: `8283`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5892`

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

- `news_risk_high->unknown_24h` score `6577.9466` n `50` status `ready` deltaP `40.2778` edge `547.8937` maxDD `0.0`
- `news_risk_high->equity_4h` score `7.1457` n `54` status `ready` deltaP `26.2308` edge `0.4803` maxDD `-3.4427`
- `news_risk_high->equity_1h` score `2.9335` n `54` status `ready` deltaP `20.9304` edge `0.1358` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.6917` n `54` status `ready` deltaP `22.4198` edge `0.0939` maxDD `-0.191`
- `news_risk_high->crypto_major_4h` score `2.0375` n `54` status `ready` deltaP `9.8691` edge `0.2648` maxDD `-2.8833`
- `news_risk_high->crypto_alt_1h` score `1.7656` n `54` status `ready` deltaP `13.8057` edge `0.0985` maxDD `-1.1388`
- `news_risk_high->crypto_alt_4h` score `1.5412` n `54` status `ready` deltaP `17.2313` edge `0.2219` maxDD `-5.8012`
- `news_risk_high->crypto_major_1h` score `1.4807` n `54` status `ready` deltaP `10.0078` edge `0.0964` maxDD `-1.1783`
- `news_risk_high->metal_4h` score `1.0005` n `54` status `ready` deltaP `9.1294` edge `0.0693` maxDD `-0.7433`
- `news_risk_high->index_1h` score `0.386` n `54` status `ready` deltaP `6.1544` edge `0.02` maxDD `-0.3089`
- `news_risk_high->fx_1h` score `0.1689` n `54` status `ready` deltaP `6.9971` edge `0.0031` maxDD `-0.2475`
- `news_risk_high->metal_1h` score `-0.1539` n `54` status `ready` deltaP `2.5061` edge `0.0108` maxDD `-0.5599`
- `news_risk_high->fx_4h` score `-0.3986` n `54` status `ready` deltaP `5.5273` edge `0.0078` maxDD `-0.6604`
- `news_risk_high->commodity_1h` score `-2.0952` n `54` status `ready` deltaP `-8.3611` edge `-0.0403` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-4.7368` n `50` status `ready` deltaP `-19.9514` edge `-0.049` maxDD `-5.0181`
- `news_risk_high->metal_24h` score `-5.4953` n `50` status `ready` deltaP `-18.1806` edge `-0.0621` maxDD `-10.6379`
- `news_risk_high->commodity_4h` score `-8.7518` n `54` status `ready` deltaP `-30.5048` edge `-0.1952` maxDD `-13.1269`
- `news_risk_high->index_24h` score `-12.0787` n `50` status `ready` deltaP `-24.2014` edge `-0.3208` maxDD `-27.2864`
- `news_risk_high->commodity_24h` score `-12.2404` n `50` status `ready` deltaP `-12.9236` edge `-0.3399` maxDD `-33.8515`
- `news_risk_high->crypto_major_24h` score `-34.7328` n `50` status `ready` deltaP `-17.1458` edge `-1.3276` maxDD `-103.8662`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
