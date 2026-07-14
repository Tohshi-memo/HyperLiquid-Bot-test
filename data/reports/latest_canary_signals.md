# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-14T04:52:24.565267+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0267` n `12`; crypto_alt avg `-0.0681` n `230`; crypto_major avg `-0.0942` n `8`; equity avg `0.1725` n `92`; fx avg `0.0081` n `6`; index avg `0.0408` n `25`; metal avg `-0.0062` n `20`; unknown avg `-0.0906` n `766`
- 1h: commodity avg `0.056` n `12`; crypto_alt avg `0.2086` n `230`; crypto_major avg `0.1824` n `8`; equity avg `0.5022` n `92`; fx avg `0.0124` n `6`; index avg `0.129` n `25`; metal avg `0.0728` n `20`; unknown avg `-0.1724` n `766`
- 4h: commodity avg `-0.0612` n `12`; crypto_alt avg `0.0376` n `230`; crypto_major avg `0.1116` n `8`; equity avg `-0.1851` n `92`; fx avg `-0.0769` n `6`; index avg `0.0158` n `25`; metal avg `0.1953` n `20`; unknown avg `-0.5553` n `766`
- 24h: commodity avg `1.025` n `12`; crypto_alt avg `-0.4152` n `230`; crypto_major avg `-0.5962` n `8`; equity avg `-0.8825` n `92`; fx avg `-0.2248` n `6`; index avg `-0.1136` n `25`; metal avg `0.0869` n `20`; unknown avg `-0.301` n `750`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1933`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1832`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1183`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.118`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1179`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1111`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1063`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1047`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0861`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0739`, n `668`, weak_sample_signal
