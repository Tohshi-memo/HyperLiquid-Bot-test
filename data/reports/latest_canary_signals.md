# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-06T05:07:26.731024+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0206` n `13`; crypto_alt avg `0.1543` n `235`; crypto_major avg `0.1412` n `8`; equity avg `0.1069` n `149`; fx avg `-0.0225` n `6`; index avg `0.0199` n `26`; metal avg `0.0082` n `20`; unknown avg `0.6773` n `1070`
- 1h: commodity avg `0.0493` n `13`; crypto_alt avg `0.2664` n `235`; crypto_major avg `0.0808` n `8`; equity avg `0.0399` n `149`; fx avg `-0.0113` n `6`; index avg `-0.0026` n `26`; metal avg `-0.0633` n `20`; unknown avg `0.272` n `1068`
- 4h: commodity avg `0.0873` n `13`; crypto_alt avg `-0.8118` n `235`; crypto_major avg `-0.5875` n `8`; equity avg `-0.174` n `149`; fx avg `0.0073` n `6`; index avg `-0.0508` n `26`; metal avg `-0.2352` n `20`; unknown avg `0.9318` n `1062`
- 24h: commodity avg `0.0351` n `13`; crypto_alt avg `-0.3946` n `235`; crypto_major avg `0.2179` n `8`; equity avg `0.1775` n `149`; fx avg `0.0154` n `6`; index avg `0.1323` n `26`; metal avg `-0.0219` n `20`; unknown avg `587.4471` n `852`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1897`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.173`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1647`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1435`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1121`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1044`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1011`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.099`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0959`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0909`, n `668`, weak_sample_signal
