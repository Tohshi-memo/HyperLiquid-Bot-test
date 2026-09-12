# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-12T16:07:30.921652+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `12636`

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

- `market_context_high->unknown_24h` score `6509.1956` n `91` status `ready` deltaP `13.2536` edge `542.3498` maxDD `-0.082`
- `risk_on_high->unknown_24h` score `4157.7385` n `46` status `ready` deltaP `15.4514` edge `346.3752` maxDD `0.0`
- `risk_on_and_context->unknown_24h` score `4157.7385` n `46` status `ready` deltaP `15.4514` edge `346.3752` maxDD `0.0`
- `news_risk_high->unknown_1h` score `382.9648` n `82` status `ready` deltaP `-5.5499` edge `31.9929` maxDD `-1.7068`
- `news_risk_high->crypto_major_24h` score `23.227` n `62` status `ready` deltaP `51.9041` edge `1.6796` maxDD `-5.8705`
- `risk_on_high->crypto_alt_24h` score `17.3417` n `46` status `ready` deltaP `39.304` edge `1.2061` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `17.3417` n `46` status `ready` deltaP `39.304` edge `1.2061` maxDD `-0.8386`
- `news_risk_high->crypto_alt_24h` score `17.0191` n `62` status `ready` deltaP `27.593` edge `1.2831` maxDD `-2.2369`
- `market_context_high->crypto_alt_24h` score `15.2681` n `91` status `ready` deltaP `32.5912` edge `1.1378` maxDD `-3.9523`
- `news_risk_high->equity_24h` score `11.4441` n `62` status `ready` deltaP `31.6924` edge `0.7701` maxDD `-1.2164`
- `risk_on_high->equity_24h` score `9.3822` n `46` status `ready` deltaP `39.7569` edge `0.5168` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `9.3822` n `46` status `ready` deltaP `39.7569` edge `0.5168` maxDD `0.0`
- `market_context_high->equity_24h` score `9.0534` n `91` status `ready` deltaP `39.7569` edge `0.4894` maxDD `0.0`
- `risk_on_high->crypto_alt_4h` score `8.5417` n `46` status `ready` deltaP `41.8015` edge `0.4703` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `8.5417` n `46` status `ready` deltaP `41.8015` edge `0.4703` maxDD `-1.9733`
- `news_risk_high->metal_24h` score `7.7609` n `62` status `ready` deltaP `49.8488` edge `0.3303` maxDD `-0.2708`
- `news_risk_high->index_24h` score `7.411` n `62` status `ready` deltaP `48.0119` edge `0.311` maxDD `-0.0797`
- `risk_on_high->index_24h` score `4.8856` n `46` status `ready` deltaP `49.5547` edge `0.081` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `4.8856` n `46` status `ready` deltaP `49.5547` edge `0.081` maxDD `-0.0051`
- `risk_on_high->equity_4h` score `4.1296` n `46` status `ready` deltaP `36.5787` edge `0.1096` maxDD `-0.079`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
