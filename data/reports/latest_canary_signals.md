# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-27T02:07:31.881187+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0066` n `13`; crypto_alt avg `-0.1512` n `237`; crypto_major avg `-0.0689` n `8`; equity avg `-0.1252` n `154`; fx avg `-0.0026` n `6`; index avg `-0.025` n `27`; metal avg `-0.0021` n `20`; unknown avg `-0.068` n `1236`
- 1h: commodity avg `-0.0107` n `13`; crypto_alt avg `-0.5152` n `237`; crypto_major avg `-0.4215` n `8`; equity avg `-0.2527` n `154`; fx avg `-0.0064` n `6`; index avg `-0.0391` n `27`; metal avg `-0.0162` n `20`; unknown avg `2.6639` n `1236`
- 4h: commodity avg `-0.0617` n `13`; crypto_alt avg `-0.0901` n `237`; crypto_major avg `0.2495` n `8`; equity avg `0.2126` n `154`; fx avg `-0.0184` n `6`; index avg `0.0914` n `27`; metal avg `-0.0847` n `20`; unknown avg `-0.0151` n `1210`
- 24h: commodity avg `0.0214` n `13`; crypto_alt avg `0.1622` n `237`; crypto_major avg `0.4431` n `8`; equity avg `1.7626` n `153`; fx avg `-0.0367` n `6`; index avg `0.0842` n `27`; metal avg `-0.0421` n `20`; unknown avg `997.2531` n `1004`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2217`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.2015`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1973`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1402`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1308`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1211`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.11`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1091`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0987`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0773`, n `668`, weak_sample_signal
