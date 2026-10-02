# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-02T23:44:43.127225+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.019` n `13`; crypto_alt avg `0.3268` n `235`; crypto_major avg `0.2544` n `8`; equity avg `0.04` n `143`; fx avg `-0.0032` n `6`; index avg `0.0016` n `26`; metal avg `-0.0069` n `20`; unknown avg `1.3788` n `984`
- 1h: commodity avg `-0.05` n `13`; crypto_alt avg `0.6947` n `235`; crypto_major avg `0.4091` n `8`; equity avg `0.048` n `143`; fx avg `0.0033` n `6`; index avg `0.0063` n `26`; metal avg `0.0051` n `20`; unknown avg `1.0646` n `982`
- 4h: commodity avg `0.2595` n `13`; crypto_alt avg `1.197` n `235`; crypto_major avg `0.7973` n `8`; equity avg `-0.0651` n `143`; fx avg `-0.0247` n `6`; index avg `-0.0189` n `26`; metal avg `-0.0332` n `20`; unknown avg `1.3886` n `906`
- 24h: commodity avg `0.1208` n `13`; crypto_alt avg `-0.326` n `235`; crypto_major avg `-0.2365` n `8`; equity avg `0.7203` n `142`; fx avg `-0.1366` n `6`; index avg `0.2976` n `26`; metal avg `-0.2592` n `20`; unknown avg `-0.5654` n `826`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1679`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1625`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1397`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1218`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1217`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1203`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1083`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1009`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0905`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0897`, n `668`, weak_sample_signal
