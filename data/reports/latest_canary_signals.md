# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-25T14:52:28.248413+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0146` n `13`; crypto_alt avg `0.4229` n `237`; crypto_major avg `0.3221` n `8`; equity avg `0.104` n `152`; fx avg `-0.0002` n `6`; index avg `0.0138` n `26`; metal avg `0.0034` n `20`; unknown avg `0.6072` n `1231`
- 1h: commodity avg `0.025` n `13`; crypto_alt avg `0.1149` n `237`; crypto_major avg `0.1711` n `8`; equity avg `0.0658` n `152`; fx avg `-0.0043` n `6`; index avg `0.0096` n `26`; metal avg `0.0208` n `20`; unknown avg `0.772` n `1231`
- 4h: commodity avg `-0.0777` n `13`; crypto_alt avg `0.7853` n `237`; crypto_major avg `0.5934` n `8`; equity avg `0.3715` n `152`; fx avg `0.016` n `6`; index avg `0.0664` n `26`; metal avg `0.0762` n `20`; unknown avg `0.4296` n `1225`
- 24h: commodity avg `-0.168` n `13`; crypto_alt avg `-0.0668` n `237`; crypto_major avg `0.8134` n `8`; equity avg `0.5083` n `152`; fx avg `0.0192` n `6`; index avg `0.116` n `26`; metal avg `0.1068` n `20`; unknown avg `18.0751` n `1080`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2232`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1795`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1714`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1697`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.159`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1444`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1414`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1401`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1211`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1147`, n `668`, weak_sample_signal
