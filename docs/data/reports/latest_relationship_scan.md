# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-25T07:52:19.243793+00:00`
- Price records: `672`
- Market context records: `1823`
- Flow alert records: `7145`
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

- `market_context_high->metal_24h` score `6.8572` n `178` status `ready` deltaP `27.5905` edge `0.6301` maxDD `-12.7414`
- `market_context_high->crypto_alt_4h` score `6.8278` n `186` status `ready` deltaP `22.148` edge `0.5358` maxDD `-5.1574`
- `news_risk_high->commodity_4h` score `6.5316` n `30` status `ready` deltaP `29.4106` edge `0.4137` maxDD `-3.5713`
- `market_context_high->crypto_major_4h` score `6.4288` n `186` status `ready` deltaP `26.0162` edge `0.4869` maxDD `-4.9684`
- `market_context_high->unknown_4h` score `4.5755` n `186` status `ready` deltaP `16.9322` edge `0.4708` maxDD `-9.8581`
- `market_context_high->index_24h` score `3.6262` n `178` status `ready` deltaP `17.8683` edge `0.3059` maxDD `-4.1604`
- `news_risk_high->commodity_1h` score `3.2111` n `30` status `ready` deltaP `24.4212` edge `0.1365` maxDD `-1.2043`
- `market_context_high->equity_4h` score `3.009` n `186` status `ready` deltaP `16.0504` edge `0.2532` maxDD `-5.0894`
- `market_context_high->unknown_24h` score `2.5608` n `178` status `ready` deltaP `13.8655` edge `0.653` maxDD `-35.8966`
- `market_context_high->equity_24h` score `2.4855` n `178` status `ready` deltaP `16.93` edge `0.5841` maxDD `-33.1875`
- `news_risk_high->fx_4h` score `0.9042` n `30` status `ready` deltaP `21.6362` edge `-0.0011` maxDD `-0.1774`
- `market_context_high->index_4h` score `0.8324` n `186` status `ready` deltaP `11.7247` edge `0.1001` maxDD `-3.7119`
- `market_context_high->crypto_major_1h` score `0.4361` n `194` status `ready` deltaP `6.218` edge `0.0935` maxDD `-3.2225`
- `market_context_high->crypto_alt_1h` score `0.3241` n `194` status `ready` deltaP `6.4171` edge `0.0956` maxDD `-4.9097`
- `news_risk_high->unknown_4h` score `0.2588` n `30` status `ready` deltaP `8.7601` edge `0.0471` maxDD `-2.7857`
- `market_context_high->equity_1h` score `-0.0523` n `194` status `ready` deltaP `4.8028` edge `0.043` maxDD `-2.6836`
- `market_context_high->crypto_major_24h` score `-0.1174` n `178` status `ready` deltaP `18.1648` edge `0.7277` maxDD `-62.3533`
- `market_context_high->fx_24h` score `-0.1754` n `178` status `ready` deltaP `11.6086` edge `0.0129` maxDD `-1.3925`
- `market_context_high->index_1h` score `-0.383` n `194` status `ready` deltaP `0.2809` edge `0.0122` maxDD `-1.7205`
- `news_risk_high->unknown_1h` score `-0.4107` n `30` status `ready` deltaP `16.8563` edge `-0.1178` maxDD `-2.1115`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
