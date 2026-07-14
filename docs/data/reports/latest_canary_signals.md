# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-14T10:22:25.358372+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0629` n `12`; crypto_alt avg `-0.0637` n `230`; crypto_major avg `-0.0316` n `8`; equity avg `-0.0491` n `92`; fx avg `-0.0128` n `6`; index avg `0.0049` n `25`; metal avg `-0.056` n `20`; unknown avg `-0.017` n `766`
- 1h: commodity avg `0.025` n `12`; crypto_alt avg `-0.0782` n `230`; crypto_major avg `-0.0364` n `8`; equity avg `0.0346` n `92`; fx avg `-0.0155` n `6`; index avg `0.0178` n `25`; metal avg `-0.0721` n `20`; unknown avg `-0.0388` n `766`
- 4h: commodity avg `0.2128` n `12`; crypto_alt avg `-0.2403` n `230`; crypto_major avg `-0.0411` n `8`; equity avg `0.2583` n `92`; fx avg `0.0411` n `6`; index avg `0.0149` n `25`; metal avg `-0.1084` n `20`; unknown avg `-0.2017` n `766`
- 24h: commodity avg `1.4908` n `12`; crypto_alt avg `-0.9756` n `230`; crypto_major avg `-0.5563` n `8`; equity avg `-0.5094` n `92`; fx avg `-0.0051` n `6`; index avg `-0.1147` n `25`; metal avg `-0.1804` n `20`; unknown avg `-0.3188` n `750`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1784`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1621`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1093`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.103`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1014`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0883`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0878`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0845`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.084`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0775`, n `668`, weak_sample_signal
