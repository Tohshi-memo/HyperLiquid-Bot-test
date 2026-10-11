# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-11T22:37:32.972514+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0119` n `13`; crypto_alt avg `0.175` n `235`; crypto_major avg `0.089` n `8`; equity avg `0.0584` n `150`; fx avg `0.0059` n `6`; index avg `0.0073` n `26`; metal avg `0.0301` n `20`; unknown avg `0.0048` n `1134`
- 1h: commodity avg `0.0248` n `13`; crypto_alt avg `0.4322` n `235`; crypto_major avg `0.3352` n `8`; equity avg `0.0848` n `150`; fx avg `-0.0048` n `6`; index avg `0.0209` n `26`; metal avg `-0.02` n `20`; unknown avg `0.1926` n `1122`
- 4h: commodity avg `0.1237` n `13`; crypto_alt avg `0.0507` n `235`; crypto_major avg `-0.2595` n `8`; equity avg `0.0306` n `150`; fx avg `-0.0225` n `6`; index avg `0.0044` n `26`; metal avg `-0.022` n `20`; unknown avg `-0.0501` n `1096`
- 24h: commodity avg `0.209` n `13`; crypto_alt avg `1.6577` n `235`; crypto_major avg `0.6319` n `8`; equity avg `0.2923` n `150`; fx avg `0.0002` n `6`; index avg `0.0408` n `26`; metal avg `0.0363` n `20`; unknown avg `0.5887` n `965`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1436`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1342`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1106`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1095`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0902`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.084`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0833`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0804`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0739`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0724`, n `668`, weak_sample_signal
