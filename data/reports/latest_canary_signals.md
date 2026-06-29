# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-29T23:52:33.359095+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0042` n `12`; crypto_alt avg `-0.0481` n `228`; crypto_major avg `0.0004` n `8`; equity avg `-0.0831` n `88`; fx avg `-0.0069` n `6`; index avg `-0.0084` n `23`; metal avg `-0.0243` n `20`; unknown avg `-0.0199` n `765`
- 1h: commodity avg `-0.0027` n `12`; crypto_alt avg `-0.1026` n `228`; crypto_major avg `-0.1558` n `8`; equity avg `0.0193` n `88`; fx avg `-0.0137` n `6`; index avg `0.0085` n `23`; metal avg `0.0818` n `20`; unknown avg `0.0172` n `765`
- 4h: commodity avg `-0.0572` n `12`; crypto_alt avg `-0.5962` n `228`; crypto_major avg `-0.7038` n `8`; equity avg `0.2172` n `88`; fx avg `0.0161` n `6`; index avg `0.005` n `23`; metal avg `0.1123` n `20`; unknown avg `1.0481` n `763`
- 24h: commodity avg `-0.1783` n `12`; crypto_alt avg `1.3245` n `228`; crypto_major avg `2.5102` n `8`; equity avg `1.6052` n `88`; fx avg `0.2004` n `6`; index avg `0.1177` n `23`; metal avg `-0.2665` n `20`; unknown avg `1.8943` n `730`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1553`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1264`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1088`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.107`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1058`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1056`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1053`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1048`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0983`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0974`, n `668`, weak_sample_signal
