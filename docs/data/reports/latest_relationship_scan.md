# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-18T04:07:34.096964+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8592`

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

- `market_context_high->unknown_4h` score `38.5336` n `149` status `ready` deltaP `-0.0061` edge `3.2345` maxDD `-0.5326`
- `risk_on_high->unknown_4h` score `12.4123` n `52` status `ready` deltaP `-7.2467` edge `1.1052` maxDD `-0.4694`
- `risk_on_and_context->unknown_4h` score `12.4123` n `52` status `ready` deltaP `-7.2467` edge `1.1052` maxDD `-0.4694`
- `risk_on_high->commodity_24h` score `8.9764` n `52` status `ready` deltaP `50.0` edge `0.4147` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `8.9764` n `52` status `ready` deltaP `50.0` edge `0.4147` maxDD `0.0`
- `market_context_high->commodity_24h` score `7.6773` n `149` status `ready` deltaP `43.2886` edge `0.4037` maxDD `-0.8682`
- `news_risk_high->crypto_alt_24h` score `4.4428` n `34` status `ready` deltaP `24.5609` edge `0.3444` maxDD `-9.3661`
- `risk_on_high->commodity_4h` score `2.9873` n `52` status `ready` deltaP `33.3021` edge `0.0619` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.9873` n `52` status `ready` deltaP `33.3021` edge `0.0619` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.887` n `149` status `ready` deltaP `29.8044` edge `0.0837` maxDD `-0.345`
- `news_risk_high->unknown_1h` score `2.8852` n `78` status `ready` deltaP `2.2148` edge `0.2501` maxDD `-0.9543`
- `news_risk_high->index_24h` score `2.5555` n `34` status `ready` deltaP `19.2096` edge `0.1025` maxDD `-0.075`
- `risk_on_high->fx_24h` score `1.4467` n `52` status `ready` deltaP `22.9033` edge `-0.0279` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `1.4467` n `52` status `ready` deltaP `22.9033` edge `-0.0279` maxDD `-0.0054`
- `market_context_high->fx_24h` score `1.3118` n `149` status `ready` deltaP `20.1284` edge `-0.0033` maxDD `-0.0593`
- `market_context_high->commodity_1h` score `1.2607` n `149` status `ready` deltaP `17.4085` edge `0.0267` maxDD `-0.3491`
- `news_risk_high->crypto_alt_4h` score `1.1848` n `68` status `ready` deltaP `13.6837` edge `0.2863` maxDD `-13.05`
- `risk_on_high->commodity_1h` score `0.6374` n `52` status `ready` deltaP `10.4906` edge `0.0184` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.6374` n `52` status `ready` deltaP `10.4906` edge `0.0184` maxDD `-0.1507`
- `news_risk_high->equity_4h` score `0.5373` n `68` status `ready` deltaP `9.7292` edge `0.0636` maxDD `-3.3619`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
