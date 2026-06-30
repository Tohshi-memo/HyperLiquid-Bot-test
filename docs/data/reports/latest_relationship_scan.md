# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-30T10:37:25.482946+00:00`
- Price records: `672`
- Market context records: `5240`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5604`

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

- `market_context_high->unknown_24h` score `23.8247` n `130` status `ready` deltaP `31.6453` edge `1.7934` maxDD `-0.8515`
- `market_context_high->crypto_major_24h` score `12.8508` n `130` status `ready` deltaP `32.7244` edge `1.2189` maxDD `-22.6266`
- `market_context_high->crypto_alt_24h` score `6.2996` n `130` status `ready` deltaP `21.21` edge `0.7431` maxDD `-23.4292`
- `market_context_high->crypto_alt_4h` score `4.2365` n `155` status `ready` deltaP `14.3037` edge `0.4176` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `4.0808` n `155` status `ready` deltaP `15.1367` edge `0.4684` maxDD `-14.0065`
- `market_context_high->unknown_4h` score `2.2494` n `155` status `ready` deltaP `17.44` edge `0.1734` maxDD `-5.5109`
- `market_context_high->unknown_1h` score `1.6258` n `156` status `ready` deltaP `8.1798` edge `0.1451` maxDD `-2.7986`
- `market_context_high->equity_24h` score `1.5374` n `130` status `ready` deltaP `17.9995` edge `0.571` maxDD `-40.0306`
- `market_context_high->fx_24h` score `0.5934` n `130` status `ready` deltaP `13.4829` edge `0.0491` maxDD `-0.8294`
- `market_context_high->crypto_alt_1h` score `0.4897` n `156` status `ready` deltaP `4.9593` edge `0.1039` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `0.394` n `156` status `ready` deltaP `6.3719` edge `0.1149` maxDD `-6.9639`
- `market_context_high->equity_4h` score `0.2495` n `155` status `ready` deltaP `6.7879` edge `0.1394` maxDD `-7.4425`
- `market_context_high->index_24h` score `-0.1042` n `130` status `ready` deltaP `17.9914` edge `0.0302` maxDD `-7.413`
- `market_context_high->equity_1h` score `-0.148` n `156` status `ready` deltaP `5.6387` edge `0.0466` maxDD `-5.0555`
- `market_context_high->metal_1h` score `-0.1745` n `156` status `ready` deltaP `3.827` edge `0.0113` maxDD `-2.0682`
- `market_context_high->index_1h` score `-0.2098` n `156` status `ready` deltaP `3.6734` edge `0.0084` maxDD `-1.0296`
- `market_context_high->fx_1h` score `-0.3013` n `156` status `ready` deltaP `1.0671` edge `-0.0005` maxDD `-0.6194`
- `market_context_high->commodity_1h` score `-0.665` n `156` status `ready` deltaP `-0.2994` edge `-0.0024` maxDD `-2.4692`
- `market_context_high->fx_4h` score `-0.775` n `155` status `ready` deltaP `0.2901` edge `0.0021` maxDD `-1.6047`
- `market_context_high->index_4h` score `-0.8509` n `155` status `ready` deltaP `3.6192` edge `0.0167` maxDD `-2.9391`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
