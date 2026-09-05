# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-05T11:22:27.113017+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.011` n `12`; crypto_alt avg `-0.1545` n `232`; crypto_major avg `-0.0204` n `8`; equity avg `0.0228` n `134`; fx avg `-0.0064` n `6`; index avg `0.0007` n `26`; metal avg `0.0015` n `20`; unknown avg `0.0951` n `789`
- 1h: commodity avg `-0.0108` n `12`; crypto_alt avg `-0.0958` n `232`; crypto_major avg `0.0429` n `8`; equity avg `0.0245` n `134`; fx avg `-0.0035` n `6`; index avg `-0.0017` n `26`; metal avg `0.0022` n `20`; unknown avg `0.221` n `786`
- 4h: commodity avg `-0.0272` n `12`; crypto_alt avg `0.1072` n `232`; crypto_major avg `0.4088` n `8`; equity avg `0.078` n `134`; fx avg `-0.0043` n `6`; index avg `0.0145` n `26`; metal avg `-0.0084` n `20`; unknown avg `0.2698` n `780`
- 24h: commodity avg `0.1356` n `12`; crypto_alt avg `0.3438` n `232`; crypto_major avg `-1.4127` n `8`; equity avg `0.8494` n `134`; fx avg `-0.1195` n `6`; index avg `0.0518` n `26`; metal avg `-0.1081` n `20`; unknown avg `16.9002` n `650`

## Correlations

- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1677`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1498`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1279`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1262`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1201`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1155`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1117`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1104`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1049`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0951`, n `668`, weak_sample_signal
