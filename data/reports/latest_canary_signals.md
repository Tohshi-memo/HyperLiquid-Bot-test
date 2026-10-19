# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-19T07:56:16.712687+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0067` n `13`; crypto_alt avg `-0.1855` n `237`; crypto_major avg `-0.2664` n `8`; equity avg `-0.1614` n `151`; fx avg `0.0001` n `6`; index avg `-0.0293` n `26`; metal avg `-0.0931` n `20`; unknown avg `0.6533` n `1195`
- 1h: commodity avg `-0.0335` n `13`; crypto_alt avg `0.2268` n `237`; crypto_major avg `-0.0781` n `8`; equity avg `-0.1088` n `151`; fx avg `-0.0098` n `6`; index avg `-0.0319` n `26`; metal avg `-0.0681` n `20`; unknown avg `0.0486` n `1190`
- 4h: commodity avg `-0.0415` n `13`; crypto_alt avg `0.3999` n `237`; crypto_major avg `0.2275` n `8`; equity avg `-0.018` n `151`; fx avg `-0.0585` n `6`; index avg `-0.015` n `26`; metal avg `-0.1084` n `20`; unknown avg `2.4192` n `1162`
- 24h: commodity avg `-0.5045` n `13`; crypto_alt avg `0.6928` n `237`; crypto_major avg `1.2654` n `8`; equity avg `2.6835` n `151`; fx avg `-0.0568` n `6`; index avg `0.471` n `26`; metal avg `0.2204` n `20`; unknown avg `2.3759` n `903`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1937`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1416`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1188`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1151`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1011`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0672`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0641`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0628`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0627`, n `666`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0579`, n `668`, weak_sample_signal
