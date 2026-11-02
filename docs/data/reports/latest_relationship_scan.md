# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-02T11:37:30.838990+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4861`

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

- `news_risk_high->crypto_alt_24h` score `1.0549` n `116` status `ready` deltaP `19.3068` edge `0.6551` maxDD `-44.5518`
- `news_risk_high->crypto_alt_4h` score `0.4175` n `138` status `ready` deltaP `6.7912` edge `0.2369` maxDD `-11.9591`
- `news_risk_high->fx_1h` score `-0.5105` n `146` status `ready` deltaP `1.0705` edge `-0.0025` maxDD `-0.6065`
- `news_risk_high->crypto_alt_1h` score `-0.5415` n `146` status `ready` deltaP `1.2837` edge `0.0448` maxDD `-5.8225`
- `news_risk_high->metal_24h` score `-0.7848` n `116` status `ready` deltaP `14.1583` edge `0.1306` maxDD `-14.0483`
- `news_risk_high->index_1h` score `-1.1215` n `146` status `ready` deltaP `-1.0479` edge `-0.0065` maxDD `-1.3981`
- `news_risk_high->fx_4h` score `-1.2411` n `138` status `ready` deltaP `-3.2786` edge `-0.0121` maxDD `-1.6794`
- `news_risk_high->metal_1h` score `-1.2883` n `146` status `ready` deltaP `-5.098` edge `-0.009` maxDD `-3.1082`
- `news_risk_high->fx_24h` score `-2.2349` n `116` status `ready` deltaP `-15.9244` edge `-0.0095` maxDD `-2.336`
- `news_risk_high->index_4h` score `-2.2504` n `138` status `ready` deltaP `-4.803` edge `-0.0264` maxDD `-4.0745`
- `news_risk_high->commodity_1h` score `-2.3613` n `146` status `ready` deltaP `-8.3279` edge `-0.0046` maxDD `-3.2657`
- `news_risk_high->equity_1h` score `-2.9323` n `146` status `ready` deltaP `-7.6839` edge `-0.0571` maxDD `-16.4088`
- `news_risk_high->index_24h` score `-2.9979` n `116` status `ready` deltaP `-11.2129` edge `-0.0254` maxDD `-7.402`
- `news_risk_high->crypto_major_1h` score `-3.335` n `146` status `ready` deltaP `-8.7544` edge `-0.047` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-4.102` n `138` status `ready` deltaP `-13.5803` edge `-0.0194` maxDD `-9.2186`
- `news_risk_high->metal_4h` score `-4.4756` n `138` status `ready` deltaP `-3.6276` edge `-0.0283` maxDD `-9.3056`
- `news_risk_high->equity_24h` score `-5.7515` n `116` status `ready` deltaP `5.825` edge `0.2333` maxDD `-67.0937`
- `news_risk_high->crypto_major_4h` score `-7.2491` n `138` status `ready` deltaP `-14.3779` edge `-0.1063` maxDD `-24.1554`
- `news_risk_high->equity_4h` score `-8.4165` n `138` status `ready` deltaP `-3.6209` edge `-0.2188` maxDD `-52.2214`
- `news_risk_high->commodity_24h` score `-11.1449` n `116` status `ready` deltaP `-25.5987` edge `-0.1439` maxDD `-26.8016`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
