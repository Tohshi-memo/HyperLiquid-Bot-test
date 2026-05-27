# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-27T05:22:16.447352+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0033` n `12`; crypto_alt avg `0.0047` n `228`; crypto_major avg `-0.0075` n `8`; equity avg `-0.0699` n `67`; fx avg `0.0146` n `6`; index avg `-0.0038` n `23`; metal avg `-0.0813` n `18`; unknown avg `0.7657` n `418`
- 1h: commodity avg `0.0039` n `12`; crypto_alt avg `0.4709` n `228`; crypto_major avg `0.5145` n `8`; equity avg `-0.1306` n `67`; fx avg `0.0174` n `6`; index avg `-0.071` n `23`; metal avg `0.0586` n `18`; unknown avg `0.6934` n `418`
- 4h: commodity avg `-0.4138` n `12`; crypto_alt avg `-0.7257` n `228`; crypto_major avg `-0.0085` n `8`; equity avg `-0.4029` n `67`; fx avg `-0.0399` n `6`; index avg `-0.1792` n `23`; metal avg `-0.3497` n `18`; unknown avg `0.15` n `418`
- 24h: commodity avg `-0.3857` n `12`; crypto_alt avg `-1.332` n `228`; crypto_major avg `-0.6081` n `8`; equity avg `0.4592` n `67`; fx avg `-0.056` n `6`; index avg `0.7991` n `23`; metal avg `-0.049` n `18`; unknown avg `1.3431` n `397`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1861`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1846`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1834`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1817`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1704`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1693`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1435`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.141`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1367`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1323`, n `668`, weak_sample_signal
