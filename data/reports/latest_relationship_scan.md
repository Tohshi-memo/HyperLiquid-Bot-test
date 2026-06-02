# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-02T18:07:28.445572+00:00`
- Price records: `672`
- Market context records: `2686`
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

- `market_context_high->crypto_alt_24h` score `9.3293` n `111` status `ready` deltaP `16.0051` edge `1.0201` maxDD `-19.9486`
- `market_context_high->unknown_24h` score `8.6911` n `111` status `ready` deltaP `17.652` edge `0.6394` maxDD `-1.626`
- `market_context_high->unknown_4h` score `1.0321` n `136` status `ready` deltaP `5.7569` edge `0.1526` maxDD `-3.7312`
- `market_context_high->index_4h` score `0.3026` n `136` status `ready` deltaP `11.1998` edge `0.0347` maxDD `-2.3986`
- `market_context_high->crypto_alt_4h` score `0.1814` n `136` status `ready` deltaP `17.7367` edge `0.2947` maxDD `-25.826`
- `market_context_high->index_1h` score `-0.1514` n `142` status `ready` deltaP `3.0446` edge `0.0097` maxDD `-1.2855`
- `market_context_high->unknown_1h` score `-0.2163` n `142` status `ready` deltaP `2.5787` edge `0.0376` maxDD `-3.1587`
- `market_context_high->fx_24h` score `-0.3689` n `111` status `ready` deltaP `8.7369` edge `-0.0018` maxDD `-0.6418`
- `market_context_high->commodity_1h` score `-0.4286` n `142` status `ready` deltaP `1.963` edge `0.0073` maxDD `-4.3601`
- `market_context_high->fx_1h` score `-0.4604` n `142` status `ready` deltaP `0.3163` edge `0.0039` maxDD `-0.2164`
- `market_context_high->commodity_24h` score `-0.6378` n `111` status `ready` deltaP `7.4419` edge `0.178` maxDD `-12.4171`
- `market_context_high->fx_4h` score `-0.6618` n `136` status `ready` deltaP `-0.2062` edge `0.0116` maxDD `-0.5631`
- `market_context_high->index_24h` score `-0.6985` n `111` status `ready` deltaP `4.8846` edge `0.0073` maxDD `-2.5127`
- `market_context_high->crypto_alt_1h` score `-0.7794` n `142` status `ready` deltaP `6.6986` edge `0.0664` maxDD `-10.747`
- `market_context_high->metal_1h` score `-0.8219` n `142` status `ready` deltaP `-2.2181` edge `-0.006` maxDD `-3.0996`
- `market_context_high->crypto_major_1h` score `-0.9661` n `142` status `ready` deltaP `3.8817` edge `0.0372` maxDD `-9.622`
- `market_context_high->crypto_major_24h` score `-1.0733` n `111` status `ready` deltaP `5.9967` edge `0.5787` maxDD `-44.169`
- `market_context_high->commodity_4h` score `-1.0922` n `136` status `ready` deltaP `4.3041` edge `0.0233` maxDD `-10.0279`
- `market_context_high->equity_1h` score `-1.1756` n `142` status `ready` deltaP `-4.0967` edge `0.0132` maxDD `-2.7085`
- `market_context_high->crypto_major_4h` score `-1.5734` n `136` status `ready` deltaP `5.99` edge `0.1382` maxDD `-25.721`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
