# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-23T18:52:28.042811+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0174` n `12`; crypto_alt avg `-0.0779` n `231`; crypto_major avg `-0.1461` n `8`; equity avg `0.0441` n `122`; fx avg `0.0078` n `6`; index avg `0.0076` n `25`; metal avg `0.0019` n `20`; unknown avg `0.4053` n `793`
- 1h: commodity avg `-0.0335` n `12`; crypto_alt avg `0.1914` n `231`; crypto_major avg `0.1794` n `8`; equity avg `0.1333` n `122`; fx avg `-0.0033` n `6`; index avg `0.0453` n `25`; metal avg `0.0311` n `20`; unknown avg `0.6287` n `793`
- 4h: commodity avg `-0.0636` n `12`; crypto_alt avg `1.1084` n `231`; crypto_major avg `0.2148` n `8`; equity avg `0.3163` n `122`; fx avg `0.0044` n `6`; index avg `0.0637` n `25`; metal avg `0.0621` n `20`; unknown avg `0.8634` n `793`
- 24h: commodity avg `-0.0365` n `12`; crypto_alt avg `2.6892` n `231`; crypto_major avg `0.9418` n `8`; equity avg `0.8066` n `122`; fx avg `0.0284` n `6`; index avg `0.1225` n `25`; metal avg `0.1032` n `20`; unknown avg `5.64` n `776`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1099`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1088`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1078`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.105`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1048`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0971`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0923`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0911`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0895`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0851`, n `668`, weak_sample_signal
