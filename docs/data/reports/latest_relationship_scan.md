# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-06T13:52:24.540394+00:00`
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

- `risk_on_high->unknown_24h` score `116.5522` n `109` status `ready` deltaP `23.1412` edge `9.5694` maxDD `-0.2126`
- `risk_on_and_context->unknown_24h` score `116.5522` n `109` status `ready` deltaP `23.1412` edge `9.5694` maxDD `-0.2126`
- `risk_on_high->crypto_major_24h` score `8.2099` n `109` status `ready` deltaP `20.8891` edge `1.0902` maxDD `-35.2909`
- `risk_on_and_context->crypto_major_24h` score `8.2099` n `109` status `ready` deltaP `20.8891` edge `1.0902` maxDD `-35.2909`
- `market_context_high->equity_24h` score `2.1158` n `196` status `ready` deltaP `14.3389` edge `0.3433` maxDD `-12.3396`
- `risk_on_high->crypto_alt_24h` score `0.1279` n `109` status `ready` deltaP `9.1584` edge `0.4407` maxDD `-29.9545`
- `risk_on_and_context->crypto_alt_24h` score `0.1279` n `109` status `ready` deltaP `9.1584` edge `0.4407` maxDD `-29.9545`
- `risk_on_high->index_1h` score `-0.105` n `138` status `ready` deltaP `5.1506` edge `-0.0031` maxDD `-0.5764`
- `risk_on_and_context->index_1h` score `-0.105` n `138` status `ready` deltaP `5.1506` edge `-0.0031` maxDD `-0.5764`
- `risk_on_high->metal_1h` score `-0.2089` n `138` status `ready` deltaP `6.8927` edge `-0.0015` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `-0.2089` n `138` status `ready` deltaP `6.8927` edge `-0.0015` maxDD `-1.699`
- `risk_on_high->crypto_alt_1h` score `-0.3913` n `138` status `ready` deltaP `1.7075` edge `0.0577` maxDD `-5.4685`
- `risk_on_and_context->crypto_alt_1h` score `-0.3913` n `138` status `ready` deltaP `1.7075` edge `0.0577` maxDD `-5.4685`
- `risk_on_high->equity_1h` score `-0.4725` n `138` status `ready` deltaP `5.9837` edge `-0.013` maxDD `-2.6638`
- `risk_on_and_context->equity_1h` score `-0.4725` n `138` status `ready` deltaP `5.9837` edge `-0.013` maxDD `-2.6638`
- `risk_on_high->equity_24h` score `-0.4928` n `109` status `ready` deltaP `4.6684` edge `0.18` maxDD `-11.8416`
- `risk_on_and_context->equity_24h` score `-0.4928` n `109` status `ready` deltaP `4.6684` edge `0.18` maxDD `-11.8416`
- `risk_on_high->commodity_1h` score `-0.4995` n `138` status `ready` deltaP `1.2345` edge `0.0005` maxDD `-1.0281`
- `risk_on_and_context->commodity_1h` score `-0.4995` n `138` status `ready` deltaP `1.2345` edge `0.0005` maxDD `-1.0281`
- `market_context_high->commodity_1h` score `-0.7286` n `250` status `ready` deltaP `0.8635` edge `-0.0015` maxDD `-1.5315`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
