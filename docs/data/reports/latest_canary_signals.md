# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-31T11:37:25.484206+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0949` n `12`; crypto_alt avg `-0.1596` n `232`; crypto_major avg `-0.1746` n `8`; equity avg `-0.0039` n `128`; fx avg `0.0045` n `6`; index avg `-0.01` n `26`; metal avg `-0.008` n `20`; unknown avg `0.5425` n `794`
- 1h: commodity avg `0.1115` n `12`; crypto_alt avg `0.0824` n `232`; crypto_major avg `0.1113` n `8`; equity avg `-0.0134` n `128`; fx avg `-0.0122` n `6`; index avg `-0.0004` n `26`; metal avg `0.101` n `20`; unknown avg `0.1935` n `792`
- 4h: commodity avg `0.5214` n `12`; crypto_alt avg `-0.0995` n `232`; crypto_major avg `0.3822` n `8`; equity avg `-0.3375` n `128`; fx avg `-0.0231` n `6`; index avg `-0.0488` n `26`; metal avg `0.0557` n `20`; unknown avg `0.2118` n `791`
- 24h: commodity avg `0.7648` n `12`; crypto_alt avg `-0.3069` n `231`; crypto_major avg `-0.8808` n `8`; equity avg `-0.4895` n `128`; fx avg `-0.1379` n `6`; index avg `-0.0973` n `26`; metal avg `-0.1292` n `20`; unknown avg `0.074` n `761`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1014`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0985`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0945`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0674`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0667`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0653`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0636`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0554`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0492`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0475`, n `668`, weak_sample_signal
