# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-05T06:52:22.330380+00:00`
- Price records: `672`
- Market context records: `2946`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6954`

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

- `market_context_high->crypto_alt_24h` score `16.7528` n `136` status `ready` deltaP `15.2165` edge `1.6863` maxDD `-22.6673`
- `market_context_high->equity_24h` score `8.0154` n `136` status `ready` deltaP `18.3926` edge `0.7457` maxDD `-12.6963`
- `market_context_high->unknown_24h` score `7.2728` n `136` status `ready` deltaP `16.6258` edge `0.5417` maxDD `-1.7175`
- `market_context_high->index_24h` score `2.9702` n `136` status `ready` deltaP `14.3689` edge `0.2498` maxDD `-2.5127`
- `market_context_high->commodity_24h` score `2.9637` n `136` status `ready` deltaP `18.4538` edge `0.3899` maxDD `-10.9425`
- `market_context_high->equity_4h` score `1.4358` n `137` status `ready` deltaP `10.1088` edge `0.1638` maxDD `-4.9235`
- `market_context_high->index_4h` score `0.7873` n `137` status `ready` deltaP `15.3885` edge `0.0825` maxDD `-2.3986`
- `market_context_high->crypto_alt_4h` score `0.4779` n `137` status `ready` deltaP `16.7783` edge `0.3841` maxDD `-30.8239`
- `market_context_high->unknown_4h` score `0.2794` n `137` status `ready` deltaP `3.6774` edge `0.1041` maxDD `-3.7602`
- `market_context_high->index_1h` score `0.096` n `137` status `ready` deltaP `6.1672` edge `0.0206` maxDD `-1.2855`
- `market_context_high->equity_1h` score `-0.2925` n `137` status `ready` deltaP `1.002` edge `0.0485` maxDD `-2.3646`
- `market_context_high->crypto_alt_1h` score `-0.3154` n `137` status `ready` deltaP `6.0547` edge `0.0952` maxDD `-10.747`
- `market_context_high->fx_1h` score `-0.4375` n `137` status `ready` deltaP `-0.5518` edge `0.0029` maxDD `-0.1875`
- `market_context_high->crypto_major_1h` score `-0.5014` n `137` status `ready` deltaP `6.129` edge `0.0818` maxDD `-9.622`
- `market_context_high->metal_1h` score `-0.659` n `137` status `ready` deltaP `0.0087` edge `0.0042` maxDD `-3.4325`
- `market_context_high->unknown_1h` score `-0.6848` n `137` status `ready` deltaP `1.7877` edge `0.0041` maxDD `-3.1801`
- `market_context_high->commodity_1h` score `-0.7092` n `137` status `ready` deltaP `-1.3189` edge `-0.0068` maxDD `-4.3601`
- `market_context_high->fx_4h` score `-0.8472` n `137` status `ready` deltaP `-0.1246` edge `0.0081` maxDD `-0.5631`
- `market_context_high->commodity_4h` score `-1.1869` n `137` status `ready` deltaP `2.9619` edge `0.0201` maxDD `-10.0279`
- `market_context_high->crypto_major_4h` score `-1.4115` n `137` status `ready` deltaP `7.9313` edge `0.2787` maxDD `-33.6701`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
