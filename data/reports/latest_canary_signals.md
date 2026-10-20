# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-20T04:52:28.104119+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0002` n `13`; crypto_alt avg `-0.2201` n `237`; crypto_major avg `-0.0981` n `8`; equity avg `-0.0922` n `151`; fx avg `0.0043` n `6`; index avg `-0.0152` n `26`; metal avg `0.0042` n `20`; unknown avg `-0.2328` n `1198`
- 1h: commodity avg `-0.0335` n `13`; crypto_alt avg `-0.2949` n `237`; crypto_major avg `-0.0426` n `8`; equity avg `-0.4189` n `151`; fx avg `-0.0104` n `6`; index avg `-0.0764` n `26`; metal avg `-0.0112` n `20`; unknown avg `0.0942` n `1188`
- 4h: commodity avg `0.0622` n `13`; crypto_alt avg `0.4711` n `237`; crypto_major avg `0.3902` n `8`; equity avg `0.029` n `151`; fx avg `0.0397` n `6`; index avg `-0.025` n `26`; metal avg `0.1718` n `20`; unknown avg `1.4839` n `1188`
- 24h: commodity avg `0.2656` n `13`; crypto_alt avg `0.2731` n `237`; crypto_major avg `-0.5019` n `8`; equity avg `-1.2928` n `151`; fx avg `-0.0248` n `6`; index avg `-0.2285` n `26`; metal avg `-0.2365` n `20`; unknown avg `5.4058` n `1010`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.199`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1435`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1179`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0989`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.094`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0884`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.087`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0745`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0727`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0722`, n `668`, weak_sample_signal
