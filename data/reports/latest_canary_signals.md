# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-03T11:07:26.984593+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0703` n `12`; crypto_alt avg `0.0265` n `232`; crypto_major avg `0.1003` n `8`; equity avg `0.188` n `133`; fx avg `0.0012` n `6`; index avg `0.032` n `26`; metal avg `-0.0162` n `20`; unknown avg `0.0654` n `790`
- 1h: commodity avg `0.0596` n `12`; crypto_alt avg `-0.0279` n `232`; crypto_major avg `0.0382` n `8`; equity avg `0.0991` n `133`; fx avg `-0.0079` n `6`; index avg `0.0139` n `26`; metal avg `-0.0386` n `20`; unknown avg `-0.2144` n `790`
- 4h: commodity avg `0.4149` n `12`; crypto_alt avg `-0.2718` n `232`; crypto_major avg `-0.4072` n `8`; equity avg `-0.1001` n `133`; fx avg `-0.0107` n `6`; index avg `-0.0326` n `26`; metal avg `-0.0187` n `20`; unknown avg `0.0803` n `790`
- 24h: commodity avg `0.5302` n `12`; crypto_alt avg `2.2405` n `232`; crypto_major avg `2.0065` n `8`; equity avg `1.9486` n `133`; fx avg `-0.3967` n `6`; index avg `0.1865` n `26`; metal avg `0.7655` n `20`; unknown avg `-0.2967` n `735`

## Correlations

- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1075`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0771`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0759`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0737`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0652`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0543`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0492`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0463`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0441`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0415`, n `668`, weak_sample_signal
