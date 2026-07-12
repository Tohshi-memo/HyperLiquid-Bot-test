# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-12T12:52:26.292210+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0217` n `12`; crypto_alt avg `-0.0762` n `230`; crypto_major avg `-0.0303` n `8`; equity avg `-0.0053` n `92`; fx avg `-0.0008` n `6`; index avg `0.0042` n `25`; metal avg `0.0004` n `20`; unknown avg `-0.0073` n `765`
- 1h: commodity avg `-0.0685` n `12`; crypto_alt avg `-0.0474` n `230`; crypto_major avg `0.0113` n `8`; equity avg `0.0031` n `92`; fx avg `-0.0034` n `6`; index avg `-0.0012` n `25`; metal avg `-0.0113` n `20`; unknown avg `-0.0376` n `765`
- 4h: commodity avg `-0.057` n `12`; crypto_alt avg `-0.0055` n `230`; crypto_major avg `0.2758` n `8`; equity avg `0.0448` n `92`; fx avg `-0.0052` n `6`; index avg `-0.0126` n `25`; metal avg `-0.0034` n `20`; unknown avg `-0.0733` n `763`
- 24h: commodity avg `0.4225` n `12`; crypto_alt avg `-1.0473` n `230`; crypto_major avg `-0.4758` n `8`; equity avg `-0.0756` n `92`; fx avg `0.0091` n `6`; index avg `-0.1096` n `25`; metal avg `-0.0956` n `20`; unknown avg `0.0896` n `745`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.183`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1657`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1396`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1314`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1217`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1192`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.11`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1055`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.104`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1015`, n `668`, weak_sample_signal
