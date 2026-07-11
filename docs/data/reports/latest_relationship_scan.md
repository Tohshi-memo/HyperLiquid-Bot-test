# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-11T12:22:25.825618+00:00`
- Price records: `672`
- Market context records: `6390`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11074`

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

- `news_risk_high->crypto_alt_24h` score `14.0254` n `32` status `ready` deltaP `36.9792` edge `0.937` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `6.5012` n `32` status `ready` deltaP `54.3403` edge `0.1795` maxDD `0.0`
- `news_risk_high->commodity_24h` score `4.3839` n `32` status `ready` deltaP `38.0208` edge `0.1324` maxDD `-0.3101`
- `news_risk_high->crypto_major_24h` score `4.2786` n `32` status `ready` deltaP `17.5347` edge `0.5096` maxDD `-4.2368`
- `news_risk_high->fx_4h` score `3.9852` n `32` status `ready` deltaP `41.2348` edge `0.0618` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.4099` n `32` status `ready` deltaP `29.0419` edge `0.0211` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `1.4609` n `32` status `ready` deltaP `13.9783` edge `0.1408` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.8177` n `32` status `ready` deltaP `10.2732` edge `0.0825` maxDD `-1.6923`
- `market_context_high->metal_4h` score `0.4522` n `216` status `ready` deltaP `14.4196` edge `0.0415` maxDD `-2.7056`
- `market_context_high->index_4h` score `0.1718` n `216` status `ready` deltaP `9.0673` edge `0.0215` maxDD `-0.4108`
- `market_context_high->unknown_1h` score `0.158` n `226` status `ready` deltaP `-6.0781` edge `0.1545` maxDD `-3.7317`
- `news_risk_high->unknown_1h` score `-0.1734` n `32` status `ready` deltaP `7.2792` edge `-0.0285` maxDD `-0.7581`
- `market_context_high->metal_24h` score `-0.2257` n `146` status `ready` deltaP `19.6205` edge `0.0971` maxDD `-11.8809`
- `market_context_high->metal_1h` score `-0.4563` n `226` status `ready` deltaP `2.4853` edge `0.0027` maxDD `-1.8877`
- `market_context_high->equity_4h` score `-0.4934` n `216` status `ready` deltaP `8.3898` edge `0.0507` maxDD `-8.2573`
- `news_risk_high->metal_1h` score `-0.6609` n `32` status `ready` deltaP `-1.497` edge `-0.025` maxDD `-1.6464`
- `market_context_high->index_1h` score `-0.6797` n `226` status `ready` deltaP `-2.6681` edge `0.0026` maxDD `-0.7564`
- `market_context_high->commodity_1h` score `-0.7078` n `226` status `ready` deltaP `-2.9609` edge `-0.0027` maxDD `-2.1314`
- `market_context_high->fx_1h` score `-0.7247` n `226` status `ready` deltaP `-0.8254` edge `-0.0015` maxDD `-0.9376`
- `news_risk_high->index_24h` score `-0.7409` n `32` status `ready` deltaP `0.5208` edge `-0.0113` maxDD `-2.3058`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
