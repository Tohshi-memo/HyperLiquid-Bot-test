# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-13T13:07:29.168467+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `12978`

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

- `market_context_high->unknown_24h` score `18098.6758` n `56` status `ready` deltaP `11.8226` edge `1508.1586` maxDD `-0.4878`
- `news_risk_high->unknown_1h` score `414.0074` n `82` status `ready` deltaP `-4.6517` edge `34.5738` maxDD `-1.7068`
- `news_risk_high->crypto_major_24h` score `18.097` n `82` status `ready` deltaP `37.8512` edge `1.4028` maxDD `-9.098`
- `news_risk_high->crypto_alt_24h` score `18.092` n `82` status `ready` deltaP `34.1337` edge `1.3289` maxDD `-2.2369`
- `market_context_high->crypto_alt_24h` score `10.3449` n `56` status `ready` deltaP `24.4212` edge `0.782` maxDD `-3.9523`
- `news_risk_high->equity_24h` score `8.1193` n `82` status `ready` deltaP `23.4777` edge `0.6981` maxDD `-6.5742`
- `market_context_high->equity_24h` score `7.6146` n `56` status `ready` deltaP `41.4655` edge `0.4893` maxDD `-8.1614`
- `news_risk_high->index_24h` score `6.721` n `82` status `ready` deltaP `47.767` edge `0.2593` maxDD `-0.0797`
- `news_risk_high->metal_24h` score `4.5648` n `82` status `ready` deltaP `24.2431` edge `0.2642` maxDD `-0.6334`
- `market_context_high->index_24h` score `4.0753` n `56` status `ready` deltaP `45.7636` edge `0.0801` maxDD `-1.3132`
- `market_context_high->commodity_24h` score `4.037` n `56` status `ready` deltaP `39.8276` edge `0.0709` maxDD `0.0`
- `market_context_high->metal_24h` score `1.4369` n `56` status `ready` deltaP `17.0567` edge `0.1259` maxDD `-1.0984`
- `risk_on_high->crypto_alt_4h` score `0.4994` n `65` status `ready` deltaP `11.2938` edge `0.1562` maxDD `-6.7304`
- `risk_on_and_context->crypto_alt_4h` score `0.4994` n `65` status `ready` deltaP `11.2938` edge `0.1562` maxDD `-6.7304`
- `news_risk_high->index_4h` score `0.4203` n `82` status `ready` deltaP `12.4234` edge `0.0339` maxDD `-0.6935`
- `risk_on_high->fx_1h` score `0.1101` n `65` status `ready` deltaP `4.7029` edge `0.0034` maxDD `-0.0464`
- `risk_on_and_context->fx_1h` score `0.1101` n `65` status `ready` deltaP `4.7029` edge `0.0034` maxDD `-0.0464`
- `risk_on_high->metal_1h` score `-0.0113` n `65` status `ready` deltaP `4.5117` edge `0.002` maxDD `-0.3081`
- `risk_on_and_context->metal_1h` score `-0.0113` n `65` status `ready` deltaP `4.5117` edge `0.002` maxDD `-0.3081`
- `market_context_high->fx_1h` score `-0.0556` n `144` status `ready` deltaP `3.7841` edge `-0.0007` maxDD `-0.5323`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
