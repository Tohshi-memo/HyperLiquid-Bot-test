# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-01T10:07:20.382476+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.01` n `12`; crypto_alt avg `-0.0984` n `228`; crypto_major avg `-0.2574` n `8`; equity avg `0.0369` n `69`; fx avg `0.0008` n `6`; index avg `0.0193` n `23`; metal avg `0.141` n `18`; unknown avg `0.7055` n `422`
- 1h: commodity avg `-0.0153` n `12`; crypto_alt avg `-0.1391` n `228`; crypto_major avg `0.1676` n `8`; equity avg `-0.108` n `69`; fx avg `-0.0028` n `6`; index avg `-0.0777` n `23`; metal avg `0.1246` n `18`; unknown avg `0.4114` n `422`
- 4h: commodity avg `0.2843` n `12`; crypto_alt avg `-0.8849` n `228`; crypto_major avg `-0.3511` n `8`; equity avg `-0.5021` n `69`; fx avg `0.032` n `6`; index avg `-0.1216` n `23`; metal avg `-0.1535` n `18`; unknown avg `0.4561` n `422`
- 24h: commodity avg `1.2642` n `12`; crypto_alt avg `-0.3775` n `228`; crypto_major avg `-0.6452` n `8`; equity avg `-0.2473` n `69`; fx avg `-0.006` n `6`; index avg `0.468` n `23`; metal avg `0.2126` n `18`; unknown avg `1.9236` n `411`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2877`, n `668`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.2122`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.2062`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1523`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1476`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1261`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0998`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.097`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0966`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0948`, n `668`, weak_sample_signal
