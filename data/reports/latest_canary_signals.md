# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-29T16:06:38.968457+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0923` n `12`; crypto_alt avg `0.2421` n `228`; crypto_major avg `0.2353` n `8`; equity avg `0.2137` n `69`; fx avg `-0.0105` n `6`; index avg `0.0432` n `23`; metal avg `-0.043` n `18`; unknown avg `0.9688` n `418`
- 1h: commodity avg `0.4392` n `12`; crypto_alt avg `1.3499` n `228`; crypto_major avg `0.9073` n `8`; equity avg `0.5867` n `69`; fx avg `0.0229` n `6`; index avg `0.1445` n `23`; metal avg `-0.4716` n `18`; unknown avg `1.9619` n `418`
- 4h: commodity avg `-0.0991` n `12`; crypto_alt avg `1.8341` n `228`; crypto_major avg `1.6286` n `8`; equity avg `0.7799` n `69`; fx avg `0.1285` n `6`; index avg `-0.1072` n `23`; metal avg `0.1778` n `18`; unknown avg `0.5009` n `417`
- 24h: commodity avg `-0.6494` n `12`; crypto_alt avg `3.1276` n `228`; crypto_major avg `3.1132` n `8`; equity avg `2.2505` n `69`; fx avg `0.2035` n `6`; index avg `0.1562` n `23`; metal avg `0.6841` n `18`; unknown avg `2.3654` n `407`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1788`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1604`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1577`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1366`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1311`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1306`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.129`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1221`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1201`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1188`, n `668`, weak_sample_signal
