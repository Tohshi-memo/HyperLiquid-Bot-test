# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-27T11:22:29.761739+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0107` n `12`; crypto_alt avg `0.0426` n `234`; crypto_major avg `0.0076` n `8`; equity avg `0.0168` n `141`; fx avg `-0.0071` n `6`; index avg `0.005` n `26`; metal avg `-0.0013` n `20`; unknown avg `0.05` n `962`
- 1h: commodity avg `-0.0001` n `12`; crypto_alt avg `-0.2663` n `234`; crypto_major avg `-0.2023` n `8`; equity avg `-0.0047` n `141`; fx avg `-0.004` n `6`; index avg `-0.0044` n `26`; metal avg `-0.0088` n `20`; unknown avg `0.4778` n `960`
- 4h: commodity avg `0.0197` n `12`; crypto_alt avg `0.2521` n `234`; crypto_major avg `0.5769` n `8`; equity avg `0.1104` n `141`; fx avg `-0.0206` n `6`; index avg `0.0235` n `26`; metal avg `-0.0078` n `20`; unknown avg `1.7809` n `943`
- 24h: commodity avg `0.0625` n `12`; crypto_alt avg `0.5184` n `234`; crypto_major avg `0.6668` n `8`; equity avg `0.3684` n `141`; fx avg `-0.018` n `6`; index avg `0.0353` n `26`; metal avg `-0.0051` n `20`; unknown avg `4.1858` n `887`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1614`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1494`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1487`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1429`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1385`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1226`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1158`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0969`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0896`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0876`, n `668`, weak_sample_signal
