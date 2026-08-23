# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-23T14:44:33.617308+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0043` n `12`; crypto_alt avg `-1.234` n `231`; crypto_major avg `-1.1906` n `8`; equity avg `-0.1177` n `122`; fx avg `0.0021` n `6`; index avg `0.0053` n `25`; metal avg `-0.0121` n `20`; unknown avg `0.3066` n `793`
- 1h: commodity avg `-0.0068` n `12`; crypto_alt avg `-0.8514` n `231`; crypto_major avg `-0.8667` n `8`; equity avg `-0.084` n `122`; fx avg `-0.0066` n `6`; index avg `0.0106` n `25`; metal avg `-0.0277` n `20`; unknown avg `0.314` n `793`
- 4h: commodity avg `-0.0132` n `12`; crypto_alt avg `1.2656` n `231`; crypto_major avg `0.2661` n `8`; equity avg `0.1266` n `122`; fx avg `-0.0194` n `6`; index avg `0.0225` n `25`; metal avg `0.0284` n `20`; unknown avg `2.7388` n `793`
- 24h: commodity avg `0.0478` n `12`; crypto_alt avg `1.1705` n `231`; crypto_major avg `1.0949` n `8`; equity avg `0.4329` n `122`; fx avg `0.0456` n `6`; index avg `0.0641` n `25`; metal avg `0.0397` n `20`; unknown avg `8.1548` n `776`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1088`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1045`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1043`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1038`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1009`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0982`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.091`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0886`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0861`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0853`, n `668`, weak_sample_signal
