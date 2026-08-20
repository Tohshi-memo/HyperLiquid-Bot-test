# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-20T20:22:48.995578+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0006` n `12`; crypto_alt avg `0.2203` n `230`; crypto_major avg `0.1742` n `8`; equity avg `-0.0684` n `121`; fx avg `0.001` n `6`; index avg `-0.0056` n `25`; metal avg `-0.0305` n `20`; unknown avg `-0.112` n `792`
- 1h: commodity avg `-0.0196` n `12`; crypto_alt avg `0.1042` n `230`; crypto_major avg `0.1175` n `8`; equity avg `0.2393` n `121`; fx avg `-0.018` n `6`; index avg `-0.0039` n `25`; metal avg `0.0174` n `20`; unknown avg `-0.2688` n `792`
- 4h: commodity avg `0.0632` n `12`; crypto_alt avg `0.232` n `230`; crypto_major avg `-0.179` n `8`; equity avg `0.3092` n `121`; fx avg `-0.0247` n `6`; index avg `-0.0432` n `25`; metal avg `0.0646` n `20`; unknown avg `0.9229` n `792`
- 24h: commodity avg `0.406` n `12`; crypto_alt avg `5.2094` n `230`; crypto_major avg `7.2334` n `8`; equity avg `-0.5205` n `121`; fx avg `0.1916` n `6`; index avg `-0.0334` n `25`; metal avg `0.1898` n `20`; unknown avg `2.9778` n `776`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.2242`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1882`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1855`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1757`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1113`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1034`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1011`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1009`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0979`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0978`, n `668`, weak_sample_signal
