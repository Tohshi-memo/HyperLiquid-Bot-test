# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-02T17:22:31.687203+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.2752` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `1.7823` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0229` n `13`; crypto_alt avg `-0.1037` n `235`; crypto_major avg `-0.08` n `8`; equity avg `-0.0736` n `143`; fx avg `0.0163` n `6`; index avg `-0.0094` n `26`; metal avg `-0.0015` n `20`; unknown avg `-0.5319` n `984`
- 1h: commodity avg `0.1784` n `13`; crypto_alt avg `-0.8898` n `235`; crypto_major avg `-0.3605` n `8`; equity avg `-0.2686` n `143`; fx avg `0.0212` n `6`; index avg `-0.0264` n `26`; metal avg `-0.0026` n `20`; unknown avg `1.9397` n `982`
- 4h: commodity avg `0.4102` n `13`; crypto_alt avg `-1.4275` n `235`; crypto_major avg `-1.865` n `8`; equity avg `-0.5734` n `143`; fx avg `0.0817` n `6`; index avg `-0.0827` n `26`; metal avg `-0.3831` n `20`; unknown avg `1.9419` n `934`
- 24h: commodity avg `-0.0526` n `13`; crypto_alt avg `1.1956` n `235`; crypto_major avg `0.3364` n `8`; equity avg `0.8545` n `142`; fx avg `-0.0761` n `6`; index avg `0.341` n `26`; metal avg `-0.3144` n `20`; unknown avg `100.2647` n `824`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1679`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1652`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1432`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1233`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1206`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1144`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.107`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.097`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0869`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0851`, n `668`, weak_sample_signal
