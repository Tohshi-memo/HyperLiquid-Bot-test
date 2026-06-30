# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-30T15:52:30.964545+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.01` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0716` n `12`; crypto_alt avg `0.1408` n `228`; crypto_major avg `0.2374` n `8`; equity avg `0.0107` n `88`; fx avg `-0.0083` n `6`; index avg `0.0123` n `23`; metal avg `0.0025` n `20`; unknown avg `0.3084` n `765`
- 1h: commodity avg `-0.1235` n `12`; crypto_alt avg `0.0466` n `228`; crypto_major avg `0.224` n `8`; equity avg `0.1415` n `88`; fx avg `0.0224` n `6`; index avg `0.0414` n `23`; metal avg `-0.1876` n `20`; unknown avg `-0.0881` n `765`
- 4h: commodity avg `-0.0866` n `12`; crypto_alt avg `-0.1238` n `228`; crypto_major avg `-0.7999` n `8`; equity avg `0.0905` n `88`; fx avg `0.0856` n `6`; index avg `0.1516` n `23`; metal avg `-0.1421` n `20`; unknown avg `-0.1941` n `765`
- 24h: commodity avg `0.147` n `12`; crypto_alt avg `-1.5241` n `228`; crypto_major avg `-0.9575` n `8`; equity avg `1.8291` n `88`; fx avg `0.1548` n `6`; index avg `0.3899` n `23`; metal avg `0.2505` n `20`; unknown avg `7.6239` n `735`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1251`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1014`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0904`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0875`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0864`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0846`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0666`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0646`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.064`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0612`, n `668`, weak_sample_signal
