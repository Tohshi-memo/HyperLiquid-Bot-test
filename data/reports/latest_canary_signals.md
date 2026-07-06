# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-06T11:37:31.030805+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0198` n `12`; crypto_alt avg `0.0536` n `229`; crypto_major avg `0.1218` n `8`; equity avg `0.045` n `88`; fx avg `0.004` n `6`; index avg `0.0062` n `25`; metal avg `-0.0043` n `20`; unknown avg `0.0578` n `765`
- 1h: commodity avg `0.0379` n `12`; crypto_alt avg `0.0731` n `229`; crypto_major avg `0.1769` n `8`; equity avg `-0.0602` n `88`; fx avg `0.0051` n `6`; index avg `-0.0047` n `25`; metal avg `-0.0125` n `20`; unknown avg `-0.0713` n `765`
- 4h: commodity avg `-0.0188` n `12`; crypto_alt avg `0.1622` n `229`; crypto_major avg `0.009` n `8`; equity avg `0.0098` n `88`; fx avg `-0.0058` n `6`; index avg `0.012` n `25`; metal avg `0.0126` n `20`; unknown avg `-0.0635` n `765`
- 24h: commodity avg `-0.1639` n `12`; crypto_alt avg `0.4957` n `229`; crypto_major avg `0.9809` n `8`; equity avg `-0.7009` n `88`; fx avg `0.0838` n `6`; index avg `0.0021` n `25`; metal avg `-0.1426` n `20`; unknown avg `1.1138` n `661`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.107`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0905`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0902`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0868`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0831`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0708`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0679`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0658`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0653`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.06`, n `668`, weak_sample_signal
