# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-21T13:37:28.306769+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0434` n `12`; crypto_alt avg `-0.4658` n `234`; crypto_major avg `-0.5831` n `8`; equity avg `-0.1231` n `140`; fx avg `-0.0019` n `6`; index avg `0.0111` n `26`; metal avg `-0.0922` n `20`; unknown avg `27.3008` n `944`
- 1h: commodity avg `-0.0626` n `12`; crypto_alt avg `-0.643` n `234`; crypto_major avg `-0.4691` n `8`; equity avg `-0.11` n `140`; fx avg `-0.0132` n `6`; index avg `0.0019` n `26`; metal avg `0.0062` n `20`; unknown avg `85.5931` n `942`
- 4h: commodity avg `-0.2688` n `12`; crypto_alt avg `-0.1185` n `234`; crypto_major avg `-0.3721` n `8`; equity avg `-0.0909` n `140`; fx avg `0.0108` n `6`; index avg `0.026` n `26`; metal avg `0.1851` n `20`; unknown avg `1.4262` n `910`
- 24h: commodity avg `-0.8232` n `12`; crypto_alt avg `6.9893` n `234`; crypto_major avg `5.8172` n `8`; equity avg `1.9574` n `140`; fx avg `-0.0605` n `6`; index avg `0.3694` n `26`; metal avg `0.2002` n `20`; unknown avg `2.4468` n `733`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1943`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.157`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1475`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1168`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.11`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1084`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1032`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0977`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0943`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0895`, n `668`, weak_sample_signal
