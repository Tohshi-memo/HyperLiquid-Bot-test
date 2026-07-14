# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-14T22:37:24.836545+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0178` n `12`; crypto_alt avg `0.2153` n `230`; crypto_major avg `0.2272` n `8`; equity avg `0.0266` n `92`; fx avg `-0.0032` n `6`; index avg `0.0034` n `25`; metal avg `-0.0006` n `20`; unknown avg `-0.0713` n `768`
- 1h: commodity avg `0.0215` n `12`; crypto_alt avg `0.3168` n `230`; crypto_major avg `0.3718` n `8`; equity avg `-0.0363` n `92`; fx avg `0.0075` n `6`; index avg `-0.0153` n `25`; metal avg `-0.0432` n `20`; unknown avg `2.1112` n `768`
- 4h: commodity avg `0.0414` n `12`; crypto_alt avg `0.4805` n `230`; crypto_major avg `0.5111` n `8`; equity avg `0.1477` n `92`; fx avg `0.0106` n `6`; index avg `-0.018` n `25`; metal avg `0.042` n `20`; unknown avg `-0.2905` n `768`
- 24h: commodity avg `0.265` n `12`; crypto_alt avg `2.6799` n `230`; crypto_major avg `4.1128` n `8`; equity avg `1.4106` n `92`; fx avg `0.0282` n `6`; index avg `0.3859` n `25`; metal avg `0.5368` n `20`; unknown avg `0.2775` n `742`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1186`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1066`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0965`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0886`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0828`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0793`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0679`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0628`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0563`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0546`, n `668`, weak_sample_signal
