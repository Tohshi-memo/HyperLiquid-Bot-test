# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-11T12:07:25.101636+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0113` n `12`; crypto_alt avg `0.0691` n `230`; crypto_major avg `0.0477` n `8`; equity avg `-0.0146` n `92`; fx avg `-0.0011` n `6`; index avg `-0.0026` n `25`; metal avg `-0.0001` n `20`; unknown avg `-0.0094` n `765`
- 1h: commodity avg `0.0584` n `12`; crypto_alt avg `0.1898` n `230`; crypto_major avg `0.037` n `8`; equity avg `-0.0222` n `92`; fx avg `-0.0001` n `6`; index avg `-0.0029` n `25`; metal avg `-0.0078` n `20`; unknown avg `-0.0578` n `765`
- 4h: commodity avg `0.0615` n `12`; crypto_alt avg `0.3358` n `230`; crypto_major avg `0.2574` n `8`; equity avg `0.0379` n `92`; fx avg `-0.0041` n `6`; index avg `0.0004` n `25`; metal avg `-0.0119` n `20`; unknown avg `-0.1993` n `761`
- 24h: commodity avg `-0.3008` n `12`; crypto_alt avg `0.3298` n `229`; crypto_major avg `-0.3228` n `8`; equity avg `-0.1634` n `92`; fx avg `-0.1023` n `6`; index avg `0.1686` n `25`; metal avg `0.1551` n `20`; unknown avg `2.7939` n `727`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1151`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1117`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1057`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1055`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1051`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1023`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1018`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0902`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0895`, n `668`, weak_sample_signal
