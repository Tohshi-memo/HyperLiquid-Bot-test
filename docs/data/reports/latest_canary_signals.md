# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-08T04:22:23.340716+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.026` n `13`; crypto_alt avg `-0.1004` n `239`; crypto_major avg `-0.0522` n `8`; equity avg `-0.0373` n `158`; fx avg `-0.0015` n `6`; index avg `-0.0047` n `27`; metal avg `-0.0005` n `20`; unknown avg `-0.1384` n `1258`
- 1h: commodity avg `0.0226` n `13`; crypto_alt avg `-0.0699` n `239`; crypto_major avg `0.0128` n `8`; equity avg `-0.0796` n `158`; fx avg `-0.0053` n `6`; index avg `-0.0106` n `27`; metal avg `-0.0043` n `20`; unknown avg `0.198` n `1246`
- 4h: commodity avg `0.0662` n `13`; crypto_alt avg `-0.5658` n `239`; crypto_major avg `-0.1751` n `8`; equity avg `-0.0519` n `158`; fx avg `0.0111` n `6`; index avg `-0.0145` n `27`; metal avg `-0.0157` n `20`; unknown avg `-0.0169` n `1242`
- 24h: commodity avg `0.196` n `13`; crypto_alt avg `-1.5488` n `239`; crypto_major avg `-0.4558` n `8`; equity avg `-0.119` n `158`; fx avg `0.0066` n `6`; index avg `0.0352` n `27`; metal avg `-0.0495` n `20`; unknown avg `163.2898` n `1083`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2111`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1632`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1586`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.124`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1197`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1113`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1103`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1054`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1033`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1015`, n `668`, weak_sample_signal
