# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-15T14:22:35.981622+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0235` n `12`; crypto_alt avg `-0.0218` n `233`; crypto_major avg `-0.0775` n `8`; equity avg `-0.1332` n `137`; fx avg `0.0203` n `6`; index avg `-0.0354` n `27`; metal avg `-0.1142` n `20`; unknown avg `1.8109` n `905`
- 1h: commodity avg `0.1394` n `12`; crypto_alt avg `-0.6889` n `233`; crypto_major avg `-0.8092` n `8`; equity avg `-0.3019` n `137`; fx avg `0.02` n `6`; index avg `-0.1069` n `27`; metal avg `-0.0622` n `20`; unknown avg `2.5295` n `887`
- 4h: commodity avg `0.0913` n `12`; crypto_alt avg `-0.2859` n `233`; crypto_major avg `-0.3848` n `8`; equity avg `-0.2514` n `137`; fx avg `0.0322` n `6`; index avg `-0.0362` n `27`; metal avg `0.1309` n `20`; unknown avg `2.9543` n `881`
- 24h: commodity avg `-0.0578` n `12`; crypto_alt avg `-1.4417` n `233`; crypto_major avg `-1.3197` n `8`; equity avg `-0.2717` n `137`; fx avg `0.1998` n `6`; index avg `-0.007` n `27`; metal avg `0.1882` n `20`; unknown avg `0.9396` n `813`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1064`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.102`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0991`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0927`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.09`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0886`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.087`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.079`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0769`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0647`, n `668`, weak_sample_signal
