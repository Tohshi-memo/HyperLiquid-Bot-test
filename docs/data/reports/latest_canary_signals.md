# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-16T14:37:40.742358+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.2843` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.2137` n `12`; crypto_alt avg `-0.5983` n `228`; crypto_major avg `-0.449` n `8`; equity avg `-0.0908` n `77`; fx avg `-0.0101` n `6`; index avg `-0.1324` n `23`; metal avg `-0.1531` n `18`; unknown avg `-0.1766` n `687`
- 1h: commodity avg `-0.2747` n `12`; crypto_alt avg `-1.2018` n `228`; crypto_major avg `-1.2056` n `8`; equity avg `-1.0428` n `77`; fx avg `-0.0219` n `6`; index avg `-0.5315` n `23`; metal avg `-0.4808` n `18`; unknown avg `-0.0329` n `687`
- 4h: commodity avg `-0.1099` n `12`; crypto_alt avg `-2.175` n `228`; crypto_major avg `-1.7629` n `8`; equity avg `-1.4413` n `77`; fx avg `-0.0384` n `6`; index avg `-0.4786` n `23`; metal avg `-0.3011` n `18`; unknown avg `0.3989` n `687`
- 24h: commodity avg `-0.3951` n `12`; crypto_alt avg `-2.609` n `228`; crypto_major avg `-0.4061` n `8`; equity avg `-0.0523` n `77`; fx avg `-0.0825` n `6`; index avg `-0.1478` n `23`; metal avg `-0.4764` n `18`; unknown avg `-0.0939` n `623`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.076`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0759`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0647`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0635`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0596`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0562`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0538`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.048`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0449`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0407`, n `668`, weak_sample_signal
