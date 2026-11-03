# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-03T06:52:35.736110+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4520`

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

- `news_risk_high->crypto_alt_4h` score `0.2294` n `146` status `ready` deltaP `5.9326` edge `0.2535` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.4004` n `146` status `ready` deltaP `2.3316` edge `0.0559` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.6117` n `146` status `ready` deltaP `-0.8756` edge `-0.0025` maxDD `-0.6065`
- `news_risk_high->index_1h` score `-0.9323` n `146` status `ready` deltaP `0.8982` edge `-0.0037` maxDD `-1.3981`
- `news_risk_high->metal_24h` score `-0.9752` n `135` status `ready` deltaP `11.1574` edge `0.1262` maxDD `-14.0483`
- `news_risk_high->fx_4h` score `-1.2333` n `146` status `ready` deltaP `-3.3537` edge `-0.0106` maxDD `-1.6794`
- `news_risk_high->metal_1h` score `-1.2938` n `146` status `ready` deltaP `-5.098` edge `-0.0097` maxDD `-3.1082`
- `news_risk_high->index_4h` score `-2.0797` n `146` status `ready` deltaP `-3.2743` edge `-0.0147` maxDD `-4.0745`
- `news_risk_high->index_24h` score `-2.1781` n `135` status `ready` deltaP `-2.9629` edge `0.0247` maxDD `-7.402`
- `news_risk_high->commodity_1h` score `-2.3804` n `146` status `ready` deltaP `-9.0764` edge `-0.0012` maxDD `-3.2657`
- `news_risk_high->fx_24h` score `-2.3894` n `135` status `ready` deltaP `-17.6042` edge `-0.0181` maxDD `-2.336`
- `news_risk_high->equity_1h` score `-2.7155` n `146` status `ready` deltaP `-7.0851` edge `-0.0333` maxDD `-16.4088`
- `news_risk_high->crypto_alt_24h` score `-3.0425` n `135` status `ready` deltaP `20.7639` edge `0.7906` maxDD `-91.8604`
- `news_risk_high->crypto_major_1h` score `-3.1995` n `146` status `ready` deltaP `-8.0059` edge `-0.0407` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-3.8086` n `146` status `ready` deltaP `-12.3225` edge `0.0002` maxDD `-9.5011`
- `news_risk_high->equity_24h` score `-4.3378` n `135` status `ready` deltaP `15.9028` edge `0.542` maxDD `-67.0937`
- `news_risk_high->metal_4h` score `-4.8357` n `146` status `ready` deltaP `-7.4528` edge `-0.0328` maxDD `-9.3056`
- `news_risk_high->crypto_major_4h` score `-7.0104` n `146` status `ready` deltaP `-14.0787` edge `-0.0884` maxDD `-24.1554`
- `news_risk_high->equity_4h` score `-11.6314` n `146` status `ready` deltaP `-1.9024` edge `-0.1205` maxDD `-52.2214`
- `news_risk_high->crypto_major_24h` score `-11.7878` n `135` status `ready` deltaP `-12.7894` edge `0.042` maxDD `-61.4574`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
