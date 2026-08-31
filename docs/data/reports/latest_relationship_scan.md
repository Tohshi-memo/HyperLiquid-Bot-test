# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-31T17:22:29.680228+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11704`

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

- `risk_on_high->unknown_4h` score `7.9652` n `107` status `ready` deltaP `24.1837` edge `0.5642` maxDD `-2.266`
- `risk_on_and_context->unknown_4h` score `7.9652` n `107` status `ready` deltaP `24.1837` edge `0.5642` maxDD `-2.266`
- `market_context_high->unknown_4h` score `6.4192` n `159` status `ready` deltaP `20.8803` edge `0.4651` maxDD `-2.5493`
- `risk_on_high->crypto_alt_24h` score `4.6868` n `75` status `ready` deltaP `24.8334` edge `0.9041` maxDD `-30.1695`
- `risk_on_and_context->crypto_alt_24h` score `4.6868` n `75` status `ready` deltaP `24.8334` edge `0.9041` maxDD `-30.1695`
- `risk_on_high->unknown_1h` score `2.5125` n `107` status `ready` deltaP `7.264` edge `0.2186` maxDD `-1.9453`
- `risk_on_and_context->unknown_1h` score `2.5125` n `107` status `ready` deltaP `7.264` edge `0.2186` maxDD `-1.9453`
- `market_context_high->unknown_1h` score `2.2899` n `159` status `ready` deltaP `6.6057` edge `0.2098` maxDD `-2.041`
- `risk_on_high->fx_24h` score `2.0783` n `75` status `ready` deltaP `51.1111` edge `0.0336` maxDD `-1.9648`
- `risk_on_and_context->fx_24h` score `2.0783` n `75` status `ready` deltaP `51.1111` edge `0.0336` maxDD `-1.9648`
- `risk_on_high->commodity_24h` score `1.7624` n `75` status `ready` deltaP `12.1598` edge `0.1646` maxDD `-0.5706`
- `risk_on_and_context->commodity_24h` score `1.7624` n `75` status `ready` deltaP `12.1598` edge `0.1646` maxDD `-0.5706`
- `news_risk_high->unknown_1h` score `1.609` n `61` status `ready` deltaP `4.3683` edge `0.1396` maxDD `-1.1043`
- `market_context_high->crypto_alt_24h` score `1.4311` n `118` status `ready` deltaP `11.7938` edge `0.5436` maxDD `-32.2376`
- `market_context_high->fx_24h` score `0.9473` n `118` status `ready` deltaP `32.0151` edge `0.0234` maxDD `-2.6312`
- `news_risk_high->commodity_4h` score `0.3079` n `61` status `ready` deltaP `8.2542` edge `0.0261` maxDD `-1.3325`
- `news_risk_high->commodity_24h` score `0.2258` n `44` status `ready` deltaP `5.1295` edge `0.0263` maxDD `-1.1904`
- `market_context_high->commodity_1h` score `0.2091` n `159` status `ready` deltaP `9.6298` edge `0.0182` maxDD `-1.5315`
- `market_context_high->metal_24h` score `0.1988` n `118` status `ready` deltaP `22.1986` edge `0.139` maxDD `-10.5867`
- `news_risk_high->fx_4h` score `0.1963` n `61` status `ready` deltaP `11.263` edge `0.0006` maxDD `-0.7461`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
