# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-10T14:07:28.846007+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0021` n `13`; crypto_alt avg `-0.0287` n `235`; crypto_major avg `-0.0519` n `8`; equity avg `-0.0171` n `150`; fx avg `-0.0018` n `6`; index avg `-0.0019` n `26`; metal avg `-0.0027` n `20`; unknown avg `0.0857` n `1115`
- 1h: commodity avg `-0.0035` n `13`; crypto_alt avg `0.2587` n `235`; crypto_major avg `0.0366` n `8`; equity avg `0.0026` n `150`; fx avg `-0.0096` n `6`; index avg `-0.0053` n `26`; metal avg `0.008` n `20`; unknown avg `0.5484` n `1115`
- 4h: commodity avg `0.069` n `13`; crypto_alt avg `0.2655` n `235`; crypto_major avg `0.0231` n `8`; equity avg `0.0239` n `150`; fx avg `-0.0036` n `6`; index avg `-0.0141` n `26`; metal avg `0.0022` n `20`; unknown avg `0.9212` n `1109`
- 24h: commodity avg `-0.4195` n `13`; crypto_alt avg `2.3045` n `235`; crypto_major avg `0.4787` n `8`; equity avg `0.3619` n `150`; fx avg `-0.0045` n `6`; index avg `0.0393` n `26`; metal avg `-0.0179` n `20`; unknown avg `0.9167` n `936`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1564`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1503`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1212`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1167`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1131`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1054`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1047`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1045`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0961`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0898`, n `668`, weak_sample_signal
