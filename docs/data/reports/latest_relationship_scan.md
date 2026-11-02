# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-02T20:52:26.749413+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4933`

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

- `news_risk_high->crypto_alt_4h` score `0.1752` n `146` status `ready` deltaP `5.4753` edge `0.2496` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.4682` n `146` status `ready` deltaP `1.5831` edge `0.0522` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.5977` n `146` status `ready` deltaP `-0.5762` edge `-0.0027` maxDD `-0.6065`
- `news_risk_high->metal_24h` score `-0.8906` n `126` status `ready` deltaP `12.5744` edge `0.1276` maxDD `-14.0483`
- `news_risk_high->index_1h` score `-0.9622` n `146` status `ready` deltaP `0.5988` edge `-0.0042` maxDD `-1.3981`
- `news_risk_high->fx_4h` score `-1.2688` n `146` status `ready` deltaP `-3.811` edge `-0.0121` maxDD `-1.6794`
- `news_risk_high->metal_1h` score `-1.2907` n `146` status `ready` deltaP `-4.9483` edge `-0.0103` maxDD `-3.1082`
- `news_risk_high->crypto_alt_24h` score `-1.3355` n `126` status `ready` deltaP `18.1051` edge `0.6586` maxDD `-65.3749`
- `news_risk_high->index_4h` score `-2.1687` n `146` status `ready` deltaP `-4.3414` edge `-0.019` maxDD `-4.0745`
- `news_risk_high->commodity_1h` score `-2.2726` n `146` status `ready` deltaP `-7.8788` edge `-0.0002` maxDD `-3.2657`
- `news_risk_high->fx_24h` score `-2.3365` n `126` status `ready` deltaP `-17.8324` edge `-0.0098` maxDD `-2.336`
- `news_risk_high->index_24h` score `-2.4664` n `126` status `ready` deltaP `-6.0764` edge `0.0085` maxDD `-7.402`
- `news_risk_high->equity_1h` score `-2.6369` n `146` status `ready` deltaP `-6.0372` edge `-0.0302` maxDD `-16.4088`
- `news_risk_high->crypto_major_1h` score `-3.2043` n `146` status `ready` deltaP `-8.0059` edge `-0.0411` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-3.6904` n `146` status `ready` deltaP `-10.9506` edge `0.0009` maxDD `-9.5011`
- `news_risk_high->equity_24h` score `-3.8096` n `126` status `ready` deltaP `13.244` edge `0.4328` maxDD `-67.0937`
- `news_risk_high->metal_4h` score `-4.7961` n `146` status `ready` deltaP `-6.5382` edge `-0.0356` maxDD `-9.3056`
- `news_risk_high->crypto_major_4h` score `-6.9128` n `146` status `ready` deltaP `-13.7738` edge `-0.0823` maxDD `-24.1554`
- `news_risk_high->crypto_major_24h` score `-10.6708` n `126` status `ready` deltaP `-17.8819` edge `-0.089` maxDD `-43.1482`
- `news_risk_high->equity_4h` score `-11.7292` n `146` status `ready` deltaP `-2.3597` edge `-0.1256` maxDD `-52.2214`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
