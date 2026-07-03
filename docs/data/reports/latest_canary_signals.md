# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-03T04:22:30.209555+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.01` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0058` n `12`; crypto_alt avg `-0.0556` n `229`; crypto_major avg `-0.0259` n `8`; equity avg `0.1001` n `88`; fx avg `-0.0067` n `6`; index avg `0.0265` n `25`; metal avg `0.0999` n `20`; unknown avg `-0.1217` n `765`
- 1h: commodity avg `0.0139` n `12`; crypto_alt avg `-0.2693` n `229`; crypto_major avg `-0.2116` n `8`; equity avg `0.2964` n `88`; fx avg `-0.0223` n `6`; index avg `0.0739` n `25`; metal avg `0.0577` n `20`; unknown avg `-0.2903` n `765`
- 4h: commodity avg `0.1814` n `12`; crypto_alt avg `0.3727` n `229`; crypto_major avg `0.1803` n `8`; equity avg `1.2848` n `88`; fx avg `-0.0157` n `6`; index avg `0.313` n `25`; metal avg `0.5686` n `20`; unknown avg `0.2014` n `761`
- 24h: commodity avg `0.3765` n `12`; crypto_alt avg `1.5738` n `228`; crypto_major avg `2.3379` n `8`; equity avg `-0.5945` n `88`; fx avg `-0.0418` n `6`; index avg `-0.0432` n `25`; metal avg `1.2443` n `20`; unknown avg `6.1614` n `737`

## Correlations

- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1159`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1077`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0885`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0769`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0714`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0661`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0626`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0604`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0596`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0562`, n `668`, weak_sample_signal
