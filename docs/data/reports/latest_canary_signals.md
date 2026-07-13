# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-13T21:22:25.581394+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0467` n `12`; crypto_alt avg `-0.1215` n `230`; crypto_major avg `-0.1321` n `8`; equity avg `-0.0583` n `92`; fx avg `0.0055` n `6`; index avg `0.0064` n `25`; metal avg `-0.009` n `20`; unknown avg `-0.0221` n `766`
- 1h: commodity avg `-0.0129` n `12`; crypto_alt avg `-0.1667` n `230`; crypto_major avg `-0.1512` n `8`; equity avg `-0.0116` n `92`; fx avg `0.0023` n `6`; index avg `-0.0189` n `25`; metal avg `0.0208` n `20`; unknown avg `-0.0931` n `766`
- 4h: commodity avg `0.3918` n `12`; crypto_alt avg `-0.757` n `230`; crypto_major avg `-0.515` n `8`; equity avg `-0.3258` n `92`; fx avg `-0.0153` n `6`; index avg `-0.1261` n `25`; metal avg `-0.0291` n `20`; unknown avg `-0.3621` n `766`
- 24h: commodity avg `0.6367` n `12`; crypto_alt avg `-2.4496` n `230`; crypto_major avg `-3.0082` n `8`; equity avg `-3.3146` n `92`; fx avg `-0.0382` n `6`; index avg `-0.6717` n `25`; metal avg `-0.5335` n `20`; unknown avg `-0.3859` n `749`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1879`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1757`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1137`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1127`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1098`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1037`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1032`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0996`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0777`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0683`, n `668`, weak_sample_signal
