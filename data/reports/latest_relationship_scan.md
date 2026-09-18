# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-18T00:07:33.348817+00:00`
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

- `market_context_high->unknown_4h` score `35.6712` n `149` status `ready` deltaP `-0.311` edge `2.998` maxDD `-0.5326`
- `news_risk_high->unknown_4h` score `19.9286` n `71` status `ready` deltaP `-8.5538` edge `1.7738` maxDD `-2.4848`
- `risk_on_high->unknown_4h` score `9.5499` n `52` status `ready` deltaP `-7.5516` edge `0.8687` maxDD `-0.4694`
- `risk_on_and_context->unknown_4h` score `9.5499` n `52` status `ready` deltaP `-7.5516` edge `0.8687` maxDD `-0.4694`
- `risk_on_high->commodity_24h` score `9.1216` n `52` status `ready` deltaP `50.0` edge `0.4268` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `9.1216` n `52` status `ready` deltaP `50.0` edge `0.4268` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `8.9859` n `50` status `ready` deltaP `32.0903` edge `0.6728` maxDD `-9.3661`
- `market_context_high->commodity_24h` score `7.8225` n `149` status `ready` deltaP `43.2886` edge `0.4158` maxDD `-0.8682`
- `news_risk_high->equity_24h` score `4.8296` n `50` status `ready` deltaP `13.7222` edge `0.4884` maxDD `-6.5262`
- `news_risk_high->index_24h` score `4.2466` n `50` status `ready` deltaP `29.5625` edge `0.1744` maxDD `-0.075`
- `risk_on_high->commodity_4h` score `3.0353` n `52` status `ready` deltaP `33.3021` edge `0.0659` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `3.0353` n `52` status `ready` deltaP `33.3021` edge `0.0659` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.935` n `149` status `ready` deltaP `29.8044` edge `0.0877` maxDD `-0.345`
- `news_risk_high->crypto_major_24h` score `2.762` n `50` status `ready` deltaP `7.3958` edge `0.5043` maxDD `-13.2931`
- `news_risk_high->metal_24h` score `1.8697` n `50` status `ready` deltaP `13.7292` edge `0.1097` maxDD `-0.6334`
- `risk_on_high->fx_24h` score `1.7589` n `52` status `ready` deltaP `25.6811` edge `-0.0204` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `1.7589` n `52` status `ready` deltaP `25.6811` edge `-0.0204` maxDD `-0.0054`
- `market_context_high->fx_24h` score `1.624` n `149` status `ready` deltaP `22.9062` edge `0.0042` maxDD `-0.0593`
- `market_context_high->commodity_1h` score `1.2799` n `149` status `ready` deltaP `17.5582` edge `0.0273` maxDD `-0.3491`
- `news_risk_high->index_4h` score `0.7156` n `71` status `ready` deltaP `12.7641` edge `0.0257` maxDD `-0.4259`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
