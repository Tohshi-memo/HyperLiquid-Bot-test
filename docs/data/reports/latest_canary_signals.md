# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-15T17:22:40.442244+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.21` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0185` n `12`; crypto_alt avg `0.0413` n `228`; crypto_major avg `-0.0624` n `8`; equity avg `0.0685` n `77`; fx avg `-0.0031` n `6`; index avg `0.052` n `23`; metal avg `-0.0347` n `18`; unknown avg `0.463` n `687`
- 1h: commodity avg `0.2485` n `12`; crypto_alt avg `-0.7541` n `228`; crypto_major avg `-0.1581` n `8`; equity avg `-0.0441` n `77`; fx avg `0.0009` n `6`; index avg `-0.0731` n `23`; metal avg `-0.4352` n `18`; unknown avg `0.7669` n `687`
- 4h: commodity avg `0.3621` n `12`; crypto_alt avg `-0.6262` n `228`; crypto_major avg `0.2333` n `8`; equity avg `1.2318` n `76`; fx avg `-0.0029` n `6`; index avg `0.3527` n `23`; metal avg `-0.8312` n `18`; unknown avg `1.7991` n `687`
- 24h: commodity avg `-0.688` n `12`; crypto_alt avg `5.687` n `228`; crypto_major avg `7.1136` n `8`; equity avg `3.067` n `76`; fx avg `0.0487` n `6`; index avg `1.3478` n `23`; metal avg `2.1995` n `18`; unknown avg `2.9454` n `527`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1499`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1464`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1352`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1118`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0925`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0895`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.084`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.067`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0655`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0647`, n `668`, weak_sample_signal
