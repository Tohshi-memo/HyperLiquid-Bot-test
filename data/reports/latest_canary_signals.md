# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-01T12:37:34.874624+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1399` n `12`; crypto_alt avg `-0.0252` n `228`; crypto_major avg `-0.0692` n `8`; equity avg `-0.4844` n `88`; fx avg `-0.0033` n `6`; index avg `-0.0654` n `23`; metal avg `0.0124` n `20`; unknown avg `-0.1238` n `765`
- 1h: commodity avg `-0.1021` n `12`; crypto_alt avg `-0.248` n `228`; crypto_major avg `-0.3333` n `8`; equity avg `-0.6003` n `88`; fx avg `-0.031` n `6`; index avg `-0.0737` n `23`; metal avg `-0.0686` n `20`; unknown avg `-0.0897` n `765`
- 4h: commodity avg `-0.0845` n `12`; crypto_alt avg `0.3226` n `228`; crypto_major avg `-0.3499` n `8`; equity avg `-0.2847` n `88`; fx avg `0.0104` n `6`; index avg `-0.0143` n `23`; metal avg `0.4617` n `20`; unknown avg `0.0329` n `765`
- 24h: commodity avg `-0.8122` n `12`; crypto_alt avg `1.0569` n `228`; crypto_major avg `0.0494` n `8`; equity avg `0.4637` n `88`; fx avg `0.1309` n `6`; index avg `-0.0332` n `23`; metal avg `-0.1799` n `20`; unknown avg `0.146` n `743`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1214`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1113`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0867`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0862`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0782`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0717`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0714`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0695`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0626`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0554`, n `668`, weak_sample_signal
