# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-16T02:22:30.040845+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0385` n `12`; crypto_alt avg `0.3985` n `234`; crypto_major avg `0.3821` n `8`; equity avg `0.0722` n `137`; fx avg `-0.0223` n `6`; index avg `0.0085` n `27`; metal avg `0.0632` n `20`; unknown avg `0.1738` n `919`
- 1h: commodity avg `-0.0225` n `12`; crypto_alt avg `-0.3385` n `234`; crypto_major avg `-0.1318` n `8`; equity avg `-0.0336` n `137`; fx avg `-0.0091` n `6`; index avg `-0.0105` n `27`; metal avg `-0.001` n `20`; unknown avg `-0.0157` n `917`
- 4h: commodity avg `-0.0908` n `12`; crypto_alt avg `0.2381` n `234`; crypto_major avg `0.5801` n `8`; equity avg `0.0263` n `137`; fx avg `0.0991` n `6`; index avg `0.0065` n `27`; metal avg `0.0026` n `20`; unknown avg `0.1565` n `903`
- 24h: commodity avg `0.3124` n `12`; crypto_alt avg `-4.1052` n `234`; crypto_major avg `-3.9248` n `8`; equity avg `-1.5836` n `137`; fx avg `0.2132` n `6`; index avg `-0.1565` n `27`; metal avg `0.1323` n `20`; unknown avg `1.0888` n `802`

## Correlations

- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1219`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1182`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0976`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0942`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0933`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0903`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.088`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0722`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0714`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0671`, n `668`, weak_sample_signal
