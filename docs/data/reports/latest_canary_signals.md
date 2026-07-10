# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-10T18:37:29.547467+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0894` n `12`; crypto_alt avg `-0.0471` n `229`; crypto_major avg `-0.0902` n `8`; equity avg `-0.0184` n `92`; fx avg `-0.0069` n `6`; index avg `0.0068` n `25`; metal avg `0.0059` n `20`; unknown avg `-0.0027` n `765`
- 1h: commodity avg `0.0856` n `12`; crypto_alt avg `-0.0853` n `229`; crypto_major avg `-0.004` n `8`; equity avg `-0.0518` n `92`; fx avg `-0.0137` n `6`; index avg `-0.0051` n `25`; metal avg `-0.0178` n `20`; unknown avg `-0.023` n `765`
- 4h: commodity avg `0.0941` n `12`; crypto_alt avg `0.4475` n `229`; crypto_major avg `0.231` n `8`; equity avg `0.4366` n `92`; fx avg `-0.0494` n `6`; index avg `0.1196` n `25`; metal avg `0.049` n `20`; unknown avg `-0.1343` n `765`
- 24h: commodity avg `-0.2214` n `12`; crypto_alt avg `0.4079` n `229`; crypto_major avg `0.5744` n `8`; equity avg `-0.8275` n `92`; fx avg `-0.1725` n `6`; index avg `0.0194` n `25`; metal avg `-0.0731` n `20`; unknown avg `-0.1623` n `732`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1244`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1066`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1048`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1042`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0992`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0946`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0903`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0811`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0793`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0756`, n `668`, weak_sample_signal
