# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-18T19:07:50.755347+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.13` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0234` n `13`; crypto_alt avg `-0.3708` n `239`; crypto_major avg `-0.4834` n `8`; equity avg `-0.4951` n `164`; fx avg `-0.0074` n `6`; index avg `-0.0563` n `27`; metal avg `-0.0754` n `20`; unknown avg `0.5773` n `1259`
- 1h: commodity avg `0.1842` n `13`; crypto_alt avg `0.0395` n `239`; crypto_major avg `-0.2128` n `8`; equity avg `-0.2268` n `164`; fx avg `0.007` n `6`; index avg `-0.02` n `27`; metal avg `-0.0369` n `20`; unknown avg `0.3397` n `1263`
- 4h: commodity avg `0.0239` n `13`; crypto_alt avg `-0.574` n `239`; crypto_major avg `-0.6779` n `8`; equity avg `-0.7292` n `164`; fx avg `-0.0076` n `6`; index avg `-0.0672` n `27`; metal avg `-0.0798` n `20`; unknown avg `-0.0939` n `1257`
- 24h: commodity avg `-0.3956` n `13`; crypto_alt avg `0.5002` n `239`; crypto_major avg `-0.3715` n `8`; equity avg `0.0413` n `164`; fx avg `-0.1941` n `6`; index avg `0.0282` n `27`; metal avg `-1.1426` n `20`; unknown avg `-0.3168` n `1138`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1037`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0836`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0803`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0744`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0662`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0613`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.053`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0527`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0483`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0476`, n `668`, weak_sample_signal
