# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-05T15:52:33.873354+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0869` n `13`; crypto_alt avg `-0.1004` n `235`; crypto_major avg `-0.0388` n `8`; equity avg `0.0999` n `144`; fx avg `-0.0035` n `6`; index avg `0.018` n `26`; metal avg `-0.021` n `20`; unknown avg `2.2543` n `1079`
- 1h: commodity avg `-0.0561` n `13`; crypto_alt avg `0.0275` n `235`; crypto_major avg `-0.1843` n `8`; equity avg `0.1465` n `144`; fx avg `0.0179` n `6`; index avg `0.0248` n `26`; metal avg `-0.0128` n `20`; unknown avg `0.3951` n `1047`
- 4h: commodity avg `-0.0551` n `13`; crypto_alt avg `-1.2025` n `235`; crypto_major avg `-0.8485` n `8`; equity avg `0.2911` n `144`; fx avg `-0.0517` n `6`; index avg `0.1087` n `26`; metal avg `-0.0721` n `20`; unknown avg `0.5173` n `989`
- 24h: commodity avg `-0.1984` n `13`; crypto_alt avg `-0.0071` n `235`; crypto_major avg `0.095` n `8`; equity avg `0.3255` n `144`; fx avg `-0.0972` n `6`; index avg `0.0873` n `26`; metal avg `0.1849` n `20`; unknown avg `-0.369` n `826`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.2031`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1828`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1736`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1249`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1078`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1015`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0993`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0938`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0921`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0877`, n `668`, weak_sample_signal
