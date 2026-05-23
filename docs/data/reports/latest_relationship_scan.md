# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-23T10:59:55.050093+00:00`
- Price records: `672`
- Market context records: `1624`
- Flow alert records: `6581`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8824`

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

- `market_context_high->metal_24h` score `10.5355` n `191` status `ready` deltaP `26.1389` edge `0.9463` maxDD `-12.7414`
- `market_context_high->index_24h` score `3.0674` n `191` status `ready` deltaP `18.3182` edge `0.2713` maxDD `-5.3574`
- `market_context_high->equity_4h` score `1.4651` n `191` status `ready` deltaP `11.9916` edge `0.1516` maxDD `-5.0894`
- `market_context_high->crypto_alt_4h` score `0.6` n `191` status `ready` deltaP `14.2654` edge `0.3086` maxDD `-19.4759`
- `market_context_high->crypto_major_4h` score `0.3544` n `191` status `ready` deltaP `10.1432` edge `0.2487` maxDD `-13.3376`
- `market_context_high->equity_24h` score `0.195` n `191` status `ready` deltaP `16.9185` edge `0.3933` maxDD `-33.1875`
- `market_context_high->crypto_alt_1h` score `-0.2351` n `196` status `ready` deltaP `1.4145` edge `0.0628` maxDD `-4.1892`
- `market_context_high->fx_24h` score `-0.2424` n `191` status `ready` deltaP `7.9207` edge `0.0319` maxDD `-1.3925`
- `market_context_high->equity_1h` score `-0.3854` n `196` status `ready` deltaP `2.4197` edge `0.0326` maxDD `-2.8014`
- `market_context_high->index_1h` score `-0.6759` n `196` status `ready` deltaP `0.5622` edge `0.0031` maxDD `-1.7205`
- `market_context_high->index_4h` score `-0.7883` n `191` status `ready` deltaP `0.9306` edge `0.037` maxDD `-3.7119`
- `market_context_high->fx_1h` score `-0.8013` n `196` status `ready` deltaP `-0.0825` edge `-0.003` maxDD `-0.3914`
- `market_context_high->crypto_major_1h` score `-0.9047` n `196` status `ready` deltaP `-1.3198` edge `0.0285` maxDD `-6.1883`
- `market_context_high->commodity_1h` score `-1.0454` n `196` status `ready` deltaP `0.6324` edge `0.0008` maxDD `-4.7041`
- `market_context_high->metal_1h` score `-1.2437` n `196` status `ready` deltaP `3.8158` edge `0.0045` maxDD `-6.3532`
- `market_context_high->metal_4h` score `-1.3512` n `191` status `ready` deltaP `9.2684` edge `0.0948` maxDD `-12.5349`
- `market_context_high->fx_4h` score `-1.382` n `191` status `ready` deltaP `-10.5279` edge `-0.0141` maxDD `-1.4313`
- `market_context_high->crypto_major_24h` score `-1.4653` n `191` status `ready` deltaP `22.3168` edge `0.5877` maxDD `-62.3533`
- `market_context_high->crypto_alt_24h` score `-3.3872` n `191` status `ready` deltaP `22.3413` edge `0.7497` maxDD `-88.8062`
- `market_context_high->commodity_4h` score `-5.1858` n `191` status `ready` deltaP `-13.8808` edge `-0.1096` maxDD `-24.683`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
