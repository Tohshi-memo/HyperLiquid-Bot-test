# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-14T03:37:24.457770+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0265` n `12`; crypto_alt avg `0.0179` n `228`; crypto_major avg `-0.0295` n `8`; equity avg `0.0015` n `74`; fx avg `-0.0073` n `6`; index avg `-0.0328` n `23`; metal avg `-0.0057` n `18`; unknown avg `1.3051` n `645`
- 1h: commodity avg `0.0047` n `12`; crypto_alt avg `-0.0627` n `228`; crypto_major avg `-0.19` n `8`; equity avg `0.0245` n `74`; fx avg `0.0076` n `6`; index avg `-0.0214` n `23`; metal avg `-0.0093` n `18`; unknown avg `0.035` n `629`
- 4h: commodity avg `-0.25` n `12`; crypto_alt avg `-0.1489` n `228`; crypto_major avg `-0.0389` n `8`; equity avg `0.1182` n `74`; fx avg `0.0032` n `6`; index avg `-0.054` n `23`; metal avg `0.0035` n `18`; unknown avg `-0.2775` n `629`
- 24h: commodity avg `-0.5984` n `12`; crypto_alt avg `1.7403` n `228`; crypto_major avg `1.788` n `8`; equity avg `0.5804` n `74`; fx avg `0.0038` n `6`; index avg `0.1893` n `23`; metal avg `0.2775` n `18`; unknown avg `-0.3203` n `595`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.096`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0938`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0701`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0677`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.064`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0617`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0601`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0596`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0586`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0569`, n `668`, weak_sample_signal
