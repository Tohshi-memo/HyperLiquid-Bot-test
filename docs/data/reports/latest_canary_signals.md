# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-06T10:22:33.348756+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0224` n `12`; crypto_alt avg `0.0761` n `229`; crypto_major avg `0.098` n `8`; equity avg `0.0297` n `88`; fx avg `0.0026` n `6`; index avg `0.0075` n `25`; metal avg `0.074` n `20`; unknown avg `-0.0282` n `765`
- 1h: commodity avg `-0.0029` n `12`; crypto_alt avg `0.3002` n `229`; crypto_major avg `0.1841` n `8`; equity avg `0.0248` n `88`; fx avg `-0.0029` n `6`; index avg `0.001` n `25`; metal avg `-0.0306` n `20`; unknown avg `0.0693` n `765`
- 4h: commodity avg `-0.1331` n `12`; crypto_alt avg `0.1627` n `229`; crypto_major avg `-0.1009` n `8`; equity avg `0.1577` n `88`; fx avg `-0.0027` n `6`; index avg `0.0482` n `25`; metal avg `0.0743` n `20`; unknown avg `-0.0811` n `763`
- 24h: commodity avg `-0.1353` n `12`; crypto_alt avg `0.1952` n `229`; crypto_major avg `0.7667` n `8`; equity avg `-0.5579` n `88`; fx avg `0.0794` n `6`; index avg `-0.0054` n `25`; metal avg `-0.2171` n `20`; unknown avg `1.2145` n `661`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1052`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0887`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0869`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0863`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0775`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0725`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0661`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0653`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0642`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0625`, n `668`, weak_sample_signal
