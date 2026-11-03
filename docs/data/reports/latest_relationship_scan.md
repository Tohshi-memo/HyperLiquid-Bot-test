# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-03T06:07:32.859076+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4526`

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

- `news_risk_high->crypto_alt_4h` score `0.2129` n `146` status `ready` deltaP `5.7802` edge `0.2524` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.4495` n `146` status `ready` deltaP `1.8825` edge `0.0526` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.6039` n `146` status `ready` deltaP `-0.7259` edge `-0.0025` maxDD `-0.6065`
- `news_risk_high->metal_24h` score `-0.9123` n `132` status `ready` deltaP `11.9161` edge `0.1292` maxDD `-14.0483`
- `news_risk_high->index_1h` score `-0.9311` n `146` status `ready` deltaP `0.8982` edge `-0.0036` maxDD `-1.3981`
- `news_risk_high->fx_4h` score `-1.2167` n `146` status `ready` deltaP `-3.0488` edge `-0.0105` maxDD `-1.6794`
- `news_risk_high->metal_1h` score `-1.2954` n `146` status `ready` deltaP `-5.098` edge `-0.0099` maxDD `-3.1082`
- `news_risk_high->crypto_alt_24h` score `-1.8748` n `132` status `ready` deltaP `21.6067` edge `0.8208` maxDD `-83.7492`
- `news_risk_high->index_4h` score `-2.1097` n `146` status `ready` deltaP `-3.7316` edge `-0.0155` maxDD `-4.0745`
- `news_risk_high->index_24h` score `-2.1312` n `132` status `ready` deltaP `-2.5411` edge `0.0279` maxDD `-7.402`
- `news_risk_high->commodity_1h` score `-2.3852` n `146` status `ready` deltaP `-9.0764` edge `-0.0016` maxDD `-3.2657`
- `news_risk_high->equity_24h` score `-2.3982` n `132` status `ready` deltaP `16.7455` edge `0.5904` maxDD `-67.0937`
- `news_risk_high->fx_24h` score `-2.4139` n `132` status `ready` deltaP `-18.1819` edge `-0.0174` maxDD `-2.336`
- `news_risk_high->equity_1h` score `-2.7062` n `146` status `ready` deltaP `-6.9354` edge `-0.0331` maxDD `-16.4088`
- `news_risk_high->crypto_major_1h` score `-3.2415` n `146` status `ready` deltaP `-8.3053` edge `-0.0422` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-3.7844` n `146` status `ready` deltaP `-12.1701` edge `0.0012` maxDD `-9.5011`
- `news_risk_high->metal_4h` score `-4.8829` n `146` status `ready` deltaP `-7.7577` edge `-0.0347` maxDD `-9.3056`
- `news_risk_high->crypto_major_4h` score `-7.0442` n `146` status `ready` deltaP `-14.2312` edge `-0.0902` maxDD `-24.1554`
- `news_risk_high->crypto_major_24h` score `-10.676` n `132` status `ready` deltaP `-12.7209` edge `0.0524` maxDD `-55.9143`
- `news_risk_high->equity_4h` score `-11.752` n `146` status `ready` deltaP `-2.3597` edge `-0.1275` maxDD `-52.2214`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
