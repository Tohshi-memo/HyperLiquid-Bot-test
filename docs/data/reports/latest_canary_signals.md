# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-11T16:37:29.432335+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0056` n `12`; crypto_alt avg `0.1106` n `230`; crypto_major avg `-0.0282` n `8`; equity avg `0.0117` n `92`; fx avg `0.0072` n `6`; index avg `-0.0004` n `25`; metal avg `0.0055` n `20`; unknown avg `-0.004` n `765`
- 1h: commodity avg `-0.026` n `12`; crypto_alt avg `0.0593` n `230`; crypto_major avg `-0.0853` n `8`; equity avg `0.0411` n `92`; fx avg `-0.0137` n `6`; index avg `-0.0016` n `25`; metal avg `0.0084` n `20`; unknown avg `-0.0048` n `765`
- 4h: commodity avg `-0.0775` n `12`; crypto_alt avg `0.2618` n `230`; crypto_major avg `0.3166` n `8`; equity avg `-0.0687` n `92`; fx avg `-0.0255` n `6`; index avg `0.0149` n `25`; metal avg `-0.0142` n `20`; unknown avg `0.1256` n `765`
- 24h: commodity avg `0.0982` n `12`; crypto_alt avg `0.9478` n `229`; crypto_major avg `0.6481` n `8`; equity avg `0.1046` n `92`; fx avg `-0.0419` n `6`; index avg `0.0616` n `25`; metal avg `-0.0041` n `20`; unknown avg `2.2972` n `727`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1161`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1118`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1118`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1115`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1057`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1031`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1021`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1012`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0907`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0895`, n `668`, weak_sample_signal
