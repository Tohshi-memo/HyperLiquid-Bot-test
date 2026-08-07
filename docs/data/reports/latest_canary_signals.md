# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-07T23:37:28.959496+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0154` n `12`; crypto_alt avg `-0.0779` n `230`; crypto_major avg `-0.0225` n `8`; equity avg `0.0168` n `112`; fx avg `-0.0057` n `6`; index avg `-0.0169` n `25`; metal avg `-0.01` n `20`; unknown avg `0.0231` n `783`
- 1h: commodity avg `0.0423` n `12`; crypto_alt avg `0.0711` n `230`; crypto_major avg `0.0388` n `8`; equity avg `0.0225` n `112`; fx avg `-0.0009` n `6`; index avg `-0.0156` n `25`; metal avg `-0.007` n `20`; unknown avg `-0.1324` n `782`
- 4h: commodity avg `0.0013` n `12`; crypto_alt avg `-0.411` n `230`; crypto_major avg `-0.2368` n `8`; equity avg `0.3332` n `112`; fx avg `0.034` n `6`; index avg `0.0034` n `25`; metal avg `0.0064` n `20`; unknown avg `-0.0965` n `782`
- 24h: commodity avg `-0.165` n `12`; crypto_alt avg `-0.3207` n `230`; crypto_major avg `0.0469` n `8`; equity avg `1.66` n `112`; fx avg `-0.1135` n `6`; index avg `0.0693` n `25`; metal avg `0.4337` n `20`; unknown avg `0.123` n `766`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1568`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.093`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0889`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0758`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0714`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0702`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0635`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0586`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0568`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0564`, n `668`, weak_sample_signal
