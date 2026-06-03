# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-03T14:37:30.766180+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.04` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.1449` n `12`; crypto_alt avg `0.3056` n `228`; crypto_major avg `0.2904` n `8`; equity avg `-0.0186` n `73`; fx avg `-0.0229` n `6`; index avg `0.133` n `23`; metal avg `0.0353` n `18`; unknown avg `0.0583` n `419`
- 1h: commodity avg `0.0723` n `12`; crypto_alt avg `0.0249` n `228`; crypto_major avg `-0.2758` n `8`; equity avg `-0.309` n `73`; fx avg `-0.0382` n `6`; index avg `-0.0392` n `23`; metal avg `-0.2512` n `18`; unknown avg `0.9261` n `419`
- 4h: commodity avg `-0.7288` n `12`; crypto_alt avg `0.2033` n `228`; crypto_major avg `-0.7866` n `8`; equity avg `-1.2632` n `73`; fx avg `-0.0617` n `6`; index avg `-0.3831` n `23`; metal avg `-0.7455` n `18`; unknown avg `0.8891` n `419`
- 24h: commodity avg `1.0364` n `12`; crypto_alt avg `0.8988` n `228`; crypto_major avg `-2.697` n `8`; equity avg `-0.777` n `72`; fx avg `-0.0245` n `6`; index avg `0.3076` n `23`; metal avg `-1.6574` n `18`; unknown avg `1.2052` n `409`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1215`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0867`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0819`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0735`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.065`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0647`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0629`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0579`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0551`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0551`, n `668`, weak_sample_signal
