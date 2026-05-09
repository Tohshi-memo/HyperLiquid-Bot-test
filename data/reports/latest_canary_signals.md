# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-09T11:37:16.891297+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0796` n `12`; crypto_alt avg `0.1159` n `228`; crypto_major avg `-0.0407` n `8`; equity avg `0.0001` n `65`; fx avg `0.0` n `5`; index avg `-0.0124` n `23`; metal avg `0.0067` n `18`; unknown avg `0.0677` n `376`
- 1h: commodity avg `-0.0768` n `12`; crypto_alt avg `0.4276` n `228`; crypto_major avg `0.1392` n `8`; equity avg `-0.0154` n `65`; fx avg `0.0055` n `5`; index avg `-0.0266` n `23`; metal avg `0.0068` n `18`; unknown avg `-0.3445` n `376`
- 4h: commodity avg `-0.1062` n `12`; crypto_alt avg `-0.1378` n `228`; crypto_major avg `-0.1618` n `8`; equity avg `0.1159` n `65`; fx avg `0.0096` n `5`; index avg `-0.039` n `23`; metal avg `-0.045` n `18`; unknown avg `-0.4917` n `376`
- 24h: commodity avg `-0.1229` n `12`; crypto_alt avg `3.268` n `228`; crypto_major avg `2.0172` n `8`; equity avg `2.7944` n `65`; fx avg `-0.0215` n `5`; index avg `1.1319` n `23`; metal avg `-0.2294` n `18`; unknown avg `0.5099` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1195`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1149`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.089`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0838`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0835`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0794`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0784`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0692`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0665`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0655`, n `668`, weak_sample_signal
