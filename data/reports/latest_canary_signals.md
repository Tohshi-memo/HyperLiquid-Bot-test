# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-02T19:38:08.388884+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.012` n `12`; crypto_alt avg `-0.2916` n `232`; crypto_major avg `-0.3166` n `8`; equity avg `-0.0083` n `133`; fx avg `-0.0093` n `6`; index avg `0.0047` n `26`; metal avg `0.0105` n `20`; unknown avg `1.7299` n `792`
- 1h: commodity avg `0.1277` n `12`; crypto_alt avg `-0.3198` n `232`; crypto_major avg `-0.2215` n `8`; equity avg `0.156` n `133`; fx avg `0.0067` n `6`; index avg `0.0167` n `26`; metal avg `0.0302` n `20`; unknown avg `-0.6684` n `790`
- 4h: commodity avg `0.0715` n `12`; crypto_alt avg `-0.1473` n `232`; crypto_major avg `-0.1672` n `8`; equity avg `0.7344` n `133`; fx avg `0.0062` n `6`; index avg `0.038` n `26`; metal avg `0.0745` n `20`; unknown avg `14.7057` n `790`
- 24h: commodity avg `0.1783` n `12`; crypto_alt avg `-0.7322` n `232`; crypto_major avg `-0.7013` n `8`; equity avg `0.6984` n `133`; fx avg `-0.3502` n `6`; index avg `0.1321` n `26`; metal avg `0.4752` n `20`; unknown avg `-0.4731` n `751`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.0908`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0878`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0822`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0674`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0667`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0571`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0563`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0487`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0447`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.042`, n `668`, weak_sample_signal
