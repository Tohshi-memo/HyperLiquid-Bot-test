# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-15T06:52:27.340619+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `9718`

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

- `market_context_high->unknown_24h` score `544.8177` n `66` status `ready` deltaP `2.4263` edge `45.3853` maxDD `0.0`
- `news_risk_high->equity_24h` score `44.357` n `50` status `ready` deltaP `48.8319` edge `3.4415` maxDD `-3.6503`
- `market_context_high->equity_24h` score `38.1259` n `66` status `ready` deltaP `42.6501` edge `3.047` maxDD `-9.0005`
- `market_context_high->crypto_alt_24h` score `30.3316` n `66` status `ready` deltaP `57.8121` edge `2.2499` maxDD `-6.2814`
- `news_risk_high->crypto_major_24h` score `23.617` n `50` status `ready` deltaP `46.3882` edge `2.8329` maxDD `-6.8139`
- `news_risk_high->equity_4h` score `12.2012` n `50` status `ready` deltaP `38.5327` edge `0.8729` maxDD `-7.0416`
- `news_risk_high->crypto_alt_24h` score `7.8236` n `50` status `ready` deltaP `16.9636` edge `1.3405` maxDD `-29.0448`
- `market_context_high->index_24h` score `7.5292` n `66` status `ready` deltaP `44.9372` edge `0.337` maxDD `-0.0653`
- `news_risk_high->commodity_24h` score `7.4129` n `50` status `ready` deltaP `49.5667` edge `0.2873` maxDD `0.0`
- `news_risk_high->index_24h` score `6.3329` n `50` status `ready` deltaP `40.513` edge `0.288` maxDD `-0.4279`
- `market_context_high->metal_24h` score `5.9659` n `66` status `ready` deltaP `56.2523` edge `0.479` maxDD `-3.7989`
- `news_risk_high->crypto_major_4h` score `5.5046` n `50` status `ready` deltaP `23.3394` edge `0.4407` maxDD `-9.0062`
- `news_risk_high->metal_4h` score `5.0544` n `50` status `ready` deltaP `45.6651` edge `0.1544` maxDD `-1.0104`
- `news_risk_high->crypto_alt_4h` score `4.9828` n `50` status `ready` deltaP `29.3394` edge `0.3632` maxDD `-9.4848`
- `news_risk_high->equity_1h` score `3.9792` n `50` status `ready` deltaP `21.0479` edge `0.2543` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.4578` n `50` status `ready` deltaP `31.6195` edge `0.1027` maxDD `-0.3611`
- `market_context_high->crypto_major_24h` score `2.8649` n `66` status `ready` deltaP `12.6306` edge `1.1871` maxDD `-76.2717`
- `news_risk_high->index_4h` score `2.7998` n `50` status `ready` deltaP `27.4673` edge `0.0852` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.3095` n `50` status `ready` deltaP `26.3413` edge `0.0423` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.2855` n `50` status `ready` deltaP `17.0479` edge `0.0236` maxDD `-0.4103`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
