# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-25T06:07:17.471962+00:00`
- Price records: `672`
- Market context records: `1815`
- Flow alert records: `7124`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4474`

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

- `market_context_high->crypto_alt_4h` score `7.0231` n `183` status `ready` deltaP `22.8183` edge `0.5476` maxDD `-5.1574`
- `market_context_high->metal_24h` score `6.8584` n `178` status `ready` deltaP `27.5905` edge `0.6302` maxDD `-12.7414`
- `market_context_high->crypto_major_4h` score `6.6123` n `183` status `ready` deltaP `26.8101` edge `0.4969` maxDD `-4.9684`
- `news_risk_high->commodity_4h` score `6.5593` n `30` status `ready` deltaP `29.563` edge `0.415` maxDD `-3.5713`
- `market_context_high->unknown_4h` score `4.7231` n `183` status `ready` deltaP `17.5322` edge `0.4791` maxDD `-9.8581`
- `market_context_high->index_24h` score `3.6586` n `178` status `ready` deltaP `17.8683` edge `0.3086` maxDD `-4.1604`
- `news_risk_high->commodity_1h` score `3.3333` n `30` status `ready` deltaP `25.3194` edge `0.1407` maxDD `-1.2043`
- `market_context_high->equity_4h` score `2.9797` n `183` status `ready` deltaP `15.6537` edge `0.2534` maxDD `-5.0894`
- `market_context_high->equity_24h` score `2.7603` n `178` status `ready` deltaP `18.1452` edge `0.5989` maxDD `-33.1875`
- `market_context_high->unknown_24h` score `2.4075` n `178` status `ready` deltaP `13.3447` edge `0.6437` maxDD `-35.8966`
- `news_risk_high->fx_4h` score `0.9058` n `30` status `ready` deltaP `21.6362` edge `-0.0009` maxDD `-0.1774`
- `market_context_high->index_4h` score `0.809` n `183` status `ready` deltaP `11.3572` edge `0.1006` maxDD `-3.7119`
- `market_context_high->crypto_major_1h` score `0.4513` n `191` status `ready` deltaP `6.0938` edge `0.0956` maxDD `-3.2225`
- `market_context_high->crypto_alt_1h` score `0.4156` n `191` status `ready` deltaP `6.9905` edge `0.0994` maxDD `-4.9097`
- `news_risk_high->unknown_4h` score `0.3884` n `30` status `ready` deltaP `9.8272` edge `0.0566` maxDD `-2.7857`
- `market_context_high->equity_1h` score `-0.129` n `191` status `ready` deltaP `4.1446` edge `0.041` maxDD `-2.6836`
- `market_context_high->crypto_major_24h` score `-0.246` n `178` status `ready` deltaP `17.8176` edge `0.7193` maxDD `-62.3533`
- `market_context_high->fx_24h` score `-0.3182` n `178` status `ready` deltaP `10.3933` edge `0.0091` maxDD `-1.3925`
- `news_risk_high->unknown_1h` score `-0.4169` n `30` status `ready` deltaP `16.8563` edge `-0.1186` maxDD `-2.1115`
- `market_context_high->metal_4h` score `-0.4387` n `183` status `ready` deltaP `12.3959` edge `0.1303` maxDD `-12.5349`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
