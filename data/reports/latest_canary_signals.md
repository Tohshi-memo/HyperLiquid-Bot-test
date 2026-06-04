# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-04T13:52:25.966636+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0633` n `12`; crypto_alt avg `-0.0797` n `228`; crypto_major avg `-0.1617` n `8`; equity avg `-0.1081` n `73`; fx avg `0.0012` n `6`; index avg `-0.0677` n `23`; metal avg `-0.0951` n `18`; unknown avg `0.0237` n `425`
- 1h: commodity avg `0.0653` n `12`; crypto_alt avg `-0.1654` n `228`; crypto_major avg `-0.3952` n `8`; equity avg `0.3` n `73`; fx avg `-0.0143` n `6`; index avg `0.1225` n `23`; metal avg `0.0424` n `18`; unknown avg `-0.2664` n `425`
- 4h: commodity avg `0.0934` n `12`; crypto_alt avg `1.9196` n `228`; crypto_major avg `1.137` n `8`; equity avg `0.7766` n `73`; fx avg `-0.0099` n `6`; index avg `0.0778` n `23`; metal avg `0.6787` n `18`; unknown avg `0.3199` n `422`
- 24h: commodity avg `-0.2444` n `12`; crypto_alt avg `-6.5097` n `228`; crypto_major avg `-4.8619` n `8`; equity avg `-2.137` n `73`; fx avg `0.1127` n `6`; index avg `-0.5811` n `23`; metal avg `0.5926` n `18`; unknown avg `-1.4285` n `401`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1501`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1442`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1318`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1282`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1236`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1203`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1115`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1022`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0786`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0765`, n `668`, weak_sample_signal
