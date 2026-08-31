# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-31T09:52:24.636767+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.078` n `12`; crypto_alt avg `-0.0039` n `232`; crypto_major avg `-0.0011` n `8`; equity avg `-0.1789` n `128`; fx avg `0.0171` n `6`; index avg `-0.037` n `26`; metal avg `-0.0244` n `20`; unknown avg `-0.0211` n `794`
- 1h: commodity avg `0.1254` n `12`; crypto_alt avg `-0.042` n `232`; crypto_major avg `0.0452` n `8`; equity avg `-0.239` n `128`; fx avg `0.0367` n `6`; index avg `-0.0463` n `26`; metal avg `-0.0082` n `20`; unknown avg `-0.0129` n `791`
- 4h: commodity avg `0.1598` n `12`; crypto_alt avg `0.0488` n `232`; crypto_major avg `0.2777` n `8`; equity avg `0.1021` n `128`; fx avg `-0.0466` n `6`; index avg `0.0363` n `26`; metal avg `0.0195` n `20`; unknown avg `0.3917` n `773`
- 24h: commodity avg `0.6492` n `12`; crypto_alt avg `-0.0149` n `231`; crypto_major avg `-0.7941` n `8`; equity avg `-0.4566` n `128`; fx avg `-0.111` n `6`; index avg `-0.0913` n `26`; metal avg `-0.2573` n `20`; unknown avg `-0.307` n `759`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1214`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1135`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1134`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.066`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0641`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0612`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0593`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0563`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0556`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0521`, n `668`, weak_sample_signal
