# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-01T02:07:27.322854+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `6237`

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

- `market_context_high->unknown_24h` score `4663.7984` n `74` status `ready` deltaP `-6.9163` edge `388.7209` maxDD `-0.9938`
- `market_context_high->unknown_4h` score `194.2055` n `74` status `ready` deltaP `1.0176` edge `16.1903` maxDD `-0.3966`
- `news_risk_high->unknown_1h` score `81.3508` n `108` status `ready` deltaP `-5.1951` edge `6.8425` maxDD `-0.9571`
- `news_risk_high->crypto_alt_24h` score `14.7325` n `92` status `ready` deltaP `35.0921` edge `1.1111` maxDD `-6.3871`
- `market_context_high->equity_24h` score `12.7233` n `74` status `ready` deltaP `24.7091` edge `1.1173` maxDD `-11.4068`
- `news_risk_high->crypto_alt_4h` score `5.4908` n `108` status `ready` deltaP `20.7317` edge `0.458` maxDD `-7.4246`
- `market_context_high->index_24h` score `5.3526` n `74` status `ready` deltaP `46.2087` edge `0.1563` maxDD `-0.1315`
- `market_context_high->commodity_4h` score `2.7732` n `74` status `ready` deltaP `27.8098` edge `0.0791` maxDD `-0.3387`
- `market_context_high->fx_1h` score `1.0071` n `74` status `ready` deltaP `15.3221` edge `0.0002` maxDD `-0.1407`
- `news_risk_high->crypto_alt_1h` score `0.8337` n `108` status `ready` deltaP `8.727` edge `0.1067` maxDD `-3.9659`
- `market_context_high->metal_4h` score `0.706` n `74` status `ready` deltaP `13.5754` edge `0.0425` maxDD `-0.7323`
- `market_context_high->metal_1h` score `0.618` n `74` status `ready` deltaP `9.0023` edge `0.0205` maxDD `-0.3209`
- `market_context_high->fx_4h` score `0.5158` n `74` status `ready` deltaP `11.9686` edge `0.0023` maxDD `-0.1285`
- `market_context_high->commodity_24h` score `0.3332` n `74` status `ready` deltaP `25.3566` edge `0.0969` maxDD `-11.5243`
- `market_context_high->equity_1h` score `0.2929` n `74` status `ready` deltaP `1.5011` edge `0.1151` maxDD `-2.3383`
- `market_context_high->equity_4h` score `0.1799` n `74` status `ready` deltaP `-6.147` edge `0.1981` maxDD `-4.3912`
- `market_context_high->crypto_major_1h` score `-0.2619` n `74` status `ready` deltaP `0.8982` edge `0.0632` maxDD `-5.2213`
- `market_context_high->commodity_1h` score `-0.3862` n `74` status `ready` deltaP `0.1416` edge `0.0183` maxDD `-0.4475`
- `market_context_high->index_1h` score `-0.4856` n `74` status `ready` deltaP `-1.2017` edge `0.0016` maxDD `-1.1344`
- `market_context_high->crypto_alt_1h` score `-0.6257` n `74` status `ready` deltaP `-0.4572` edge `0.0811` maxDD `-5.9953`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
