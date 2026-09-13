# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-13T15:07:33.350744+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13378`

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

- `market_context_high->unknown_24h` score `17867.8865` n `56` status `ready` deltaP `8.596` edge `1488.9534` maxDD `-0.613`
- `risk_on_high->unknown_24h` score `11234.9392` n `32` status `ready` deltaP `13.0603` edge `936.1636` maxDD `-0.1252`
- `risk_on_and_context->unknown_24h` score `11234.9392` n `32` status `ready` deltaP `13.0603` edge `936.1636` maxDD `-0.1252`
- `news_risk_high->unknown_1h` score `421.7895` n `82` status `ready` deltaP `-4.8014` edge `35.2233` maxDD `-1.7068`
- `news_risk_high->crypto_alt_24h` score `18.3067` n `82` status `ready` deltaP `34.8234` edge `1.3422` maxDD `-2.2369`
- `news_risk_high->crypto_major_24h` score `18.3064` n `82` status `ready` deltaP `38.0236` edge `1.4191` maxDD `-9.098`
- `news_risk_high->equity_24h` score `8.5548` n `82` status `ready` deltaP `24.857` edge `0.7252` maxDD `-6.5742`
- `news_risk_high->index_24h` score `6.8356` n `82` status `ready` deltaP `48.6291` edge `0.2631` maxDD `-0.0797`
- `risk_on_high->crypto_alt_24h` score `5.7142` n `32` status `ready` deltaP `23.7716` edge `0.6211` maxDD `-2.0921`
- `risk_on_and_context->crypto_alt_24h` score `5.7142` n `32` status `ready` deltaP `23.7716` edge `0.6211` maxDD `-2.0921`
- `market_context_high->crypto_alt_24h` score `5.3389` n `56` status `ready` deltaP `17.968` edge `0.6567` maxDD `-4.6943`
- `news_risk_high->metal_24h` score `4.5564` n `82` status `ready` deltaP `24.2431` edge `0.2635` maxDD `-0.6334`
- `market_context_high->commodity_24h` score `4.1342` n `56` status `ready` deltaP `39.8276` edge `0.079` maxDD `0.0`
- `risk_on_high->commodity_24h` score `4.0934` n `32` status `ready` deltaP `39.8276` edge `0.0756` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `4.0934` n `32` status `ready` deltaP `39.8276` edge `0.0756` maxDD `0.0`
- `market_context_high->metal_24h` score `2.3388` n `56` status `ready` deltaP `17.0567` edge `0.1326` maxDD `-0.7798`
- `risk_on_high->index_24h` score `1.9185` n `32` status `ready` deltaP `39.4828` edge `0.0427` maxDD `-2.1304`
- `risk_on_and_context->index_24h` score `1.9185` n `32` status `ready` deltaP `39.4828` edge `0.0427` maxDD `-2.1304`
- `risk_on_high->equity_24h` score `1.6513` n `32` status `ready` deltaP `30.3448` edge `0.2137` maxDD `-13.6772`
- `risk_on_and_context->equity_24h` score `1.6513` n `32` status `ready` deltaP `30.3448` edge `0.2137` maxDD `-13.6772`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
