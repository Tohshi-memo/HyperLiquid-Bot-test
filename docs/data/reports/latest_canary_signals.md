# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-04T11:21:16.544141+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0518` n `13`; crypto_alt avg `0.0155` n `235`; crypto_major avg `0.0259` n `8`; equity avg `0.0145` n `143`; fx avg `0.0025` n `6`; index avg `0.0043` n `26`; metal avg `0.0026` n `20`; unknown avg `-0.0417` n `1079`
- 1h: commodity avg `0.0839` n `13`; crypto_alt avg `-0.0761` n `235`; crypto_major avg `-0.1295` n `8`; equity avg `0.0101` n `143`; fx avg `0.0196` n `6`; index avg `0.0053` n `26`; metal avg `-0.0005` n `20`; unknown avg `0.9109` n `1077`
- 4h: commodity avg `0.0438` n `13`; crypto_alt avg `-0.2806` n `235`; crypto_major avg `0.3095` n `8`; equity avg `0.0451` n `143`; fx avg `0.0269` n `6`; index avg `0.0151` n `26`; metal avg `-0.008` n `20`; unknown avg `0.8112` n `1061`
- 24h: commodity avg `0.2244` n `13`; crypto_alt avg `1.82` n `235`; crypto_major avg `1.3997` n `8`; equity avg `0.2744` n `143`; fx avg `-0.0003` n `6`; index avg `0.0443` n `26`; metal avg `-0.0004` n `20`; unknown avg `1.1115` n `898`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.2077`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1799`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.15`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1491`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.135`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1097`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1025`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0945`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0942`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0938`, n `668`, weak_sample_signal
