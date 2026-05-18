# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-18T16:22:20.893849+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0415` n `12`; crypto_alt avg `0.1856` n `228`; crypto_major avg `0.1934` n `8`; equity avg `0.2577` n `66`; fx avg `0.0033` n `5`; index avg `0.1122` n `23`; metal avg `0.1087` n `18`; unknown avg `0.3069` n `384`
- 1h: commodity avg `0.1551` n `12`; crypto_alt avg `0.4254` n `228`; crypto_major avg `0.4689` n `8`; equity avg `0.2965` n `66`; fx avg `0.0045` n `5`; index avg `0.1048` n `23`; metal avg `0.2658` n `18`; unknown avg `0.1607` n `384`
- 4h: commodity avg `0.416` n `12`; crypto_alt avg `-0.9161` n `228`; crypto_major avg `-1.2402` n `8`; equity avg `-1.3659` n `66`; fx avg `-0.0259` n `5`; index avg `-0.3554` n `23`; metal avg `0.1417` n `18`; unknown avg `0.0447` n `383`
- 24h: commodity avg `0.9637` n `12`; crypto_alt avg `-2.684` n `228`; crypto_major avg `-2.0362` n `8`; equity avg `-0.6569` n `66`; fx avg `0.0548` n `5`; index avg `-0.3448` n `23`; metal avg `0.5428` n `18`; unknown avg `-0.4816` n `363`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1614`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1573`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.149`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1204`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1187`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1151`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.11`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1065`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1064`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0982`, n `668`, weak_sample_signal
