# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-12T21:22:26.842262+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0021` n `12`; crypto_alt avg `-0.1512` n `233`; crypto_major avg `-0.0959` n `8`; equity avg `0.0037` n `136`; fx avg `0.0006` n `6`; index avg `-0.0002` n `26`; metal avg `0.0056` n `20`; unknown avg `14.61` n `830`
- 1h: commodity avg `-0.0186` n `12`; crypto_alt avg `-0.1366` n `233`; crypto_major avg `-0.0624` n `8`; equity avg `-0.0275` n `136`; fx avg `-0.005` n `6`; index avg `-0.0007` n `26`; metal avg `-0.013` n `20`; unknown avg `4.3281` n `822`
- 4h: commodity avg `0.0228` n `12`; crypto_alt avg `-0.428` n `233`; crypto_major avg `-0.3769` n `8`; equity avg `-0.284` n `136`; fx avg `-0.0066` n `6`; index avg `-0.0314` n `26`; metal avg `-0.0287` n `20`; unknown avg `0.3805` n `782`
- 24h: commodity avg `-0.0898` n `12`; crypto_alt avg `0.6667` n `233`; crypto_major avg `-0.4711` n `8`; equity avg `-0.2809` n `136`; fx avg `-0.0251` n `6`; index avg `0.0053` n `26`; metal avg `-0.02` n `20`; unknown avg `4.1466` n `728`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0721`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0645`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0638`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0627`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0611`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0575`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0516`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0494`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0461`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0457`, n `668`, weak_sample_signal
