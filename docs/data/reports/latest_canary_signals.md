# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-21T10:52:31.389617+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0112` n `13`; crypto_alt avg `0.2347` n `239`; crypto_major avg `0.3172` n `8`; equity avg `0.069` n `166`; fx avg `0.0035` n `6`; index avg `0.0063` n `27`; metal avg `-0.0004` n `20`; unknown avg `0.4081` n `1262`
- 1h: commodity avg `-0.0093` n `13`; crypto_alt avg `-0.1508` n `239`; crypto_major avg `0.2387` n `8`; equity avg `-0.045` n `166`; fx avg `0.0153` n `6`; index avg `-0.0116` n `27`; metal avg `0.0205` n `20`; unknown avg `161.4706` n `1256`
- 4h: commodity avg `-0.0632` n `13`; crypto_alt avg `-0.5712` n `239`; crypto_major avg `-0.2704` n `8`; equity avg `-0.2489` n `166`; fx avg `0.032` n `6`; index avg `-0.0084` n `27`; metal avg `-0.0086` n `20`; unknown avg `246.6071` n `1238`
- 24h: commodity avg `0.7014` n `13`; crypto_alt avg `-5.4857` n `239`; crypto_major avg `-6.2877` n `8`; equity avg `-4.7443` n `166`; fx avg `-0.0924` n `6`; index avg `-0.5305` n `27`; metal avg `-0.5212` n `20`; unknown avg `177.7191` n `1145`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1554`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1496`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1421`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1215`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.097`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.095`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0907`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0906`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0804`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0779`, n `668`, weak_sample_signal
