# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-09T18:52:20.883411+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `5.28` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0031` n `12`; crypto_alt avg `-0.0562` n `228`; crypto_major avg `-0.0987` n `8`; equity avg `0.0241` n `65`; fx avg `0.0` n `5`; index avg `0.0394` n `23`; metal avg `0.0018` n `18`; unknown avg `-0.0708` n `376`
- 1h: commodity avg `0.0153` n `12`; crypto_alt avg `0.0553` n `228`; crypto_major avg `0.0888` n `8`; equity avg `0.033` n `65`; fx avg `-0.0051` n `5`; index avg `0.0225` n `23`; metal avg `0.0343` n `18`; unknown avg `0.0367` n `376`
- 4h: commodity avg `0.0582` n `12`; crypto_alt avg `0.7201` n `228`; crypto_major avg `0.5024` n `8`; equity avg `0.1766` n `65`; fx avg `-0.0257` n `5`; index avg `0.094` n `23`; metal avg `0.0863` n `18`; unknown avg `0.1192` n `376`
- 24h: commodity avg `0.1547` n `12`; crypto_alt avg `0.4685` n `228`; crypto_major avg `0.2777` n `8`; equity avg `1.232` n `65`; fx avg `-0.0248` n `5`; index avg `0.3936` n `23`; metal avg `-0.157` n `18`; unknown avg `0.0441` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1258`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1134`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0912`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0889`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0873`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0828`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0766`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0741`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0692`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.067`, n `668`, weak_sample_signal
