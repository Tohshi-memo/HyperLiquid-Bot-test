# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-03T05:22:33.037167+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4564`

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

- `news_risk_high->crypto_alt_4h` score `0.2041` n `146` status `ready` deltaP `5.6277` edge `0.2523` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.4643` n `146` status `ready` deltaP `1.7328` edge `0.0517` maxDD `-5.8225`
- `news_risk_high->crypto_alt_24h` score `-0.491` n `129` status `ready` deltaP `22.5129` edge `0.8623` maxDD `-74.3602`
- `news_risk_high->fx_1h` score `-0.5953` n `146` status `ready` deltaP `-0.5762` edge `-0.0024` maxDD `-0.6065`
- `news_risk_high->metal_24h` score `-0.8347` n `129` status `ready` deltaP `12.7341` edge `0.1337` maxDD `-14.0483`
- `news_risk_high->index_1h` score `-0.9179` n `146` status `ready` deltaP `1.0479` edge `-0.0035` maxDD `-1.3981`
- `news_risk_high->fx_4h` score `-1.208` n `146` status `ready` deltaP `-2.8963` edge `-0.0104` maxDD `-1.6794`
- `news_risk_high->metal_1h` score `-1.2922` n `146` status `ready` deltaP `-5.098` edge `-0.0095` maxDD `-3.1082`
- `news_risk_high->equity_24h` score `-1.8979` n `129` status `ready` deltaP `17.6518` edge `0.6485` maxDD `-67.0937`
- `news_risk_high->index_24h` score `-2.0727` n `129` status `ready` deltaP `-2.0752` edge `0.0323` maxDD `-7.402`
- `news_risk_high->index_4h` score `-2.1389` n `146` status `ready` deltaP `-4.1889` edge `-0.0162` maxDD `-4.0745`
- `news_risk_high->commodity_1h` score `-2.39` n `146` status `ready` deltaP `-9.0764` edge `-0.002` maxDD `-3.2657`
- `news_risk_high->fx_24h` score `-2.4747` n `129` status `ready` deltaP `-19.3799` edge `-0.0172` maxDD `-2.336`
- `news_risk_high->equity_1h` score `-2.7062` n `146` status `ready` deltaP `-6.9354` edge `-0.0331` maxDD `-16.4088`
- `news_risk_high->crypto_major_1h` score `-3.2463` n `146` status `ready` deltaP `-8.3053` edge `-0.0426` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-3.7832` n `146` status `ready` deltaP `-12.1701` edge `0.0013` maxDD `-9.5011`
- `news_risk_high->metal_4h` score `-4.8997` n `146` status `ready` deltaP `-7.7577` edge `-0.0361` maxDD `-9.3056`
- `news_risk_high->crypto_major_4h` score `-7.0538` n `146` status `ready` deltaP `-14.2312` edge `-0.091` maxDD `-24.1554`
- `news_risk_high->crypto_major_24h` score `-9.2486` n `129` status `ready` deltaP `-12.6251` edge `0.0733` maxDD `-49.1215`
- `news_risk_high->commodity_24h` score `-11.5204` n `129` status `ready` deltaP `-24.1239` edge `-0.0803` maxDD `-35.1794`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
