# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-04T07:37:24.799587+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0161` n `13`; crypto_alt avg `-0.0978` n `235`; crypto_major avg `-0.0573` n `8`; equity avg `-0.0064` n `143`; fx avg `0.0022` n `6`; index avg `-0.0009` n `26`; metal avg `-0.0005` n `20`; unknown avg `-0.0717` n `1079`
- 1h: commodity avg `-0.0202` n `13`; crypto_alt avg `0.0851` n `235`; crypto_major avg `-0.0012` n `8`; equity avg `-0.0199` n `143`; fx avg `0.0037` n `6`; index avg `-0.0053` n `26`; metal avg `0.0015` n `20`; unknown avg `0.015` n `1077`
- 4h: commodity avg `-0.0047` n `13`; crypto_alt avg `0.4946` n `235`; crypto_major avg `0.1589` n `8`; equity avg `0.0024` n `143`; fx avg `-0.0168` n `6`; index avg `-0.0063` n `26`; metal avg `-0.0027` n `20`; unknown avg `0.1702` n `1043`
- 24h: commodity avg `0.1417` n `13`; crypto_alt avg `2.3873` n `235`; crypto_major avg `1.0144` n `8`; equity avg `0.2341` n `143`; fx avg `-0.0447` n `6`; index avg `0.0166` n `26`; metal avg `0.0019` n `20`; unknown avg `0.3007` n `898`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1923`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1708`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1473`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.141`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1224`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1096`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1075`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1075`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1049`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0916`, n `668`, weak_sample_signal
