# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-15T11:52:37.229159+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9006`

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

- `risk_on_high->commodity_24h` score `7.9195` n `54` status `ready` deltaP `41.2892` edge `0.3847` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `7.9195` n `54` status `ready` deltaP `41.2892` edge `0.3847` maxDD `0.0`
- `market_context_high->crypto_alt_4h` score `7.4879` n `123` status `ready` deltaP `17.8354` edge `0.6495` maxDD `-9.2196`
- `risk_on_high->crypto_alt_4h` score `6.4442` n `54` status `ready` deltaP `21.1778` edge `0.4405` maxDD `-1.907`
- `risk_on_and_context->crypto_alt_4h` score `6.4442` n `54` status `ready` deltaP `21.1778` edge `0.4405` maxDD `-1.907`
- `market_context_high->crypto_major_4h` score `5.8853` n `123` status `ready` deltaP `19.4614` edge `0.5166` maxDD `-7.4722`
- `risk_on_high->crypto_major_4h` score `4.4836` n `54` status `ready` deltaP `33.4632` edge `0.437` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `4.4836` n `54` status `ready` deltaP `33.4632` edge `0.437` maxDD `-4.1548`
- `market_context_high->crypto_alt_1h` score `1.7643` n `123` status `ready` deltaP `13.1797` edge `0.1656` maxDD `-5.8485`
- `market_context_high->crypto_major_1h` score `1.0261` n `123` status `ready` deltaP `4.9` edge `0.1334` maxDD `-3.7781`
- `market_context_high->metal_4h` score `0.0373` n `123` status `ready` deltaP `10.4166` edge `0.0382` maxDD `-1.6961`
- `market_context_high->fx_1h` score `-0.3405` n `123` status `ready` deltaP `-0.5201` edge `-0.0018` maxDD `-0.4047`
- `risk_on_high->crypto_alt_1h` score `-0.3738` n `54` status `ready` deltaP `4.5077` edge `0.0243` maxDD `-5.8485`
- `risk_on_and_context->crypto_alt_1h` score `-0.3738` n `54` status `ready` deltaP `4.5077` edge `0.0243` maxDD `-5.8485`
- `risk_on_high->crypto_major_1h` score `-0.3765` n `54` status `ready` deltaP `0.6543` edge `0.0196` maxDD `-3.7781`
- `risk_on_and_context->crypto_major_1h` score `-0.3765` n `54` status `ready` deltaP `0.6543` edge `0.0196` maxDD `-3.7781`
- `market_context_high->commodity_24h` score `-0.4421` n `116` status `ready` deltaP `12.8409` edge `0.1462` maxDD `-12.0788`
- `market_context_high->index_1h` score `-0.4827` n `123` status `ready` deltaP `1.7835` edge `0.001` maxDD `-1.3154`
- `market_context_high->metal_1h` score `-0.5035` n `123` status `ready` deltaP `6.0124` edge `0.0049` maxDD `-0.9556`
- `risk_on_high->metal_1h` score `-0.5108` n `54` status `ready` deltaP `0.9537` edge `0.0013` maxDD `-0.8513`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
