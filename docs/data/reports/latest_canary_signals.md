# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-28T14:07:25.620824+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.2154` n `12`; crypto_alt avg `-0.8662` n `228`; crypto_major avg `-0.5402` n `8`; equity avg `0.2845` n `67`; fx avg `-0.0126` n `6`; index avg `0.0682` n `23`; metal avg `-0.0634` n `18`; unknown avg `-0.1451` n `419`
- 1h: commodity avg `0.5048` n `12`; crypto_alt avg `-0.8821` n `228`; crypto_major avg `-0.5726` n `8`; equity avg `0.1439` n `67`; fx avg `-0.0284` n `6`; index avg `-0.0966` n `23`; metal avg `-0.4103` n `18`; unknown avg `-0.075` n `419`
- 4h: commodity avg `0.7895` n `12`; crypto_alt avg `-1.4871` n `228`; crypto_major avg `-0.841` n `8`; equity avg `0.4546` n `67`; fx avg `0.0652` n `6`; index avg `0.1536` n `23`; metal avg `-0.0961` n `18`; unknown avg `-0.2191` n `419`
- 24h: commodity avg `0.8849` n `12`; crypto_alt avg `-5.83` n `228`; crypto_major avg `-3.6078` n `8`; equity avg `-0.5535` n `67`; fx avg `-0.0009` n `6`; index avg `-0.3372` n `23`; metal avg `-1.1274` n `18`; unknown avg `-1.6832` n `408`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.194`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1828`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1794`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1778`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1586`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.154`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1539`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1443`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1429`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1355`, n `668`, weak_sample_signal
