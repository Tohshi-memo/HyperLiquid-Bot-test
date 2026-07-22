# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-22T12:22:24.759180+00:00`
- Price records: `672`
- Market context records: `7564`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14475`

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

- `market_context_high->commodity_4h` score `-0.0089` n `174` status `ready` deltaP `7.6453` edge `0.0243` maxDD `-2.4139`
- `market_context_high->index_1h` score `-0.0945` n `174` status `ready` deltaP `5.9025` edge `0.0081` maxDD `-1.7657`
- `market_context_high->fx_1h` score `-0.2314` n `174` status `ready` deltaP `2.9512` edge `0.0006` maxDD `-0.6615`
- `market_context_high->unknown_1h` score `-0.3832` n `174` status `ready` deltaP `2.8977` edge `0.0111` maxDD `-1.3217`
- `market_context_high->commodity_1h` score `-0.3887` n `174` status `ready` deltaP `3.4689` edge `0.0017` maxDD `-1.5775`
- `market_context_high->unknown_4h` score `-0.4129` n `174` status `ready` deltaP `11.9148` edge `0.1035` maxDD `-6.2031`
- `market_context_high->commodity_24h` score `-0.4255` n `153` status `ready` deltaP `11.4436` edge `0.0466` maxDD `-7.0012`
- `market_context_high->crypto_alt_1h` score `-0.6138` n `174` status `ready` deltaP `0.5988` edge `0.0212` maxDD `-5.9775`
- `market_context_high->crypto_major_1h` score `-0.6338` n `174` status `ready` deltaP `5.0227` edge `0.0263` maxDD `-7.6171`
- `market_context_high->fx_24h` score `-0.7066` n `153` status `ready` deltaP `10.3869` edge `0.0159` maxDD `-3.8554`
- `market_context_high->index_4h` score `-0.8251` n `174` status `ready` deltaP `9.6489` edge `0.024` maxDD `-5.1957`
- `market_context_high->metal_1h` score `-1.049` n `174` status `ready` deltaP `1.2699` edge `0.0145` maxDD `-1.4971`
- `market_context_high->fx_4h` score `-1.239` n `174` status `ready` deltaP `0.8278` edge `0.0041` maxDD `-2.1439`
- `market_context_high->equity_1h` score `-1.4338` n `174` status `ready` deltaP `4.3285` edge `0.0284` maxDD `-14.6193`
- `market_context_high->metal_4h` score `-1.4879` n `174` status `ready` deltaP `1.3247` edge `0.0486` maxDD `-4.8549`
- `market_context_high->unknown_24h` score `-1.6888` n `154` status `ready` deltaP `4.5117` edge `0.0283` maxDD `-9.9917`
- `market_context_high->crypto_alt_4h` score `-1.7907` n `174` status `ready` deltaP `0.9497` edge `0.0384` maxDD `-15.2776`
- `market_context_high->crypto_major_4h` score `-2.3852` n `174` status `ready` deltaP `5.0901` edge `0.0497` maxDD `-23.4879`
- `market_context_high->equity_4h` score `-3.7254` n `174` status `ready` deltaP `1.7927` edge `0.1396` maxDD `-37.3335`
- `market_context_high->index_24h` score `-4.4785` n `153` status `ready` deltaP `-19.7604` edge `-0.0173` maxDD `-19.3436`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
