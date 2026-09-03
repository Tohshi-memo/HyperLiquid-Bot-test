# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-03T03:37:26.070553+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.002` n `12`; crypto_alt avg `-0.1713` n `232`; crypto_major avg `-0.1874` n `8`; equity avg `0.0276` n `133`; fx avg `0.0185` n `6`; index avg `0.0076` n `26`; metal avg `0.0218` n `20`; unknown avg `0.1401` n `792`
- 1h: commodity avg `-0.0742` n `12`; crypto_alt avg `-0.0954` n `232`; crypto_major avg `-0.1612` n `8`; equity avg `0.2026` n `133`; fx avg `0.003` n `6`; index avg `0.036` n `26`; metal avg `0.0736` n `20`; unknown avg `-0.1959` n `790`
- 4h: commodity avg `0.0507` n `12`; crypto_alt avg `0.8956` n `232`; crypto_major avg `0.7769` n `8`; equity avg `0.2542` n `133`; fx avg `-0.0741` n `6`; index avg `0.0214` n `26`; metal avg `0.247` n `20`; unknown avg `0.5178` n `790`
- 24h: commodity avg `0.1899` n `12`; crypto_alt avg `0.2193` n `232`; crypto_major avg `0.2018` n `8`; equity avg `1.5868` n `133`; fx avg `-0.3808` n `6`; index avg `0.1986` n `26`; metal avg `0.9936` n `20`; unknown avg `-0.3324` n `751`

## Correlations

- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0859`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0762`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0662`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0653`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0562`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0536`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0508`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0477`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0474`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0463`, n `668`, weak_sample_signal
