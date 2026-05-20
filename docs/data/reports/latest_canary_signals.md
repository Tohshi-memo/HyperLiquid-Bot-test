# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-20T04:07:14.432857+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1636` n `12`; crypto_alt avg `0.1157` n `228`; crypto_major avg `0.1101` n `8`; equity avg `0.1246` n `66`; fx avg `0.0025` n `6`; index avg `0.1183` n `23`; metal avg `0.128` n `18`; unknown avg `-0.0846` n `384`
- 1h: commodity avg `-0.26` n `12`; crypto_alt avg `0.3424` n `228`; crypto_major avg `0.2426` n `8`; equity avg `0.2037` n `66`; fx avg `0.043` n `6`; index avg `0.1303` n `23`; metal avg `0.3875` n `18`; unknown avg `17.4283` n `384`
- 4h: commodity avg `-0.2263` n `12`; crypto_alt avg `0.1443` n `228`; crypto_major avg `-0.0203` n `8`; equity avg `0.1392` n `66`; fx avg `-0.0381` n `6`; index avg `-0.1236` n `23`; metal avg `-0.2316` n `18`; unknown avg `-0.5061` n `383`
- 24h: commodity avg `0.4515` n `12`; crypto_alt avg `-1.0176` n `228`; crypto_major avg `-0.8107` n `8`; equity avg `0.2051` n `66`; fx avg `-0.1186` n `6`; index avg `-0.4402` n `23`; metal avg `-1.8562` n `18`; unknown avg `0.8607` n `363`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1406`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0898`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0752`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0682`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0657`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0654`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0608`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0595`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0555`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0543`, n `668`, weak_sample_signal
