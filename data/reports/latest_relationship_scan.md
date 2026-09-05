# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-05T17:07:26.977330+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10537`

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

- `risk_on_high->unknown_4h` score `21.6828` n `139` status `ready` deltaP `0.8148` edge `1.9307` maxDD `-4.0053`
- `risk_on_and_context->unknown_4h` score `21.6828` n `139` status `ready` deltaP `0.8148` edge `1.9307` maxDD `-4.0053`
- `market_context_high->unknown_4h` score `9.396` n `228` status `ready` deltaP `3.5221` edge `0.9157` maxDD `-4.8281`
- `news_risk_high->crypto_alt_24h` score `7.0979` n `37` status `ready` deltaP `25.1783` edge `0.4506` maxDD `-0.8236`
- `news_risk_high->commodity_24h` score `3.7721` n `37` status `ready` deltaP `19.7917` edge `0.1824` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `3.5188` n `37` status `ready` deltaP `17.0279` edge `0.221` maxDD `-0.9693`
- `news_risk_high->metal_4h` score `2.3807` n `37` status `ready` deltaP `24.1513` edge `0.0595` maxDD `-0.7692`
- `news_risk_high->commodity_4h` score `1.8059` n `37` status `ready` deltaP `10.3618` edge `0.1015` maxDD `-0.2737`
- `news_risk_high->equity_1h` score `1.5464` n `37` status `ready` deltaP `12.6356` edge `0.0837` maxDD `-0.7924`
- `news_risk_high->metal_1h` score `1.2598` n `37` status `ready` deltaP `15.0146` edge `0.0242` maxDD `-0.2118`
- `news_risk_high->index_1h` score `1.1371` n `37` status `ready` deltaP `14.2742` edge `0.013` maxDD `-0.0724`
- `news_risk_high->crypto_major_1h` score `1.1307` n `37` status `ready` deltaP `5.8667` edge `0.0734` maxDD `-0.4628`
- `news_risk_high->crypto_alt_1h` score `0.9321` n `37` status `ready` deltaP `9.0266` edge `0.044` maxDD `-0.7867`
- `news_risk_high->crypto_major_24h` score `0.8798` n `37` status `ready` deltaP `16.5776` edge `0.2799` maxDD `-18.2098`
- `news_risk_high->fx_24h` score `0.6021` n `37` status `ready` deltaP `16.31` edge `0.043` maxDD `-3.1244`
- `news_risk_high->crypto_alt_4h` score `0.5583` n `37` status `ready` deltaP `5.7886` edge `0.0408` maxDD `-1.296`
- `market_context_high->equity_24h` score `0.5216` n `178` status `ready` deltaP `13.9552` edge `0.385` maxDD `-20.7654`
- `risk_on_high->index_1h` score `0.025` n `148` status `ready` deltaP `7.5174` edge `-0.0022` maxDD `-0.5764`
- `risk_on_and_context->index_1h` score `0.025` n `148` status `ready` deltaP `7.5174` edge `-0.0022` maxDD `-0.5764`
- `news_risk_high->commodity_1h` score `-0.0247` n `37` status `ready` deltaP `5.7251` edge `0.0033` maxDD `-0.9036`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
