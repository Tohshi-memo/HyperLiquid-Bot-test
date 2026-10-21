# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-21T04:37:27.148714+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0413` n `13`; crypto_alt avg `0.0557` n `237`; crypto_major avg `0.0706` n `8`; equity avg `-0.0093` n `151`; fx avg `-0.0106` n `6`; index avg `0.0084` n `26`; metal avg `-0.0575` n `20`; unknown avg `-0.0439` n `1200`
- 1h: commodity avg `-0.0591` n `13`; crypto_alt avg `-0.109` n `237`; crypto_major avg `-0.136` n `8`; equity avg `-0.1828` n `151`; fx avg `-0.0274` n `6`; index avg `-0.0317` n `26`; metal avg `-0.0563` n `20`; unknown avg `0.0027` n `1192`
- 4h: commodity avg `0.0739` n `13`; crypto_alt avg `-0.1143` n `237`; crypto_major avg `-0.3977` n `8`; equity avg `-0.5275` n `151`; fx avg `-0.018` n `6`; index avg `-0.0943` n `26`; metal avg `-0.1694` n `20`; unknown avg `1.9383` n `1191`
- 24h: commodity avg `0.0171` n `13`; crypto_alt avg `2.1084` n `237`; crypto_major avg `1.2817` n `8`; equity avg `2.2448` n `151`; fx avg `-0.0038` n `6`; index avg `0.3209` n `26`; metal avg `-0.189` n `20`; unknown avg `221.0328` n `990`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1694`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1257`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1219`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.12`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1148`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1011`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0952`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0875`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0847`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0804`, n `668`, weak_sample_signal
