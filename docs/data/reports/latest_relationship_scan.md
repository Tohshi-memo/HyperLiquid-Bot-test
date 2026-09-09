# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-09T02:52:30.175880+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10200`

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

- `risk_on_high->crypto_alt_24h` score `7.3766` n `117` status `ready` deltaP `17.7751` edge `0.5192` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `7.3766` n `117` status `ready` deltaP `17.7751` edge `0.5192` maxDD `-0.8386`
- `risk_on_high->crypto_alt_4h` score `5.95` n `117` status `ready` deltaP `32.1594` edge `0.3186` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `5.95` n `117` status `ready` deltaP `32.1594` edge `0.3186` maxDD `-1.9733`
- `risk_on_high->crypto_major_4h` score `4.1388` n `117` status `ready` deltaP `23.6945` edge `0.2728` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `4.1388` n `117` status `ready` deltaP `23.6945` edge `0.2728` maxDD `-3.8693`
- `risk_on_high->crypto_major_24h` score `4.1057` n `117` status `ready` deltaP `17.4546` edge `0.8168` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `4.1057` n `117` status `ready` deltaP `17.4546` edge `0.8168` maxDD `-24.5429`
- `market_context_high->crypto_alt_24h` score `2.3292` n `241` status `ready` deltaP `10.4303` edge `0.2073` maxDD `-3.9523`
- `risk_on_high->index_24h` score `1.4169` n `117` status `ready` deltaP `16.1859` edge `0.0144` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `1.4169` n `117` status `ready` deltaP `16.1859` edge `0.0144` maxDD `-0.0051`
- `risk_on_high->crypto_alt_1h` score `1.0125` n `117` status `ready` deltaP `4.3964` edge `0.0903` maxDD `-1.1521`
- `risk_on_and_context->crypto_alt_1h` score `1.0125` n `117` status `ready` deltaP `4.3964` edge `0.0903` maxDD `-1.1521`
- `market_context_high->index_24h` score `0.6954` n `241` status `ready` deltaP `11.2811` edge `0.0221` maxDD `-0.1483`
- `risk_on_high->metal_1h` score `0.1609` n `117` status `ready` deltaP `8.1824` edge `-0.0009` maxDD `-0.3081`
- `risk_on_and_context->metal_1h` score `0.1609` n `117` status `ready` deltaP `8.1824` edge `-0.0009` maxDD `-0.3081`
- `risk_on_high->index_1h` score `0.1196` n `117` status `ready` deltaP `8.5202` edge `-0.0051` maxDD `-0.5764`
- `risk_on_and_context->index_1h` score `0.1196` n `117` status `ready` deltaP `8.5202` edge `-0.0051` maxDD `-0.5764`
- `risk_on_high->equity_1h` score `0.1009` n `117` status `ready` deltaP `11.9774` edge `-0.0183` maxDD `-2.2516`
- `risk_on_and_context->equity_1h` score `0.1009` n `117` status `ready` deltaP `11.9774` edge `-0.0183` maxDD `-2.2516`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
