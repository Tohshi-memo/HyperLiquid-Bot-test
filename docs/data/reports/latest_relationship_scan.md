# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-27T05:07:22.274640+00:00`
- Price records: `672`
- Market context records: `2011`
- Flow alert records: `7679`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9107`

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

- `market_context_high->crypto_major_4h` score `8.8993` n `210` status `ready` deltaP `30.9306` edge `0.5884` maxDD `-1.9063`
- `market_context_high->crypto_alt_4h` score `8.353` n `210` status `ready` deltaP `24.608` edge `0.6465` maxDD `-5.1574`
- `market_context_high->unknown_4h` score `5.7621` n `210` status `ready` deltaP `18.9881` edge `0.4285` maxDD `-2.6599`
- `market_context_high->equity_4h` score `2.7964` n `210` status `ready` deltaP `16.0323` edge `0.2356` maxDD `-5.0894`
- `market_context_high->crypto_major_1h` score `1.5418` n `210` status `ready` deltaP `12.5848` edge `0.1432` maxDD `-3.2225`
- `market_context_high->crypto_alt_1h` score `1.2535` n `210` status `ready` deltaP `10.1896` edge `0.1479` maxDD `-4.9097`
- `market_context_high->index_4h` score `1.225` n `210` status `ready` deltaP `11.6318` edge `0.0929` maxDD `-1.8022`
- `market_context_high->unknown_24h` score `0.9194` n `186` status `ready` deltaP `15.7442` edge `0.5037` maxDD `-35.8966`
- `market_context_high->metal_24h` score `0.6951` n `186` status `ready` deltaP `14.3136` edge `0.2051` maxDD `-12.7414`
- `market_context_high->equity_24h` score `0.4861` n `186` status `ready` deltaP `14.5732` edge `0.4332` maxDD `-33.1875`
- `market_context_high->fx_24h` score `0.2627` n `186` status `ready` deltaP `14.8918` edge `0.0269` maxDD `-2.0099`
- `market_context_high->equity_1h` score `0.1348` n `210` status `ready` deltaP `6.3103` edge `0.048` maxDD `-2.6402`
- `market_context_high->index_24h` score `-0.0575` n `186` status `ready` deltaP `2.8576` edge `0.099` maxDD `-4.1604`
- `market_context_high->index_1h` score `-0.3934` n `210` status `ready` deltaP `1.6439` edge `0.0153` maxDD `-1.3898`
- `market_context_high->unknown_1h` score `-0.616` n `210` status `ready` deltaP `3.7539` edge `-0.0044` maxDD `-3.0902`
- `market_context_high->fx_1h` score `-0.7915` n `210` status `ready` deltaP `-0.5988` edge `0.0008` maxDD `-0.3548`
- `market_context_high->fx_4h` score `-1.0347` n `210` status `ready` deltaP `-6.4213` edge `-0.0017` maxDD `-1.0513`
- `market_context_high->metal_1h` score `-1.077` n `210` status `ready` deltaP `2.7887` edge `0.0104` maxDD `-5.166`
- `market_context_high->crypto_major_24h` score `-1.4603` n `186` status `ready` deltaP `17.2485` edge `0.6219` maxDD `-62.3533`
- `market_context_high->metal_4h` score `-1.6` n `210` status `ready` deltaP `7.0092` edge `0.0822` maxDD `-11.9812`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
