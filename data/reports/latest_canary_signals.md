# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-15T19:22:34.496864+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.52` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0538` n `12`; crypto_alt avg `-0.9445` n `228`; crypto_major avg `-0.6535` n `8`; equity avg `-0.0279` n `77`; fx avg `-0.0107` n `6`; index avg `0.0303` n `23`; metal avg `0.0464` n `18`; unknown avg `0.1801` n `687`
- 1h: commodity avg `0.2131` n `12`; crypto_alt avg `-1.1112` n `228`; crypto_major avg `-0.5532` n `8`; equity avg `-0.2411` n `77`; fx avg `-0.0327` n `6`; index avg `-0.0535` n `23`; metal avg `-0.05` n `18`; unknown avg `0.0896` n `687`
- 4h: commodity avg `0.4273` n `12`; crypto_alt avg `-1.0756` n `228`; crypto_major avg `0.1563` n `8`; equity avg `0.3963` n `77`; fx avg `-0.0298` n `6`; index avg `0.0827` n `23`; metal avg `-0.6084` n `18`; unknown avg `3.4104` n `687`
- 24h: commodity avg `-0.6108` n `12`; crypto_alt avg `4.6185` n `228`; crypto_major avg `6.6816` n `8`; equity avg `2.8018` n `76`; fx avg `0.0436` n `6`; index avg `1.2539` n `23`; metal avg `2.1662` n `18`; unknown avg `5.3548` n `527`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1357`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1265`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1242`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1024`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0842`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0773`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0664`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.066`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.063`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0582`, n `668`, weak_sample_signal
