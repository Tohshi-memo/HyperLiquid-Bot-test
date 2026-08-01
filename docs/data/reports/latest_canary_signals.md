# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-01T21:06:52.369560+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0437` n `12`; crypto_alt avg `0.1837` n `230`; crypto_major avg `0.2266` n `8`; equity avg `0.0555` n `102`; fx avg `0.0028` n `6`; index avg `0.0034` n `25`; metal avg `0.0354` n `20`; unknown avg `0.4325` n `782`
- 1h: commodity avg `-0.1241` n `12`; crypto_alt avg `0.0277` n `230`; crypto_major avg `0.2553` n `8`; equity avg `0.0516` n `102`; fx avg `-0.0058` n `6`; index avg `-0.0041` n `25`; metal avg `0.0121` n `20`; unknown avg `0.0617` n `782`
- 4h: commodity avg `-0.0518` n `12`; crypto_alt avg `-0.8868` n `230`; crypto_major avg `-0.8348` n `8`; equity avg `-0.2259` n `102`; fx avg `-0.005` n `6`; index avg `-0.046` n `25`; metal avg `0.0197` n `20`; unknown avg `2.4783` n `782`
- 24h: commodity avg `0.0876` n `12`; crypto_alt avg `-0.6074` n `230`; crypto_major avg `-1.0196` n `8`; equity avg `-0.6057` n `102`; fx avg `-0.027` n `6`; index avg `-0.0321` n `25`; metal avg `0.0307` n `20`; unknown avg `4.333` n `765`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1102`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0998`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0841`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0821`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0774`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0727`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0718`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0687`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0669`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0664`, n `668`, weak_sample_signal
