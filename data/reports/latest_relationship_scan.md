# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-18T10:22:28.586068+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3867`

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

- `market_context_high->unknown_24h` score `1364.2308` n `98` status `ready` deltaP `2.4306` edge `113.6697` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `14.6672` n `98` status `ready` deltaP `41.6773` edge `1.9296` maxDD `-22.8301`
- `market_context_high->crypto_alt_24h` score `13.2624` n `98` status `ready` deltaP `27.5652` edge `1.7289` maxDD `-13.3222`
- `market_context_high->metal_1h` score `-0.2756` n `98` status `ready` deltaP `2.328` edge `0.0093` maxDD `-2.1461`
- `market_context_high->metal_4h` score `-0.5106` n `98` status `ready` deltaP `11.6196` edge `0.0107` maxDD `-6.1238`
- `market_context_high->metal_24h` score `-0.6049` n `98` status `ready` deltaP `15.3557` edge `0.1697` maxDD `-15.7982`
- `market_context_high->crypto_alt_4h` score `-0.9423` n `98` status `ready` deltaP `-1.4093` edge `0.1696` maxDD `-17.1476`
- `market_context_high->index_1h` score `-1.0037` n `98` status `ready` deltaP `-4.2711` edge `-0.0015` maxDD `-1.2295`
- `market_context_high->crypto_alt_1h` score `-1.3014` n `98` status `ready` deltaP `-3.0062` edge `0.0035` maxDD `-7.6911`
- `market_context_high->fx_1h` score `-1.3819` n `98` status `ready` deltaP `-8.8965` edge `-0.0012` maxDD `-0.3721`
- `market_context_high->crypto_major_4h` score `-1.5815` n `98` status `ready` deltaP `-4.5172` edge `0.1856` maxDD `-22.3259`
- `market_context_high->crypto_major_1h` score `-2.3478` n `98` status `ready` deltaP `-2.2852` edge `0.0063` maxDD `-10.2705`
- `market_context_high->index_4h` score `-2.7614` n `98` status `ready` deltaP `-10.8263` edge `-0.0236` maxDD `-4.7471`
- `market_context_high->commodity_1h` score `-2.8947` n `98` status `ready` deltaP `-15.523` edge `-0.033` maxDD `-3.7125`
- `market_context_high->equity_1h` score `-3.3175` n `98` status `ready` deltaP `-0.6385` edge `-0.0536` maxDD `-11.1548`
- `market_context_high->fx_4h` score `-4.6218` n `98` status `ready` deltaP `-25.6067` edge `-0.0102` maxDD `-2.0058`
- `market_context_high->fx_24h` score `-6.7936` n `98` status `ready` deltaP `-18.8138` edge `-0.0098` maxDD `-5.8059`
- `market_context_high->commodity_4h` score `-7.2508` n `98` status `ready` deltaP `-22.9902` edge `-0.1049` maxDD `-14.6855`
- `market_context_high->index_24h` score `-8.5678` n `98` status `ready` deltaP `-11.2139` edge `-0.097` maxDD `-20.7114`
- `market_context_high->equity_4h` score `-12.9523` n `98` status `ready` deltaP `-16.563` edge `-0.2835` maxDD `-44.5018`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
