# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-04T14:37:35.339009+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4038`

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

- `news_risk_high->crypto_alt_4h` score `0.0249` n `146` status `ready` deltaP `7.6113` edge `0.2161` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.4956` n `146` status `ready` deltaP `2.1819` edge `0.0447` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.6918` n `146` status `ready` deltaP `-2.3726` edge `-0.0028` maxDD `-0.6065`
- `news_risk_high->index_1h` score `-0.8532` n `146` status `ready` deltaP `1.6467` edge `-0.0021` maxDD `-1.3981`
- `news_risk_high->metal_1h` score `-1.3522` n `146` status `ready` deltaP `-5.6968` edge `-0.0132` maxDD `-3.1082`
- `news_risk_high->fx_4h` score `-1.4587` n `146` status `ready` deltaP `-7.5988` edge `-0.0112` maxDD `-1.6794`
- `news_risk_high->index_4h` score `-1.8391` n `146` status `ready` deltaP `0.3768` edge `-0.0082` maxDD `-4.0745`
- `news_risk_high->index_24h` score `-2.0017` n `146` status `ready` deltaP `-2.3012` edge `0.0429` maxDD `-7.402`
- `news_risk_high->commodity_1h` score `-2.2342` n `146` status `ready` deltaP `-7.8788` edge `0.003` maxDD `-3.2657`
- `news_risk_high->fx_24h` score `-2.4335` n `146` status `ready` deltaP `-18.6638` edge `-0.0167` maxDD `-2.336`
- `news_risk_high->equity_1h` score `-2.6384` n `146` status `ready` deltaP `-6.4863` edge `-0.0274` maxDD `-16.4088`
- `news_risk_high->metal_24h` score `-2.8196` n `146` status `ready` deltaP `6.034` edge `0.083` maxDD `-16.6552`
- `news_risk_high->crypto_major_1h` score `-3.2691` n `146` status `ready` deltaP `-8.3053` edge `-0.0445` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-3.483` n `146` status `ready` deltaP `-9.9034` edge `0.0112` maxDD `-9.5011`
- `news_risk_high->metal_4h` score `-4.8261` n `146` status `ready` deltaP `-5.4878` edge `-0.0451` maxDD `-9.3056`
- `news_risk_high->crypto_major_4h` score `-6.9592` n `146` status `ready` deltaP `-12.104` edge `-0.0973` maxDD `-24.1554`
- `news_risk_high->crypto_alt_24h` score `-8.7964` n `146` status `ready` deltaP `14.8221` edge `0.4729` maxDD `-118.6236`
- `news_risk_high->equity_4h` score `-11.2991` n `146` status `ready` deltaP `-0.839` edge `-0.0999` maxDD `-52.2214`
- `news_risk_high->equity_24h` score `-11.3898` n `146` status `ready` deltaP `12.5729` edge `0.4174` maxDD `-102.3626`
- `news_risk_high->commodity_24h` score `-12.2537` n `146` status `ready` deltaP `-20.6807` edge `-0.0572` maxDD `-43.7525`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
