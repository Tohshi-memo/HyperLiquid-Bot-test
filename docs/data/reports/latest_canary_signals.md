# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-05T03:37:27.957959+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.2275` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.007` n `12`; crypto_alt avg `-0.0175` n `229`; crypto_major avg `0.021` n `8`; equity avg `0.0187` n `88`; fx avg `-0.0041` n `6`; index avg `-0.0162` n `25`; metal avg `-0.0015` n `20`; unknown avg `-0.0548` n `765`
- 1h: commodity avg `0.0076` n `12`; crypto_alt avg `-0.1609` n `229`; crypto_major avg `-0.0988` n `8`; equity avg `0.0093` n `88`; fx avg `-0.0015` n `6`; index avg `-0.0049` n `25`; metal avg `-0.0114` n `20`; unknown avg `-0.1123` n `765`
- 4h: commodity avg `0.0313` n `12`; crypto_alt avg `-1.0933` n `229`; crypto_major avg `-1.2488` n `8`; equity avg `0.0732` n `88`; fx avg `0.0013` n `6`; index avg `-0.0213` n `25`; metal avg `-0.0301` n `20`; unknown avg `-0.4554` n `763`
- 24h: commodity avg `0.0547` n `12`; crypto_alt avg `-1.0991` n `229`; crypto_major avg `-1.0765` n `8`; equity avg `0.1323` n `88`; fx avg `-0.0007` n `6`; index avg `0.0176` n `25`; metal avg `0.0829` n `20`; unknown avg `-0.9987` n `741`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1117`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1032`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0977`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0926`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0898`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.089`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0888`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0736`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0675`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0662`, n `668`, weak_sample_signal
