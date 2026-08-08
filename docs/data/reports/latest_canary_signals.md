# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-08T07:07:29.364017+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0015` n `12`; crypto_alt avg `0.0468` n `230`; crypto_major avg `-0.0407` n `8`; equity avg `0.0204` n `112`; fx avg `0.0015` n `6`; index avg `0.0122` n `25`; metal avg `0.0093` n `20`; unknown avg `-0.0906` n `784`
- 1h: commodity avg `0.0018` n `12`; crypto_alt avg `0.1236` n `230`; crypto_major avg `0.0512` n `8`; equity avg `0.0006` n `112`; fx avg `-0.0028` n `6`; index avg `0.0074` n `25`; metal avg `0.0012` n `20`; unknown avg `-0.1044` n `784`
- 4h: commodity avg `0.0005` n `12`; crypto_alt avg `0.3724` n `230`; crypto_major avg `0.3379` n `8`; equity avg `-0.1197` n `112`; fx avg `0.0046` n `6`; index avg `-0.0397` n `25`; metal avg `0.0035` n `20`; unknown avg `-0.0914` n `751`
- 24h: commodity avg `-0.2574` n `12`; crypto_alt avg `0.0141` n `230`; crypto_major avg `0.6535` n `8`; equity avg `1.1903` n `112`; fx avg `-0.0293` n `6`; index avg `0.0953` n `25`; metal avg `0.0526` n `20`; unknown avg `-0.0643` n `750`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1589`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1154`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0875`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0793`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0712`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0689`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0661`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0641`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0605`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.058`, n `668`, weak_sample_signal
