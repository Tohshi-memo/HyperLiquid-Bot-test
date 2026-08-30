# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-30T17:07:28.566332+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0181` n `12`; crypto_alt avg `0.1107` n `231`; crypto_major avg `-0.0073` n `8`; equity avg `-0.0053` n `128`; fx avg `0.0063` n `6`; index avg `-0.0005` n `26`; metal avg `-0.007` n `20`; unknown avg `-0.0685` n `793`
- 1h: commodity avg `0.0226` n `12`; crypto_alt avg `0.6765` n `231`; crypto_major avg `0.6288` n `8`; equity avg `0.1204` n `128`; fx avg `0.0095` n `6`; index avg `0.0237` n `26`; metal avg `0.0342` n `20`; unknown avg `0.2611` n `793`
- 4h: commodity avg `0.0342` n `12`; crypto_alt avg `0.4883` n `231`; crypto_major avg `0.8073` n `8`; equity avg `0.1465` n `128`; fx avg `0.0103` n `6`; index avg `0.024` n `26`; metal avg `0.1096` n `20`; unknown avg `0.1457` n `793`
- 24h: commodity avg `0.0454` n `12`; crypto_alt avg `1.7628` n `231`; crypto_major avg `1.3768` n `8`; equity avg `0.3997` n `128`; fx avg `0.0307` n `6`; index avg `0.0979` n `26`; metal avg `0.1449` n `20`; unknown avg `0.1558` n `740`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1282`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1246`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1207`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1164`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1089`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0923`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0873`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0848`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0832`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0605`, n `668`, weak_sample_signal
