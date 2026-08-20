# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-20T06:07:31.241100+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.024` n `12`; crypto_alt avg `-0.0186` n `230`; crypto_major avg `-0.0031` n `8`; equity avg `0.1395` n `121`; fx avg `-0.0012` n `6`; index avg `0.0424` n `25`; metal avg `0.0929` n `20`; unknown avg `-0.0314` n `776`
- 1h: commodity avg `0.0066` n `12`; crypto_alt avg `-0.1586` n `230`; crypto_major avg `-0.1356` n `8`; equity avg `0.026` n `121`; fx avg `0.012` n `6`; index avg `0.0307` n `25`; metal avg `-0.0382` n `20`; unknown avg `-0.0747` n `776`
- 4h: commodity avg `-0.0043` n `12`; crypto_alt avg `-0.3518` n `230`; crypto_major avg `-0.2126` n `8`; equity avg `-0.1652` n `121`; fx avg `0.0149` n `6`; index avg `-0.0277` n `25`; metal avg `-0.0221` n `20`; unknown avg `-0.0555` n `776`
- 24h: commodity avg `-0.0902` n `12`; crypto_alt avg `5.5231` n `230`; crypto_major avg `10.0134` n `8`; equity avg `1.8168` n `120`; fx avg `0.1165` n `6`; index avg `0.4002` n `25`; metal avg `1.1602` n `20`; unknown avg `1.6672` n `773`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1952`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1607`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1454`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1319`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1291`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1276`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1189`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1036`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0945`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0893`, n `668`, weak_sample_signal
