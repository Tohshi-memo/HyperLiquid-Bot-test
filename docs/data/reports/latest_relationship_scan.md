# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-06T18:52:24.776104+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10185`

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

- `risk_on_high->unknown_24h` score `226.1781` n `103` status `ready` deltaP `25.2124` edge `18.69` maxDD `-0.1262`
- `risk_on_and_context->unknown_24h` score `226.1781` n `103` status `ready` deltaP `25.2124` edge `18.69` maxDD `-0.1262`
- `risk_on_high->crypto_major_24h` score `19.2489` n `103` status `ready` deltaP `32.376` edge `1.4789` maxDD `-5.2535`
- `risk_on_and_context->crypto_major_24h` score `19.2489` n `103` status `ready` deltaP `32.376` edge `1.4789` maxDD `-5.2535`
- `risk_on_high->crypto_alt_24h` score `10.4829` n `103` status `ready` deltaP `22.583` edge `0.8412` maxDD `-6.4544`
- `risk_on_and_context->crypto_alt_24h` score `10.4829` n `103` status `ready` deltaP `22.583` edge `0.8412` maxDD `-6.4544`
- `market_context_high->crypto_alt_24h` score `6.3005` n `196` status `ready` deltaP `19.5366` edge `0.5383` maxDD `-7.8138`
- `market_context_high->equity_24h` score `5.8863` n `196` status `ready` deltaP `21.0707` edge `0.3954` maxDD `-1.628`
- `risk_on_high->equity_24h` score `4.7687` n `103` status `ready` deltaP `18.3067` edge `0.3207` maxDD `-1.628`
- `risk_on_and_context->equity_24h` score `4.7687` n `103` status `ready` deltaP `18.3067` edge `0.3207` maxDD `-1.628`
- `risk_on_high->index_24h` score `1.4238` n `103` status `ready` deltaP `17.0982` edge `0.0716` maxDD `-1.6884`
- `risk_on_and_context->index_24h` score `1.4238` n `103` status `ready` deltaP `17.0982` edge `0.0716` maxDD `-1.6884`
- `market_context_high->index_24h` score `1.3662` n `196` status `ready` deltaP `18.5941` edge `0.0882` maxDD `-2.1979`
- `risk_on_high->metal_24h` score `0.3473` n `103` status `ready` deltaP `14.7013` edge `0.0797` maxDD `-5.5683`
- `risk_on_and_context->metal_24h` score `0.3473` n `103` status `ready` deltaP `14.7013` edge `0.0797` maxDD `-5.5683`
- `risk_on_high->crypto_alt_1h` score `0.1097` n `129` status `ready` deltaP `3.8516` edge `0.066` maxDD `-4.6031`
- `risk_on_and_context->crypto_alt_1h` score `0.1097` n `129` status `ready` deltaP `3.8516` edge `0.066` maxDD `-4.6031`
- `risk_on_high->index_1h` score `0.0738` n `129` status `ready` deltaP `8.5457` edge `-0.0028` maxDD `-0.5764`
- `risk_on_and_context->index_1h` score `0.0738` n `129` status `ready` deltaP `8.5457` edge `-0.0028` maxDD `-0.5764`
- `risk_on_high->metal_1h` score `-0.1307` n `129` status `ready` deltaP `7.1079` edge `-0.0023` maxDD `-1.6137`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
