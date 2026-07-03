# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-03T01:37:27.274546+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0524` n `12`; crypto_alt avg `0.2282` n `229`; crypto_major avg `0.2348` n `8`; equity avg `0.2369` n `88`; fx avg `0.0177` n `6`; index avg `0.0514` n `25`; metal avg `0.003` n `20`; unknown avg `1.0254` n `765`
- 1h: commodity avg `0.056` n `12`; crypto_alt avg `0.7871` n `229`; crypto_major avg `0.7674` n `8`; equity avg `0.7709` n `88`; fx avg `-0.0705` n `6`; index avg `0.2109` n `25`; metal avg `0.5104` n `20`; unknown avg `0.994` n `765`
- 4h: commodity avg `0.0247` n `12`; crypto_alt avg `0.744` n `229`; crypto_major avg `0.7211` n `8`; equity avg `0.85` n `88`; fx avg `0.0233` n `6`; index avg `0.2202` n `25`; metal avg `0.6751` n `20`; unknown avg `5.6415` n `765`
- 24h: commodity avg `0.2612` n `12`; crypto_alt avg `2.4237` n `228`; crypto_major avg `3.3776` n `8`; equity avg `-1.6124` n `88`; fx avg `-0.1097` n `6`; index avg `-0.3194` n `25`; metal avg `1.3959` n `20`; unknown avg `5.5682` n `739`

## Correlations

- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0919`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0873`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0869`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0757`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0696`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0672`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0586`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0564`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0546`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0513`, n `668`, weak_sample_signal
