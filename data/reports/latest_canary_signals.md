# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-19T15:37:25.959861+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0417` n `12`; crypto_alt avg `0.2472` n `228`; crypto_major avg `0.1658` n `8`; equity avg `0.2402` n `66`; fx avg `0.0213` n `6`; index avg `0.0536` n `23`; metal avg `0.0912` n `18`; unknown avg `0.0032` n `383`
- 1h: commodity avg `0.2597` n `12`; crypto_alt avg `-0.1313` n `228`; crypto_major avg `0.2465` n `8`; equity avg `0.7517` n `66`; fx avg `0.0111` n `6`; index avg `0.2892` n `23`; metal avg `0.1042` n `18`; unknown avg `0.1919` n `383`
- 4h: commodity avg `-0.1213` n `12`; crypto_alt avg `-0.4098` n `228`; crypto_major avg `-0.155` n `8`; equity avg `-0.0691` n `66`; fx avg `-0.0128` n `6`; index avg `-0.4941` n `23`; metal avg `-1.2215` n `18`; unknown avg `-0.3044` n `383`
- 24h: commodity avg `0.748` n `12`; crypto_alt avg `0.9283` n `228`; crypto_major avg `0.9666` n `8`; equity avg `-0.5587` n `66`; fx avg `0.0656` n `6`; index avg `-0.8704` n `23`; metal avg `-1.8175` n `18`; unknown avg `-0.2738` n `363`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1944`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1495`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.112`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1103`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0977`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0882`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0868`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0864`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0826`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0809`, n `668`, weak_sample_signal
