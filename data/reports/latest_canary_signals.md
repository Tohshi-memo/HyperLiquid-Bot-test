# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-19T00:37:26.408591+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.007` n `13`; crypto_alt avg `0.4909` n `239`; crypto_major avg `0.5965` n `8`; equity avg `0.4069` n `164`; fx avg `-0.0025` n `6`; index avg `0.0537` n `27`; metal avg `0.0832` n `20`; unknown avg `13.5108` n `1265`
- 1h: commodity avg `-0.0214` n `13`; crypto_alt avg `0.2765` n `239`; crypto_major avg `0.1656` n `8`; equity avg `0.2391` n `164`; fx avg `-0.0548` n `6`; index avg `0.0221` n `27`; metal avg `0.0738` n `20`; unknown avg `0.1325` n `1257`
- 4h: commodity avg `-0.0808` n `13`; crypto_alt avg `0.8208` n `239`; crypto_major avg `0.7304` n `8`; equity avg `1.1522` n `164`; fx avg `-0.0553` n `6`; index avg `0.1474` n `27`; metal avg `0.2344` n `20`; unknown avg `1.2013` n `1221`
- 24h: commodity avg `-0.1937` n `13`; crypto_alt avg `-0.8119` n `239`; crypto_major avg `-2.0577` n `8`; equity avg `-1.5088` n `164`; fx avg `-0.1344` n `6`; index avg `-0.084` n `27`; metal avg `-0.7485` n `20`; unknown avg `47.0875` n `1127`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1154`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0958`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.084`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0714`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0693`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0651`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0641`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0629`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0605`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0538`, n `668`, weak_sample_signal
