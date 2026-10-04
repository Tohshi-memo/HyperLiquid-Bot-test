# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-04T12:22:31.161741+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0032` n `13`; crypto_alt avg `-0.1606` n `235`; crypto_major avg `-0.0353` n `8`; equity avg `-0.0144` n `143`; fx avg `-0.0005` n `6`; index avg `0.0005` n `26`; metal avg `-0.0007` n `20`; unknown avg `0.2282` n `1079`
- 1h: commodity avg `-0.0296` n `13`; crypto_alt avg `-0.1688` n `235`; crypto_major avg `0.0276` n `8`; equity avg `-0.0059` n `143`; fx avg `0.0038` n `6`; index avg `-0.0032` n `26`; metal avg `0.0024` n `20`; unknown avg `-0.1338` n `1071`
- 4h: commodity avg `0.0359` n `13`; crypto_alt avg `-0.5769` n `235`; crypto_major avg `0.1551` n `8`; equity avg `0.0347` n `143`; fx avg `0.0274` n `6`; index avg `0.0136` n `26`; metal avg `-0.008` n `20`; unknown avg `-0.1056` n `1071`
- 24h: commodity avg `0.1828` n `13`; crypto_alt avg `1.5731` n `235`; crypto_major avg `1.204` n `8`; equity avg `0.2484` n `143`; fx avg `0.0072` n `6`; index avg `0.0392` n `26`; metal avg `0.0031` n `20`; unknown avg `0.047` n `902`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.2067`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.18`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1506`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1504`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1388`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.109`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1009`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0959`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0912`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0903`, n `668`, weak_sample_signal
