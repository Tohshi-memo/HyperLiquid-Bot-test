# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-18T01:07:29.942507+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8686`

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

- `market_context_high->unknown_4h` score `35.6496` n `149` status `ready` deltaP `-0.311` edge `2.9962` maxDD `-0.5326`
- `news_risk_high->unknown_4h` score `23.822` n `68` status `ready` deltaP `-4.9498` edge `2.0514` maxDD `-1.3257`
- `risk_on_high->unknown_4h` score `9.5283` n `52` status `ready` deltaP `-7.5516` edge `0.8669` maxDD `-0.4694`
- `risk_on_and_context->unknown_4h` score `9.5283` n `52` status `ready` deltaP `-7.5516` edge `0.8669` maxDD `-0.4694`
- `risk_on_high->commodity_24h` score `9.0688` n `52` status `ready` deltaP `50.0` edge `0.4224` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `9.0688` n `52` status `ready` deltaP `50.0` edge `0.4224` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `8.5062` n `46` status `ready` deltaP `30.699` edge `0.6421` maxDD `-9.3661`
- `market_context_high->commodity_24h` score `7.7697` n `149` status `ready` deltaP `43.2886` edge `0.4114` maxDD `-0.8682`
- `news_risk_high->index_24h` score `3.9231` n `46` status `ready` deltaP `27.6495` edge `0.1602` maxDD `-0.075`
- `news_risk_high->equity_24h` score `3.9036` n `46` status `ready` deltaP `9.7222` edge `0.4379` maxDD `-6.5262`
- `risk_on_high->commodity_4h` score `3.0317` n `52` status `ready` deltaP `33.3021` edge `0.0656` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `3.0317` n `52` status `ready` deltaP `33.3021` edge `0.0656` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.9314` n `149` status `ready` deltaP `29.8044` edge `0.0874` maxDD `-0.345`
- `news_risk_high->crypto_major_24h` score `1.8137` n `46` status `ready` deltaP `3.9175` edge `0.4059` maxDD `-13.2931`
- `risk_on_high->fx_24h` score `1.6805` n `52` status `ready` deltaP `24.9866` edge `-0.0223` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `1.6805` n `52` status `ready` deltaP `24.9866` edge `-0.0223` maxDD `-0.0054`
- `market_context_high->fx_24h` score `1.5456` n `149` status `ready` deltaP `22.2117` edge `0.0023` maxDD `-0.0593`
- `news_risk_high->metal_24h` score `1.3916` n `46` status `ready` deltaP `10.077` edge `0.0942` maxDD `-0.6334`
- `market_context_high->commodity_1h` score `1.2607` n `149` status `ready` deltaP `17.4085` edge `0.0267` maxDD `-0.3491`
- `news_risk_high->equity_4h` score `0.9139` n `68` status `ready` deltaP `11.0474` edge `0.0862` maxDD `-3.3619`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
