# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-02T14:07:23.211926+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0818` n `12`; crypto_alt avg `-0.0378` n `230`; crypto_major avg `-0.0508` n `8`; equity avg `0.0022` n `102`; fx avg `0.003` n `6`; index avg `-0.0105` n `25`; metal avg `-0.0006` n `20`; unknown avg `-0.0199` n `782`
- 1h: commodity avg `-0.0949` n `12`; crypto_alt avg `-0.1323` n `230`; crypto_major avg `0.0385` n `8`; equity avg `-0.014` n `102`; fx avg `-0.0248` n `6`; index avg `0.0058` n `25`; metal avg `0.003` n `20`; unknown avg `-0.0584` n `782`
- 4h: commodity avg `0.0077` n `12`; crypto_alt avg `-0.3811` n `230`; crypto_major avg `-0.3375` n `8`; equity avg `-0.2586` n `102`; fx avg `-0.0406` n `6`; index avg `-0.0453` n `25`; metal avg `0.0079` n `20`; unknown avg `-0.1475` n `782`
- 24h: commodity avg `-1.0899` n `12`; crypto_alt avg `0.0135` n `230`; crypto_major avg `-0.0398` n `8`; equity avg `0.8293` n `102`; fx avg `-0.1322` n `6`; index avg `0.2214` n `25`; metal avg `0.2453` n `20`; unknown avg `0.2067` n `766`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1262`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1232`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.107`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0873`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.087`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0818`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0804`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0745`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0721`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0697`, n `668`, weak_sample_signal
