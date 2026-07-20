# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-20T22:52:31.840223+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0132` n `12`; crypto_alt avg `-0.1173` n `230`; crypto_major avg `-0.0612` n `8`; equity avg `0.0362` n `98`; fx avg `0.0006` n `6`; index avg `-0.009` n `25`; metal avg `-0.0226` n `20`; unknown avg `-0.1945` n `770`
- 1h: commodity avg `0.0449` n `12`; crypto_alt avg `-0.3029` n `230`; crypto_major avg `-0.3488` n `8`; equity avg `-0.1187` n `98`; fx avg `-0.0158` n `6`; index avg `-0.0556` n `25`; metal avg `-0.0865` n `20`; unknown avg `-0.1229` n `770`
- 4h: commodity avg `-0.0979` n `12`; crypto_alt avg `-0.3272` n `230`; crypto_major avg `-0.3141` n `8`; equity avg `-0.4432` n `98`; fx avg `-0.0333` n `6`; index avg `-0.1041` n `25`; metal avg `-0.0997` n `20`; unknown avg `-0.4107` n `770`
- 24h: commodity avg `-0.3764` n `12`; crypto_alt avg `0.9823` n `230`; crypto_major avg `0.7634` n `8`; equity avg `-0.4684` n `98`; fx avg `-0.1976` n `6`; index avg `-0.0537` n `25`; metal avg `0.1357` n `20`; unknown avg `0.1407` n `745`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1559`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.128`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1271`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1085`, n `666`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1064`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1054`, n `666`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.102`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0987`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0959`, n `666`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0875`, n `666`, weak_sample_signal
