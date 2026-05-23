# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-23T11:22:14.152094+00:00`
- Price records: `672`
- Market context records: `1626`
- Flow alert records: `6587`
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

- `market_context_high->metal_24h` score `10.4561` n `189` status `ready` deltaP `26.331` edge `0.9384` maxDD `-12.7414`
- `market_context_high->index_24h` score `3.1151` n `189` status `ready` deltaP `18.4937` edge `0.2741` maxDD `-5.3574`
- `market_context_high->equity_4h` score `1.4611` n `189` status `ready` deltaP `11.9863` edge `0.1513` maxDD `-5.0894`
- `market_context_high->crypto_alt_4h` score `0.7883` n `189` status `ready` deltaP `14.9358` edge `0.3159` maxDD `-19.1522`
- `market_context_high->crypto_major_4h` score `0.4348` n `189` status `ready` deltaP `10.7748` edge `0.2548` maxDD `-13.3376`
- `market_context_high->equity_24h` score `0.2888` n `189` status `ready` deltaP `17.0718` edge `0.4001` maxDD `-33.1875`
- `market_context_high->crypto_alt_1h` score `-0.1905` n `196` status `ready` deltaP `2.1355` edge `0.0637` maxDD `-4.1892`
- `market_context_high->fx_24h` score `-0.2639` n `189` status `ready` deltaP `7.7877` edge `0.031` maxDD `-1.3925`
- `market_context_high->equity_1h` score `-0.3938` n `196` status `ready` deltaP `2.4197` edge `0.0319` maxDD `-2.8014`
- `market_context_high->index_1h` score `-0.7011` n `196` status `ready` deltaP `0.2017` edge `0.0034` maxDD `-1.7205`
- `market_context_high->index_4h` score `-0.7973` n `189` status `ready` deltaP `0.8034` edge `0.0371` maxDD `-3.7119`
- `market_context_high->fx_1h` score `-0.8013` n `196` status `ready` deltaP `-0.0825` edge `-0.003` maxDD `-0.3914`
- `market_context_high->crypto_major_1h` score `-0.8498` n `196` status `ready` deltaP `-0.5988` edge `0.0297` maxDD `-6.1058`
- `market_context_high->commodity_1h` score `-1.0406` n `196` status `ready` deltaP `0.6324` edge `0.0012` maxDD `-4.7041`
- `market_context_high->metal_1h` score `-1.2798` n `196` status `ready` deltaP `3.4553` edge `0.0039` maxDD `-6.3532`
- `market_context_high->crypto_major_24h` score `-1.2895` n `189` status `ready` deltaP `22.5033` edge `0.6011` maxDD `-62.3533`
- `market_context_high->fx_4h` score `-1.3567` n `189` status `ready` deltaP `-10.057` edge `-0.014` maxDD `-1.4313`
- `market_context_high->metal_4h` score `-1.3579` n `189` status `ready` deltaP `9.1246` edge `0.0952` maxDD `-12.5349`
- `market_context_high->crypto_alt_24h` score `-3.0575` n `189` status `ready` deltaP `22.5777` edge `0.7756` maxDD `-88.8062`
- `market_context_high->unknown_4h` score `-4.8722` n `189` status `ready` deltaP `7.2147` edge `-0.227` maxDD `-11.1695`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
