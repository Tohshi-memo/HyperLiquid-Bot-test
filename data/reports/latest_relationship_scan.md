# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-04T09:37:28.684122+00:00`
- Price records: `672`
- Market context records: `5649`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `8684`

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

- `market_context_high->equity_24h` score `2.568` n `181` status `ready` deltaP `14.5488` edge `0.6249` maxDD `-31.6316`
- `market_context_high->fx_24h` score `0.9819` n `181` status `ready` deltaP `19.7236` edge `0.0596` maxDD `-1.7414`
- `market_context_high->crypto_major_4h` score `0.7002` n `237` status `ready` deltaP `10.3948` edge `0.2183` maxDD `-14.0065`
- `market_context_high->equity_4h` score `0.4673` n `237` status `ready` deltaP `7.3814` edge `0.1536` maxDD `-7.4425`
- `market_context_high->crypto_alt_4h` score `-0.1039` n `237` status `ready` deltaP `6.0693` edge `0.1358` maxDD `-9.46`
- `market_context_high->fx_1h` score `-0.2743` n `241` status `ready` deltaP `1.7175` edge `0.001` maxDD `-0.4764`
- `market_context_high->equity_1h` score `-0.3869` n `241` status `ready` deltaP `5.2731` edge `0.0333` maxDD `-5.0555`
- `market_context_high->metal_1h` score `-0.5608` n `241` status `ready` deltaP `-0.6566` edge `0.0` maxDD `-2.0682`
- `market_context_high->crypto_alt_1h` score `-0.6452` n `241` status `ready` deltaP `1.3628` edge `0.0333` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `-0.7292` n `241` status `ready` deltaP `3.4928` edge `0.0405` maxDD `-6.9639`
- `market_context_high->index_1h` score `-0.9584` n `241` status `ready` deltaP `0.2205` edge `0.0055` maxDD `-0.9472`
- `market_context_high->commodity_1h` score `-1.0109` n `241` status `ready` deltaP `-0.4044` edge `-0.005` maxDD `-3.7906`
- `market_context_high->fx_4h` score `-1.2844` n `237` status `ready` deltaP `1.828` edge `0.0065` maxDD `-1.335`
- `market_context_high->index_4h` score `-2.0099` n `237` status `ready` deltaP `-1.3841` edge `0.0089` maxDD `-3.04`
- `market_context_high->index_24h` score `-2.3133` n `181` status `ready` deltaP `10.0963` edge `0.0348` maxDD `-16.8946`
- `market_context_high->metal_4h` score `-3.0607` n `237` status `ready` deltaP `-14.8265` edge `-0.0552` maxDD `-11.7351`
- `market_context_high->commodity_4h` score `-3.802` n `237` status `ready` deltaP `-2.1875` edge `-0.0347` maxDD `-14.071`
- `market_context_high->crypto_major_24h` score `-4.4842` n `181` status `ready` deltaP `4.1465` edge `0.0527` maxDD `-29.6555`
- `market_context_high->metal_24h` score `-8.3576` n `181` status `ready` deltaP `-12.5096` edge `-0.252` maxDD `-32.8874`
- `market_context_high->commodity_24h` score `-13.0058` n `181` status `ready` deltaP `-16.4883` edge `-0.113` maxDD `-45.8715`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
