# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-16T06:07:26.568052+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0254` n `12`; crypto_alt avg `0.0108` n `234`; crypto_major avg `0.0823` n `8`; equity avg `0.0248` n `137`; fx avg `-0.0066` n `6`; index avg `0.0132` n `27`; metal avg `-0.0747` n `20`; unknown avg `0.1271` n `889`
- 1h: commodity avg `-0.0074` n `12`; crypto_alt avg `0.0178` n `234`; crypto_major avg `0.1799` n `8`; equity avg `0.1989` n `137`; fx avg `0.0302` n `6`; index avg `0.0335` n `27`; metal avg `-0.0496` n `20`; unknown avg `0.3455` n `889`
- 4h: commodity avg `-0.0974` n `12`; crypto_alt avg `0.6565` n `234`; crypto_major avg `0.5832` n `8`; equity avg `0.8678` n `137`; fx avg `-0.0277` n `6`; index avg `0.1103` n `27`; metal avg `0.2531` n `20`; unknown avg `0.3139` n `877`
- 24h: commodity avg `0.1714` n `12`; crypto_alt avg `-3.3897` n `234`; crypto_major avg `-3.3268` n `8`; equity avg `-0.2108` n `137`; fx avg `0.1816` n `6`; index avg `0.0531` n `27`; metal avg `0.3912` n `20`; unknown avg `18937.4819` n `796`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1287`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.108`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1065`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0957`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0923`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0886`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0866`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0835`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0781`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.077`, n `668`, weak_sample_signal
