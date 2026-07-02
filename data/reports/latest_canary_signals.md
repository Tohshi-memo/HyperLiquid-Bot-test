# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-02T06:09:24.394079+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0417` n `12`; crypto_alt avg `-0.2219` n `228`; crypto_major avg `-0.1736` n `8`; equity avg `-0.3873` n `88`; fx avg `-0.0353` n `6`; index avg `-0.1089` n `25`; metal avg `0.1164` n `20`; unknown avg `-0.2481` n `741`
- 1h: commodity avg `-0.0226` n `12`; crypto_alt avg `-0.5319` n `228`; crypto_major avg `-0.5266` n `8`; equity avg `-0.741` n `88`; fx avg `-0.0192` n `6`; index avg `-0.2333` n `25`; metal avg `0.0881` n `20`; unknown avg `-0.1108` n `741`
- 4h: commodity avg `-0.0483` n `12`; crypto_alt avg `0.0524` n `228`; crypto_major avg `0.2128` n `8`; equity avg `-1.1757` n `88`; fx avg `-0.0311` n `6`; index avg `-0.3373` n `25`; metal avg `0.2216` n `20`; unknown avg `-0.2418` n `739`
- 24h: commodity avg `-0.5534` n `12`; crypto_alt avg `1.4009` n `228`; crypto_major avg `0.9232` n `8`; equity avg `-2.0622` n `88`; fx avg `-0.0129` n `6`; index avg `-0.5511` n `25`; metal avg `1.2754` n `20`; unknown avg `24.96` n `739`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.131`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1145`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1065`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0989`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0879`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.086`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0788`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0754`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0719`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0701`, n `668`, weak_sample_signal
