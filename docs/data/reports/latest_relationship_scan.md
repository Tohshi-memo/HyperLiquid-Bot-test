# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-06T11:37:22.839566+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4236`

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

- `news_risk_high->crypto_alt_4h` score `-0.4279` n `124` status `ready` deltaP `5.2321` edge `0.1739` maxDD `-14.0916`
- `news_risk_high->index_4h` score `-0.4613` n `124` status `ready` deltaP `6.9089` edge `0.0121` maxDD `-2.3845`
- `news_risk_high->index_1h` score `-0.4982` n `124` status `ready` deltaP `4.7566` edge `0.0016` maxDD `-0.9862`
- `news_risk_high->equity_24h` score `-0.5632` n `124` status `ready` deltaP `19.8209` edge `0.9543` maxDD `-86.0244`
- `news_risk_high->fx_1h` score `-0.6561` n `124` status `ready` deltaP `-3.8922` edge `-0.0023` maxDD `-0.469`
- `news_risk_high->crypto_alt_1h` score `-0.8239` n `124` status `ready` deltaP `-0.5312` edge `0.0207` maxDD `-5.8225`
- `news_risk_high->index_24h` score `-0.8276` n `124` status `ready` deltaP `-5.3577` edge `0.1131` maxDD `-6.6786`
- `news_risk_high->fx_4h` score `-0.9152` n `124` status `ready` deltaP `-4.2879` edge `-0.0051` maxDD `-0.6916`
- `news_risk_high->metal_1h` score `-1.498` n `124` status `ready` deltaP `-5.0464` edge `-0.0159` maxDD `-2.0231`
- `news_risk_high->fx_24h` score `-1.5334` n `124` status `ready` deltaP `-17.9429` edge `-0.0109` maxDD `-0.619`
- `news_risk_high->equity_1h` score `-1.6723` n `124` status `ready` deltaP `-2.7767` edge `0.0112` maxDD `-11.5672`
- `news_risk_high->crypto_major_4h` score `-1.9331` n `124` status `ready` deltaP `-4.2535` edge `0.0521` maxDD `-9.4536`
- `news_risk_high->crypto_major_1h` score `-2.1223` n `124` status `ready` deltaP `-5.2782` edge `-0.0162` maxDD `-6.0373`
- `news_risk_high->commodity_1h` score `-2.9367` n `124` status `ready` deltaP `-14.9652` edge `-0.0083` maxDD `-3.2657`
- `news_risk_high->metal_4h` score `-3.3549` n `124` status `ready` deltaP `-8.453` edge `-0.0552` maxDD `-4.4417`
- `news_risk_high->equity_4h` score `-4.3085` n `124` status `ready` deltaP `7.3662` edge `0.0733` maxDD `-31.1825`
- `news_risk_high->commodity_4h` score `-4.6318` n `124` status `ready` deltaP `-20.9481` edge `-0.0109` maxDD `-9.5011`
- `news_risk_high->metal_24h` score `-5.6929` n `124` status `ready` deltaP `-7.7408` edge `-0.2332` maxDD `-8.5019`
- `news_risk_high->commodity_24h` score `-10.3265` n `124` status `ready` deltaP `-22.7285` edge `0.0227` maxDD `-40.8706`
- `news_risk_high->crypto_major_24h` score `-10.7931` n `124` status `ready` deltaP `-18.833` edge `0.083` maxDD `-51.2165`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
