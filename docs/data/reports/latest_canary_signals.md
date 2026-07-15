# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-15T04:37:29.223861+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0097` n `12`; crypto_alt avg `-0.0569` n `230`; crypto_major avg `0.0379` n `8`; equity avg `-0.1091` n `93`; fx avg `0.0102` n `6`; index avg `-0.0047` n `25`; metal avg `-0.0125` n `20`; unknown avg `0.0843` n `767`
- 1h: commodity avg `-0.0689` n `12`; crypto_alt avg `-0.0327` n `230`; crypto_major avg `0.0584` n `8`; equity avg `0.0916` n `93`; fx avg `0.0169` n `6`; index avg `0.014` n `25`; metal avg `-0.0259` n `20`; unknown avg `0.2259` n `767`
- 4h: commodity avg `-0.1846` n `12`; crypto_alt avg `-0.0774` n `230`; crypto_major avg `0.2097` n `8`; equity avg `1.1132` n `93`; fx avg `0.0368` n `6`; index avg `0.1314` n `25`; metal avg `-0.0801` n `20`; unknown avg `-0.1519` n `767`
- 24h: commodity avg `0.0633` n `12`; crypto_alt avg `1.6775` n `230`; crypto_major avg `3.1413` n `8`; equity avg `2.5488` n `92`; fx avg `0.1661` n `6`; index avg `0.6794` n `25`; metal avg `0.3361` n `20`; unknown avg `0.3996` n `740`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1086`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1023`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0884`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0781`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0667`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0644`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0544`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0533`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0465`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0423`, n `668`, weak_sample_signal
