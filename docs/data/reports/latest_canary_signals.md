# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-21T05:18:31.713893+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0363` n `13`; crypto_alt avg `-0.0367` n `237`; crypto_major avg `0.0592` n `8`; equity avg `0.0019` n `151`; fx avg `0.0014` n `6`; index avg `0.0176` n `26`; metal avg `0.0056` n `20`; unknown avg `-0.2096` n `1200`
- 1h: commodity avg `-0.0575` n `13`; crypto_alt avg `0.0608` n `237`; crypto_major avg `0.2296` n `8`; equity avg `0.004` n `151`; fx avg `-0.0091` n `6`; index avg `0.0177` n `26`; metal avg `-0.0313` n `20`; unknown avg `-0.3285` n `1198`
- 4h: commodity avg `-0.0071` n `13`; crypto_alt avg `0.1932` n `237`; crypto_major avg `-0.0191` n `8`; equity avg `-0.254` n `151`; fx avg `-0.0443` n `6`; index avg `-0.0103` n `26`; metal avg `-0.0387` n `20`; unknown avg `1.0782` n `1191`
- 24h: commodity avg `-0.0117` n `13`; crypto_alt avg `2.4666` n `237`; crypto_major avg `1.6223` n `8`; equity avg `2.5576` n `151`; fx avg `-0.0201` n `6`; index avg `0.3734` n `26`; metal avg `-0.1059` n `20`; unknown avg `221.2206` n `990`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1647`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1236`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1204`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1204`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1175`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1011`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0956`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0942`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0878`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0806`, n `668`, weak_sample_signal
