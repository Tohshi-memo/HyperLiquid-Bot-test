# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-02T18:52:30.893082+00:00`
- Price records: `672`
- Market context records: `2689`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9250`

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

- `market_context_high->crypto_alt_24h` score `9.4913` n `111` status `ready` deltaP `16.0051` edge `1.0336` maxDD `-19.9486`
- `market_context_high->unknown_24h` score `8.6551` n `111` status `ready` deltaP `17.652` edge `0.6364` maxDD `-1.626`
- `market_context_high->unknown_4h` score `0.8865` n `138` status `ready` deltaP `5.3774` edge `0.143` maxDD `-3.7312`
- `market_context_high->index_4h` score `0.2239` n `138` status `ready` deltaP `11.5589` edge `0.0358` maxDD `-2.3986`
- `market_context_high->index_1h` score `-0.1254` n `143` status `ready` deltaP `3.4997` edge `0.01` maxDD `-1.2855`
- `market_context_high->unknown_1h` score `-0.1643` n `143` status `ready` deltaP `2.7491` edge `0.0408` maxDD `-3.1587`
- `market_context_high->crypto_alt_4h` score `-0.3987` n `138` status `ready` deltaP `16.8522` edge `0.2796` maxDD `-28.0137`
- `market_context_high->fx_24h` score `-0.4178` n `111` status `ready` deltaP `8.2161` edge `-0.0024` maxDD `-0.6418`
- `market_context_high->commodity_1h` score `-0.4314` n `143` status `ready` deltaP `1.9985` edge `0.0067` maxDD `-4.3601`
- `market_context_high->fx_1h` score `-0.4668` n `143` status `ready` deltaP `0.2513` edge `0.0038` maxDD `-0.2164`
- `market_context_high->crypto_alt_1h` score `-0.5705` n `143` status `ready` deltaP `6.2948` edge `0.0609` maxDD `-10.747`
- `market_context_high->fx_4h` score `-0.6921` n `138` status `ready` deltaP `-0.4949` edge `0.011` maxDD `-0.5631`
- `market_context_high->commodity_24h` score `-0.7104` n `111` status `ready` deltaP `7.0946` edge `0.171` maxDD `-12.4171`
- `market_context_high->index_24h` score `-0.7611` n `111` status `ready` deltaP `4.5374` edge `0.0044` maxDD `-2.5127`
- `market_context_high->metal_1h` score `-0.7824` n `143` status `ready` deltaP `-1.6991` edge `-0.0044` maxDD `-3.0996`
- `market_context_high->crypto_major_24h` score `-0.9485` n `111` status `ready` deltaP `5.9967` edge `0.5947` maxDD `-44.169`
- `market_context_high->crypto_major_1h` score `-1.015` n `143` status `ready` deltaP `3.4976` edge `0.0335` maxDD `-9.622`
- `market_context_high->commodity_4h` score `-1.0604` n `138` status `ready` deltaP `4.4649` edge `0.0263` maxDD `-10.0279`
- `market_context_high->equity_1h` score `-1.2247` n `143` status `ready` deltaP `-4.4857` edge `0.0117` maxDD `-2.7085`
- `market_context_high->metal_4h` score `-2.0493` n `138` status `ready` deltaP `-1.5686` edge `-0.0193` maxDD `-9.6374`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
