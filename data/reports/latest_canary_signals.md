# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-23T23:32:12.512844+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0155` n `12`; crypto_alt avg `0.4012` n `231`; crypto_major avg `0.4239` n `8`; equity avg `0.034` n `122`; fx avg `-0.0053` n `6`; index avg `0.0185` n `25`; metal avg `0.0369` n `20`; unknown avg `-0.155` n `793`
- 1h: commodity avg `-0.0442` n `12`; crypto_alt avg `0.1162` n `231`; crypto_major avg `0.4076` n `8`; equity avg `0.218` n `122`; fx avg `-0.0112` n `6`; index avg `0.0626` n `25`; metal avg `0.0008` n `20`; unknown avg `-0.0294` n `793`
- 4h: commodity avg `-0.1233` n `12`; crypto_alt avg `0.3739` n `231`; crypto_major avg `1.095` n `8`; equity avg `0.13` n `122`; fx avg `-0.0764` n `6`; index avg `0.0149` n `25`; metal avg `0.0217` n `20`; unknown avg `1.7391` n `793`
- 24h: commodity avg `-0.2474` n `12`; crypto_alt avg `4.088` n `231`; crypto_major avg `2.5289` n `8`; equity avg `0.8702` n `122`; fx avg `-0.121` n `6`; index avg `0.132` n `25`; metal avg `0.1037` n `20`; unknown avg `5.9436` n `776`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1112`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1022`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1006`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0969`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0924`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0923`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0898`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0877`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0837`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0812`, n `668`, weak_sample_signal
