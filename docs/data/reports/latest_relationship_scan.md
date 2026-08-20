# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-20T16:02:48.873035+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `10819`

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

- `market_context_high->equity_4h` score `0.6248` n `105` status `ready` deltaP `7.6365` edge `0.1641` maxDD `-8.3685`
- `market_context_high->equity_1h` score `0.4648` n `105` status `ready` deltaP `9.3185` edge `0.0581` maxDD `-3.1861`
- `market_context_high->index_1h` score `0.3275` n `105` status `ready` deltaP `10.4078` edge `0.0066` maxDD `-0.5622`
- `market_context_high->metal_4h` score `0.1136` n `105` status `ready` deltaP `11.2558` edge `-0.0029` maxDD `-1.273`
- `market_context_high->fx_4h` score `0.0218` n `105` status `ready` deltaP `7.0281` edge `0.0062` maxDD `-0.3539`
- `market_context_high->commodity_24h` score `-0.1013` n `96` status `ready` deltaP `4.3403` edge `0.1414` maxDD `-4.666`
- `market_context_high->metal_1h` score `-0.1957` n `105` status `ready` deltaP `3.2378` edge `0.0008` maxDD `-0.4291`
- `market_context_high->fx_1h` score `-0.2099` n `105` status `ready` deltaP `0.7756` edge `0.0038` maxDD `-0.2043`
- `market_context_high->index_4h` score `-0.2357` n `105` status `ready` deltaP `6.3429` edge `0.0199` maxDD `-1.7252`
- `market_context_high->unknown_1h` score `-0.4001` n `105` status `ready` deltaP `7.1814` edge `-0.0585` maxDD `-0.4843`
- `market_context_high->crypto_alt_1h` score `-0.487` n `105` status `ready` deltaP `1.5498` edge `0.0074` maxDD `-2.413`
- `market_context_high->crypto_major_1h` score `-0.6594` n `105` status `ready` deltaP `1.6866` edge `-0.0113` maxDD `-2.7581`
- `market_context_high->commodity_4h` score `-0.7072` n `105` status `ready` deltaP `-2.1951` edge `0.009` maxDD `-2.4692`
- `market_context_high->commodity_1h` score `-0.772` n `105` status `ready` deltaP `-6.3273` edge `-0.0002` maxDD `-1.1941`
- `market_context_high->crypto_alt_4h` score `-1.2948` n `105` status `ready` deltaP `4.7387` edge `-0.0125` maxDD `-5.4926`
- `market_context_high->crypto_major_4h` score `-1.5303` n `105` status `ready` deltaP `6.8351` edge `-0.071` maxDD `-3.1677`
- `market_context_high->unknown_24h` score `-1.7085` n `96` status `ready` deltaP `17.7083` edge `-0.2098` maxDD `-1.0505`
- `market_context_high->index_24h` score `-3.5838` n `96` status `ready` deltaP `1.2152` edge `-0.0508` maxDD `-18.3411`
- `market_context_high->fx_24h` score `-3.7886` n `96` status `ready` deltaP `-21.1805` edge `-0.0162` maxDD `-1.9981`
- `market_context_high->metal_24h` score `-4.9502` n `96` status `ready` deltaP `-21.0069` edge `-0.1638` maxDD `-11.4635`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
