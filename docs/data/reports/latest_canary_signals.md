# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-31T03:52:30.246662+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0076` n `12`; crypto_alt avg `0.095` n `231`; crypto_major avg `0.0626` n `8`; equity avg `-0.042` n `128`; fx avg `-0.0111` n `6`; index avg `-0.0063` n `26`; metal avg `0.0239` n `20`; unknown avg `0.1153` n `793`
- 1h: commodity avg `-0.0113` n `12`; crypto_alt avg `0.8486` n `231`; crypto_major avg `0.5516` n `8`; equity avg `0.2592` n `128`; fx avg `-0.0234` n `6`; index avg `0.0577` n `26`; metal avg `0.0406` n `20`; unknown avg `0.3794` n `791`
- 4h: commodity avg `0.1616` n `12`; crypto_alt avg `1.5786` n `231`; crypto_major avg `0.3598` n `8`; equity avg `-0.1096` n `128`; fx avg `-0.0794` n `6`; index avg `0.0443` n `26`; metal avg `-0.2095` n `20`; unknown avg `-0.0681` n `779`
- 24h: commodity avg `0.4014` n `12`; crypto_alt avg `-0.0576` n `231`; crypto_major avg `-1.8383` n `8`; equity avg `-1.1753` n `128`; fx avg `-0.0605` n `6`; index avg `-0.2191` n `26`; metal avg `-0.3805` n `20`; unknown avg `-0.4159` n `757`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1272`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1193`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1178`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0765`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0702`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0627`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0541`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0541`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0533`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.049`, n `668`, weak_sample_signal
