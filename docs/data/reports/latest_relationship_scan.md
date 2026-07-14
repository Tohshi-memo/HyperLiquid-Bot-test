# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-14T04:22:26.238378+00:00`
- Price records: `672`
- Market context records: `6674`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11784`

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

- `market_context_high->unknown_1h` score `2.6881` n `202` status `ready` deltaP `-4.2138` edge `0.3422` maxDD `-3.2083`
- `market_context_high->commodity_24h` score `1.201` n `202` status `ready` deltaP `12.2852` edge `0.205` maxDD `-5.2791`
- `market_context_high->unknown_4h` score `0.3145` n `202` status `ready` deltaP `-13.7436` edge `0.3584` maxDD `-10.5788`
- `market_context_high->crypto_major_1h` score `0.0499` n `202` status `ready` deltaP `8.0127` edge `0.0473` maxDD `-4.2122`
- `market_context_high->crypto_alt_1h` score `-0.1296` n `202` status `ready` deltaP `5.5834` edge `0.0409` maxDD `-3.7803`
- `market_context_high->unknown_24h` score `-0.229` n `202` status `ready` deltaP `-3.9346` edge `0.3721` maxDD `-12.3511`
- `market_context_high->fx_1h` score `-0.2318` n `202` status `ready` deltaP `2.9718` edge `0.0012` maxDD `-0.7249`
- `market_context_high->index_1h` score `-0.4969` n `202` status `ready` deltaP `0.5647` edge `0.0043` maxDD `-0.7417`
- `market_context_high->commodity_1h` score `-0.6549` n `202` status `ready` deltaP `-0.9219` edge `-0.0095` maxDD `-2.1314`
- `market_context_high->index_4h` score `-0.8572` n `202` status `ready` deltaP `10.5862` edge `0.0075` maxDD `-5.7046`
- `market_context_high->equity_1h` score `-0.894` n `202` status `ready` deltaP `3.3156` edge `0.0061` maxDD `-3.8827`
- `market_context_high->metal_1h` score `-1.2655` n `202` status `ready` deltaP `-4.5355` edge `-0.0011` maxDD `-1.5966`
- `market_context_high->crypto_major_4h` score `-1.3234` n `202` status `ready` deltaP `9.5976` edge `0.0978` maxDD `-16.8495`
- `market_context_high->fx_4h` score `-1.3995` n `202` status `ready` deltaP `6.253` edge `0.0001` maxDD `-3.3635`
- `market_context_high->commodity_4h` score `-1.4881` n `202` status `ready` deltaP `-1.6814` edge `-0.0301` maxDD `-5.6246`
- `market_context_high->crypto_alt_4h` score `-1.6242` n `202` status `ready` deltaP `6.8929` edge `0.086` maxDD `-19.2145`
- `market_context_high->metal_4h` score `-2.0927` n `202` status `ready` deltaP `-0.9071` edge `0.0238` maxDD `-5.2172`
- `market_context_high->equity_4h` score `-4.7822` n `202` status `ready` deltaP `7.6944` edge `-0.0229` maxDD `-27.1529`
- `market_context_high->fx_24h` score `-6.4242` n `202` status `ready` deltaP `-12.3367` edge `-0.0132` maxDD `-10.8591`
- `market_context_high->metal_24h` score `-6.9162` n `202` status `ready` deltaP `-5.3664` edge `-0.0024` maxDD `-28.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
