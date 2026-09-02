# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-02T17:07:28.342135+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0217` n `12`; crypto_alt avg `-0.3012` n `232`; crypto_major avg `-0.3241` n `8`; equity avg `0.0698` n `133`; fx avg `-0.0031` n `6`; index avg `0.013` n `26`; metal avg `0.0306` n `20`; unknown avg `-0.2026` n `790`
- 1h: commodity avg `0.0029` n `12`; crypto_alt avg `-0.3797` n `232`; crypto_major avg `-0.57` n `8`; equity avg `-0.0353` n `133`; fx avg `-0.0159` n `6`; index avg `-0.0153` n `26`; metal avg `-0.0246` n `20`; unknown avg `0.2337` n `790`
- 4h: commodity avg `0.3448` n `12`; crypto_alt avg `0.0052` n `232`; crypto_major avg `0.1363` n `8`; equity avg `0.4511` n `133`; fx avg `-0.0955` n `6`; index avg `0.1488` n `26`; metal avg `0.186` n `20`; unknown avg `-0.043` n `789`
- 24h: commodity avg `0.3974` n `12`; crypto_alt avg `-0.6458` n `232`; crypto_major avg `-1.2395` n `8`; equity avg `-0.0897` n `133`; fx avg `-0.34` n `6`; index avg `0.0411` n `26`; metal avg `0.1785` n `20`; unknown avg `0.0793` n `751`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.0905`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0882`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0749`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0704`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0688`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0505`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.048`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0451`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0443`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0416`, n `668`, weak_sample_signal
