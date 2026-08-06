# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-06T04:26:48.196965+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0466` n `12`; crypto_alt avg `0.2793` n `230`; crypto_major avg `0.267` n `8`; equity avg `0.1572` n `108`; fx avg `-0.0143` n `6`; index avg `0.0235` n `25`; metal avg `-0.0269` n `20`; unknown avg `0.0602` n `782`
- 1h: commodity avg `-0.1782` n `12`; crypto_alt avg `0.2237` n `230`; crypto_major avg `0.2798` n `8`; equity avg `0.126` n `108`; fx avg `-0.0023` n `6`; index avg `0.0117` n `25`; metal avg `-0.0082` n `20`; unknown avg `0.082` n `782`
- 4h: commodity avg `0.0062` n `12`; crypto_alt avg `-0.1448` n `230`; crypto_major avg `-0.4851` n `8`; equity avg `0.059` n `108`; fx avg `-0.0522` n `6`; index avg `-0.0802` n `25`; metal avg `-0.0765` n `20`; unknown avg `-0.1692` n `782`
- 24h: commodity avg `-0.1083` n `12`; crypto_alt avg `0.189` n `230`; crypto_major avg `0.2132` n `8`; equity avg `-1.6638` n `108`; fx avg `0.0061` n `6`; index avg `-0.3016` n `25`; metal avg `0.4691` n `20`; unknown avg `0.9566` n `749`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1811`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1579`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1358`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1253`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1027`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0849`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0814`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0778`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0776`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0688`, n `668`, weak_sample_signal
