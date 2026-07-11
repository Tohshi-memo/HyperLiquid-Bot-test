# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-11T10:37:26.476897+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0299` n `12`; crypto_alt avg `0.0644` n `230`; crypto_major avg `0.0527` n `8`; equity avg `0.0099` n `92`; fx avg `-0.0002` n `6`; index avg `0.0018` n `25`; metal avg `0.0014` n `20`; unknown avg `0.0069` n `765`
- 1h: commodity avg `0.0229` n `12`; crypto_alt avg `-0.0758` n `230`; crypto_major avg `-0.0544` n `8`; equity avg `-0.0377` n `92`; fx avg `-0.0045` n `6`; index avg `-0.0033` n `25`; metal avg `0.0078` n `20`; unknown avg `-0.0953` n `765`
- 4h: commodity avg `0.0661` n `12`; crypto_alt avg `0.0187` n `230`; crypto_major avg `-0.0435` n `8`; equity avg `0.1092` n `92`; fx avg `-0.0136` n `6`; index avg `0.027` n `25`; metal avg `0.0015` n `20`; unknown avg `-0.082` n `759`
- 24h: commodity avg `-0.1386` n `12`; crypto_alt avg `-0.1416` n `229`; crypto_major avg `-0.7726` n `8`; equity avg `-0.2263` n `92`; fx avg `-0.0845` n `6`; index avg `0.1104` n `25`; metal avg `0.1175` n `20`; unknown avg `2.9272` n `727`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1146`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1118`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1059`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1048`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1042`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1028`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1017`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0991`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0897`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0893`, n `668`, weak_sample_signal
