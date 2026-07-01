# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-01T20:22:31.131514+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0026` n `12`; crypto_alt avg `-0.0744` n `228`; crypto_major avg `-0.2302` n `8`; equity avg `-0.0333` n `88`; fx avg `-0.0023` n `6`; index avg `0.01` n `25`; metal avg `0.0326` n `20`; unknown avg `0.8999` n `763`
- 1h: commodity avg `-0.0701` n `12`; crypto_alt avg `-0.3686` n `228`; crypto_major avg `-0.7264` n `8`; equity avg `-0.7213` n `88`; fx avg `0.007` n `6`; index avg `-0.1156` n `25`; metal avg `-0.2257` n `20`; unknown avg `1.795` n `763`
- 4h: commodity avg `-0.0678` n `12`; crypto_alt avg `-0.9697` n `228`; crypto_major avg `-0.7116` n `8`; equity avg `-1.212` n `88`; fx avg `0.0069` n `6`; index avg `-0.2045` n `25`; metal avg `-0.4382` n `20`; unknown avg `0.2414` n `761`
- 24h: commodity avg `-0.62` n `12`; crypto_alt avg `1.2157` n `228`; crypto_major avg `1.0203` n `8`; equity avg `-1.7604` n `88`; fx avg `-0.0148` n `6`; index avg `-0.5436` n `25`; metal avg `0.0843` n `20`; unknown avg `0.2746` n `739`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1223`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1133`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0988`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0979`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0871`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0827`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0755`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0744`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0727`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0648`, n `668`, weak_sample_signal
