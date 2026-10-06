# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-06T11:37:31.848864+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0263` n `13`; crypto_alt avg `-0.0007` n `235`; crypto_major avg `-0.0424` n `8`; equity avg `0.0006` n `150`; fx avg `0.012` n `6`; index avg `0.0032` n `26`; metal avg `0.0165` n `20`; unknown avg `0.6122` n `1074`
- 1h: commodity avg `0.0413` n `13`; crypto_alt avg `0.2086` n `235`; crypto_major avg `0.189` n `8`; equity avg `0.1776` n `150`; fx avg `0.0476` n `6`; index avg `0.0615` n `26`; metal avg `0.0598` n `20`; unknown avg `-0.0271` n `1072`
- 4h: commodity avg `-0.3285` n `13`; crypto_alt avg `0.7634` n `235`; crypto_major avg `0.6542` n `8`; equity avg `0.4012` n `149`; fx avg `0.0593` n `6`; index avg `0.0979` n `26`; metal avg `0.154` n `20`; unknown avg `0.8468` n `1056`
- 24h: commodity avg `-0.6685` n `13`; crypto_alt avg `-0.3932` n `235`; crypto_major avg `-0.2438` n `8`; equity avg `0.7391` n `149`; fx avg `0.07` n `6`; index avg `0.2452` n `26`; metal avg `-0.1032` n `20`; unknown avg `-0.3294` n `876`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.178`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.161`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.152`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1436`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0939`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0913`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0889`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0852`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0798`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0737`, n `668`, weak_sample_signal
