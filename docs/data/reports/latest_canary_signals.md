# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-09T04:07:28.397757+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0054` n `12`; crypto_alt avg `0.5193` n `233`; crypto_major avg `0.4463` n `8`; equity avg `0.08` n `134`; fx avg `-0.0075` n `6`; index avg `0.0075` n `26`; metal avg `-0.0325` n `20`; unknown avg `0.482` n `795`
- 1h: commodity avg `-0.0621` n `12`; crypto_alt avg `0.3944` n `233`; crypto_major avg `0.2945` n `8`; equity avg `-0.1567` n `134`; fx avg `-0.0125` n `6`; index avg `-0.0271` n `26`; metal avg `-0.0597` n `20`; unknown avg `0.6061` n `795`
- 4h: commodity avg `-0.0633` n `12`; crypto_alt avg `-0.4525` n `233`; crypto_major avg `0.0472` n `8`; equity avg `0.0924` n `134`; fx avg `0.0161` n `6`; index avg `0.0111` n `26`; metal avg `0.096` n `20`; unknown avg `-0.2111` n `785`
- 24h: commodity avg `0.0352` n `12`; crypto_alt avg `-0.3216` n `232`; crypto_major avg `0.8546` n `8`; equity avg `-0.0377` n `134`; fx avg `-0.0059` n `6`; index avg `-0.2344` n `26`; metal avg `-0.4745` n `20`; unknown avg `1.0767` n `681`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `0.1486`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1098`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1035`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1033`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1033`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0882`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0861`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.084`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0753`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0725`, n `668`, weak_sample_signal
