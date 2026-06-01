# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-01T11:07:21.785936+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0675` n `12`; crypto_alt avg `-0.0659` n `228`; crypto_major avg `-0.0853` n `8`; equity avg `-0.0757` n `69`; fx avg `-0.0093` n `6`; index avg `-0.0581` n `23`; metal avg `-0.1239` n `18`; unknown avg `-0.2544` n `422`
- 1h: commodity avg `-0.1828` n `12`; crypto_alt avg `0.1573` n `228`; crypto_major avg `0.083` n `8`; equity avg `0.0463` n `69`; fx avg `-0.012` n `6`; index avg `0.0359` n `23`; metal avg `-0.0086` n `18`; unknown avg `0.0133` n `422`
- 4h: commodity avg `-0.0946` n `12`; crypto_alt avg `-0.3939` n `228`; crypto_major avg `-0.2794` n `8`; equity avg `-0.2979` n `69`; fx avg `-0.0066` n `6`; index avg `-0.4475` n `23`; metal avg `0.0607` n `18`; unknown avg `0.5462` n `422`
- 24h: commodity avg `0.9539` n `12`; crypto_alt avg `-0.4808` n `228`; crypto_major avg `-0.5314` n `8`; equity avg `-0.1751` n `69`; fx avg `0.0044` n `6`; index avg `0.4647` n `23`; metal avg `0.1977` n `18`; unknown avg `2.2925` n `411`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2865`, n `668`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.2119`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.2061`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1523`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.148`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1224`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0977`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0958`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0945`, n `668`, weak_sample_signal
