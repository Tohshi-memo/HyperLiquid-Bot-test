# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-11T02:22:27.407098+00:00`
- Price records: `672`
- Market context records: `6346`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11134`

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

- `news_risk_high->crypto_alt_24h` score `15.2248` n `32` status `ready` deltaP `42.8819` edge `0.9976` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `6.1298` n `32` status `ready` deltaP `50.8681` edge `0.1717` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `4.4189` n `32` status `ready` deltaP `17.1875` edge `0.5299` maxDD `-4.2368`
- `news_risk_high->fx_4h` score `4.1533` n `32` status `ready` deltaP `43.2165` edge `0.0626` maxDD `-0.0345`
- `news_risk_high->commodity_24h` score `3.635` n `32` status `ready` deltaP `31.9444` edge `0.1105` maxDD `-0.3101`
- `news_risk_high->fx_1h` score `2.3751` n `32` status `ready` deltaP `28.5928` edge `0.0212` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `1.5497` n `32` status `ready` deltaP `15.1759` edge `0.1442` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.9556` n `32` status `ready` deltaP `11.9199` edge `0.0892` maxDD `-1.6923`
- `market_context_high->metal_4h` score `0.5845` n `196` status `ready` deltaP `12.9387` edge `0.0421` maxDD `-2.7056`
- `market_context_high->unknown_1h` score `0.1261` n `207` status `ready` deltaP `-7.182` edge `0.1592` maxDD `-3.7317`
- `market_context_high->index_4h` score `0.0701` n `196` status `ready` deltaP `6.4118` edge `0.0224` maxDD `-0.4108`
- `market_context_high->metal_1h` score `-0.4326` n `207` status `ready` deltaP `3.0446` edge `0.002` maxDD `-1.8877`
- `market_context_high->commodity_1h` score `-0.6079` n `207` status `ready` deltaP `-1.3234` edge `-0.0008` maxDD `-2.1314`
- `market_context_high->commodity_24h` score `-0.6455` n `132` status `ready` deltaP `-4.7033` edge `0.135` maxDD `-6.2457`
- `market_context_high->metal_24h` score `-0.6761` n `132` status `ready` deltaP `14.1256` edge `0.076` maxDD `-11.8809`
- `market_context_high->fx_1h` score `-0.7045` n `207` status `ready` deltaP `-0.5135` edge `-0.0019` maxDD `-0.9376`
- `news_risk_high->index_24h` score `-0.714` n `32` status `ready` deltaP `0.3472` edge `-0.0067` maxDD `-2.3058`
- `news_risk_high->metal_1h` score `-0.7387` n `32` status `ready` deltaP `-2.994` edge `-0.025` maxDD `-1.6464`
- `market_context_high->equity_4h` score `-0.7448` n `196` status `ready` deltaP `4.6043` edge `0.0437` maxDD `-8.2573`
- `news_risk_high->unknown_1h` score `-0.8199` n `32` status `ready` deltaP `5.3331` edge `-0.0694` maxDD `-0.7581`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
