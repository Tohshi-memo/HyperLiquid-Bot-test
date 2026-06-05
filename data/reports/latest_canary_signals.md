# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-05T10:52:22.151473+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1322` n `12`; crypto_alt avg `-0.4051` n `228`; crypto_major avg `0.0056` n `8`; equity avg `-0.0754` n `74`; fx avg `-0.006` n `6`; index avg `0.0045` n `23`; metal avg `0.1018` n `18`; unknown avg `2.0419` n `424`
- 1h: commodity avg `-0.0138` n `12`; crypto_alt avg `-0.7788` n `228`; crypto_major avg `-0.4825` n `8`; equity avg `0.0252` n `74`; fx avg `0.021` n `6`; index avg `0.0453` n `23`; metal avg `0.1489` n `18`; unknown avg `1.7393` n `424`
- 4h: commodity avg `-0.1485` n `12`; crypto_alt avg `1.1508` n `228`; crypto_major avg `1.3552` n `8`; equity avg `0.8317` n `74`; fx avg `0.0861` n `6`; index avg `0.1887` n `23`; metal avg `0.3262` n `18`; unknown avg `4.5735` n `424`
- 24h: commodity avg `-0.588` n `12`; crypto_alt avg `-3.507` n `228`; crypto_major avg `-1.7803` n `8`; equity avg `0.3599` n `73`; fx avg `0.1143` n `6`; index avg `0.1983` n `23`; metal avg `-0.1848` n `18`; unknown avg `3.6363` n `402`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.106`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1035`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.102`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0992`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0932`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0909`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0899`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0878`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0848`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0828`, n `668`, weak_sample_signal
