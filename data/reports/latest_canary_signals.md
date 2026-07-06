# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-06T12:52:27.725483+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_index_leads_crypto: score `1.5352` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_index_leads_crypto: score `1.2576` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0423` n `12`; crypto_alt avg `-0.2642` n `229`; crypto_major avg `-0.4577` n `8`; equity avg `0.0114` n `88`; fx avg `0.0001` n `6`; index avg `0.0051` n `25`; metal avg `-0.1012` n `20`; unknown avg `-0.1235` n `765`
- 1h: commodity avg `-0.0935` n `12`; crypto_alt avg `-1.1802` n `229`; crypto_major avg `-1.5344` n `8`; equity avg `-0.1754` n `88`; fx avg `0.01` n `6`; index avg `0.0008` n `25`; metal avg `-0.3057` n `20`; unknown avg `0.0609` n `765`
- 4h: commodity avg `-0.0811` n `12`; crypto_alt avg `-0.7715` n `229`; crypto_major avg `-1.2491` n `8`; equity avg `-0.2201` n `88`; fx avg `0.0102` n `6`; index avg `0.0085` n `25`; metal avg `-0.2884` n `20`; unknown avg `-0.0817` n `765`
- 24h: commodity avg `-0.1794` n `12`; crypto_alt avg `-1.2107` n `229`; crypto_major avg `-1.0432` n `8`; equity avg `-0.8729` n `88`; fx avg `0.1276` n `6`; index avg `-0.0011` n `25`; metal avg `-0.5084` n `20`; unknown avg `0.6656` n `661`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1087`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0917`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.087`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0758`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0723`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0685`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0652`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.058`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0562`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0552`, n `668`, weak_sample_signal
