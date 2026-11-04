# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-04T00:07:29.410438+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4411`

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

- `news_risk_high->crypto_alt_4h` score `0.3951` n `146` status `ready` deltaP `8.2192` edge `0.2595` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.427` n `146` status `ready` deltaP `2.3316` edge `0.0525` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.7113` n `146` status `ready` deltaP `-2.672` edge `-0.0033` maxDD `-0.6065`
- `news_risk_high->index_1h` score `-0.8855` n `146` status `ready` deltaP `1.3473` edge `-0.0028` maxDD `-1.3981`
- `news_risk_high->metal_1h` score `-1.1591` n `146` status `ready` deltaP `-3.0022` edge `-0.0064` maxDD `-3.1082`
- `news_risk_high->metal_24h` score `-1.4196` n `146` status `ready` deltaP `12.2979` edge `0.1579` maxDD `-16.6552`
- `news_risk_high->fx_4h` score `-1.4709` n `146` status `ready` deltaP `-7.622` edge `-0.0126` maxDD `-1.6794`
- `news_risk_high->index_24h` score `-1.7433` n `146` status `ready` deltaP `1.7243` edge `0.0492` maxDD `-7.402`
- `news_risk_high->index_4h` score `-1.967` n `146` status `ready` deltaP `-1.9024` edge `-0.0094` maxDD `-4.0745`
- `news_risk_high->fx_24h` score `-2.2318` n `146` status `ready` deltaP `-16.4645` edge `-0.0055` maxDD `-2.336`
- `news_risk_high->commodity_1h` score `-2.5732` n `146` status `ready` deltaP `-11.1722` edge `-0.0033` maxDD `-3.2657`
- `news_risk_high->equity_1h` score `-2.7179` n `146` status `ready` deltaP `-7.0851` edge `-0.0336` maxDD `-16.4088`
- `news_risk_high->crypto_major_1h` score `-3.1803` n `146` status `ready` deltaP `-7.8562` edge `-0.0401` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-4.0981` n `146` status `ready` deltaP `-14.4567` edge `-0.0097` maxDD `-9.5011`
- `news_risk_high->metal_4h` score `-4.2898` n `146` status `ready` deltaP `-2.8796` edge `-0.0178` maxDD `-9.3056`
- `news_risk_high->crypto_alt_24h` score `-6.0071` n `146` status `ready` deltaP `21.7989` edge `0.784` maxDD `-118.6236`
- `news_risk_high->crypto_major_4h` score `-6.7055` n `146` status `ready` deltaP `-12.097` edge `-0.0762` maxDD `-24.1554`
- `news_risk_high->equity_24h` score `-8.3234` n `146` status `ready` deltaP `18.8476` edge `0.6311` maxDD `-102.3626`
- `news_risk_high->equity_4h` score `-11.4656` n `146` status `ready` deltaP `-1.7499` edge `-0.1077` maxDD `-52.2214`
- `news_risk_high->commodity_24h` score `-12.2561` n `146` status `ready` deltaP `-19.9153` edge `-0.0625` maxDD `-43.7525`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
