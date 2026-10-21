# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-21T00:07:26.979128+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0139` n `13`; crypto_alt avg `0.0191` n `237`; crypto_major avg `-0.034` n `8`; equity avg `-0.0209` n `151`; fx avg `0.009` n `6`; index avg `-0.054` n `26`; metal avg `0.018` n `20`; unknown avg `10.1927` n `1191`
- 1h: commodity avg `0.0241` n `13`; crypto_alt avg `0.1392` n `237`; crypto_major avg `-0.0128` n `8`; equity avg `0.0716` n `151`; fx avg `-0.0206` n `6`; index avg `-0.0208` n `26`; metal avg `-0.0127` n `20`; unknown avg `10.1758` n `1175`
- 4h: commodity avg `0.0514` n `13`; crypto_alt avg `0.4834` n `237`; crypto_major avg `0.2916` n `8`; equity avg `1.5154` n `151`; fx avg `-0.0308` n `6`; index avg `0.1276` n `26`; metal avg `0.0081` n `20`; unknown avg `11.7264` n `1045`
- 24h: commodity avg `0.0379` n `13`; crypto_alt avg `2.5691` n `237`; crypto_major avg `1.7212` n `8`; equity avg `2.0269` n `151`; fx avg `0.0385` n `6`; index avg `0.1994` n `26`; metal avg `0.0678` n `20`; unknown avg `215.2447` n `988`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1731`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1294`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1166`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1096`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1071`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0963`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0905`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0883`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0826`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.079`, n `668`, weak_sample_signal
