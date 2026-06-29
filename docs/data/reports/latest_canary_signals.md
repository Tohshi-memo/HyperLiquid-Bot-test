# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-29T23:31:02.706577+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `4.29` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0023` n `12`; crypto_alt avg `-0.0575` n `228`; crypto_major avg `-0.0892` n `8`; equity avg `0.0056` n `88`; fx avg `-0.0062` n `6`; index avg `-0.0015` n `23`; metal avg `-0.0215` n `20`; unknown avg `0.0649` n `765`
- 1h: commodity avg `-0.0084` n `12`; crypto_alt avg `-0.2009` n `228`; crypto_major avg `-0.2181` n `8`; equity avg `0.0676` n `88`; fx avg `-0.0063` n `6`; index avg `0.0127` n `23`; metal avg `0.0833` n `20`; unknown avg `0.2316` n `765`
- 4h: commodity avg `-0.043` n `12`; crypto_alt avg `-0.7766` n `228`; crypto_major avg `-0.5439` n `8`; equity avg `0.2552` n `88`; fx avg `0.0251` n `6`; index avg `0.0024` n `23`; metal avg `0.0618` n `20`; unknown avg `0.5092` n `763`
- 24h: commodity avg `-0.2024` n `12`; crypto_alt avg `1.1405` n `228`; crypto_major avg `2.3473` n `8`; equity avg `1.6012` n `88`; fx avg `0.2195` n `6`; index avg `0.1015` n `23`; metal avg `-0.2136` n `20`; unknown avg `1.723` n `730`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1551`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1263`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.109`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1071`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1069`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1067`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1059`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1053`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0998`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0989`, n `668`, weak_sample_signal
