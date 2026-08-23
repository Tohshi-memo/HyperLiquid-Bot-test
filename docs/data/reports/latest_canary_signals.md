# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-23T14:52:23.804888+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0044` n `12`; crypto_alt avg `0.6255` n `231`; crypto_major avg `0.5177` n `8`; equity avg `0.0527` n `122`; fx avg `0.0073` n `6`; index avg `-0.0031` n `25`; metal avg `0.012` n `20`; unknown avg `0.1427` n `793`
- 1h: commodity avg `-0.0151` n `12`; crypto_alt avg `-0.3694` n `231`; crypto_major avg `-0.4419` n `8`; equity avg `-0.0209` n `122`; fx avg `0.0007` n `6`; index avg `0.0131` n `25`; metal avg `-0.0164` n `20`; unknown avg `0.3922` n `793`
- 4h: commodity avg `-0.0112` n `12`; crypto_alt avg `1.9373` n `231`; crypto_major avg `0.9169` n `8`; equity avg `0.1788` n `122`; fx avg `0.0016` n `6`; index avg `0.023` n `25`; metal avg `0.0283` n `20`; unknown avg `2.657` n `793`
- 24h: commodity avg `0.0528` n `12`; crypto_alt avg `2.1799` n `231`; crypto_major avg `1.8761` n `8`; equity avg `0.5211` n `122`; fx avg `0.0547` n `6`; index avg `0.0579` n `25`; metal avg `0.0534` n `20`; unknown avg `8.1154` n `776`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1099`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1057`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1053`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.105`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0989`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0979`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0906`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0894`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0865`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0858`, n `668`, weak_sample_signal
