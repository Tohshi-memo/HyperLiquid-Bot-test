# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-21T22:37:29.989731+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0119` n `13`; crypto_alt avg `-0.0432` n `239`; crypto_major avg `-0.1125` n `8`; equity avg `-0.0806` n `166`; fx avg `0.0015` n `6`; index avg `-0.0068` n `27`; metal avg `-0.01` n `20`; unknown avg `-0.149` n `1262`
- 1h: commodity avg `-0.0131` n `13`; crypto_alt avg `0.0365` n `239`; crypto_major avg `-0.2389` n `8`; equity avg `-0.0148` n `166`; fx avg `0.0169` n `6`; index avg `-0.0023` n `27`; metal avg `-0.0534` n `20`; unknown avg `217.0668` n `1256`
- 4h: commodity avg `0.0283` n `13`; crypto_alt avg `-0.4183` n `239`; crypto_major avg `-0.1885` n `8`; equity avg `0.1592` n `166`; fx avg `0.0003` n `6`; index avg `0.0627` n `27`; metal avg `-0.0615` n `20`; unknown avg `42.719` n `1206`
- 24h: commodity avg `0.0144` n `13`; crypto_alt avg `-0.0711` n `239`; crypto_major avg `1.3219` n `8`; equity avg `0.6014` n `166`; fx avg `-0.0608` n `6`; index avg `0.17` n `27`; metal avg `0.103` n `20`; unknown avg `230.3856` n `1090`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1487`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1428`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1351`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1231`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1168`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1164`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1078`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1074`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1061`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1003`, n `668`, weak_sample_signal
