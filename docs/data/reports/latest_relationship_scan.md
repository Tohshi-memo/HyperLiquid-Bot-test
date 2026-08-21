# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-21T10:37:30.661604+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `13758`

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

- `market_context_high->equity_1h` score `0.5506` n `111` status `ready` deltaP `10.3766` edge `0.0582` maxDD `-3.1861`
- `market_context_high->index_1h` score `0.3914` n `111` status `ready` deltaP `11.264` edge `0.0063` maxDD `-0.5685`
- `market_context_high->fx_4h` score `0.1064` n `105` status `ready` deltaP `8.4001` edge `0.0079` maxDD `-0.3539`
- `market_context_high->equity_4h` score `0.0257` n `105` status `ready` deltaP `4.5877` edge `0.1345` maxDD `-8.3685`
- `market_context_high->fx_1h` score `-0.0668` n `111` status `ready` deltaP `3.3029` edge `0.0053` maxDD `-0.2043`
- `market_context_high->metal_4h` score `-0.257` n `105` status `ready` deltaP `6.5302` edge `-0.0189` maxDD `-1.273`
- `market_context_high->index_4h` score `-0.3012` n `105` status `ready` deltaP `5.4283` edge `0.0176` maxDD `-1.7252`
- `market_context_high->metal_1h` score `-0.3359` n `111` status `ready` deltaP `0.4559` edge `-0.0066` maxDD `-0.4934`
- `market_context_high->commodity_24h` score `-0.4209` n `105` status `ready` deltaP `4.7619` edge `0.1165` maxDD `-4.666`
- `market_context_high->unknown_1h` score `-0.4942` n `111` status `ready` deltaP `8.7353` edge `-0.0767` maxDD `-0.4843`
- `market_context_high->commodity_1h` score `-0.6775` n `111` status `ready` deltaP `-4.7945` edge `0.0017` maxDD `-1.1941`
- `market_context_high->commodity_4h` score `-0.79` n `105` status `ready` deltaP `-3.2622` edge `0.0055` maxDD `-2.4692`
- `market_context_high->crypto_major_1h` score `-1.0755` n `111` status `ready` deltaP `-2.0863` edge `-0.0395` maxDD `-2.7581`
- `market_context_high->crypto_alt_1h` score `-1.4317` n `111` status `ready` deltaP `-2.8267` edge `-0.0203` maxDD `-2.413`
- `market_context_high->fx_24h` score `-3.2345` n `105` status `ready` deltaP `-14.5586` edge `-0.0115` maxDD `-2.2121`
- `market_context_high->crypto_alt_4h` score `-3.4626` n `105` status `ready` deltaP `-1.3589` edge `-0.1525` maxDD `-5.4926`
- `market_context_high->crypto_major_4h` score `-3.7921` n `105` status `ready` deltaP `0.4326` edge `-0.2168` maxDD `-3.1677`
- `market_context_high->index_24h` score `-4.0388` n `105` status `ready` deltaP `-3.6855` edge `-0.043` maxDD `-18.6848`
- `market_context_high->unknown_24h` score `-4.2126` n `105` status `ready` deltaP `10.377` edge `-0.3696` maxDD `-1.0505`
- `market_context_high->metal_24h` score `-4.3514` n `105` status `ready` deltaP `-16.7212` edge `-0.1156` maxDD `-11.4635`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
