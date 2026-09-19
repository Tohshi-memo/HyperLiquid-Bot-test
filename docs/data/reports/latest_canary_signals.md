# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-19T02:07:31.454465+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0035` n `12`; crypto_alt avg `0.1123` n `234`; crypto_major avg `0.0513` n `8`; equity avg `-0.0473` n `140`; fx avg `0.0011` n `6`; index avg `-0.0011` n `26`; metal avg `-0.0078` n `20`; unknown avg `-0.0611` n `940`
- 1h: commodity avg `0.0074` n `12`; crypto_alt avg `0.0474` n `234`; crypto_major avg `0.0323` n `8`; equity avg `-0.1371` n `140`; fx avg `0.0165` n `6`; index avg `-0.0261` n `26`; metal avg `0.0098` n `20`; unknown avg `0.0453` n `940`
- 4h: commodity avg `0.193` n `12`; crypto_alt avg `0.2629` n `234`; crypto_major avg `0.1985` n `8`; equity avg `-0.1917` n `140`; fx avg `-0.0044` n `6`; index avg `-0.0138` n `26`; metal avg `-0.0251` n `20`; unknown avg `0.1681` n `934`
- 24h: commodity avg `0.1278` n `12`; crypto_alt avg `5.5043` n `234`; crypto_major avg `6.2037` n `8`; equity avg `1.3515` n `140`; fx avg `0.1345` n `6`; index avg `0.1374` n `26`; metal avg `0.1855` n `20`; unknown avg `3.9112` n `777`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.16`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1528`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1486`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1346`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1322`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1309`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1295`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1288`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1261`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1179`, n `668`, weak_sample_signal
