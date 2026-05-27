# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-27T10:07:19.501436+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0823` n `12`; crypto_alt avg `0.0151` n `228`; crypto_major avg `-0.069` n `8`; equity avg `0.0755` n `67`; fx avg `0.0002` n `6`; index avg `0.039` n `23`; metal avg `0.0285` n `18`; unknown avg `-0.0642` n `418`
- 1h: commodity avg `0.1014` n `12`; crypto_alt avg `-0.1747` n `228`; crypto_major avg `0.0958` n `8`; equity avg `0.2874` n `67`; fx avg `-0.0092` n `6`; index avg `0.1043` n `23`; metal avg `0.1519` n `18`; unknown avg `-0.4079` n `418`
- 4h: commodity avg `-0.7139` n `12`; crypto_alt avg `-0.3326` n `228`; crypto_major avg `0.2335` n `8`; equity avg `0.8158` n `67`; fx avg `-0.0257` n `6`; index avg `0.2038` n `23`; metal avg `0.0442` n `18`; unknown avg `-0.1639` n `418`
- 24h: commodity avg `-1.5015` n `12`; crypto_alt avg `-1.1629` n `228`; crypto_major avg `0.2309` n `8`; equity avg `0.9521` n `67`; fx avg `-0.069` n `6`; index avg `0.8711` n `23`; metal avg `-0.1463` n `18`; unknown avg `0.6685` n `397`

## Correlations

- risk_on_score -> index_forward_1h_return_pct: corr `0.1901`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1866`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1742`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1686`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1646`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1464`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1361`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1325`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1294`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1281`, n `668`, weak_sample_signal
