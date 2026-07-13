# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-13T20:37:27.419741+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0001` n `12`; crypto_alt avg `0.0385` n `230`; crypto_major avg `0.0712` n `8`; equity avg `0.0062` n `92`; fx avg `-0.0155` n `6`; index avg `-0.0239` n `25`; metal avg `0.0015` n `20`; unknown avg `-0.0209` n `766`
- 1h: commodity avg `0.0669` n `12`; crypto_alt avg `-0.1322` n `230`; crypto_major avg `-0.1039` n `8`; equity avg `0.1543` n `92`; fx avg `-0.0158` n `6`; index avg `-0.0098` n `25`; metal avg `0.029` n `20`; unknown avg `-0.1587` n `766`
- 4h: commodity avg `0.5958` n `12`; crypto_alt avg `-0.5117` n `230`; crypto_major avg `-0.0316` n `8`; equity avg `-0.1109` n `92`; fx avg `-0.0169` n `6`; index avg `-0.0653` n `25`; metal avg `0.0156` n `20`; unknown avg `-0.3632` n `766`
- 24h: commodity avg `0.632` n `12`; crypto_alt avg `-2.3804` n `230`; crypto_major avg `-3.0044` n `8`; equity avg `-3.3224` n `92`; fx avg `-0.0842` n `6`; index avg `-0.6889` n `25`; metal avg `-0.5532` n `20`; unknown avg `-0.3088` n `749`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1897`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1767`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1136`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1122`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1088`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1068`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1068`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0989`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0791`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0679`, n `668`, weak_sample_signal
