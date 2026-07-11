# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-11T14:52:27.838829+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0129` n `12`; crypto_alt avg `-0.0893` n `230`; crypto_major avg `-0.0492` n `8`; equity avg `-0.0176` n `92`; fx avg `-0.0005` n `6`; index avg `0.0043` n `25`; metal avg `0.0111` n `20`; unknown avg `0.0344` n `765`
- 1h: commodity avg `-0.0128` n `12`; crypto_alt avg `0.2149` n `230`; crypto_major avg `0.4132` n `8`; equity avg `-0.0009` n `92`; fx avg `-0.0051` n `6`; index avg `0.0078` n `25`; metal avg `0.0078` n `20`; unknown avg `0.1139` n `765`
- 4h: commodity avg `0.006` n `12`; crypto_alt avg `0.6502` n `230`; crypto_major avg `0.5757` n `8`; equity avg `-0.1069` n `92`; fx avg `-0.0062` n `6`; index avg `0.0031` n `25`; metal avg `-0.0034` n `20`; unknown avg `-0.0835` n `765`
- 24h: commodity avg `0.0499` n `12`; crypto_alt avg `1.3148` n `229`; crypto_major avg `0.8225` n `8`; equity avg `0.4277` n `92`; fx avg `-0.05` n `6`; index avg `0.1158` n `25`; metal avg `0.0756` n `20`; unknown avg `2.991` n `727`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1157`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1119`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.11`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1097`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1052`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.102`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1018`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1011`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0908`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0894`, n `668`, weak_sample_signal
