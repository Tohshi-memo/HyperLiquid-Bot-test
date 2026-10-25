# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-25T12:52:28.797105+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0021` n `13`; crypto_alt avg `0.1254` n `237`; crypto_major avg `0.0444` n `8`; equity avg `0.0189` n `152`; fx avg `-0.0057` n `6`; index avg `0.0088` n `26`; metal avg `0.0035` n `20`; unknown avg `2.7693` n `1231`
- 1h: commodity avg `-0.0425` n `13`; crypto_alt avg `-0.0627` n `237`; crypto_major avg `-0.2282` n `8`; equity avg `0.0589` n `152`; fx avg `0.0072` n `6`; index avg `0.0078` n `26`; metal avg `-0.0013` n `20`; unknown avg `1.6277` n `1225`
- 4h: commodity avg `-0.0448` n `13`; crypto_alt avg `0.5199` n `237`; crypto_major avg `0.2005` n `8`; equity avg `0.1982` n `152`; fx avg `0.0126` n `6`; index avg `0.0226` n `26`; metal avg `0.0375` n `20`; unknown avg `15.5324` n `1195`
- 24h: commodity avg `-0.1464` n `13`; crypto_alt avg `-1.4288` n `237`; crypto_major avg `-0.151` n `8`; equity avg `0.0234` n `152`; fx avg `0.0019` n `6`; index avg `0.0307` n `26`; metal avg `-0.0226` n `20`; unknown avg `17.6508` n `1048`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2245`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1804`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1751`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1719`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1635`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1497`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1465`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1443`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.127`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1238`, n `668`, weak_sample_signal
