# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-02T15:07:28.005146+00:00`
- Price records: `672`
- Market context records: `2673`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9240`

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

- `market_context_high->crypto_alt_24h` score `9.0089` n `111` status `ready` deltaP `16.0051` edge `0.9934` maxDD `-19.9486`
- `market_context_high->unknown_24h` score `8.5553` n `111` status `ready` deltaP `17.3048` edge `0.6304` maxDD `-1.626`
- `market_context_high->crypto_alt_4h` score `3.9437` n `127` status `ready` deltaP `21.9092` edge `0.4477` maxDD `-15.2094`
- `market_context_high->crypto_major_4h` score `1.9157` n `127` status `ready` deltaP `9.7417` edge `0.2757` maxDD `-10.1468`
- `market_context_high->unknown_4h` score `1.5723` n `127` status `ready` deltaP `8.1153` edge `0.1819` maxDD `-3.7312`
- `market_context_high->index_4h` score `-0.0613` n `127` status `ready` deltaP `8.6986` edge `0.0183` maxDD `-2.3986`
- `market_context_high->crypto_alt_1h` score `-0.0708` n `136` status `ready` deltaP `7.2032` edge `0.0706` maxDD `-6.8821`
- `market_context_high->fx_24h` score `-0.1555` n `111` status `ready` deltaP `10.8202` edge `0.0021` maxDD `-0.6418`
- `market_context_high->index_1h` score `-0.1836` n `136` status `ready` deltaP `2.7254` edge `0.0077` maxDD `-1.2855`
- `market_context_high->unknown_1h` score `-0.2352` n `136` status `ready` deltaP `2.316` edge `0.0229` maxDD `-1.9684`
- `market_context_high->index_24h` score `-0.2818` n `111` status `ready` deltaP `6.7943` edge `0.0293` maxDD `-2.5127`
- `market_context_high->commodity_1h` score `-0.3841` n `136` status `ready` deltaP `2.8179` edge `0.0073` maxDD `-4.3601`
- `market_context_high->fx_4h` score `-0.4751` n `127` status `ready` deltaP `1.9169` edge `0.013` maxDD `-0.5631`
- `market_context_high->commodity_24h` score `-0.5015` n `111` status `ready` deltaP `7.9627` edge `0.192` maxDD `-12.4171`
- `market_context_high->fx_1h` score `-0.5248` n `136` status `ready` deltaP `-0.4887` edge `0.0039` maxDD `-0.2164`
- `market_context_high->crypto_major_1h` score `-0.5894` n `136` status `ready` deltaP `3.9627` edge `0.0473` maxDD `-6.6093`
- `market_context_high->metal_1h` score `-0.7687` n `136` status `ready` deltaP `-1.7568` edge `-0.0045` maxDD `-2.9203`
- `market_context_high->commodity_4h` score `-1.2447` n `127` status `ready` deltaP `3.4413` edge `0.0095` maxDD `-10.0279`
- `market_context_high->metal_4h` score `-1.2942` n `127` status `ready` deltaP `-0.6974` edge `-0.0103` maxDD `-6.0774`
- `market_context_high->equity_1h` score `-1.3106` n `136` status `ready` deltaP `-5.169` edge `0.0091` maxDD `-2.7085`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
