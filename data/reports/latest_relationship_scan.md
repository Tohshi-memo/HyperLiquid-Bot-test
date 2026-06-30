# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-30T04:07:26.211102+00:00`
- Price records: `672`
- Market context records: `5213`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5650`

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

- `market_context_high->unknown_24h` score `16.1813` n `107` status `ready` deltaP `33.5881` edge `1.1435` maxDD `-0.8515`
- `market_context_high->crypto_major_24h` score `14.3255` n `107` status `ready` deltaP `31.4187` edge `1.3505` maxDD `-22.6266`
- `market_context_high->crypto_alt_24h` score `9.4688` n `107` status `ready` deltaP `27.6398` edge `0.9435` maxDD `-23.4292`
- `market_context_high->unknown_4h` score `4.8467` n `155` status `ready` deltaP `18.8119` edge `0.3807` maxDD `-5.5109`
- `market_context_high->crypto_alt_4h` score `4.4603` n `155` status `ready` deltaP `13.8464` edge `0.4393` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `4.3422` n `155` status `ready` deltaP `14.0696` edge `0.4973` maxDD `-14.0065`
- `market_context_high->unknown_1h` score `2.4896` n `155` status `ready` deltaP `8.9878` edge `0.2117` maxDD `-2.7986`
- `market_context_high->crypto_alt_1h` score `0.644` n `155` status `ready` deltaP `4.9527` edge `0.1168` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `0.5968` n `155` status `ready` deltaP `6.7027` edge `0.1296` maxDD `-6.9639`
- `market_context_high->fx_24h` score `0.5793` n `107` status `ready` deltaP `13.6812` edge `0.0466` maxDD `-0.8294`
- `market_context_high->equity_4h` score `0.3748` n `155` status `ready` deltaP `7.2452` edge `0.1468` maxDD `-7.4425`
- `market_context_high->equity_1h` score `-0.1011` n `155` status `ready` deltaP `5.3699` edge `0.0523` maxDD `-5.0555`
- `market_context_high->metal_1h` score `-0.1246` n `155` status `ready` deltaP `4.1114` edge `0.0158` maxDD `-2.0682`
- `market_context_high->index_1h` score `-0.1966` n `155` status `ready` deltaP `3.5378` edge `0.0104` maxDD `-1.0296`
- `market_context_high->fx_1h` score `-0.2604` n `155` status `ready` deltaP `1.809` edge `-0.0002` maxDD `-0.6194`
- `market_context_high->index_24h` score `-0.5466` n `107` status `ready` deltaP `13.0971` edge `0.0061` maxDD `-7.413`
- `market_context_high->fx_4h` score `-0.6097` n `155` status `ready` deltaP `3.034` edge `0.005` maxDD `-1.6047`
- `market_context_high->commodity_1h` score `-0.6226` n `155` status `ready` deltaP `0.2762` edge `-0.0008` maxDD `-2.4692`
- `market_context_high->index_4h` score `-0.7142` n `155` status `ready` deltaP `4.5338` edge `0.022` maxDD `-2.9391`
- `market_context_high->metal_4h` score `-1.3582` n `155` status `ready` deltaP `-0.1023` edge `0.0269` maxDD `-9.3609`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
