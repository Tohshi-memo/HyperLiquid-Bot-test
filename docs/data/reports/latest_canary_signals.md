# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-09T23:28:37.366814+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0267` n `12`; crypto_alt avg `-0.1898` n `228`; crypto_major avg `-0.1273` n `8`; equity avg `0.0141` n `65`; fx avg `-0.0008` n `5`; index avg `0.0131` n `23`; metal avg `-0.023` n `18`; unknown avg `0.4626` n `376`
- 1h: commodity avg `-0.0067` n `12`; crypto_alt avg `-0.3212` n `228`; crypto_major avg `-0.2029` n `8`; equity avg `-0.0054` n `65`; fx avg `-0.0008` n `5`; index avg `0.0326` n `23`; metal avg `-0.0061` n `18`; unknown avg `0.2416` n `376`
- 4h: commodity avg `-0.0366` n `12`; crypto_alt avg `-0.2174` n `228`; crypto_major avg `-0.2212` n `8`; equity avg `0.3483` n `65`; fx avg `-0.0015` n `5`; index avg `0.1189` n `23`; metal avg `0.1467` n `18`; unknown avg `-0.2423` n `376`
- 24h: commodity avg `0.449` n `12`; crypto_alt avg `-0.1455` n `228`; crypto_major avg `0.1924` n `8`; equity avg `0.7326` n `65`; fx avg `-0.0261` n `5`; index avg `0.3824` n `23`; metal avg `0.3084` n `18`; unknown avg `0.4417` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1325`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1135`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0937`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0854`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0819`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.081`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0785`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0771`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0723`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0717`, n `668`, weak_sample_signal
