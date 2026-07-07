# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-07T18:24:55.660725+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0525` n `12`; crypto_alt avg `-0.0365` n `229`; crypto_major avg `0.0351` n `8`; equity avg `-0.0619` n `91`; fx avg `-0.0102` n `6`; index avg `-0.0127` n `25`; metal avg `0.0098` n `20`; unknown avg `0.0531` n `763`
- 1h: commodity avg `-0.1172` n `12`; crypto_alt avg `-0.2926` n `229`; crypto_major avg `-0.0349` n `8`; equity avg `0.003` n `91`; fx avg `-0.0137` n `6`; index avg `0.0099` n `25`; metal avg `0.0365` n `20`; unknown avg `-0.0293` n `763`
- 4h: commodity avg `0.048` n `12`; crypto_alt avg `0.5602` n `229`; crypto_major avg `1.1879` n `8`; equity avg `0.9467` n `91`; fx avg `-0.0492` n `6`; index avg `0.1732` n `25`; metal avg `-0.0154` n `20`; unknown avg `0.0865` n `755`
- 24h: commodity avg `0.5298` n `12`; crypto_alt avg `-1.0846` n `229`; crypto_major avg `-0.1767` n `8`; equity avg `-2.6843` n `91`; fx avg `-0.2487` n `6`; index avg `-0.4886` n `25`; metal avg `-0.2006` n `20`; unknown avg `-0.3532` n `731`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1213`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1046`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0911`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0862`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0828`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0718`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0654`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0595`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0563`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0538`, n `668`, weak_sample_signal
