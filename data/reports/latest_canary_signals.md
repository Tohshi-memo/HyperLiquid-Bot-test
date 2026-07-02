# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-02T22:07:26.294449+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0186` n `12`; crypto_alt avg `0.0404` n `229`; crypto_major avg `-0.1219` n `8`; equity avg `0.0371` n `88`; fx avg `-0.0025` n `6`; index avg `0.0055` n `25`; metal avg `0.0074` n `20`; unknown avg `4.3095` n `765`
- 1h: commodity avg `-0.0091` n `12`; crypto_alt avg `0.012` n `229`; crypto_major avg `-0.2523` n `8`; equity avg `0.068` n `88`; fx avg `0.0403` n `6`; index avg `0.0167` n `25`; metal avg `0.0131` n `20`; unknown avg `3.9495` n `765`
- 4h: commodity avg `0.0582` n `12`; crypto_alt avg `-0.069` n `229`; crypto_major avg `-0.5032` n `8`; equity avg `0.5026` n `88`; fx avg `0.021` n `6`; index avg `0.1587` n `25`; metal avg `0.0891` n `20`; unknown avg `4.0483` n `765`
- 24h: commodity avg `0.1054` n `12`; crypto_alt avg `1.1498` n `228`; crypto_major avg `1.7171` n `8`; equity avg `-2.3716` n `88`; fx avg `-0.1392` n `6`; index avg `-0.4672` n `25`; metal avg `0.9619` n `20`; unknown avg `4.8478` n `739`

## Correlations

- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0912`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0901`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.085`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.074`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0679`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0656`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0639`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0603`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0603`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0601`, n `668`, weak_sample_signal
