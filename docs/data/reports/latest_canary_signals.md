# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-12T05:07:28.026467+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0137` n `12`; crypto_alt avg `0.1018` n `230`; crypto_major avg `0.067` n `8`; equity avg `-0.0381` n `92`; fx avg `0.001` n `6`; index avg `-0.0042` n `25`; metal avg `-0.0007` n `20`; unknown avg `-0.195` n `765`
- 1h: commodity avg `0.0218` n `12`; crypto_alt avg `-0.1968` n `230`; crypto_major avg `-0.2496` n `8`; equity avg `-0.0583` n `92`; fx avg `-0.001` n `6`; index avg `0.0042` n `25`; metal avg `0.0042` n `20`; unknown avg `0.7301` n `765`
- 4h: commodity avg `-0.1544` n `12`; crypto_alt avg `0.7015` n `230`; crypto_major avg `0.377` n `8`; equity avg `0.1297` n `92`; fx avg `0.0011` n `6`; index avg `0.0068` n `25`; metal avg `0.0168` n `20`; unknown avg `-0.2324` n `765`
- 24h: commodity avg `0.4644` n `12`; crypto_alt avg `-0.2462` n `230`; crypto_major avg `-0.34` n `8`; equity avg `0.0697` n `92`; fx avg `0.01` n `6`; index avg `-0.0975` n `25`; metal avg `-0.0897` n `20`; unknown avg `-0.0157` n `729`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1812`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1638`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1464`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1318`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1233`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1213`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1152`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1067`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1014`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1002`, n `668`, weak_sample_signal
