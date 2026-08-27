# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-27T16:07:49.509720+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `1.6054` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0089` n `12`; crypto_alt avg `-0.155` n `231`; crypto_major avg `-0.2561` n `8`; equity avg `0.0727` n `127`; fx avg `0.0067` n `6`; index avg `0.0007` n `26`; metal avg `0.0303` n `20`; unknown avg `0.0573` n `792`
- 1h: commodity avg `0.0253` n `12`; crypto_alt avg `0.0717` n `231`; crypto_major avg `-0.0674` n `8`; equity avg `0.0076` n `127`; fx avg `0.0079` n `6`; index avg `0.0161` n `26`; metal avg `0.1704` n `20`; unknown avg `0.0485` n `792`
- 4h: commodity avg `0.0114` n `12`; crypto_alt avg `0.9807` n `231`; crypto_major avg `1.2581` n `8`; equity avg `-0.3473` n `127`; fx avg `0.0247` n `6`; index avg `-0.026` n `26`; metal avg `0.1999` n `20`; unknown avg `-0.0073` n `792`
- 24h: commodity avg `-0.0311` n `12`; crypto_alt avg `3.4549` n `231`; crypto_major avg `4.1321` n `8`; equity avg `1.8172` n `127`; fx avg `-0.0638` n `6`; index avg `0.2219` n `26`; metal avg `0.1154` n `20`; unknown avg `0.7514` n `775`

## Correlations

- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1285`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.124`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0917`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0819`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0805`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0767`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0701`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0646`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0586`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0552`, n `668`, weak_sample_signal
