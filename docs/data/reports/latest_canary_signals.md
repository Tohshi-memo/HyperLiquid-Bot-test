# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-04T10:29:13.564968+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0022` n `12`; crypto_alt avg `-0.01` n `229`; crypto_major avg `-0.0522` n `8`; equity avg `0.0297` n `88`; fx avg `-0.0051` n `6`; index avg `0.0028` n `25`; metal avg `0.0042` n `20`; unknown avg `-0.0004` n `765`
- 1h: commodity avg `0.0791` n `12`; crypto_alt avg `-0.2184` n `229`; crypto_major avg `-0.204` n `8`; equity avg `0.0473` n `88`; fx avg `-0.0068` n `6`; index avg `0.011` n `25`; metal avg `-0.0011` n `20`; unknown avg `-0.081` n `765`
- 4h: commodity avg `0.075` n `12`; crypto_alt avg `-0.2066` n `229`; crypto_major avg `0.0103` n `8`; equity avg `0.0514` n `88`; fx avg `-0.0276` n `6`; index avg `0.01` n `25`; metal avg `0.0202` n `20`; unknown avg `0.2757` n `765`
- 24h: commodity avg `0.0768` n `12`; crypto_alt avg `0.942` n `229`; crypto_major avg `1.8095` n `8`; equity avg `0.2824` n `88`; fx avg `-0.0699` n `6`; index avg `-0.0157` n `25`; metal avg `-0.1421` n `20`; unknown avg `5.4473` n `743`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.0932`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0881`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0841`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0828`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0802`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0785`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0767`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0766`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0687`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0568`, n `668`, weak_sample_signal
