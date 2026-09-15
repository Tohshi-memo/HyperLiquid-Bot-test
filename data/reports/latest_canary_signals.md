# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-15T14:37:35.522166+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0403` n `12`; crypto_alt avg `-0.3659` n `233`; crypto_major avg `-0.5363` n `8`; equity avg `-0.2312` n `137`; fx avg `0.0039` n `6`; index avg `-0.0107` n `27`; metal avg `-0.0589` n `20`; unknown avg `0.2132` n `905`
- 1h: commodity avg `0.0362` n `12`; crypto_alt avg `-0.5311` n `233`; crypto_major avg `-0.775` n `8`; equity avg `-0.602` n `137`; fx avg `0.0062` n `6`; index avg `-0.0843` n `27`; metal avg `-0.1624` n `20`; unknown avg `0.6785` n `887`
- 4h: commodity avg `0.1663` n `12`; crypto_alt avg `-0.666` n `233`; crypto_major avg `-0.9824` n `8`; equity avg `-0.5853` n `137`; fx avg `0.035` n `6`; index avg `-0.0656` n `27`; metal avg `0.0566` n `20`; unknown avg `1.3036` n `881`
- 24h: commodity avg `0.0114` n `12`; crypto_alt avg `-1.6645` n `233`; crypto_major avg `-1.7217` n `8`; equity avg `-0.1885` n `137`; fx avg `0.2092` n `6`; index avg `0.0407` n `27`; metal avg `0.1338` n `20`; unknown avg `0.4056` n `813`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1027`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1012`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0987`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0958`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0896`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0875`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0868`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0774`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0724`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0618`, n `668`, weak_sample_signal
