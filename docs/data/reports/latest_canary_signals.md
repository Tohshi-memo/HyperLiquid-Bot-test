# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-02T09:07:22.823801+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.008` n `12`; crypto_alt avg `-0.0441` n `230`; crypto_major avg `-0.1105` n `8`; equity avg `-0.0891` n `102`; fx avg `0.0609` n `6`; index avg `-0.021` n `25`; metal avg `-0.0063` n `20`; unknown avg `-0.0187` n `782`
- 1h: commodity avg `0.0309` n `12`; crypto_alt avg `-0.1332` n `230`; crypto_major avg `-0.284` n `8`; equity avg `-0.088` n `102`; fx avg `-0.0213` n `6`; index avg `-0.0192` n `25`; metal avg `-0.0142` n `20`; unknown avg `-0.0077` n `782`
- 4h: commodity avg `-0.1105` n `12`; crypto_alt avg `-0.0579` n `230`; crypto_major avg `-0.4757` n `8`; equity avg `0.0435` n `102`; fx avg `-0.054` n `6`; index avg `0.0253` n `25`; metal avg `-0.0007` n `20`; unknown avg `0.256` n `766`
- 24h: commodity avg `-1.1731` n `12`; crypto_alt avg `0.2122` n `230`; crypto_major avg `0.0586` n `8`; equity avg `0.8255` n `102`; fx avg `-0.1754` n `6`; index avg `0.258` n `25`; metal avg `0.2289` n `20`; unknown avg `0.249` n `765`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1315`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.121`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1103`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0932`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.088`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0777`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0712`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.07`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0691`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0685`, n `668`, weak_sample_signal
