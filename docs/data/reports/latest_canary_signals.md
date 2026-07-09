# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-09T14:07:30.786695+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0118` n `12`; crypto_alt avg `0.0408` n `229`; crypto_major avg `-0.16` n `8`; equity avg `0.0322` n `91`; fx avg `0.0099` n `6`; index avg `-0.0052` n `25`; metal avg `0.0291` n `20`; unknown avg `0.107` n `765`
- 1h: commodity avg `-0.4863` n `12`; crypto_alt avg `0.2794` n `229`; crypto_major avg `0.3513` n `8`; equity avg `0.7001` n `91`; fx avg `0.0004` n `6`; index avg `0.1343` n `25`; metal avg `0.2542` n `20`; unknown avg `0.2341` n `765`
- 4h: commodity avg `-0.3758` n `12`; crypto_alt avg `0.1257` n `229`; crypto_major avg `-0.1988` n `8`; equity avg `1.112` n `91`; fx avg `-0.0197` n `6`; index avg `0.298` n `25`; metal avg `0.3867` n `20`; unknown avg `0.2291` n `764`
- 24h: commodity avg `-0.6929` n `12`; crypto_alt avg `1.4283` n `229`; crypto_major avg `0.8292` n `8`; equity avg `2.5494` n `91`; fx avg `0.0937` n `6`; index avg `0.4748` n `25`; metal avg `0.9543` n `20`; unknown avg `0.9594` n `748`

## Correlations

- market_context_score -> fx_forward_1h_return_pct: corr `-0.0966`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0963`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0729`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0654`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0651`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0647`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0618`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0611`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0602`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0601`, n `668`, weak_sample_signal
