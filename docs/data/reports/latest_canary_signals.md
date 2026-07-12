# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-12T21:07:31.764140+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0298` n `12`; crypto_alt avg `0.085` n `230`; crypto_major avg `0.0123` n `8`; equity avg `-0.0186` n `92`; fx avg `-0.0284` n `6`; index avg `0.0029` n `25`; metal avg `0.0005` n `20`; unknown avg `-0.0174` n `765`
- 1h: commodity avg `0.0561` n `12`; crypto_alt avg `-0.0528` n `230`; crypto_major avg `-0.0375` n `8`; equity avg `-0.0339` n `92`; fx avg `-0.043` n `6`; index avg `-0.0121` n `25`; metal avg `0.0015` n `20`; unknown avg `-0.0214` n `765`
- 4h: commodity avg `0.1012` n `12`; crypto_alt avg `0.0041` n `230`; crypto_major avg `-0.0099` n `8`; equity avg `0.0549` n `92`; fx avg `-0.0635` n `6`; index avg `-0.0169` n `25`; metal avg `-0.0039` n `20`; unknown avg `-0.1875` n `765`
- 24h: commodity avg `0.6406` n `12`; crypto_alt avg `-1.4847` n `230`; crypto_major avg `-0.7212` n `8`; equity avg `-0.2293` n `92`; fx avg `-0.0485` n `6`; index avg `-0.0962` n `25`; metal avg `-0.1031` n `20`; unknown avg `0.1962` n `741`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1768`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1618`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1294`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1285`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1211`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1059`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1006`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0986`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0968`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0953`, n `668`, weak_sample_signal
