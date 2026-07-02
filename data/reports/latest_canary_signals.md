# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-02T10:37:25.558814+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.008` n `12`; crypto_alt avg `0.1202` n `229`; crypto_major avg `0.2319` n `8`; equity avg `0.1387` n `88`; fx avg `0.0139` n `6`; index avg `0.0547` n `25`; metal avg `-0.0321` n `20`; unknown avg `-0.1071` n `763`
- 1h: commodity avg `0.0734` n `12`; crypto_alt avg `0.1974` n `229`; crypto_major avg `0.3426` n `8`; equity avg `-0.031` n `88`; fx avg `0.0038` n `6`; index avg `0.001` n `25`; metal avg `-0.029` n `20`; unknown avg `-0.1787` n `763`
- 4h: commodity avg `-0.0394` n `12`; crypto_alt avg `1.1723` n `228`; crypto_major avg `1.3174` n `8`; equity avg `0.2306` n `88`; fx avg `-0.0765` n `6`; index avg `0.0083` n `25`; metal avg `-0.016` n `20`; unknown avg `0.7962` n `763`
- 24h: commodity avg `-0.3983` n `12`; crypto_alt avg `2.9635` n `228`; crypto_major avg `3.4386` n `8`; equity avg `-1.9373` n `88`; fx avg `-0.1218` n `6`; index avg `-0.5296` n `25`; metal avg `1.0493` n `20`; unknown avg `2.8408` n `739`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1247`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1214`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1054`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0981`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0931`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0926`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.089`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0888`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0804`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0793`, n `668`, weak_sample_signal
