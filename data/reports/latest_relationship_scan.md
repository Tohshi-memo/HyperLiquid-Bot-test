# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-25T11:22:32.207239+00:00`
- Price records: `672`
- Market context records: `7872`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14667`

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

- `market_context_high->equity_24h` score `12.8071` n `117` status `ready` deltaP `29.1966` edge `1.0068` maxDD `-6.0681`
- `market_context_high->metal_24h` score `2.9547` n `118` status `ready` deltaP `16.3249` edge `0.2742` maxDD `-1.6116`
- `market_context_high->equity_4h` score `2.5748` n `118` status `ready` deltaP `10.877` edge `0.3668` maxDD `-5.4037`
- `market_context_high->crypto_major_4h` score `1.6983` n `118` status `ready` deltaP `17.9` edge `0.194` maxDD `-6.7444`
- `market_context_high->crypto_alt_4h` score `1.5172` n `118` status `ready` deltaP `13.4922` edge `0.1482` maxDD `-3.9374`
- `market_context_high->commodity_24h` score `1.4011` n `117` status `ready` deltaP `21.2263` edge `0.1336` maxDD `-7.0012`
- `market_context_high->crypto_major_1h` score `1.1995` n `118` status `ready` deltaP `13.4096` edge `0.0505` maxDD `-1.5286`
- `market_context_high->fx_24h` score `1.0972` n `117` status `ready` deltaP `30.0943` edge `0.0488` maxDD `-3.0343`
- `market_context_high->equity_1h` score `0.7373` n `118` status `ready` deltaP `10.513` edge `0.1062` maxDD `-4.2072`
- `market_context_high->crypto_alt_1h` score `0.3435` n `118` status `ready` deltaP `4.8868` edge `0.0393` maxDD `-1.4603`
- `market_context_high->commodity_4h` score `0.2792` n `118` status `ready` deltaP `6.4687` edge `0.0395` maxDD `-1.0817`
- `market_context_high->index_1h` score `0.1837` n `118` status `ready` deltaP `7.4337` edge `0.017` maxDD `-0.7743`
- `market_context_high->index_4h` score `-0.0583` n `118` status `ready` deltaP `11.1828` edge `0.0543` maxDD `-1.2397`
- `market_context_high->commodity_1h` score `-0.0604` n `118` status `ready` deltaP `4.2704` edge `0.0124` maxDD `-0.6722`
- `market_context_high->fx_1h` score `-0.3783` n `118` status `ready` deltaP `1.1045` edge `-0.0003` maxDD `-0.4201`
- `market_context_high->metal_4h` score `-0.3878` n `118` status `ready` deltaP `5.5239` edge `0.0888` maxDD `-1.3019`
- `market_context_high->index_24h` score `-0.9171` n `117` status `ready` deltaP `-2.249` edge `0.1078` maxDD `-1.8717`
- `market_context_high->metal_1h` score `-0.9748` n `118` status `ready` deltaP `-0.4948` edge `0.0224` maxDD `-0.6936`
- `market_context_high->fx_4h` score `-1.1614` n `118` status `ready` deltaP `-1.8296` edge `0.0003` maxDD `-1.6262`
- `market_context_high->crypto_alt_24h` score `-1.5599` n `118` status `ready` deltaP `13.8369` edge `0.2373` maxDD `-28.3623`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
