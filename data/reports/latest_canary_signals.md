# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-17T22:22:19.271505+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0085` n `12`; crypto_alt avg `-0.4037` n `228`; crypto_major avg `-0.3417` n `8`; equity avg `-0.095` n `65`; fx avg `-0.0003` n `5`; index avg `-0.0336` n `23`; metal avg `-0.1723` n `18`; unknown avg `-0.0179` n `384`
- 1h: commodity avg `0.0229` n `12`; crypto_alt avg `-0.5613` n `228`; crypto_major avg `-0.4107` n `8`; equity avg `0.01` n `65`; fx avg `0.0089` n `5`; index avg `0.022` n `23`; metal avg `0.364` n `18`; unknown avg `0.0944` n `384`
- 4h: commodity avg `-0.1147` n `12`; crypto_alt avg `0.4159` n `228`; crypto_major avg `0.9343` n `8`; equity avg `0.418` n `65`; fx avg `-0.0182` n `5`; index avg `0.1293` n `23`; metal avg `0.2953` n `18`; unknown avg `0.2396` n `384`
- 24h: commodity avg `1.7156` n `12`; crypto_alt avg `-9.4603` n `228`; crypto_major avg `-1.5821` n `8`; equity avg `-2.207` n `65`; fx avg `-0.1733` n `5`; index avg `-1.4567` n `23`; metal avg `-5.6202` n `18`; unknown avg `550.5578` n `367`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1396`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1139`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0825`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.076`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0717`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0712`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0676`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.067`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.056`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0518`, n `668`, weak_sample_signal
