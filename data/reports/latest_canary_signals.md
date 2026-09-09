# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-09T15:52:30.933848+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0479` n `12`; crypto_alt avg `0.1878` n `233`; crypto_major avg `0.0407` n `8`; equity avg `0.1595` n `134`; fx avg `-0.0037` n `6`; index avg `0.0142` n `26`; metal avg `0.0237` n `20`; unknown avg `0.7999` n `797`
- 1h: commodity avg `-0.0403` n `12`; crypto_alt avg `-0.8878` n `233`; crypto_major avg `-0.6091` n `8`; equity avg `-0.2242` n `134`; fx avg `0.0077` n `6`; index avg `-0.0744` n `26`; metal avg `-0.1468` n `20`; unknown avg `9.4744` n `795`
- 4h: commodity avg `0.1006` n `12`; crypto_alt avg `-1.2824` n `233`; crypto_major avg `-1.018` n `8`; equity avg `0.1087` n `134`; fx avg `0.0256` n `6`; index avg `-0.0293` n `26`; metal avg `0.2899` n `20`; unknown avg `8.9155` n `766`
- 24h: commodity avg `0.5313` n `12`; crypto_alt avg `-1.7857` n `232`; crypto_major avg `-0.5446` n `8`; equity avg `-0.6257` n `134`; fx avg `-0.0879` n `6`; index avg `-0.2152` n `26`; metal avg `0.3382` n `20`; unknown avg `7.3781` n `685`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `0.1134`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1104`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0922`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0869`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0861`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.086`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0788`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0786`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0784`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.077`, n `668`, weak_sample_signal
