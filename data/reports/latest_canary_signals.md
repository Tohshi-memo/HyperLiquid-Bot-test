# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-08T08:37:28.698688+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0054` n `12`; crypto_alt avg `0.1094` n `230`; crypto_major avg `0.0788` n `8`; equity avg `-0.0041` n `112`; fx avg `0.0113` n `6`; index avg `-0.0004` n `25`; metal avg `-0.0034` n `20`; unknown avg `0.2009` n `784`
- 1h: commodity avg `0.008` n `12`; crypto_alt avg `0.1742` n `230`; crypto_major avg `0.036` n `8`; equity avg `0.0494` n `112`; fx avg `0.0108` n `6`; index avg `0.0005` n `25`; metal avg `0.0039` n `20`; unknown avg `0.1386` n `784`
- 4h: commodity avg `0.0007` n `12`; crypto_alt avg `0.1605` n `230`; crypto_major avg `0.0413` n `8`; equity avg `-0.0174` n `112`; fx avg `0.0088` n `6`; index avg `-0.0239` n `25`; metal avg `-0.0033` n `20`; unknown avg `0.2202` n `751`
- 24h: commodity avg `-0.1637` n `12`; crypto_alt avg `0.0629` n `230`; crypto_major avg `0.514` n `8`; equity avg `0.7181` n `112`; fx avg `-0.0261` n `6`; index avg `0.0559` n `25`; metal avg `-0.1219` n `20`; unknown avg `0.2396` n `750`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1591`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1144`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0878`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0794`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0715`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0687`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.066`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0641`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0607`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0583`, n `668`, weak_sample_signal
