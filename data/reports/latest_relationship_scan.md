# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-02T23:37:19.798539+00:00`
- Price records: `672`
- Market context records: `2710`
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

- `market_context_high->crypto_alt_24h` score `10.7983` n `111` status `ready` deltaP `16.3523` edge `1.1402` maxDD `-19.9486`
- `market_context_high->unknown_24h` score `8.6218` n `111` status `ready` deltaP `17.1312` edge `0.6371` maxDD `-1.626`
- `market_context_high->unknown_4h` score `0.883` n `143` status `ready` deltaP `6.249` edge `0.1369` maxDD `-3.7312`
- `market_context_high->crypto_major_24h` score `0.2782` n `111` status `ready` deltaP `6.5175` edge `0.7485` maxDD `-44.169`
- `market_context_high->index_4h` score `0.2697` n `143` status `ready` deltaP `12.2282` edge `0.0372` maxDD `-2.3986`
- `market_context_high->index_1h` score `-0.1191` n `143` status `ready` deltaP `3.6494` edge `0.0098` maxDD `-1.2855`
- `market_context_high->unknown_1h` score `-0.2686` n `143` status `ready` deltaP `2.4497` edge `0.0341` maxDD `-3.1587`
- `market_context_high->fx_1h` score `-0.3913` n `143` status `ready` deltaP `1.1495` edge `0.0041` maxDD `-0.2164`
- `market_context_high->crypto_alt_4h` score `-0.4319` n `143` status `ready` deltaP `16.3633` edge `0.289` maxDD `-28.7261`
- `market_context_high->crypto_alt_1h` score `-0.4426` n `143` status `ready` deltaP `6.7439` edge `0.0743` maxDD `-10.747`
- `market_context_high->commodity_1h` score `-0.4852` n `143` status `ready` deltaP `1.5494` edge `0.0028` maxDD `-4.3601`
- `market_context_high->metal_1h` score `-0.6889` n `143` status `ready` deltaP `-0.6512` edge `0.0006` maxDD `-3.0996`
- `market_context_high->fx_24h` score `-0.7417` n `111` status `ready` deltaP `4.9174` edge `-0.0074` maxDD `-0.6418`
- `market_context_high->fx_4h` score `-0.8948` n `143` status `ready` deltaP `-1.049` edge `0.0103` maxDD `-0.5631`
- `market_context_high->crypto_major_1h` score `-0.8988` n `143` status `ready` deltaP `3.797` edge `0.0464` maxDD `-9.622`
- `market_context_high->commodity_4h` score `-1.1397` n `143` status `ready` deltaP `3.4955` edge `0.0226` maxDD `-10.0279`
- `market_context_high->commodity_24h` score `-1.1712` n `111` status `ready` deltaP `5.3585` edge `0.1235` maxDD `-12.4171`
- `market_context_high->equity_1h` score `-1.2068` n `143` status `ready` deltaP `-4.336` edge `0.0122` maxDD `-2.7085`
- `market_context_high->index_24h` score `-1.4402` n `111` status `ready` deltaP `1.2388` edge `-0.0302` maxDD `-2.5127`
- `market_context_high->equity_4h` score `-1.9851` n `143` status `ready` deltaP `-0.8816` edge `-0.0191` maxDD `-5.9024`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
