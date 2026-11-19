# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-19T02:52:24.541718+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.011` n `13`; crypto_alt avg `-0.153` n `239`; crypto_major avg `-0.0966` n `8`; equity avg `0.0396` n `164`; fx avg `-0.0018` n `6`; index avg `0.0013` n `27`; metal avg `-0.1176` n `20`; unknown avg `-0.1562` n `1265`
- 1h: commodity avg `-0.1349` n `13`; crypto_alt avg `0.0058` n `239`; crypto_major avg `-0.1315` n `8`; equity avg `0.0008` n `164`; fx avg `-0.0293` n `6`; index avg `0.0` n `27`; metal avg `-0.2639` n `20`; unknown avg `-0.1572` n `1263`
- 4h: commodity avg `0.1013` n `13`; crypto_alt avg `1.1301` n `239`; crypto_major avg `0.7012` n `8`; equity avg `0.9514` n `164`; fx avg `-0.0498` n `6`; index avg `0.0816` n `27`; metal avg `-0.0207` n `20`; unknown avg `2.7307` n `1257`
- 24h: commodity avg `0.0333` n `13`; crypto_alt avg `-0.2567` n `239`; crypto_major avg `-1.5892` n `8`; equity avg `-0.0713` n `164`; fx avg `-0.1038` n `6`; index avg `0.0956` n `27`; metal avg `-0.7081` n `20`; unknown avg `14.4432` n `1127`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1257`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0969`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0939`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0762`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0726`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0624`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0616`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0605`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0563`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0471`, n `668`, weak_sample_signal
