# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-10T03:07:18.859990+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0082` n `12`; crypto_alt avg `0.024` n `228`; crypto_major avg `0.0167` n `8`; equity avg `0.0711` n `65`; fx avg `0.0` n `5`; index avg `-0.0008` n `23`; metal avg `0.0132` n `18`; unknown avg `0.2208` n `376`
- 1h: commodity avg `-0.0117` n `12`; crypto_alt avg `0.37` n `228`; crypto_major avg `0.1629` n `8`; equity avg `0.1645` n `65`; fx avg `0.0` n `5`; index avg `0.0017` n `23`; metal avg `0.0222` n `18`; unknown avg `0.4844` n `376`
- 4h: commodity avg `-0.0195` n `12`; crypto_alt avg `-0.5293` n `228`; crypto_major avg `-0.2774` n `8`; equity avg `0.1865` n `65`; fx avg `0.0002` n `5`; index avg `0.0905` n `23`; metal avg `0.0512` n `18`; unknown avg `0.3363` n `376`
- 24h: commodity avg `0.3585` n `12`; crypto_alt avg `-1.6319` n `228`; crypto_major avg `-0.7561` n `8`; equity avg `0.7414` n `65`; fx avg `-0.0098` n `5`; index avg `0.3376` n `23`; metal avg `0.1012` n `18`; unknown avg `-0.4579` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1351`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1156`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0978`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0913`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0911`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0813`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0763`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0742`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0694`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0688`, n `668`, weak_sample_signal
