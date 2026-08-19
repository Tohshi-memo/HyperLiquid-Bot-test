# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-19T08:37:32.032013+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.02` n `12`; crypto_alt avg `0.1292` n `230`; crypto_major avg `0.1825` n `8`; equity avg `-0.0353` n `120`; fx avg `-0.0128` n `6`; index avg `0.0187` n `25`; metal avg `0.0154` n `20`; unknown avg `-0.0103` n `789`
- 1h: commodity avg `-0.0008` n `12`; crypto_alt avg `0.2092` n `230`; crypto_major avg `0.1277` n `8`; equity avg `0.2916` n `120`; fx avg `-0.0511` n `6`; index avg `0.0867` n `25`; metal avg `0.0112` n `20`; unknown avg `0.0238` n `789`
- 4h: commodity avg `-0.0635` n `12`; crypto_alt avg `0.4043` n `230`; crypto_major avg `0.2202` n `8`; equity avg `1.0839` n `120`; fx avg `-0.0503` n `6`; index avg `0.2319` n `25`; metal avg `0.076` n `20`; unknown avg `0.0104` n `757`
- 24h: commodity avg `0.3107` n `12`; crypto_alt avg `0.398` n `230`; crypto_major avg `0.2853` n `8`; equity avg `-1.5884` n `120`; fx avg `-0.2003` n `6`; index avg `-0.1772` n `25`; metal avg `-0.461` n `20`; unknown avg `-0.2338` n `757`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1468`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1199`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1092`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1046`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0901`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0889`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0883`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0882`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0873`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0848`, n `668`, weak_sample_signal
