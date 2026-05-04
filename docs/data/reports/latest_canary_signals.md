# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-04T21:00:36.314821+00:00`
- Correlation status: `ready`
- Asset price records: `298`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0893` n `7`; crypto_alt avg `0.0123` n `223`; crypto_major avg `-0.01` n `7`; equity avg `0.0533` n `47`; fx avg `0.0003` n `4`; index avg `0.0084` n `6`; metal avg `0.0306` n `7`; unknown avg `-0.0185` n `312`
- 1h: commodity avg `-0.0132` n `7`; crypto_alt avg `-0.2335` n `223`; crypto_major avg `-0.1334` n `7`; equity avg `0.0472` n `47`; fx avg `0.0167` n `4`; index avg `-0.0263` n `6`; metal avg `0.0044` n `7`; unknown avg `-0.0332` n `312`
- 4h: commodity avg `-0.4013` n `7`; crypto_alt avg `-0.0085` n `223`; crypto_major avg `-0.1808` n `7`; equity avg `-0.2932` n `47`; fx avg `0.0212` n `4`; index avg `0.1194` n `6`; metal avg `0.1646` n `7`; unknown avg `-0.1993` n `312`
- 24h: commodity avg `2.1682` n `7`; crypto_alt avg `1.2756` n `223`; crypto_major avg `0.6494` n `7`; equity avg `-0.3612` n `47`; fx avg `-0.0569` n `4`; index avg `-0.0878` n `6`; metal avg `-2.4055` n `7`; unknown avg `-0.8963` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2366`, n `294`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2309`, n `294`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1871`, n `290`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1854`, n `290`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1501`, n `294`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1496`, n `294`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.144`, n `294`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1298`, n `294`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1212`, n `290`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1208`, n `294`, weak_sample_signal
