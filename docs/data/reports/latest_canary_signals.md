# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-28T13:07:25.860012+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1521` n `12`; crypto_alt avg `-0.1124` n `228`; crypto_major avg `-0.1486` n `8`; equity avg `-0.0705` n `67`; fx avg `0.0174` n `6`; index avg `0.0369` n `23`; metal avg `0.1754` n `18`; unknown avg `-0.0393` n `419`
- 1h: commodity avg `-0.2132` n `12`; crypto_alt avg `0.2711` n `228`; crypto_major avg `0.0909` n `8`; equity avg `0.3859` n `67`; fx avg `0.0617` n `6`; index avg `0.2678` n `23`; metal avg `0.7626` n `18`; unknown avg `0.0468` n `419`
- 4h: commodity avg `0.3669` n `12`; crypto_alt avg `-0.1705` n `228`; crypto_major avg `0.057` n `8`; equity avg `0.2264` n `67`; fx avg `0.0832` n `6`; index avg `0.192` n `23`; metal avg `0.3446` n `18`; unknown avg `-0.2316` n `419`
- 24h: commodity avg `0.8145` n `12`; crypto_alt avg `-5.1614` n `228`; crypto_major avg `-3.5122` n `8`; equity avg `-1.098` n `67`; fx avg `0.003` n `6`; index avg `-0.7733` n `23`; metal avg `-0.4554` n `18`; unknown avg `-1.6809` n `408`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1885`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1814`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1756`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1684`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1556`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1528`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.151`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1396`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1359`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1324`, n `668`, weak_sample_signal
