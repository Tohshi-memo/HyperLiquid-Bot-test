# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-01T10:22:26.640199+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0437` n `12`; crypto_alt avg `-0.0479` n `228`; crypto_major avg `-0.1143` n `8`; equity avg `0.0188` n `88`; fx avg `0.0003` n `6`; index avg `0.0124` n `23`; metal avg `-0.1008` n `20`; unknown avg `-0.1042` n `765`
- 1h: commodity avg `0.0744` n `12`; crypto_alt avg `-0.0274` n `228`; crypto_major avg `-0.2322` n `8`; equity avg `0.1312` n `88`; fx avg `0.0339` n `6`; index avg `0.0232` n `23`; metal avg `0.0015` n `20`; unknown avg `-0.1632` n `765`
- 4h: commodity avg `-0.1512` n `12`; crypto_alt avg `0.0492` n `228`; crypto_major avg `-0.3495` n `8`; equity avg `0.0723` n `88`; fx avg `0.0278` n `6`; index avg `0.008` n `23`; metal avg `0.1069` n `20`; unknown avg `0.0669` n `763`
- 24h: commodity avg `-0.4551` n `12`; crypto_alt avg `-0.1432` n `228`; crypto_major avg `-0.5873` n `8`; equity avg `0.6015` n `88`; fx avg `0.1283` n `6`; index avg `0.0282` n `23`; metal avg `-0.7647` n `20`; unknown avg `-0.2815` n `743`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1217`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1152`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0977`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0908`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0856`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0836`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0722`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.072`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0718`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0617`, n `668`, weak_sample_signal
