# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-05T05:22:34.348124+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0166` n `13`; crypto_alt avg `-0.1622` n `235`; crypto_major avg `-0.1776` n `8`; equity avg `-0.0667` n `144`; fx avg `-0.005` n `6`; index avg `-0.0123` n `26`; metal avg `0.025` n `20`; unknown avg `0.005` n `1079`
- 1h: commodity avg `0.0404` n `13`; crypto_alt avg `-0.211` n `235`; crypto_major avg `-0.1778` n `8`; equity avg `-0.0591` n `144`; fx avg `0.0325` n `6`; index avg `-0.0274` n `26`; metal avg `0.0461` n `20`; unknown avg `0.1836` n `1075`
- 4h: commodity avg `-0.0829` n `13`; crypto_alt avg `-0.904` n `235`; crypto_major avg `-1.0112` n `8`; equity avg `-0.4247` n `144`; fx avg `0.0123` n `6`; index avg `-0.107` n `26`; metal avg `-0.1097` n `20`; unknown avg `2.6582` n `982`
- 24h: commodity avg `-0.3454` n `13`; crypto_alt avg `0.119` n `235`; crypto_major avg `0.6179` n `8`; equity avg `0.188` n `144`; fx avg `-0.0709` n `6`; index avg `-0.0671` n `26`; metal avg `0.0704` n `20`; unknown avg `-0.1003` n `904`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1905`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1747`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1707`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1438`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1344`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1062`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0994`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0951`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0898`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0845`, n `668`, weak_sample_signal
