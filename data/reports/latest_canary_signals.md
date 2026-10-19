# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-19T22:07:30.324740+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0112` n `13`; crypto_alt avg `0.4569` n `237`; crypto_major avg `0.3205` n `8`; equity avg `0.0644` n `151`; fx avg `0.0084` n `6`; index avg `0.0196` n `26`; metal avg `0.0037` n `20`; unknown avg `0.1233` n `1184`
- 1h: commodity avg `-0.0403` n `13`; crypto_alt avg `0.6002` n `237`; crypto_major avg `0.4246` n `8`; equity avg `0.1074` n `151`; fx avg `0.0085` n `6`; index avg `0.0413` n `26`; metal avg `0.0047` n `20`; unknown avg `1.6399` n `1184`
- 4h: commodity avg `-0.316` n `13`; crypto_alt avg `0.5304` n `237`; crypto_major avg `0.415` n `8`; equity avg `0.1935` n `151`; fx avg `0.0121` n `6`; index avg `0.0455` n `26`; metal avg `-0.0767` n `20`; unknown avg `1.4723` n `1114`
- 24h: commodity avg `-0.0745` n `13`; crypto_alt avg `1.8453` n `237`; crypto_major avg `1.1726` n `8`; equity avg `1.9597` n `151`; fx avg `-0.0033` n `6`; index avg `0.35` n `26`; metal avg `-0.0765` n `20`; unknown avg `2.8819` n `972`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1949`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1411`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1324`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1259`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0965`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0761`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0755`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0651`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0641`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0633`, n `668`, weak_sample_signal
