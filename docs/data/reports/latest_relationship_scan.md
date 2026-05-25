# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-25T04:52:22.146420+00:00`
- Price records: `672`
- Market context records: `1810`
- Flow alert records: `7108`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4514`

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

- `market_context_high->crypto_alt_4h` score `7.234` n `183` status `ready` deltaP `23.5805` edge `0.5601` maxDD `-5.1574`
- `market_context_high->metal_24h` score `6.8656` n `178` status `ready` deltaP `27.5905` edge `0.6308` maxDD `-12.7414`
- `market_context_high->crypto_major_4h` score `6.7621` n `183` status `ready` deltaP `27.5723` edge `0.5043` maxDD `-4.9684`
- `news_risk_high->commodity_4h` score `6.5269` n `30` status `ready` deltaP `29.563` edge `0.4123` maxDD `-3.5713`
- `market_context_high->unknown_4h` score `4.7015` n `183` status `ready` deltaP `17.5322` edge `0.4773` maxDD `-9.8581`
- `market_context_high->index_24h` score `3.6874` n `178` status `ready` deltaP `17.8683` edge `0.311` maxDD `-4.1604`
- `news_risk_high->commodity_1h` score `3.3189` n `30` status `ready` deltaP `25.1697` edge `0.1405` maxDD `-1.2043`
- `market_context_high->equity_24h` score `2.9785` n `178` status `ready` deltaP `19.0133` edge `0.6113` maxDD `-33.1875`
- `market_context_high->equity_4h` score `2.9413` n `183` status `ready` deltaP `15.6537` edge `0.2502` maxDD `-5.0894`
- `market_context_high->unknown_24h` score `2.2763` n `178` status `ready` deltaP `12.6502` edge `0.6374` maxDD `-35.8966`
- `news_risk_high->fx_4h` score `0.9073` n `30` status `ready` deltaP `21.6362` edge `-0.0007` maxDD `-0.1774`
- `market_context_high->index_4h` score `0.7922` n `183` status `ready` deltaP `11.3572` edge `0.0992` maxDD `-3.7119`
- `market_context_high->crypto_major_1h` score `0.4209` n `186` status `ready` deltaP `5.9687` edge `0.0939` maxDD `-3.2225`
- `news_risk_high->unknown_4h` score `0.3743` n `30` status `ready` deltaP `9.8272` edge `0.0548` maxDD `-2.7857`
- `market_context_high->crypto_alt_1h` score `0.3214` n `186` status `ready` deltaP `6.5337` edge `0.0946` maxDD `-4.9097`
- `market_context_high->equity_1h` score `-0.1407` n `186` status `ready` deltaP `3.9824` edge `0.0411` maxDD `-2.6836`
- `market_context_high->crypto_major_24h` score `-0.2033` n `178` status `ready` deltaP `17.9912` edge `0.7217` maxDD `-62.3533`
- `market_context_high->unknown_1h` score `-0.3618` n `186` status `ready` deltaP `3.3964` edge `0.0424` maxDD `-3.6151`
- `market_context_high->fx_24h` score `-0.4213` n `178` status `ready` deltaP `9.5252` edge `0.0063` maxDD `-1.3925`
- `news_risk_high->fx_1h` score `-0.4469` n `30` status `ready` deltaP `-4.6806` edge `0.0001` maxDD `-0.0948`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
