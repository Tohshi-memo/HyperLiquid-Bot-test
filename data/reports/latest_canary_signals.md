# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-25T01:07:24.837959+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `1.7259` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_metal_divergence: score `1.5161` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.033` n `12`; crypto_alt avg `0.0555` n `231`; crypto_major avg `0.1066` n `8`; equity avg `-0.0263` n `122`; fx avg `-0.0186` n `6`; index avg `-0.0089` n `25`; metal avg `-0.0172` n `20`; unknown avg `0.6391` n `794`
- 1h: commodity avg `-0.0286` n `12`; crypto_alt avg `0.803` n `231`; crypto_major avg `1.0974` n `8`; equity avg `0.2621` n `122`; fx avg `0.0172` n `6`; index avg `0.0401` n `25`; metal avg `-0.0266` n `20`; unknown avg `2.1804` n `794`
- 4h: commodity avg `-0.0006` n `12`; crypto_alt avg `0.8127` n `231`; crypto_major avg `1.6911` n `8`; equity avg `-0.0348` n `122`; fx avg `0.0091` n `6`; index avg `-0.0433` n `25`; metal avg `0.175` n `20`; unknown avg `0.3029` n `794`
- 24h: commodity avg `0.0348` n `12`; crypto_alt avg `0.4221` n `231`; crypto_major avg `1.3187` n `8`; equity avg `-2.5785` n `122`; fx avg `-0.0181` n `6`; index avg `-0.3644` n `25`; metal avg `0.2595` n `20`; unknown avg `0.8794` n `777`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1139`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.108`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0991`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0976`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0938`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0878`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.071`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0676`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0594`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0451`, n `668`, weak_sample_signal
