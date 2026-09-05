# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-05T18:37:23.783855+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10591`

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

- `risk_on_high->unknown_4h` score `20.0972` n `140` status `ready` deltaP `-1.6159` edge `1.8758` maxDD `-7.2209`
- `risk_on_and_context->unknown_4h` score `20.0972` n `140` status `ready` deltaP `-1.6159` edge `1.8758` maxDD `-7.2209`
- `market_context_high->unknown_4h` score `8.2506` n `228` status `ready` deltaP `1.8052` edge `0.9022` maxDD `-8.4683`
- `news_risk_high->crypto_alt_24h` score `6.9743` n `37` status `ready` deltaP `25.1783` edge `0.4403` maxDD `-0.8236`
- `news_risk_high->commodity_24h` score `3.7872` n `37` status `ready` deltaP `19.9653` edge `0.1825` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `3.412` n `37` status `ready` deltaP `17.0279` edge `0.2121` maxDD `-0.9693`
- `news_risk_high->metal_4h` score `2.3783` n `37` status `ready` deltaP `24.1513` edge `0.0593` maxDD `-0.7692`
- `news_risk_high->commodity_4h` score `1.7645` n `37` status `ready` deltaP `9.9044` edge `0.1011` maxDD `-0.2737`
- `news_risk_high->equity_1h` score `1.5344` n `37` status `ready` deltaP `12.4859` edge `0.0837` maxDD `-0.7924`
- `news_risk_high->metal_1h` score `1.2586` n `37` status `ready` deltaP `15.0146` edge `0.0241` maxDD `-0.2118`
- `news_risk_high->index_1h` score `1.1251` n `37` status `ready` deltaP `14.1245` edge `0.013` maxDD `-0.0724`
- `news_risk_high->crypto_major_1h` score `1.0947` n `37` status `ready` deltaP `5.8667` edge `0.0704` maxDD `-0.4628`
- `news_risk_high->crypto_alt_1h` score `0.9477` n `37` status `ready` deltaP `9.1763` edge `0.0443` maxDD `-0.7867`
- `news_risk_high->crypto_major_24h` score `0.7456` n `37` status `ready` deltaP `16.5776` edge `0.2627` maxDD `-18.2098`
- `news_risk_high->fx_24h` score `0.6903` n `37` status `ready` deltaP `17.3517` edge `0.0434` maxDD `-3.1244`
- `market_context_high->equity_24h` score `0.5711` n `174` status `ready` deltaP `13.374` edge `0.393` maxDD `-20.7654`
- `news_risk_high->crypto_alt_4h` score `0.4979` n `37` status `ready` deltaP `5.4837` edge `0.0378` maxDD `-1.296`
- `risk_on_high->index_1h` score `0.0372` n `147` status `ready` deltaP `7.7814` edge `-0.0024` maxDD `-0.5764`
- `risk_on_and_context->index_1h` score `0.0372` n `147` status `ready` deltaP `7.7814` edge `-0.0024` maxDD `-0.5764`
- `news_risk_high->commodity_1h` score `-0.0177` n `37` status `ready` deltaP `5.8748` edge `0.0032` maxDD `-0.9036`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
