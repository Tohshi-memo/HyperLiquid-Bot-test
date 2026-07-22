# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-22T19:37:28.951457+00:00`
- Price records: `672`
- Market context records: `7595`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14551`

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

- `market_context_high->unknown_24h` score `0.4635` n `145` status `ready` deltaP `12.6389` edge `0.1202` maxDD `-5.9358`
- `market_context_high->commodity_24h` score `0.419` n `144` status `ready` deltaP `15.7448` edge `0.0883` maxDD `-7.0012`
- `market_context_high->equity_24h` score `0.1432` n `144` status `ready` deltaP `17.5039` edge `0.5368` maxDD `-45.4777`
- `market_context_high->index_1h` score `0.0743` n `149` status `ready` deltaP `6.8445` edge `0.0118` maxDD `-0.8324`
- `market_context_high->commodity_4h` score `-0.0575` n `149` status `ready` deltaP `7.7274` edge `0.0197` maxDD `-2.4139`
- `market_context_high->crypto_major_1h` score `-0.2674` n `149` status `ready` deltaP `7.269` edge `0.0179` maxDD `-4.3848`
- `market_context_high->fx_24h` score `-0.301` n `144` status `ready` deltaP `9.5964` edge `0.0197` maxDD `-3.0343`
- `market_context_high->crypto_alt_1h` score `-0.3039` n `149` status `ready` deltaP `1.4558` edge `0.0166` maxDD `-2.8881`
- `market_context_high->commodity_1h` score `-0.3082` n `149` status `ready` deltaP `4.5649` edge `0.0011` maxDD `-1.5775`
- `market_context_high->equity_1h` score `-0.4616` n `149` status `ready` deltaP `6.3234` edge `0.0549` maxDD `-7.8324`
- `market_context_high->index_4h` score `-0.64` n `149` status `ready` deltaP `9.0348` edge `0.0297` maxDD `-3.4253`
- `market_context_high->fx_1h` score `-0.657` n `149` status `ready` deltaP `-0.4675` edge `-0.0017` maxDD `-0.6615`
- `market_context_high->metal_1h` score `-0.6664` n `149` status `ready` deltaP `0.8721` edge `0.0133` maxDD `-1.0307`
- `market_context_high->unknown_1h` score `-0.9771` n `149` status `ready` deltaP `-0.4079` edge `-0.0602` maxDD `-1.3217`
- `market_context_high->crypto_alt_4h` score `-1.0913` n `149` status `ready` deltaP `2.349` edge `0.0501` maxDD `-9.7866`
- `market_context_high->crypto_major_4h` score `-1.2779` n `149` status `ready` deltaP `7.932` edge `0.061` maxDD `-15.217`
- `market_context_high->equity_4h` score `-1.5795` n `149` status `ready` deltaP `2.935` edge `0.2072` maxDD `-21.341`
- `market_context_high->metal_4h` score `-1.6974` n `149` status `ready` deltaP `-1.9848` edge `0.0436` maxDD `-4.8385`
- `market_context_high->metal_24h` score `-2.1306` n `145` status `ready` deltaP `-1.796` edge `0.1099` maxDD `-10.0193`
- `market_context_high->fx_4h` score `-2.4619` n `149` status `ready` deltaP `-4.9494` edge `-0.0037` maxDD `-2.1439`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
