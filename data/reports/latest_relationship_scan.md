# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-09T02:52:31.289806+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `64`

- Symbol pattern count: `6595`

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

- `market_context_high->equity_24h` score `11.148` n `32` status `ready` deltaP `18.4028` edge `1.0436` maxDD `-16.6495`
- `market_context_high->commodity_24h` score `2.9667` n `32` status `ready` deltaP `9.8958` edge `0.24` maxDD `-1.6995`
- `market_context_high->index_24h` score `1.5427` n `32` status `ready` deltaP `18.5764` edge `0.1202` maxDD `-2.3671`
- `market_context_high->metal_1h` score `1.1622` n `67` status `ready` deltaP `13.5803` edge `0.0391` maxDD `-0.6226`
- `market_context_high->equity_1h` score `1.0878` n `67` status `ready` deltaP `5.2283` edge `0.1755` maxDD `-5.5762`
- `market_context_high->fx_24h` score `0.6144` n `32` status `ready` deltaP `10.0694` edge `-0.0071` maxDD `-0.0397`
- `market_context_high->metal_4h` score `0.344` n `55` status `ready` deltaP `6.6796` edge `0.0521` maxDD `-1.2025`
- `market_context_high->commodity_4h` score `0.0657` n `55` status `ready` deltaP `-0.0166` edge `0.0528` maxDD `-1.1102`
- `market_context_high->commodity_1h` score `-0.0234` n `67` status `ready` deltaP `6.1087` edge `0.0161` maxDD `-1.7019`
- `market_context_high->index_4h` score `-0.1974` n `55` status `ready` deltaP `9.3902` edge `0.0138` maxDD `-2.4279`
- `market_context_high->index_1h` score `-0.2481` n `67` status `ready` deltaP `2.2433` edge `0.0227` maxDD `-0.6664`
- `market_context_high->crypto_alt_1h` score `-0.3184` n `67` status `ready` deltaP `13.1491` edge `0.0608` maxDD `-10.1421`
- `market_context_high->fx_1h` score `-0.8901` n `67` status `ready` deltaP `-10.6086` edge `-0.0042` maxDD `-0.4688`
- `market_context_high->fx_4h` score `-0.9968` n `55` status `ready` deltaP `-2.7716` edge `-0.0001` maxDD `-1.0704`
- `market_context_high->metal_24h` score `-1.4911` n `32` status `ready` deltaP `1.0417` edge `-0.1428` maxDD `-1.4245`
- `market_context_high->crypto_major_1h` score `-1.6369` n `67` status `ready` deltaP `4.0397` edge `-0.0269` maxDD `-11.7911`
- `market_context_high->crypto_major_24h` score `-4.7146` n `32` status `ready` deltaP `-4.8611` edge `0.0038` maxDD `-23.1423`
- `market_context_high->equity_4h` score `-4.8752` n `55` status `ready` deltaP `4.2628` edge `-0.0567` maxDD `-24.9053`
- `market_context_high->crypto_alt_4h` score `-7.8877` n `55` status `ready` deltaP `4.7644` edge `-0.2222` maxDD `-30.6833`
- `market_context_high->crypto_alt_24h` score `-8.7838` n `32` status `ready` deltaP `-18.75` edge `-0.1491` maxDD `-29.9639`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
