# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-20T06:37:34.421143+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0244` n `13`; crypto_alt avg `0.049` n `237`; crypto_major avg `0.0491` n `8`; equity avg `0.0225` n `151`; fx avg `-0.0143` n `6`; index avg `0.0054` n `26`; metal avg `-0.0018` n `20`; unknown avg `0.3893` n `1198`
- 1h: commodity avg `0.0465` n `13`; crypto_alt avg `0.0637` n `237`; crypto_major avg `-0.0121` n `8`; equity avg `0.1768` n `151`; fx avg `0.0061` n `6`; index avg `0.0561` n `26`; metal avg `0.0` n `20`; unknown avg `4.0736` n `1176`
- 4h: commodity avg `0.0784` n `13`; crypto_alt avg `0.2202` n `237`; crypto_major avg `0.123` n `8`; equity avg `-0.6037` n `151`; fx avg `-0.0028` n `6`; index avg `-0.0754` n `26`; metal avg `0.0099` n `20`; unknown avg `1.4156` n `1168`
- 24h: commodity avg `0.3266` n `13`; crypto_alt avg `-0.0999` n `237`; crypto_major avg `-0.8355` n `8`; equity avg `-1.7109` n `151`; fx avg `0.0085` n `6`; index avg `-0.2667` n `26`; metal avg `-0.2522` n `20`; unknown avg `5.2417` n `1010`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1956`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1493`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1156`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1025`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0927`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0922`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0896`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0763`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0702`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0693`, n `668`, weak_sample_signal
