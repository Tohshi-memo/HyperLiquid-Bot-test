# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-06T07:07:29.094262+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4274`

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

- `news_risk_high->crypto_alt_4h` score `-0.0266` n `142` status `ready` deltaP `8.2403` edge `0.2053` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.5376` n `142` status `ready` deltaP `2.994` edge `0.0339` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.6656` n `142` status `ready` deltaP `-1.9735` edge `-0.0021` maxDD `-0.6065`
- `news_risk_high->index_1h` score `-0.7011` n `142` status `ready` deltaP `3.0383` edge `0.0013` maxDD `-1.3981`
- `news_risk_high->metal_1h` score `-1.3928` n `142` status `ready` deltaP `-6.9537` edge `-0.0166` maxDD `-2.5818`
- `news_risk_high->index_4h` score `-1.4982` n `142` status `ready` deltaP `2.0397` edge `0.0071` maxDD `-4.0217`
- `news_risk_high->fx_4h` score `-1.5101` n `142` status `ready` deltaP `-8.4207` edge `-0.0123` maxDD `-1.6794`
- `news_risk_high->index_24h` score `-2.0301` n `142` status `ready` deltaP `-11.0824` edge `0.0721` maxDD `-6.6786`
- `news_risk_high->equity_1h` score `-2.3791` n `142` status `ready` deltaP `-5.6507` edge `-0.0004` maxDD `-16.3557`
- `news_risk_high->commodity_1h` score `-2.504` n `142` status `ready` deltaP `-10.9071` edge `0.0007` maxDD `-3.2657`
- `news_risk_high->fx_24h` score `-2.6741` n `142` status `ready` deltaP `-24.7526` edge `-0.0275` maxDD `-2.0252`
- `news_risk_high->crypto_major_1h` score `-2.8349` n `142` status `ready` deltaP `-5.6233` edge `-0.0262` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-4.2302` n `142` status `ready` deltaP `-17.5477` edge `-0.0001` maxDD `-9.5011`
- `news_risk_high->crypto_major_4h` score `-4.3706` n `142` status `ready` deltaP `-7.7401` edge `0.0118` maxDD `-19.2867`
- `news_risk_high->metal_4h` score `-5.3287` n `142` status `ready` deltaP `-11.8409` edge `-0.0695` maxDD `-8.6496`
- `news_risk_high->equity_24h` score `-7.0131` n `142` status `ready` deltaP `11.5406` edge `0.6454` maxDD `-92.2075`
- `news_risk_high->metal_24h` score `-8.3254` n `142` status `ready` deltaP `-15.51` edge `-0.2808` maxDD `-14.0999`
- `news_risk_high->equity_4h` score `-8.9178` n `142` status `ready` deltaP `2.497` edge `0.0201` maxDD `-49.0586`
- `news_risk_high->commodity_24h` score `-10.4429` n `142` status `ready` deltaP `-18.2051` edge `0.0772` maxDD `-43.7525`
- `news_risk_high->crypto_alt_24h` score `-12.242` n `142` status `ready` deltaP `6.8206` edge `0.0845` maxDD `-118.6236`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
