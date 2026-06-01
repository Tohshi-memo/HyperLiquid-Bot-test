# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-01T12:52:21.652230+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1574` n `12`; crypto_alt avg `-0.0445` n `228`; crypto_major avg `-0.0107` n `8`; equity avg `0.0821` n `69`; fx avg `-0.006` n `6`; index avg `0.0132` n `23`; metal avg `0.2293` n `18`; unknown avg `0.1057` n `422`
- 1h: commodity avg `-0.745` n `12`; crypto_alt avg `-0.0222` n `228`; crypto_major avg `-0.0985` n `8`; equity avg `-0.1484` n `69`; fx avg `0.0069` n `6`; index avg `-0.054` n `23`; metal avg `0.0596` n `18`; unknown avg `0.7139` n `422`
- 4h: commodity avg `-1.1576` n `12`; crypto_alt avg `0.13` n `228`; crypto_major avg `0.4588` n `8`; equity avg `-0.1649` n `69`; fx avg `0.0008` n `6`; index avg `-0.0768` n `23`; metal avg `0.3491` n `18`; unknown avg `1.9142` n `416`
- 24h: commodity avg `-0.0512` n `12`; crypto_alt avg `-0.7083` n `228`; crypto_major avg `-0.6757` n `8`; equity avg `-0.4746` n `69`; fx avg `-0.0008` n `6`; index avg `0.4884` n `23`; metal avg `0.3945` n `18`; unknown avg `3.4657` n `405`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2891`, n `668`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.2132`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.2086`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.149`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1468`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1215`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1024`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1014`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1013`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0986`, n `668`, weak_sample_signal
