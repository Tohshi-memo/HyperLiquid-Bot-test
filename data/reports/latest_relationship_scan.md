# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-22T20:22:15.331768+00:00`
- Price records: `672`
- Market context records: `1561`
- Flow alert records: `6404`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8813`

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

- `market_context_high->metal_24h` score `12.6638` n `182` status `ready` deltaP `24.6852` edge `0.9908` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `10.9794` n `182` status `ready` deltaP `26.9974` edge `0.9366` maxDD `-15.1306`
- `market_context_high->crypto_major_24h` score `9.4617` n `182` status `ready` deltaP `26.7399` edge `0.7234` maxDD `-8.0553`
- `market_context_high->index_24h` score `4.0368` n `182` status `ready` deltaP `20.7799` edge `0.3065` maxDD `-5.3574`
- `market_context_high->equity_24h` score `3.0349` n `182` status `ready` deltaP `15.2835` edge `0.3837` maxDD `-14.2815`
- `market_context_high->fx_24h` score `0.4728` n `182` status `ready` deltaP `14.4459` edge `0.048` maxDD `-1.3925`
- `market_context_high->equity_4h` score `0.4556` n `199` status `ready` deltaP `5.8532` edge `0.1084` maxDD `-5.0894`
- `market_context_high->crypto_alt_4h` score `0.0211` n `199` status `ready` deltaP `13.2545` edge `0.2463` maxDD `-19.5565`
- `market_context_high->crypto_major_4h` score `-0.1313` n `199` status `ready` deltaP `9.1272` edge `0.1932` maxDD `-13.3376`
- `market_context_high->crypto_alt_1h` score `-0.2888` n `199` status `ready` deltaP `1.2668` edge `0.0569` maxDD `-4.1892`
- `market_context_high->fx_1h` score `-0.6662` n `199` status `ready` deltaP `-2.7427` edge `-0.0039` maxDD `-0.3914`
- `market_context_high->commodity_1h` score `-0.6962` n `199` status `ready` deltaP `-0.0481` edge `0.0032` maxDD `-4.7041`
- `market_context_high->index_1h` score `-0.7392` n `199` status `ready` deltaP `0.0256` edge `0.0014` maxDD `-1.7205`
- `market_context_high->metal_1h` score `-0.743` n `199` status `ready` deltaP `4.9981` edge `0.005` maxDD `-6.3532`
- `market_context_high->equity_1h` score `-0.7588` n `199` status `ready` deltaP `-1.0328` edge `0.0245` maxDD `-2.8014`
- `market_context_high->crypto_major_1h` score `-0.874` n `199` status `ready` deltaP `-0.4438` edge `0.0266` maxDD `-6.1883`
- `market_context_high->fx_4h` score `-1.3768` n `199` status `ready` deltaP `-10.3973` edge `-0.0143` maxDD `-1.4313`
- `market_context_high->metal_4h` score `-1.3947` n `199` status `ready` deltaP `10.0587` edge `0.0859` maxDD `-12.5349`
- `market_context_high->index_4h` score `-1.4024` n `199` status `ready` deltaP `-4.135` edge `0.0196` maxDD `-3.7119`
- `market_context_high->commodity_4h` score `-5.0276` n `199` status `ready` deltaP `-13.3281` edge `-0.093` maxDD `-24.683`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
