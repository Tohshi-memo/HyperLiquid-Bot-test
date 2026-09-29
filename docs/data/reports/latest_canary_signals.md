# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-29T19:52:31.392337+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0197` n `12`; crypto_alt avg `-0.4347` n `234`; crypto_major avg `-0.2488` n `8`; equity avg `0.017` n `142`; fx avg `0.0041` n `6`; index avg `-0.0025` n `26`; metal avg `-0.0156` n `20`; unknown avg `212.8549` n `962`
- 1h: commodity avg `-0.0582` n `12`; crypto_alt avg `-0.4876` n `234`; crypto_major avg `-0.379` n `8`; equity avg `-0.1039` n `142`; fx avg `0.0025` n `6`; index avg `-0.0053` n `26`; metal avg `0.002` n `20`; unknown avg `55.0969` n `960`
- 4h: commodity avg `-0.3221` n `12`; crypto_alt avg `-0.3017` n `234`; crypto_major avg `-0.0215` n `8`; equity avg `-0.0327` n `142`; fx avg `-0.018` n `6`; index avg `0.069` n `26`; metal avg `0.1999` n `20`; unknown avg `10.2228` n `954`
- 24h: commodity avg `-0.839` n `12`; crypto_alt avg `1.0227` n `234`; crypto_major avg `-0.3128` n `8`; equity avg `0.6253` n `142`; fx avg `-0.168` n `6`; index avg `0.0645` n `26`; metal avg `0.1316` n `20`; unknown avg `-0.0122` n `826`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.192`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1908`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.188`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1548`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.136`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1353`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1342`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1325`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.127`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.123`, n `668`, weak_sample_signal
