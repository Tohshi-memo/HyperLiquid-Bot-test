# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-12T18:37:30.741225+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0411` n `12`; crypto_alt avg `0.0818` n `230`; crypto_major avg `0.1266` n `8`; equity avg `0.0281` n `113`; fx avg `-0.0025` n `6`; index avg `0.004` n `25`; metal avg `0.0117` n `20`; unknown avg `0.0401` n `786`
- 1h: commodity avg `0.0339` n `12`; crypto_alt avg `-0.0572` n `230`; crypto_major avg `-0.0493` n `8`; equity avg `0.1401` n `113`; fx avg `-0.0036` n `6`; index avg `0.0107` n `25`; metal avg `0.0209` n `20`; unknown avg `1.391` n `786`
- 4h: commodity avg `0.0354` n `12`; crypto_alt avg `0.1092` n `230`; crypto_major avg `0.2806` n `8`; equity avg `0.7058` n `113`; fx avg `0.0009` n `6`; index avg `-0.0038` n `25`; metal avg `-0.174` n `20`; unknown avg `0.231` n `786`
- 24h: commodity avg `0.1171` n `12`; crypto_alt avg `0.0611` n `230`; crypto_major avg `1.0539` n `8`; equity avg `4.2102` n `113`; fx avg `0.0371` n `6`; index avg `0.474` n `25`; metal avg `0.2627` n `20`; unknown avg `0.2003` n `769`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2271`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1982`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1953`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1882`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1574`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1544`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1464`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1397`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1282`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1192`, n `668`, weak_sample_signal
