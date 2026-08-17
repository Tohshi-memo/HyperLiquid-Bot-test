# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-17T06:22:26.161674+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0138` n `12`; crypto_alt avg `0.0415` n `230`; crypto_major avg `0.0821` n `8`; equity avg `-0.0565` n `114`; fx avg `-0.0148` n `6`; index avg `-0.0078` n `25`; metal avg `-0.0595` n `20`; unknown avg `0.6884` n `792`
- 1h: commodity avg `-0.0693` n `12`; crypto_alt avg `-0.0917` n `230`; crypto_major avg `-0.0199` n `8`; equity avg `0.2179` n `114`; fx avg `-0.0022` n `6`; index avg `0.045` n `25`; metal avg `0.0129` n `20`; unknown avg `0.0352` n `776`
- 4h: commodity avg `-0.2029` n `12`; crypto_alt avg `0.4085` n `230`; crypto_major avg `0.5169` n `8`; equity avg `0.6873` n `114`; fx avg `0.0214` n `6`; index avg `0.1021` n `25`; metal avg `0.0154` n `20`; unknown avg `0.164` n `776`
- 24h: commodity avg `-0.243` n `12`; crypto_alt avg `0.5191` n `230`; crypto_major avg `0.9538` n `8`; equity avg `1.0028` n `114`; fx avg `-0.028` n `6`; index avg `0.1356` n `25`; metal avg `0.2092` n `20`; unknown avg `0.1092` n `775`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1715`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.164`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1464`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1368`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1228`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1071`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0946`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0862`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0848`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0812`, n `668`, weak_sample_signal
