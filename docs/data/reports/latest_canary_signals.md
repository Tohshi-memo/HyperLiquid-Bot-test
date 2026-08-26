# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-26T11:37:29.201079+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0483` n `12`; crypto_alt avg `-0.4367` n `231`; crypto_major avg `-0.4473` n `8`; equity avg `-0.1803` n `122`; fx avg `0.0053` n `6`; index avg `-0.0192` n `25`; metal avg `-0.0157` n `20`; unknown avg `0.1669` n `797`
- 1h: commodity avg `0.0971` n `12`; crypto_alt avg `-0.1984` n `231`; crypto_major avg `-0.3724` n `8`; equity avg `-0.059` n `122`; fx avg `0.0172` n `6`; index avg `0.009` n `25`; metal avg `-0.0227` n `20`; unknown avg `-0.0507` n `797`
- 4h: commodity avg `0.1298` n `12`; crypto_alt avg `-0.2611` n `231`; crypto_major avg `-0.3154` n `8`; equity avg `0.0979` n `122`; fx avg `-0.0163` n `6`; index avg `0.0193` n `25`; metal avg `-0.0949` n `20`; unknown avg `-0.0317` n `797`
- 24h: commodity avg `-0.181` n `12`; crypto_alt avg `-1.7992` n `231`; crypto_major avg `-1.5111` n `8`; equity avg `0.2318` n `122`; fx avg `-0.019` n `6`; index avg `-0.0222` n `25`; metal avg `0.09` n `20`; unknown avg `0.5707` n `779`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1848`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.141`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1303`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1192`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1025`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0937`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0932`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0868`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0765`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0733`, n `668`, weak_sample_signal
