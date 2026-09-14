# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-14T09:22:30.418622+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0822` n `12`; crypto_alt avg `-0.3107` n `233`; crypto_major avg `-0.1643` n `8`; equity avg `-0.2551` n `136`; fx avg `0.0009` n `6`; index avg `-0.0416` n `27`; metal avg `-0.2153` n `20`; unknown avg `4.964` n `894`
- 1h: commodity avg `0.0444` n `12`; crypto_alt avg `-0.5425` n `233`; crypto_major avg `-0.3641` n `8`; equity avg `-0.3209` n `136`; fx avg `0.0042` n `6`; index avg `-0.0722` n `27`; metal avg `-0.2547` n `20`; unknown avg `4.5342` n `886`
- 4h: commodity avg `0.2165` n `12`; crypto_alt avg `-0.4295` n `233`; crypto_major avg `0.0033` n `8`; equity avg `-0.8842` n `136`; fx avg `-0.0016` n `6`; index avg `-0.1363` n `27`; metal avg `-0.4579` n `20`; unknown avg `5.3986` n `832`
- 24h: commodity avg `0.815` n `12`; crypto_alt avg `-0.5445` n `233`; crypto_major avg `0.6589` n `8`; equity avg `-1.7652` n `136`; fx avg `0.031` n `6`; index avg `-0.3812` n `27`; metal avg `-0.5841` n `20`; unknown avg `0.7439` n `650`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1174`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1171`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1135`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1134`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0967`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0879`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0858`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0778`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0729`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0708`, n `668`, weak_sample_signal
