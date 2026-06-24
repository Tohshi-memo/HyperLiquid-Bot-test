# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-24T13:37:34.600194+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_index_leads_crypto: score `1.0062` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0122` n `12`; crypto_alt avg `0.2411` n `228`; crypto_major avg `0.5161` n `8`; equity avg `-0.3148` n `86`; fx avg `0.0067` n `6`; index avg `0.0336` n `23`; metal avg `0.1473` n `20`; unknown avg `0.1344` n `764`
- 1h: commodity avg `-0.2791` n `12`; crypto_alt avg `-1.3401` n `228`; crypto_major avg `-1.0291` n `8`; equity avg `-0.7208` n `86`; fx avg `-0.0018` n `6`; index avg `-0.0229` n `23`; metal avg `-0.2078` n `20`; unknown avg `0.1573` n `764`
- 4h: commodity avg `-0.4176` n `12`; crypto_alt avg `-1.2086` n `228`; crypto_major avg `-0.8107` n `8`; equity avg `-0.834` n `86`; fx avg `-0.0711` n `6`; index avg `0.0214` n `23`; metal avg `-1.1107` n `20`; unknown avg `0.2783` n `764`
- 24h: commodity avg `-0.6571` n `12`; crypto_alt avg `-1.4892` n `228`; crypto_major avg `-0.9049` n `8`; equity avg `3.8231` n `86`; fx avg `-0.0067` n `6`; index avg `0.2237` n `23`; metal avg `-1.5776` n `20`; unknown avg `-0.3084` n `716`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1191`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1059`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0973`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0804`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0799`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0764`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0698`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0692`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.068`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0677`, n `668`, weak_sample_signal
