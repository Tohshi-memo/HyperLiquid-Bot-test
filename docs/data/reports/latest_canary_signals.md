# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-07T03:22:30.484602+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0085` n `13`; crypto_alt avg `-0.2213` n `239`; crypto_major avg `-0.2536` n `8`; equity avg `0.047` n `158`; fx avg `-0.0029` n `6`; index avg `0.0002` n `27`; metal avg `-0.0043` n `20`; unknown avg `0.4694` n `1259`
- 1h: commodity avg `0.0203` n `13`; crypto_alt avg `-0.3318` n `239`; crypto_major avg `-0.3155` n `8`; equity avg `0.0124` n `158`; fx avg `-0.0136` n `6`; index avg `-0.0032` n `27`; metal avg `0.0105` n `20`; unknown avg `-0.1117` n `1253`
- 4h: commodity avg `-0.0558` n `13`; crypto_alt avg `-0.0946` n `239`; crypto_major avg `0.0385` n `8`; equity avg `0.0851` n `158`; fx avg `-0.0137` n `6`; index avg `0.0079` n `27`; metal avg `0.0079` n `20`; unknown avg `0.4093` n `1247`
- 24h: commodity avg `-0.1468` n `13`; crypto_alt avg `0.193` n `239`; crypto_major avg `-0.1641` n `8`; equity avg `1.0517` n `158`; fx avg `-0.1154` n `6`; index avg `0.1246` n `27`; metal avg `0.1804` n `20`; unknown avg `7.7948` n `1020`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2127`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1653`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1588`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1399`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1157`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1109`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1108`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1092`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1023`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1`, n `668`, weak_sample_signal
