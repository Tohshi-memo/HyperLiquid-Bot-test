# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-06T07:22:38.241113+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4274`

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

- `news_risk_high->crypto_alt_4h` score `-0.0267` n `141` status `ready` deltaP `8.103` edge `0.2062` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.5475` n `141` status `ready` deltaP `2.7891` edge `0.034` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.6446` n `141` status `ready` deltaP `-1.5989` edge `-0.0019` maxDD `-0.6065`
- `news_risk_high->index_1h` score `-0.7202` n `141` status `ready` deltaP `2.8284` edge `0.0011` maxDD `-1.3981`
- `news_risk_high->metal_1h` score `-1.3711` n `141` status `ready` deltaP `-6.659` edge `-0.0162` maxDD `-2.5487`
- `news_risk_high->index_4h` score `-1.4402` n `141` status `ready` deltaP `2.3893` edge `0.0074` maxDD `-3.9712`
- `news_risk_high->fx_4h` score `-1.5211` n `141` status `ready` deltaP `-8.6328` edge `-0.0123` maxDD `-1.6794`
- `news_risk_high->index_24h` score `-1.9651` n `141` status `ready` deltaP `-10.8027` edge `0.0744` maxDD `-6.6786`
- `news_risk_high->equity_1h` score `-2.3565` n `141` status `ready` deltaP `-5.5007` edge `-0.0002` maxDD `-16.2192`
- `news_risk_high->commodity_1h` score `-2.5404` n `141` status `ready` deltaP `-11.3316` edge `0.0005` maxDD `-3.2657`
- `news_risk_high->fx_24h` score `-2.6104` n `141` status `ready` deltaP `-24.403` edge `-0.0267` maxDD `-1.9558`
- `news_risk_high->crypto_major_1h` score `-2.7529` n `141` status `ready` deltaP `-5.3436` edge `-0.0246` maxDD `-9.2015`
- `news_risk_high->crypto_major_4h` score `-4.001` n `141` status `ready` deltaP `-7.4804` edge `0.0198` maxDD `-17.9342`
- `news_risk_high->commodity_4h` score `-4.2929` n `141` status `ready` deltaP `-18.0321` edge `-0.0021` maxDD `-9.5011`
- `news_risk_high->metal_4h` score `-5.2276` n `141` status `ready` deltaP `-11.5562` edge `-0.0689` maxDD `-8.5085`
- `news_risk_high->equity_24h` score `-6.3171` n `141` status `ready` deltaP `11.9451` edge `0.6651` maxDD `-89.6929`
- `news_risk_high->metal_24h` score `-8.1308` n `141` status `ready` deltaP `-15.1304` edge `-0.2779` maxDD `-13.5703`
- `news_risk_high->equity_4h` score `-8.6604` n `141` status `ready` deltaP `2.8466` edge `0.024` maxDD `-48.1745`
- `news_risk_high->commodity_24h` score `-10.548` n `141` status `ready` deltaP `-18.8594` edge `0.0728` maxDD `-43.7525`
- `news_risk_high->crypto_alt_24h` score `-12.2593` n `141` status `ready` deltaP `6.6689` edge `0.0833` maxDD `-118.6236`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
