# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-31T16:37:35.663969+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0169` n `12`; crypto_alt avg `0.1881` n `232`; crypto_major avg `0.0852` n `8`; equity avg `0.1185` n `128`; fx avg `-0.0028` n `6`; index avg `0.012` n `26`; metal avg `-0.0173` n `20`; unknown avg `0.1507` n `794`
- 1h: commodity avg `0.0356` n `12`; crypto_alt avg `0.1013` n `232`; crypto_major avg `-0.0488` n `8`; equity avg `0.061` n `128`; fx avg `-0.0328` n `6`; index avg `-0.0012` n `26`; metal avg `0.0032` n `20`; unknown avg `-0.0399` n `792`
- 4h: commodity avg `0.0881` n `12`; crypto_alt avg `0.174` n `232`; crypto_major avg `0.3381` n `8`; equity avg `0.1356` n `128`; fx avg `0.0173` n `6`; index avg `-0.1065` n `26`; metal avg `-0.2437` n `20`; unknown avg `0.0461` n `790`
- 24h: commodity avg `0.5874` n `12`; crypto_alt avg `-1.5565` n `231`; crypto_major avg `-2.1178` n `8`; equity avg `-0.5409` n `128`; fx avg `-0.0997` n `6`; index avg `-0.2322` n `26`; metal avg `-0.5723` n `20`; unknown avg `-0.1796` n `759`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1009`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0996`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0935`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0817`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.071`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0595`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0575`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0559`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0524`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0518`, n `668`, weak_sample_signal
