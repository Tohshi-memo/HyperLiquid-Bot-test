# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-01T01:22:22.417371+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0458` n `12`; crypto_alt avg `-0.2536` n `228`; crypto_major avg `-0.1407` n `8`; equity avg `-0.5248` n `69`; fx avg `-0.0034` n `6`; index avg `0.0366` n `23`; metal avg `0.1903` n `18`; unknown avg `-0.1375` n `421`
- 1h: commodity avg `0.1591` n `12`; crypto_alt avg `-0.166` n `228`; crypto_major avg `-0.0098` n `8`; equity avg `-0.0605` n `69`; fx avg `0.0451` n `6`; index avg `0.1883` n `23`; metal avg `-0.0478` n `18`; unknown avg `-0.3197` n `421`
- 4h: commodity avg `0.7089` n `12`; crypto_alt avg `1.0413` n `228`; crypto_major avg `0.4121` n `8`; equity avg `-0.1369` n `69`; fx avg `0.063` n `6`; index avg `0.0425` n `23`; metal avg `0.3295` n `18`; unknown avg `0.5561` n `421`
- 24h: commodity avg `0.987` n `12`; crypto_alt avg `0.744` n `228`; crypto_major avg `-0.1179` n `8`; equity avg `0.4229` n `69`; fx avg `0.0357` n `6`; index avg `0.3116` n `23`; metal avg `0.1896` n `18`; unknown avg `1.7988` n `401`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2817`, n `668`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.2553`, n `668`, moderate_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.2063`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1543`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1502`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1217`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1182`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1082`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1037`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0988`, n `668`, weak_sample_signal
