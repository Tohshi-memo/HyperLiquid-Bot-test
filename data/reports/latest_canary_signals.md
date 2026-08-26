# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-26T04:52:23.610042+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0413` n `12`; crypto_alt avg `-0.3423` n `231`; crypto_major avg `-0.2906` n `8`; equity avg `-0.1077` n `122`; fx avg `0.0023` n `6`; index avg `-0.0228` n `25`; metal avg `-0.0198` n `20`; unknown avg `-0.0629` n `797`
- 1h: commodity avg `0.0705` n `12`; crypto_alt avg `-0.0955` n `231`; crypto_major avg `-0.0814` n `8`; equity avg `-0.0907` n `122`; fx avg `-0.0109` n `6`; index avg `-0.0352` n `25`; metal avg `-0.0405` n `20`; unknown avg `0.2293` n `797`
- 4h: commodity avg `-0.0072` n `12`; crypto_alt avg `0.4026` n `231`; crypto_major avg `0.3037` n `8`; equity avg `0.6113` n `122`; fx avg `-0.0231` n `6`; index avg `0.161` n `25`; metal avg `0.1105` n `20`; unknown avg `0.984` n `796`
- 24h: commodity avg `-0.7444` n `12`; crypto_alt avg `-2.7614` n `231`; crypto_major avg `-2.6039` n `8`; equity avg `1.299` n `122`; fx avg `0.0311` n `6`; index avg `0.1824` n `25`; metal avg `0.3066` n `20`; unknown avg `0.3411` n `778`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1855`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1422`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1372`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1232`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1069`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0973`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0962`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0901`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0875`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0845`, n `668`, weak_sample_signal
