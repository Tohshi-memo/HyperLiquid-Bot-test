# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-09T02:07:24.324812+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `8733`

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

- `market_context_high->equity_24h` score `3.2796` n `103` status `ready` deltaP `4.5729` edge `0.5488` maxDD `-21.1456`
- `market_context_high->metal_24h` score `2.6275` n `103` status `ready` deltaP `13.2535` edge `0.1882` maxDD `-2.2743`
- `market_context_high->commodity_4h` score `1.4242` n `122` status `ready` deltaP `14.2018` edge `0.0913` maxDD `-2.7169`
- `market_context_high->commodity_1h` score `0.8776` n `134` status `ready` deltaP `10.7449` edge `0.0358` maxDD `-0.7439`
- `market_context_high->fx_24h` score `0.8482` n `103` status `ready` deltaP `22.0958` edge `0.0481` maxDD `-1.9329`
- `market_context_high->index_24h` score `0.4916` n `103` status `ready` deltaP `9.1002` edge `0.1555` maxDD `-5.9181`
- `market_context_high->fx_1h` score `-0.3918` n `134` status `ready` deltaP `3.1348` edge `-0.004` maxDD `-0.9639`
- `market_context_high->fx_4h` score `-0.4895` n `122` status `ready` deltaP `5.6602` edge `-0.0032` maxDD `-1.6928`
- `market_context_high->index_4h` score `-0.6039` n `122` status `ready` deltaP `-0.5873` edge `-0.013` maxDD `-1.1743`
- `market_context_high->metal_1h` score `-0.6598` n `134` status `ready` deltaP `-4.2005` edge `-0.007` maxDD `-0.9664`
- `market_context_high->index_1h` score `-0.85` n `134` status `ready` deltaP `-3.7514` edge `-0.0069` maxDD `-0.7809`
- `market_context_high->equity_1h` score `-0.9196` n `134` status `ready` deltaP `0.2591` edge `0.0045` maxDD `-4.6286`
- `market_context_high->metal_4h` score `-1.0455` n `122` status `ready` deltaP `-2.4541` edge `-0.0168` maxDD `-2.7373`
- `market_context_high->crypto_alt_1h` score `-2.1446` n `134` status `ready` deltaP `-11.9604` edge `-0.0348` maxDD `-2.4677`
- `market_context_high->equity_4h` score `-2.3516` n `122` status `ready` deltaP `0.9397` edge `-0.0685` maxDD `-7.6983`
- `market_context_high->crypto_major_1h` score `-3.1189` n `134` status `ready` deltaP `-10.307` edge `-0.0657` maxDD `-6.7064`
- `market_context_high->crypto_major_24h` score `-3.6295` n `103` status `ready` deltaP `6.2197` edge `-0.0945` maxDD `-14.2873`
- `market_context_high->crypto_alt_24h` score `-4.483` n `103` status `ready` deltaP `-12.4461` edge `-0.1463` maxDD `-4.5445`
- `market_context_high->crypto_alt_4h` score `-4.6819` n `122` status `ready` deltaP `-12.9023` edge `-0.1385` maxDD `-6.585`
- `market_context_high->unknown_1h` score `-8.3322` n `134` status `ready` deltaP `-5.3758` edge `-0.6138` maxDD `-1.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
