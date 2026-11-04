# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-04T01:07:27.447403+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4411`

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

- `news_risk_high->crypto_alt_4h` score `0.4806` n `146` status `ready` deltaP `8.829` edge `0.2664` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.3209` n `146` status `ready` deltaP `2.9304` edge `0.0621` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.7098` n `146` status `ready` deltaP `-2.672` edge `-0.0031` maxDD `-0.6065`
- `news_risk_high->index_1h` score `-0.8172` n `146` status `ready` deltaP `1.9461` edge `-0.0011` maxDD `-1.3981`
- `news_risk_high->metal_1h` score `-1.1645` n `146` status `ready` deltaP `-3.1519` edge `-0.0061` maxDD `-3.1082`
- `news_risk_high->metal_24h` score `-1.386` n `146` status `ready` deltaP `12.2979` edge `0.1607` maxDD `-16.6552`
- `news_risk_high->fx_4h` score `-1.467` n `146` status `ready` deltaP `-7.622` edge `-0.0121` maxDD `-1.6794`
- `news_risk_high->index_24h` score `-1.7174` n `146` status `ready` deltaP `2.0715` edge `0.0502` maxDD `-7.402`
- `news_risk_high->index_4h` score `-1.9283` n `146` status `ready` deltaP `-1.2926` edge `-0.0085` maxDD `-4.0745`
- `news_risk_high->fx_24h` score `-2.2349` n `146` status `ready` deltaP `-16.4645` edge `-0.0059` maxDD `-2.336`
- `news_risk_high->commodity_1h` score `-2.5433` n `146` status `ready` deltaP `-10.8728` edge `-0.0028` maxDD `-3.2657`
- `news_risk_high->equity_1h` score `-2.604` n `146` status `ready` deltaP `-6.4863` edge `-0.023` maxDD `-16.4088`
- `news_risk_high->crypto_major_1h` score `-3.028` n `146` status `ready` deltaP `-7.2574` edge `-0.0314` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-4.0653` n `146` status `ready` deltaP `-14.1518` edge `-0.009` maxDD `-9.5011`
- `news_risk_high->metal_4h` score `-4.3274` n `146` status `ready` deltaP `-3.1845` edge `-0.0189` maxDD `-9.3056`
- `news_risk_high->crypto_alt_24h` score `-5.9535` n `146` status `ready` deltaP `22.3198` edge `0.7874` maxDD `-118.6236`
- `news_risk_high->crypto_major_4h` score `-6.5475` n `146` status `ready` deltaP `-11.4873` edge `-0.0671` maxDD `-24.1554`
- `news_risk_high->equity_24h` score `-8.3167` n `146` status `ready` deltaP `19.0212` edge `0.6305` maxDD `-102.3626`
- `news_risk_high->equity_4h` score `-11.3354` n `146` status `ready` deltaP `-1.2926` edge `-0.0999` maxDD `-52.2214`
- `news_risk_high->commodity_24h` score `-12.2928` n `146` status `ready` deltaP `-20.089` edge `-0.0644` maxDD `-43.7525`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
