# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-04T12:37:25.001506+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0043` n `13`; crypto_alt avg `0.0454` n `235`; crypto_major avg `-0.0264` n `8`; equity avg `0.0124` n `143`; fx avg `0.0005` n `6`; index avg `-0.0017` n `26`; metal avg `0.0013` n `20`; unknown avg `0.0399` n `1079`
- 1h: commodity avg `-0.0011` n `13`; crypto_alt avg `0.023` n `235`; crypto_major avg `0.0239` n `8`; equity avg `0.0158` n `143`; fx avg `0.006` n `6`; index avg `0.0009` n `26`; metal avg `0.0033` n `20`; unknown avg `0.068` n `1071`
- 4h: commodity avg `0.0382` n `13`; crypto_alt avg `-0.4948` n `235`; crypto_major avg `0.1387` n `8`; equity avg `0.0565` n `143`; fx avg `0.0279` n `6`; index avg `0.012` n `26`; metal avg `-0.0056` n `20`; unknown avg `-0.0672` n `1071`
- 24h: commodity avg `0.2062` n `13`; crypto_alt avg `1.7955` n `235`; crypto_major avg `1.2778` n `8`; equity avg `0.2638` n `143`; fx avg `0.0077` n `6`; index avg `0.0396` n `26`; metal avg `0.0072` n `20`; unknown avg `-0.0185` n `902`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.2066`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1801`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.151`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1506`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1398`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1081`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1002`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0956`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0906`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0894`, n `668`, weak_sample_signal
