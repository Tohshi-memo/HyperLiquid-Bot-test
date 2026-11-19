# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-19T22:37:29.436675+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `24`

- Symbol pattern count: `2618`

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

- `market_context_high->unknown_1h` score `12009.4268` n `108` status `ready` deltaP `1.1367` edge `1000.7978` maxDD `-0.9181`
- `market_context_high->unknown_4h` score `7549.1392` n `107` status `ready` deltaP `-0.0071` edge `629.1234` maxDD `-0.6072`
- `market_context_high->crypto_major_24h` score `23.9451` n `88` status `ready` deltaP `42.5031` edge `1.7714` maxDD `-2.746`
- `market_context_high->crypto_alt_24h` score `12.0093` n `88` status `ready` deltaP `25.7892` edge `1.507` maxDD `-7.4749`
- `market_context_high->crypto_major_4h` score `2.0368` n `107` status `ready` deltaP `4.8481` edge `0.4193` maxDD `-16.2179`
- `market_context_high->crypto_alt_4h` score `1.3123` n `107` status `ready` deltaP `5.9152` edge `0.2775` maxDD `-12.9396`
- `market_context_high->metal_24h` score `0.5924` n `88` status `ready` deltaP `19.0656` edge `0.2311` maxDD `-14.7068`
- `market_context_high->metal_4h` score `0.4796` n `107` status `ready` deltaP `18.21` edge `0.0478` maxDD `-6.0054`
- `market_context_high->crypto_major_1h` score `-0.1954` n `108` status `ready` deltaP `5.1453` edge `0.0803` maxDD `-6.5061`
- `market_context_high->metal_1h` score `-0.2908` n `108` status `ready` deltaP `4.0419` edge `0.0153` maxDD `-2.6517`
- `market_context_high->index_1h` score `-0.2919` n `108` status `ready` deltaP `2.8166` edge `0.005` maxDD `-1.2295`
- `market_context_high->crypto_alt_1h` score `-0.6911` n `108` status `ready` deltaP `-1.6356` edge `0.0445` maxDD `-5.4428`
- `market_context_high->equity_1h` score `-1.2022` n `108` status `ready` deltaP `6.1932` edge `0.0364` maxDD `-10.8962`
- `market_context_high->fx_1h` score `-1.6325` n `108` status `ready` deltaP `-11.6988` edge `-0.0021` maxDD `-0.4757`
- `market_context_high->index_4h` score `-1.8999` n `107` status `ready` deltaP `-2.8934` edge `-0.0047` maxDD `-4.7471`
- `market_context_high->fx_4h` score `-2.3883` n `107` status `ready` deltaP `-15.0302` edge `-0.0044` maxDD `-1.794`
- `market_context_high->commodity_1h` score `-2.4403` n `108` status `ready` deltaP `-10.1187` edge `-0.0277` maxDD `-3.9892`
- `market_context_high->fx_24h` score `-7.2704` n `88` status `ready` deltaP `-24.9842` edge `-0.012` maxDD `-5.5179`
- `market_context_high->commodity_4h` score `-8.1095` n `107` status `ready` deltaP `-29.1615` edge `-0.1121` maxDD `-15.5426`
- `market_context_high->equity_4h` score `-9.3387` n `107` status `ready` deltaP `-7.3413` edge `-0.0616` maxDD `-43.0813`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
