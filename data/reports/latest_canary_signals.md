# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-16T02:22:37.696852+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1161` n `13`; crypto_alt avg `0.2741` n `236`; crypto_major avg `0.2339` n `8`; equity avg `0.2277` n `151`; fx avg `0.0048` n `6`; index avg `0.0513` n `26`; metal avg `0.0429` n `20`; unknown avg `-0.0382` n `1136`
- 1h: commodity avg `-0.1327` n `13`; crypto_alt avg `-0.2101` n `236`; crypto_major avg `0.0496` n `8`; equity avg `0.0748` n `151`; fx avg `-0.0147` n `6`; index avg `0.0086` n `26`; metal avg `0.0556` n `20`; unknown avg `0.5848` n `1134`
- 4h: commodity avg `-0.183` n `13`; crypto_alt avg `-0.2768` n `236`; crypto_major avg `-0.4068` n `8`; equity avg `-0.1364` n `151`; fx avg `0.0571` n `6`; index avg `-0.0219` n `26`; metal avg `-0.0175` n `20`; unknown avg `0.2191` n `1128`
- 24h: commodity avg `-0.1116` n `13`; crypto_alt avg `2.9545` n `236`; crypto_major avg `1.8552` n `8`; equity avg `1.7717` n `151`; fx avg `0.0163` n `6`; index avg `0.2889` n `26`; metal avg `0.2914` n `20`; unknown avg `25.4177` n `910`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.093`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0925`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.09`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0853`, n `666`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0793`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0759`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0689`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0684`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0647`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.064`, n `666`, weak_sample_signal
