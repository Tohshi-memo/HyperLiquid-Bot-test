# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-02T10:37:24.776584+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `4.72` - Polymarket crypto volume is unusually high.
- 4h_index_leads_crypto: score `1.0281` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.158` n `12`; crypto_alt avg `-0.0867` n `228`; crypto_major avg `-0.1162` n `8`; equity avg `-0.1889` n `69`; fx avg `0.004` n `6`; index avg `-0.0184` n `23`; metal avg `0.0491` n `18`; unknown avg `-0.0747` n `422`
- 1h: commodity avg `-0.0161` n `12`; crypto_alt avg `0.282` n `228`; crypto_major avg `0.0334` n `8`; equity avg `-0.1233` n `69`; fx avg `0.0052` n `6`; index avg `0.0863` n `23`; metal avg `-0.0515` n `18`; unknown avg `-0.3936` n `422`
- 4h: commodity avg `0.0474` n `12`; crypto_alt avg `-0.3831` n `228`; crypto_major avg `-0.767` n `8`; equity avg `-0.0219` n `69`; fx avg `-0.0168` n `6`; index avg `0.2611` n `23`; metal avg `-0.2662` n `18`; unknown avg `-0.468` n `422`
- 24h: commodity avg `-1.04` n `12`; crypto_alt avg `0.0348` n `228`; crypto_major avg `-1.9636` n `8`; equity avg `0.2966` n `69`; fx avg `0.1143` n `6`; index avg `0.0118` n `23`; metal avg `0.5883` n `18`; unknown avg `0.1801` n `406`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1711`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1233`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1223`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1216`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0956`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0831`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0823`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0774`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0737`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0702`, n `668`, weak_sample_signal
