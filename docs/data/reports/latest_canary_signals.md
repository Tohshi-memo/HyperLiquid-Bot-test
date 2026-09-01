# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-01T06:37:32.021568+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0368` n `12`; crypto_alt avg `0.1037` n `232`; crypto_major avg `0.0692` n `8`; equity avg `-0.0608` n `130`; fx avg `0.0052` n `6`; index avg `-0.0163` n `26`; metal avg `0.0016` n `20`; unknown avg `-0.0099` n `790`
- 1h: commodity avg `-0.0208` n `12`; crypto_alt avg `-0.0181` n `232`; crypto_major avg `-0.1398` n `8`; equity avg `0.0521` n `130`; fx avg `0.0207` n `6`; index avg `-0.0089` n `26`; metal avg `-0.0266` n `20`; unknown avg `-0.0683` n `770`
- 4h: commodity avg `-0.0346` n `12`; crypto_alt avg `0.8991` n `232`; crypto_major avg `0.6111` n `8`; equity avg `0.4182` n `130`; fx avg `0.0044` n `6`; index avg `0.0679` n `26`; metal avg `0.0804` n `20`; unknown avg `0.1719` n `770`
- 24h: commodity avg `0.316` n `12`; crypto_alt avg `1.6428` n `232`; crypto_major avg `1.4254` n `8`; equity avg `0.5083` n `130`; fx avg `0.0309` n `6`; index avg `-0.0087` n `26`; metal avg `-0.1541` n `20`; unknown avg `0.269` n `749`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1039`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1005`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0992`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0966`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0881`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0539`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0504`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.049`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0485`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0484`, n `668`, weak_sample_signal
