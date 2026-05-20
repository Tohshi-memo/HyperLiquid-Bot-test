# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-20T02:52:16.871161+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1236` n `12`; crypto_alt avg `-0.222` n `228`; crypto_major avg `-0.0224` n `8`; equity avg `0.0561` n `66`; fx avg `-0.0169` n `6`; index avg `0.0547` n `23`; metal avg `0.0104` n `18`; unknown avg `0.0216` n `384`
- 1h: commodity avg `0.1768` n `12`; crypto_alt avg `-0.122` n `228`; crypto_major avg `-0.0676` n `8`; equity avg `-0.1396` n `66`; fx avg `-0.0117` n `6`; index avg `-0.1562` n `23`; metal avg `-0.335` n `18`; unknown avg `-0.4875` n `384`
- 4h: commodity avg `-0.1727` n `12`; crypto_alt avg `0.1956` n `228`; crypto_major avg `-0.1949` n `8`; equity avg `-0.1997` n `66`; fx avg `-0.0461` n `6`; index avg `-0.2384` n `23`; metal avg `-0.4176` n `18`; unknown avg `-0.6126` n `383`
- 24h: commodity avg `0.6784` n `12`; crypto_alt avg `-0.8658` n `228`; crypto_major avg `-0.7153` n `8`; equity avg `0.0835` n `66`; fx avg `-0.1186` n `6`; index avg `-0.5589` n `23`; metal avg `-2.2905` n `18`; unknown avg `0.9998` n `363`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.142`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1206`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1067`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1006`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0991`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0864`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0765`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0703`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0697`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.066`, n `668`, weak_sample_signal
