# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-31T10:07:26.271546+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0073` n `12`; crypto_alt avg `-0.2219` n `232`; crypto_major avg `-0.2143` n `8`; equity avg `-0.0493` n `128`; fx avg `-0.0018` n `6`; index avg `-0.0094` n `26`; metal avg `0.0412` n `20`; unknown avg `6.6851` n `792`
- 1h: commodity avg `0.108` n `12`; crypto_alt avg `-0.2026` n `232`; crypto_major avg `-0.1986` n `8`; equity avg `-0.2101` n `128`; fx avg `0.0177` n `6`; index avg `-0.0488` n `26`; metal avg `-0.0006` n `20`; unknown avg `6.6497` n `791`
- 4h: commodity avg `0.1286` n `12`; crypto_alt avg `-0.041` n `232`; crypto_major avg `0.2998` n `8`; equity avg `-0.0751` n `128`; fx avg `-0.0372` n `6`; index avg `0.0138` n `26`; metal avg `0.1159` n `20`; unknown avg `7.1721` n `789`
- 24h: commodity avg `0.6594` n `12`; crypto_alt avg `-0.4441` n `231`; crypto_major avg `-1.0965` n `8`; equity avg `-0.5147` n `128`; fx avg `-0.1176` n `6`; index avg `-0.101` n `26`; metal avg `-0.2112` n `20`; unknown avg `6.4732` n `759`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.0991`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0964`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0924`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0647`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0627`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0609`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0591`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0557`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0532`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0491`, n `668`, weak_sample_signal
