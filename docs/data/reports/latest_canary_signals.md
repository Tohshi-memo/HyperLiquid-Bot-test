# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-21T05:37:27.007209+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0009` n `13`; crypto_alt avg `-0.0941` n `237`; crypto_major avg `-0.0046` n `8`; equity avg `-0.0476` n `151`; fx avg `0.0278` n `6`; index avg `-0.0325` n `26`; metal avg `0.0012` n `20`; unknown avg `17.0043` n `1200`
- 1h: commodity avg `0.0076` n `13`; crypto_alt avg `-0.1022` n `237`; crypto_major avg `0.1172` n `8`; equity avg `0.0293` n `151`; fx avg `0.0108` n `6`; index avg `-0.0088` n `26`; metal avg `0.0436` n `20`; unknown avg `2.1121` n `1198`
- 4h: commodity avg `0.0207` n `13`; crypto_alt avg `-0.0856` n `237`; crypto_major avg `-0.078` n `8`; equity avg `-0.3105` n `151`; fx avg `-0.0482` n `6`; index avg `-0.0557` n `26`; metal avg `-0.0974` n `20`; unknown avg `1.6705` n `1191`
- 24h: commodity avg `0.0358` n `13`; crypto_alt avg `2.5859` n `237`; crypto_major avg `1.8566` n `8`; equity avg `2.7304` n `151`; fx avg `0.0064` n `6`; index avg `0.369` n `26`; metal avg `-0.0674` n `20`; unknown avg `221.5041` n `990`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1637`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1219`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1209`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1206`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.117`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1009`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0958`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0952`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.088`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0807`, n `668`, weak_sample_signal
