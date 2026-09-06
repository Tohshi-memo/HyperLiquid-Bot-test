# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-06T11:52:25.970535+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0207` n `12`; crypto_alt avg `0.0318` n `232`; crypto_major avg `0.0776` n `8`; equity avg `0.0037` n `134`; fx avg `-0.0136` n `6`; index avg `-0.0132` n `26`; metal avg `0.003` n `20`; unknown avg `162.3708` n `792`
- 1h: commodity avg `-0.0344` n `12`; crypto_alt avg `0.2405` n `232`; crypto_major avg `0.0724` n `8`; equity avg `-0.0092` n `134`; fx avg `-0.0103` n `6`; index avg `-0.0042` n `26`; metal avg `0.0059` n `20`; unknown avg `161.6909` n `790`
- 4h: commodity avg `-0.0124` n `12`; crypto_alt avg `0.8699` n `232`; crypto_major avg `0.4063` n `8`; equity avg `0.1953` n `134`; fx avg `-0.0249` n `6`; index avg `0.0044` n `26`; metal avg `0.0173` n `20`; unknown avg `326.0278` n `784`
- 24h: commodity avg `0.0956` n `12`; crypto_alt avg `2.4293` n `232`; crypto_major avg `2.1523` n `8`; equity avg `0.5074` n `134`; fx avg `-0.0217` n `6`; index avg `0.0662` n `26`; metal avg `0.0085` n `20`; unknown avg `492.6098` n `677`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1292`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1125`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1085`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1036`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1001`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0974`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0932`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0929`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0839`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0812`, n `668`, weak_sample_signal
