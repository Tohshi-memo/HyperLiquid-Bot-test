# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-14T05:22:26.765020+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `1.5148` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0367` n `12`; crypto_alt avg `-0.1543` n `233`; crypto_major avg `-0.0432` n `8`; equity avg `-0.1379` n `136`; fx avg `-0.0005` n `6`; index avg `-0.0173` n `27`; metal avg `-0.0243` n `20`; unknown avg `0.5637` n `894`
- 1h: commodity avg `-0.0599` n `12`; crypto_alt avg `-0.1789` n `233`; crypto_major avg `-0.0262` n `8`; equity avg `-0.1241` n `136`; fx avg `-0.005` n `6`; index avg `-0.0251` n `27`; metal avg `-0.0096` n `20`; unknown avg `0.9835` n `886`
- 4h: commodity avg `-0.1455` n `12`; crypto_alt avg `1.2333` n `233`; crypto_major avg `1.534` n `8`; equity avg `0.3129` n `136`; fx avg `-0.0331` n `6`; index avg `0.0394` n `27`; metal avg `0.0192` n `20`; unknown avg `11.2059` n `880`
- 24h: commodity avg `0.6227` n `12`; crypto_alt avg `-0.812` n `233`; crypto_major avg `-0.071` n `8`; equity avg `-1.5022` n `136`; fx avg `0.0283` n `6`; index avg `-0.3381` n `26`; metal avg `-0.1536` n `20`; unknown avg `1.7173` n `676`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1363`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1262`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.122`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1167`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1073`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0979`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0881`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0865`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0854`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0821`, n `668`, weak_sample_signal
