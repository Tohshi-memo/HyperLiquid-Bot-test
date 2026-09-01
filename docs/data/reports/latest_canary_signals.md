# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-01T06:07:29.978507+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1092` n `12`; crypto_alt avg `-0.2635` n `232`; crypto_major avg `-0.1764` n `8`; equity avg `0.0998` n `130`; fx avg `0.0253` n `6`; index avg `0.0053` n `26`; metal avg `-0.0156` n `20`; unknown avg `0.0608` n `772`
- 1h: commodity avg `-0.0445` n `12`; crypto_alt avg `0.2144` n `232`; crypto_major avg `0.2048` n `8`; equity avg `0.2728` n `130`; fx avg `0.0137` n `6`; index avg `0.0697` n `26`; metal avg `0.0733` n `20`; unknown avg `0.0372` n `772`
- 4h: commodity avg `0.0901` n `12`; crypto_alt avg `0.7477` n `232`; crypto_major avg `0.6872` n `8`; equity avg `0.3745` n `130`; fx avg `0.0194` n `6`; index avg `0.0725` n `26`; metal avg `0.0074` n `20`; unknown avg `0.0786` n `772`
- 24h: commodity avg `0.2949` n `12`; crypto_alt avg `1.8481` n `232`; crypto_major avg `1.7144` n `8`; equity avg `0.9456` n `130`; fx avg `0.0252` n `6`; index avg `0.0824` n `26`; metal avg `-0.0061` n `20`; unknown avg `0.3573` n `751`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1042`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1009`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0977`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.097`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.087`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0538`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0527`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0502`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0497`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0485`, n `668`, weak_sample_signal
