# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-22T01:52:36.218335+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0107` n `13`; crypto_alt avg `0.1879` n `239`; crypto_major avg `0.1778` n `8`; equity avg `0.0513` n `166`; fx avg `-0.0001` n `6`; index avg `0.0045` n `27`; metal avg `0.0066` n `20`; unknown avg `158.3742` n `1263`
- 1h: commodity avg `-0.0082` n `13`; crypto_alt avg `0.1076` n `239`; crypto_major avg `0.1033` n `8`; equity avg `0.0462` n `166`; fx avg `-0.0076` n `6`; index avg `0.009` n `27`; metal avg `0.0038` n `20`; unknown avg `203.8308` n `1261`
- 4h: commodity avg `-0.0074` n `13`; crypto_alt avg `0.118` n `239`; crypto_major avg `-0.0435` n `8`; equity avg `0.0636` n `166`; fx avg `-0.0126` n `6`; index avg `0.0361` n `27`; metal avg `-0.0166` n `20`; unknown avg `165.1476` n `1236`
- 24h: commodity avg `0.0583` n `13`; crypto_alt avg `0.5864` n `239`; crypto_major avg `1.9864` n `8`; equity avg `0.6462` n `166`; fx avg `-0.0596` n `6`; index avg `0.1753` n `27`; metal avg `0.1122` n `20`; unknown avg `232.2376` n `1082`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1444`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1321`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.127`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1256`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1195`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1124`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1089`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1053`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1032`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1011`, n `668`, weak_sample_signal
