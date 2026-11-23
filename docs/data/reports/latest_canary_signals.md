# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-23T08:07:29.229356+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0465` n `13`; crypto_alt avg `0.1136` n `239`; crypto_major avg `0.0848` n `8`; equity avg `0.2959` n `166`; fx avg `-0.0049` n `6`; index avg `0.0432` n `27`; metal avg `-0.1224` n `20`; unknown avg `0.1455` n `1244`
- 1h: commodity avg `0.0429` n `13`; crypto_alt avg `0.1459` n `239`; crypto_major avg `0.009` n `8`; equity avg `0.4617` n `166`; fx avg `0.0145` n `6`; index avg `0.0596` n `27`; metal avg `-0.1415` n `20`; unknown avg `0.8381` n `1246`
- 4h: commodity avg `-0.2451` n `13`; crypto_alt avg `0.875` n `239`; crypto_major avg `0.4162` n `8`; equity avg `0.7273` n `166`; fx avg `-0.0091` n `6`; index avg `0.0504` n `27`; metal avg `0.1155` n `20`; unknown avg `0.0837` n `1218`
- 24h: commodity avg `-0.5625` n `13`; crypto_alt avg `2.457` n `239`; crypto_major avg `3.0374` n `8`; equity avg `2.8895` n `166`; fx avg `0.233` n `6`; index avg `0.1936` n `27`; metal avg `0.4611` n `20`; unknown avg `346.0854` n `1001`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.1526`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1476`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1406`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1315`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1274`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.127`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1268`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1262`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1248`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1208`, n `668`, weak_sample_signal
