# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-27T22:37:28.526210+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0189` n `12`; crypto_alt avg `-0.1128` n `231`; crypto_major avg `-0.1399` n `8`; equity avg `-0.0286` n `127`; fx avg `-0.0004` n `6`; index avg `0.0014` n `26`; metal avg `0.0097` n `20`; unknown avg `0.6724` n `792`
- 1h: commodity avg `0.0103` n `12`; crypto_alt avg `0.3285` n `231`; crypto_major avg `0.2881` n `8`; equity avg `-0.0233` n `127`; fx avg `0.0092` n `6`; index avg `-0.0142` n `26`; metal avg `0.0665` n `20`; unknown avg `0.1111` n `792`
- 4h: commodity avg `-0.0622` n `12`; crypto_alt avg `0.4246` n `231`; crypto_major avg `0.3621` n `8`; equity avg `0.057` n `127`; fx avg `0.0083` n `6`; index avg `0.0817` n `26`; metal avg `0.1026` n `20`; unknown avg `0.1753` n `792`
- 24h: commodity avg `0.3635` n `12`; crypto_alt avg `1.5568` n `231`; crypto_major avg `2.7963` n `8`; equity avg `-0.3077` n `127`; fx avg `-0.0237` n `6`; index avg `-0.138` n `26`; metal avg `0.1315` n `20`; unknown avg `0.9315` n `775`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1308`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.125`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0856`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0841`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0829`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0757`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0713`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0641`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0626`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0542`, n `668`, weak_sample_signal
