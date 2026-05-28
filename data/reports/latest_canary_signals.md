# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-28T12:52:24.969306+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0898` n `12`; crypto_alt avg `0.3207` n `228`; crypto_major avg `0.3221` n `8`; equity avg `0.2042` n `67`; fx avg `0.0216` n `6`; index avg `0.0806` n `23`; metal avg `0.2701` n `18`; unknown avg `0.1231` n `419`
- 1h: commodity avg `-0.5425` n `12`; crypto_alt avg `0.2525` n `228`; crypto_major avg `0.1833` n `8`; equity avg `0.5488` n `67`; fx avg `0.0634` n `6`; index avg `0.3008` n `23`; metal avg `0.7515` n `18`; unknown avg `0.0031` n `419`
- 4h: commodity avg `-0.0123` n `12`; crypto_alt avg `-0.151` n `228`; crypto_major avg `0.1835` n `8`; equity avg `0.3887` n `67`; fx avg `0.0532` n `6`; index avg `0.1407` n `23`; metal avg `0.2238` n `18`; unknown avg `-0.1329` n `419`
- 24h: commodity avg `0.8201` n `12`; crypto_alt avg `-5.3785` n `228`; crypto_major avg `-3.599` n `8`; equity avg `-1.0665` n `67`; fx avg `-0.0343` n `6`; index avg `-0.8763` n `23`; metal avg `-0.9302` n `18`; unknown avg `-1.8527` n `408`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.188`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1799`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1751`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1669`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1553`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1548`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1503`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1397`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1347`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1315`, n `668`, weak_sample_signal
