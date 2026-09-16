# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-16T23:37:27.991283+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0176` n `12`; crypto_alt avg `0.2222` n `234`; crypto_major avg `0.0338` n `8`; equity avg `0.0844` n `137`; fx avg `-0.0072` n `6`; index avg `0.0082` n `27`; metal avg `-0.0122` n `20`; unknown avg `0.4825` n `919`
- 1h: commodity avg `0.0002` n `12`; crypto_alt avg `1.0835` n `234`; crypto_major avg `0.6094` n `8`; equity avg `0.2637` n `137`; fx avg `-0.0054` n `6`; index avg `0.0257` n `27`; metal avg `0.0098` n `20`; unknown avg `0.2967` n `909`
- 4h: commodity avg `0.0526` n `12`; crypto_alt avg `1.798` n `234`; crypto_major avg `0.6041` n `8`; equity avg `1.3219` n `137`; fx avg `0.0025` n `6`; index avg `0.2085` n `27`; metal avg `0.1187` n `20`; unknown avg `1.2533` n `781`
- 24h: commodity avg `-0.6225` n `12`; crypto_alt avg `1.0435` n `234`; crypto_major avg `0.9999` n `8`; equity avg `1.495` n `137`; fx avg `0.0623` n `6`; index avg `0.1173` n `27`; metal avg `-0.228` n `20`; unknown avg `-0.5862` n `715`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1171`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1158`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1011`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0993`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0971`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0965`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0769`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.076`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0726`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0696`, n `668`, weak_sample_signal
