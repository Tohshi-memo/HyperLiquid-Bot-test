# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-10T02:52:24.678184+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.024` n `12`; crypto_alt avg `0.3046` n `233`; crypto_major avg `0.2536` n `8`; equity avg `0.1343` n `134`; fx avg `-0.0131` n `6`; index avg `0.0185` n `26`; metal avg `0.0306` n `20`; unknown avg `1.7973` n `797`
- 1h: commodity avg `-0.0479` n `12`; crypto_alt avg `0.8129` n `233`; crypto_major avg `0.7316` n `8`; equity avg `0.2192` n `134`; fx avg `-0.0363` n `6`; index avg `0.0479` n `26`; metal avg `0.0945` n `20`; unknown avg `0.9153` n `795`
- 4h: commodity avg `-0.1864` n `12`; crypto_alt avg `0.4185` n `233`; crypto_major avg `0.6383` n `8`; equity avg `-0.2027` n `134`; fx avg `-0.0087` n `6`; index avg `0.0041` n `26`; metal avg `0.0639` n `20`; unknown avg `120.3286` n `789`
- 24h: commodity avg `-0.0469` n `12`; crypto_alt avg `-3.0445` n `233`; crypto_major avg `-2.0061` n `8`; equity avg `-1.424` n `134`; fx avg `-0.0255` n `6`; index avg `-0.2379` n `26`; metal avg `0.4099` n `20`; unknown avg `0.8134` n `667`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1339`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1218`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1073`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1045`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1023`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1022`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0989`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.095`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0868`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.084`, n `668`, weak_sample_signal
