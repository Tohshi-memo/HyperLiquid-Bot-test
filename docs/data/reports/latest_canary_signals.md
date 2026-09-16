# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-16T06:52:26.540416+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0919` n `12`; crypto_alt avg `0.1466` n `234`; crypto_major avg `0.1539` n `8`; equity avg `0.0419` n `137`; fx avg `0.0006` n `6`; index avg `0.006` n `27`; metal avg `0.0101` n `20`; unknown avg `0.1671` n `919`
- 1h: commodity avg `-0.1055` n `12`; crypto_alt avg `-0.0886` n `234`; crypto_major avg `-0.0157` n `8`; equity avg `0.0668` n `137`; fx avg `-0.0279` n `6`; index avg `0.0519` n `27`; metal avg `-0.016` n `20`; unknown avg `-0.0274` n `889`
- 4h: commodity avg `-0.1011` n `12`; crypto_alt avg `-0.048` n `234`; crypto_major avg `-0.11` n `8`; equity avg `0.5281` n `137`; fx avg `-0.0011` n `6`; index avg `0.0999` n `27`; metal avg `0.0856` n `20`; unknown avg `0.4055` n `881`
- 24h: commodity avg `0.0528` n `12`; crypto_alt avg `-3.0441` n `234`; crypto_major avg `-2.8025` n `8`; equity avg `-0.0586` n `137`; fx avg `0.155` n `6`; index avg `0.1114` n `27`; metal avg `0.4541` n `20`; unknown avg `18937.4156` n `796`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1384`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1218`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1067`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1007`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1002`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0905`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.088`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0867`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0812`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0695`, n `668`, weak_sample_signal
