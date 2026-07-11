# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-11T02:52:29.218107+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0028` n `12`; crypto_alt avg `0.1156` n `229`; crypto_major avg `0.0631` n `8`; equity avg `0.0083` n `92`; fx avg `0.0019` n `6`; index avg `0.0001` n `25`; metal avg `0.0045` n `20`; unknown avg `-0.0794` n `765`
- 1h: commodity avg `-0.0114` n `12`; crypto_alt avg `0.1657` n `229`; crypto_major avg `0.1078` n `8`; equity avg `0.1135` n `92`; fx avg `-0.0008` n `6`; index avg `0.0105` n `25`; metal avg `0.0074` n `20`; unknown avg `-0.2051` n `765`
- 4h: commodity avg `-0.0603` n `12`; crypto_alt avg `0.1348` n `229`; crypto_major avg `-0.0901` n `8`; equity avg `0.095` n `92`; fx avg `0.0307` n `6`; index avg `-0.0172` n `25`; metal avg `0.0093` n `20`; unknown avg `3.5014` n `765`
- 24h: commodity avg `-0.4057` n `12`; crypto_alt avg `0.4237` n `229`; crypto_major avg `-0.2508` n `8`; equity avg `-0.7954` n `92`; fx avg `-0.1576` n `6`; index avg `0.0173` n `25`; metal avg `-0.0487` n `20`; unknown avg `4.5685` n `732`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1195`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1151`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1102`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1054`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1034`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1015`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0935`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0908`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0883`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0881`, n `668`, weak_sample_signal
