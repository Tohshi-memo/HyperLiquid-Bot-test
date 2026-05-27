# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-27T14:52:24.293960+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.2187` n `12`; crypto_alt avg `0.1995` n `228`; crypto_major avg `0.2138` n `8`; equity avg `0.1732` n `67`; fx avg `-0.0245` n `6`; index avg `0.1485` n `23`; metal avg `-0.0965` n `18`; unknown avg `-0.0864` n `418`
- 1h: commodity avg `0.4664` n `12`; crypto_alt avg `0.0455` n `228`; crypto_major avg `0.0335` n `8`; equity avg `0.1309` n `67`; fx avg `0.0022` n `6`; index avg `-0.2346` n `23`; metal avg `-0.0707` n `18`; unknown avg `-0.158` n `418`
- 4h: commodity avg `0.5178` n `12`; crypto_alt avg `-0.0708` n `228`; crypto_major avg `-0.8017` n `8`; equity avg `-0.6485` n `67`; fx avg `0.0031` n `6`; index avg `-0.8244` n `23`; metal avg `-0.007` n `18`; unknown avg `0.2648` n `418`
- 24h: commodity avg `-1.1299` n `12`; crypto_alt avg `-2.5631` n `228`; crypto_major avg `-2.1537` n `8`; equity avg `-0.3499` n `67`; fx avg `-0.0289` n `6`; index avg `-0.5637` n `23`; metal avg `-1.2937` n `18`; unknown avg `-0.0931` n `400`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1735`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1703`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1697`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1611`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1583`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1541`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1471`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1327`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1301`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.129`, n `668`, weak_sample_signal
