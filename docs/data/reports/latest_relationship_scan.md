# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-06T08:22:28.724170+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4042`

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

- `news_risk_high->crypto_alt_4h` score `-0.1202` n `137` status `ready` deltaP `7.0544` edge `0.2012` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.4429` n `137` status `ready` deltaP `3.359` edge `0.0436` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.6853` n `137` status `ready` deltaP `-2.3668` edge `-0.002` maxDD `-0.6065`
- `news_risk_high->index_1h` score `-0.7782` n `137` status `ready` deltaP `2.0674` edge `0.0009` maxDD `-1.3628`
- `news_risk_high->index_4h` score `-1.2032` n `137` status `ready` deltaP `3.5339` edge `0.0091` maxDD `-3.6199`
- `news_risk_high->metal_1h` score `-1.3224` n `137` status `ready` deltaP `-5.8864` edge `-0.0151` maxDD `-2.5487`
- `news_risk_high->fx_4h` score `-1.5395` n `137` status `ready` deltaP `-8.9571` edge `-0.0125` maxDD `-1.6794`
- `news_risk_high->index_24h` score `-1.6976` n `137` status `ready` deltaP `-9.6431` edge `0.0843` maxDD `-6.6786`
- `news_risk_high->crypto_major_1h` score `-1.9894` n `137` status `ready` deltaP `-4.4834` edge `-0.0049` maxDD `-6.1465`
- `news_risk_high->fx_24h` score `-2.3577` n `137` status `ready` deltaP `-22.9535` edge `-0.0237` maxDD `-1.7108`
- `news_risk_high->commodity_1h` score `-2.7184` n `137` status `ready` deltaP `-12.7923` edge `-0.0046` maxDD `-3.2657`
- `news_risk_high->crypto_major_4h` score `-3.1169` n `137` status `ready` deltaP `-6.556` edge `0.0363` maxDD `-14.8535`
- `news_risk_high->equity_1h` score `-3.2148` n `137` status `ready` deltaP `-4.7074` edge `0.007` maxDD `-14.4817`
- `news_risk_high->equity_24h` score `-4.4931` n `137` status `ready` deltaP `13.6224` edge `0.7434` maxDD `-86.0244`
- `news_risk_high->commodity_4h` score `-4.5008` n `137` status `ready` deltaP `-19.4309` edge `-0.0101` maxDD `-9.5011`
- `news_risk_high->metal_4h` score `-4.8987` n `137` status `ready` deltaP `-10.8332` edge `-0.0686` maxDD `-8.059`
- `news_risk_high->metal_24h` score `-7.3963` n `137` status `ready` deltaP `-13.5566` edge `-0.2676` maxDD `-11.6702`
- `news_risk_high->equity_4h` score `-7.5293` n `137` status `ready` deltaP `3.9912` edge `0.0412` maxDD `-43.9534`
- `news_risk_high->commodity_24h` score `-10.8824` n `137` status `ready` deltaP `-21.0151` edge `0.055` maxDD `-43.7416`
- `news_risk_high->crypto_alt_24h` score `-12.3136` n `137` status `ready` deltaP `6.0149` edge `0.0807` maxDD `-118.6236`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
