# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-25T16:22:35.465141+00:00`
- Price records: `672`
- Market context records: `4740`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7454`

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

- `market_context_high->unknown_1h` score `79.2291` n `141` status `ready` deltaP `14.2322` edge `6.5493` maxDD `-1.674`
- `market_context_high->unknown_4h` score `5.2497` n `138` status `ready` deltaP `13.503` edge `0.4685` maxDD `-4.6834`
- `market_context_high->unknown_24h` score `3.3712` n `129` status `ready` deltaP `16.7797` edge `0.2614` maxDD `-4.7201`
- `market_context_high->index_4h` score `-0.4622` n `138` status `ready` deltaP `6.5593` edge `0.0039` maxDD `-5.5505`
- `market_context_high->commodity_1h` score `-0.5089` n `141` status `ready` deltaP `2.1584` edge `0.0228` maxDD `-2.0345`
- `market_context_high->equity_4h` score `-0.7644` n `138` status `ready` deltaP `4.7676` edge `0.0388` maxDD `-8.8203`
- `market_context_high->fx_4h` score `-0.8873` n `138` status `ready` deltaP `-0.5744` edge `-0.0025` maxDD `-1.9274`
- `market_context_high->equity_1h` score `-0.9031` n `141` status `ready` deltaP `-0.9534` edge `-0.0129` maxDD `-5.3889`
- `market_context_high->fx_1h` score `-1.2775` n `141` status `ready` deltaP `-5.162` edge `-0.0052` maxDD `-1.0145`
- `market_context_high->index_1h` score `-1.5353` n `141` status `ready` deltaP `-3.0492` edge `-0.0072` maxDD `-2.6999`
- `market_context_high->commodity_4h` score `-1.6743` n `138` status `ready` deltaP `7.5048` edge `0.0212` maxDD `-9.1941`
- `market_context_high->metal_1h` score `-2.5909` n `141` status `ready` deltaP `-3.7043` edge `-0.0694` maxDD `-15.7119`
- `market_context_high->crypto_alt_1h` score `-2.6086` n `141` status `ready` deltaP `0.3939` edge `-0.0392` maxDD `-19.8288`
- `market_context_high->crypto_major_1h` score `-3.2442` n `141` status `ready` deltaP `0.2123` edge `-0.0637` maxDD `-25.624`
- `market_context_high->commodity_24h` score `-3.9984` n `129` status `ready` deltaP `16.812` edge `0.0656` maxDD `-27.5371`
- `market_context_high->fx_24h` score `-4.6317` n `129` status `ready` deltaP `-14.547` edge `-0.0204` maxDD `-5.1542`
- `market_context_high->crypto_alt_4h` score `-6.4244` n `138` status `ready` deltaP `-0.0398` edge `-0.0744` maxDD `-54.5849`
- `market_context_high->index_24h` score `-7.7776` n `129` status `ready` deltaP `-11.7289` edge `-0.1044` maxDD `-25.5765`
- `market_context_high->metal_4h` score `-8.4637` n `138` status `ready` deltaP `1.9022` edge `-0.268` maxDD `-61.7153`
- `market_context_high->crypto_major_4h` score `-9.3904` n `138` status `ready` deltaP `0.3402` edge `-0.1885` maxDD `-76.0803`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
