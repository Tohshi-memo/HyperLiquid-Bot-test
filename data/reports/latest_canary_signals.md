# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-07T16:07:30.919746+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0221` n `12`; crypto_alt avg `0.1008` n `230`; crypto_major avg `0.0572` n `8`; equity avg `0.182` n `112`; fx avg `-0.0031` n `6`; index avg `-0.0074` n `25`; metal avg `0.0868` n `20`; unknown avg `-0.0553` n `782`
- 1h: commodity avg `-0.04` n `12`; crypto_alt avg `0.3513` n `230`; crypto_major avg `0.1388` n `8`; equity avg `0.7533` n `112`; fx avg `-0.0179` n `6`; index avg `0.0485` n `25`; metal avg `-0.006` n `20`; unknown avg `-0.0763` n `782`
- 4h: commodity avg `0.4077` n `12`; crypto_alt avg `-0.1978` n `230`; crypto_major avg `-0.2367` n `8`; equity avg `0.6728` n `112`; fx avg `-0.053` n `6`; index avg `0.0248` n `25`; metal avg `-0.0024` n `20`; unknown avg `-0.0258` n `782`
- 24h: commodity avg `0.3713` n `12`; crypto_alt avg `-0.1614` n `230`; crypto_major avg `0.0364` n `8`; equity avg `1.1008` n `112`; fx avg `-0.1347` n `6`; index avg `0.0015` n `25`; metal avg `0.3416` n `20`; unknown avg `0.0323` n `765`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1472`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1395`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1263`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1109`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0952`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.085`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0751`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0711`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0621`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0618`, n `668`, weak_sample_signal
