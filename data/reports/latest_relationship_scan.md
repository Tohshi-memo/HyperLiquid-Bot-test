# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-06T13:37:27.497085+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9941`

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

- `risk_on_high->unknown_24h` score `116.434` n `109` status `ready` deltaP `22.3974` edge `9.5666` maxDD `-0.3798`
- `risk_on_and_context->unknown_24h` score `116.434` n `109` status `ready` deltaP `22.3974` edge `9.5666` maxDD `-0.3798`
- `risk_on_high->crypto_major_24h` score `7.3434` n `109` status `ready` deltaP `20.1452` edge `1.059` maxDD `-37.8412`
- `risk_on_and_context->crypto_major_24h` score `7.3434` n `109` status `ready` deltaP `20.1452` edge `1.059` maxDD `-37.8412`
- `market_context_high->equity_24h` score `1.9219` n `196` status `ready` deltaP `14.0023` edge `0.3401` maxDD `-12.863`
- `risk_on_high->index_1h` score `-0.1272` n `139` status `ready` deltaP `4.7387` edge `-0.0032` maxDD `-0.5764`
- `risk_on_and_context->index_1h` score `-0.1272` n `139` status `ready` deltaP `4.7387` edge `-0.0032` maxDD `-0.5764`
- `risk_on_high->metal_1h` score `-0.1981` n `139` status `ready` deltaP `7.0715` edge `-0.0013` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `-0.1981` n `139` status `ready` deltaP `7.0715` edge `-0.0013` maxDD `-1.699`
- `risk_on_high->crypto_alt_1h` score `-0.441` n `139` status `ready` deltaP `1.2956` edge `0.0563` maxDD `-5.4685`
- `risk_on_and_context->crypto_alt_1h` score `-0.441` n `139` status `ready` deltaP `1.2956` edge `0.0563` maxDD `-5.4685`
- `risk_on_high->equity_1h` score `-0.4987` n `139` status `ready` deltaP `5.525` edge `-0.0133` maxDD `-2.6638`
- `risk_on_and_context->equity_1h` score `-0.4987` n `139` status `ready` deltaP `5.525` edge `-0.0133` maxDD `-2.6638`
- `risk_on_high->commodity_1h` score `-0.5208` n `139` status `ready` deltaP `0.9672` edge `0.0005` maxDD `-1.0281`
- `risk_on_and_context->commodity_1h` score `-0.5208` n `139` status `ready` deltaP `0.9672` edge `0.0005` maxDD `-1.0281`
- `risk_on_high->crypto_alt_24h` score `-0.6369` n `109` status `ready` deltaP `8.4146` edge `0.4105` maxDD `-31.9071`
- `risk_on_and_context->crypto_alt_24h` score `-0.6369` n `109` status `ready` deltaP `8.4146` edge `0.4105` maxDD `-31.9071`
- `market_context_high->commodity_1h` score `-0.7487` n `250` status `ready` deltaP `0.6132` edge `-0.0015` maxDD `-1.5315`
- `risk_on_high->equity_24h` score `-0.766` n `109` status `ready` deltaP `3.9246` edge `0.1729` maxDD `-12.3649`
- `risk_on_and_context->equity_24h` score `-0.766` n `109` status `ready` deltaP `3.9246` edge `0.1729` maxDD `-12.3649`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
