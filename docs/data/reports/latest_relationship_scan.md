# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-25T03:37:27.458725+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4080`

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

- `market_context_high->unknown_1h` score `32251.4101` n `45` status `ready` deltaP `2.1656` edge `2687.6125` maxDD `-0.4209`
- `market_context_high->unknown_4h` score `21978.7597` n `45` status `ready` deltaP `3.1776` edge `1831.556` maxDD `-0.7765`
- `news_risk_high->unknown_1h` score `1016.4551` n `31` status `ready` deltaP `2.3807` edge `84.7063` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `725.8122` n `31` status `ready` deltaP `4.3962` edge `60.4607` maxDD `-0.1191`
- `news_risk_high->equity_24h` score `39.0053` n `31` status `ready` deltaP `44.2708` edge `2.9553` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `38.9615` n `31` status `ready` deltaP `50.1736` edge `2.9123` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `35.2703` n `31` status `ready` deltaP `48.9583` edge `2.6128` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `11.9578` n `31` status `ready` deltaP `27.8275` edge `0.898` maxDD `-5.2957`
- `news_risk_high->metal_24h` score `11.207` n `31` status `ready` deltaP `41.2355` edge `0.6865` maxDD `-0.1986`
- `news_risk_high->equity_4h` score `10.5733` n `31` status `ready` deltaP `35.3954` edge `0.6932` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `7.4559` n `31` status `ready` deltaP `18.3025` edge `0.9756` maxDD `-7.6714`
- `news_risk_high->index_24h` score `5.8909` n `31` status `ready` deltaP `43.5764` edge `0.2004` maxDD `0.0`
- `news_risk_high->fx_24h` score `5.431` n `31` status `ready` deltaP `46.0518` edge `0.1584` maxDD `-0.0262`
- `news_risk_high->equity_1h` score `3.7436` n `31` status `ready` deltaP `19.3886` edge `0.2014` maxDD `-0.1621`
- `news_risk_high->index_4h` score `3.1779` n `31` status `ready` deltaP `34.1759` edge `0.063` maxDD `-0.4146`
- `news_risk_high->crypto_major_1h` score `2.7392` n `31` status `ready` deltaP `12.4058` edge `0.3146` maxDD `-1.6897`
- `news_risk_high->index_1h` score `2.6303` n `31` status `ready` deltaP `31.0943` edge `0.0204` maxDD `-0.0136`
- `market_context_high->fx_4h` score `2.5968` n `45` status `ready` deltaP `31.7649` edge `0.0331` maxDD `-0.2774`
- `news_risk_high->crypto_alt_1h` score `2.3954` n `31` status `ready` deltaP `12.5555` edge `0.2591` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.5804` n `31` status `ready` deltaP `30.0318` edge `0.0303` maxDD `-0.2315`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
