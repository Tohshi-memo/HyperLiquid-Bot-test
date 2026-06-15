# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-15T19:52:47.573744+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-3.9052` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- polymarket_volume_spike: score `3.48` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0051` n `12`; crypto_alt avg `-0.0724` n `228`; crypto_major avg `-0.0231` n `8`; equity avg `0.0335` n `77`; fx avg `0.0014` n `6`; index avg `-0.003` n `23`; metal avg `0.0098` n `18`; unknown avg `0.2599` n `687`
- 1h: commodity avg `0.2155` n `12`; crypto_alt avg `-0.9649` n `228`; crypto_major avg `-0.5458` n `8`; equity avg `-0.1342` n `77`; fx avg `-0.0282` n `6`; index avg `-0.0358` n `23`; metal avg `-0.1286` n `18`; unknown avg `0.4243` n `687`
- 4h: commodity avg `0.7794` n `12`; crypto_alt avg `-1.8435` n `228`; crypto_major avg `-0.8361` n `8`; equity avg `3.0691` n `77`; fx avg `-0.022` n `6`; index avg `-0.1015` n `23`; metal avg `-0.6628` n `18`; unknown avg `2.5886` n `687`
- 24h: commodity avg `-0.4356` n `12`; crypto_alt avg `4.7064` n `228`; crypto_major avg `6.7853` n `8`; equity avg `2.9575` n `76`; fx avg `0.0251` n `6`; index avg `1.2452` n `23`; metal avg `2.1294` n `18`; unknown avg `5.0506` n `527`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1251`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1211`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1121`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0992`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0811`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0751`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0647`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0618`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0578`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0542`, n `668`, weak_sample_signal
