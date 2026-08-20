# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-20T16:22:26.653166+00:00`
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

- `market_context_high->equity_4h` score `0.6308` n `105` status `ready` deltaP `7.6365` edge `0.1646` maxDD `-8.3685`
- `market_context_high->equity_1h` score `0.4887` n `105` status `ready` deltaP `9.4682` edge `0.0591` maxDD `-3.1861`
- `market_context_high->index_1h` score `0.3419` n `105` status `ready` deltaP `10.5575` edge `0.0068` maxDD `-0.5622`
- `market_context_high->metal_4h` score `0.0994` n `105` status `ready` deltaP `11.1034` edge `-0.0037` maxDD `-1.273`
- `market_context_high->fx_4h` score `0.0131` n `105` status `ready` deltaP `6.8757` edge `0.0061` maxDD `-0.3539`
- `market_context_high->commodity_24h` score `-0.1029` n `96` status `ready` deltaP `4.3403` edge `0.1412` maxDD `-4.666`
- `market_context_high->metal_1h` score `-0.1826` n `105` status `ready` deltaP `3.3875` edge `0.0009` maxDD `-0.4291`
- `market_context_high->fx_1h` score `-0.2185` n `105` status `ready` deltaP `0.6259` edge `0.0037` maxDD `-0.2043`
- `market_context_high->index_4h` score `-0.2364` n `105` status `ready` deltaP `6.3429` edge `0.0198` maxDD `-1.7252`
- `market_context_high->unknown_1h` score `-0.4241` n `105` status `ready` deltaP `7.0317` edge `-0.0595` maxDD `-0.4843`
- `market_context_high->crypto_alt_1h` score `-0.5033` n `105` status `ready` deltaP `1.4001` edge `0.0063` maxDD `-2.413`
- `market_context_high->crypto_major_1h` score `-0.6796` n `105` status `ready` deltaP `1.5369` edge `-0.0129` maxDD `-2.7581`
- `market_context_high->commodity_4h` score `-0.7095` n `105` status `ready` deltaP `-2.1951` edge `0.0087` maxDD `-2.4692`
- `market_context_high->commodity_1h` score `-0.7829` n `105` status `ready` deltaP `-6.477` edge `-0.0006` maxDD `-1.1941`
- `market_context_high->crypto_alt_4h` score `-1.3322` n `105` status `ready` deltaP `4.5863` edge `-0.0146` maxDD `-5.4926`
- `market_context_high->crypto_major_4h` score `-1.5711` n `105` status `ready` deltaP `6.8351` edge `-0.0744` maxDD `-3.1677`
- `market_context_high->unknown_24h` score `-1.7481` n `96` status `ready` deltaP `17.7083` edge `-0.2131` maxDD `-1.0505`
- `market_context_high->index_24h` score `-3.583` n `96` status `ready` deltaP `1.2152` edge `-0.0507` maxDD `-18.3411`
- `market_context_high->fx_24h` score `-3.791` n `96` status `ready` deltaP `-21.1805` edge `-0.0164` maxDD `-1.9981`
- `market_context_high->metal_24h` score `-4.951` n `96` status `ready` deltaP `-21.0069` edge `-0.1639` maxDD `-11.4635`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
