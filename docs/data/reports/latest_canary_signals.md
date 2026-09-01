# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-01T01:07:28.378107+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0093` n `12`; crypto_alt avg `-0.0737` n `232`; crypto_major avg `-0.1085` n `8`; equity avg `0.0902` n `130`; fx avg `-0.0045` n `6`; index avg `0.0346` n `26`; metal avg `-0.0316` n `20`; unknown avg `-0.0057` n `790`
- 1h: commodity avg `-0.0276` n `12`; crypto_alt avg `0.353` n `232`; crypto_major avg `-0.0099` n `8`; equity avg `0.1463` n `130`; fx avg `0.0015` n `6`; index avg `0.0657` n `26`; metal avg `-0.0014` n `20`; unknown avg `0.2007` n `790`
- 4h: commodity avg `0.0511` n `12`; crypto_alt avg `0.717` n `232`; crypto_major avg `-0.1317` n `8`; equity avg `0.1489` n `130`; fx avg `0.0182` n `6`; index avg `0.0385` n `26`; metal avg `0.1081` n `20`; unknown avg `0.0501` n `790`
- 24h: commodity avg `0.4866` n `12`; crypto_alt avg `2.3682` n `231`; crypto_major avg `1.8976` n `8`; equity avg `1.4687` n `130`; fx avg `-0.0711` n `6`; index avg `0.2437` n `26`; metal avg `-0.0436` n `20`; unknown avg `0.2708` n `739`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.102`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1003`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0985`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0978`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.089`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0667`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0571`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.057`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0561`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0509`, n `668`, weak_sample_signal
