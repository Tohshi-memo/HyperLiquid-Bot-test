# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-02T09:07:29.693793+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0065` n `12`; crypto_alt avg `-0.1339` n `228`; crypto_major avg `-0.0686` n `8`; equity avg `-0.092` n `88`; fx avg `0.0082` n `6`; index avg `-0.0563` n `25`; metal avg `-0.0342` n `20`; unknown avg `-0.049` n `763`
- 1h: commodity avg `-0.0438` n `12`; crypto_alt avg `0.083` n `228`; crypto_major avg `0.1293` n `8`; equity avg `0.3756` n `88`; fx avg `0.0116` n `6`; index avg `0.0389` n `25`; metal avg `0.1647` n `20`; unknown avg `1.0302` n `763`
- 4h: commodity avg `-0.0604` n `12`; crypto_alt avg `-0.1057` n `228`; crypto_major avg `-0.2911` n `8`; equity avg `-0.7131` n `88`; fx avg `-0.0445` n `6`; index avg `-0.2342` n `25`; metal avg `0.1146` n `20`; unknown avg `2.0614` n `741`
- 24h: commodity avg `-0.3021` n `12`; crypto_alt avg `1.9314` n `228`; crypto_major avg `1.4917` n `8`; equity avg `-1.9389` n `88`; fx avg `-0.0506` n `6`; index avg `-0.5381` n `25`; metal avg `1.2536` n `20`; unknown avg `16.6667` n `739`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1254`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1211`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1043`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0944`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0916`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0914`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0905`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0876`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0797`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0769`, n `668`, weak_sample_signal
