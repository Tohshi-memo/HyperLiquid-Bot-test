# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-23T17:07:30.964170+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9834`

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

- `market_context_high->unknown_1h` score `81.3139` n `47` status `ready` deltaP `9.6669` edge `6.7188` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `31.6402` n `46` status `ready` deltaP `17.3536` edge `2.5366` maxDD `-0.5817`
- `market_context_high->equity_24h` score `17.9048` n `46` status `ready` deltaP `14.7494` edge `1.4038` maxDD `-0.1382`
- `market_context_high->crypto_alt_24h` score `14.1225` n `46` status `ready` deltaP `12.3264` edge `1.0947` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `6.9467` n `96` status `ready` deltaP `-5.3819` edge `1.3006` maxDD `-46.1999`
- `market_context_high->index_24h` score `6.0649` n `46` status `ready` deltaP `23.7772` edge `0.3556` maxDD `-0.03`
- `news_risk_high->crypto_major_4h` score `4.0312` n `103` status `ready` deltaP `16.0609` edge `0.2866` maxDD `-2.619`
- `news_risk_high->crypto_alt_4h` score `3.4671` n `103` status `ready` deltaP `10.878` edge `0.3162` maxDD `-5.9838`
- `news_risk_high->commodity_24h` score `3.0956` n `96` status `ready` deltaP `28.2986` edge `0.1872` maxDD `-2.431`
- `market_context_high->index_4h` score `2.5104` n `46` status `ready` deltaP `29.1092` edge `0.0285` maxDD `-0.0692`
- `news_risk_high->crypto_alt_1h` score `2.2596` n `103` status `ready` deltaP `12.1098` edge `0.1566` maxDD `-1.5895`
- `news_risk_high->crypto_major_1h` score `1.9413` n `103` status `ready` deltaP `15.4032` edge `0.1026` maxDD `-1.8141`
- `market_context_high->equity_4h` score `1.3519` n `46` status `ready` deltaP `9.6633` edge `0.0789` maxDD `-0.4529`
- `news_risk_high->fx_4h` score `1.2957` n `103` status `ready` deltaP `19.8704` edge `0.0391` maxDD `-0.421`
- `news_risk_high->crypto_alt_24h` score `1.2316` n `96` status `ready` deltaP `-7.4653` edge `0.6405` maxDD `-32.7147`
- `news_risk_high->fx_24h` score `1.1779` n `96` status `ready` deltaP `28.2986` edge `0.1213` maxDD `-1.7159`
- `market_context_high->index_1h` score `0.6984` n `47` status `ready` deltaP `11.6161` edge `0.0086` maxDD `-0.2275`
- `news_risk_high->metal_1h` score `0.6566` n `103` status `ready` deltaP `15.2026` edge `0.0127` maxDD `-0.7468`
- `market_context_high->metal_24h` score `0.6033` n `46` status `ready` deltaP `17.7537` edge `-0.0447` maxDD `-0.2042`
- `market_context_high->equity_1h` score `0.4273` n `47` status `ready` deltaP `7.2748` edge `0.0274` maxDD `-1.5564`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
