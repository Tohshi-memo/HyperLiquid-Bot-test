# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-04T04:07:28.247699+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.018` n `13`; crypto_alt avg `0.0389` n `235`; crypto_major avg `-0.0195` n `8`; equity avg `-0.0045` n `143`; fx avg `-0.0022` n `6`; index avg `-0.0007` n `26`; metal avg `-0.0031` n `20`; unknown avg `-0.0624` n `1071`
- 1h: commodity avg `-0.043` n `13`; crypto_alt avg `0.1819` n `235`; crypto_major avg `0.1276` n `8`; equity avg `0.0237` n `143`; fx avg `0.0021` n `6`; index avg `-0.0004` n `26`; metal avg `0.0004` n `20`; unknown avg `-0.1581` n `1071`
- 4h: commodity avg `-0.0557` n `13`; crypto_alt avg `0.0297` n `235`; crypto_major avg `0.1632` n `8`; equity avg `0.028` n `143`; fx avg `0.0001` n `6`; index avg `-0.0076` n `26`; metal avg `0.0131` n `20`; unknown avg `-0.2227` n `1071`
- 24h: commodity avg `0.102` n `13`; crypto_alt avg `1.3483` n `235`; crypto_major avg `0.6301` n `8`; equity avg `0.2213` n `143`; fx avg `-0.0267` n `6`; index avg `0.0085` n `26`; metal avg `0.0051` n `20`; unknown avg `0.1755` n `898`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.2014`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1849`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1542`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1514`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1216`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1201`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1179`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1074`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1029`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0866`, n `668`, weak_sample_signal
