# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-20T23:22:27.020003+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0302` n `12`; crypto_alt avg `0.1008` n `230`; crypto_major avg `0.1307` n `8`; equity avg `0.0928` n `98`; fx avg `0.0046` n `6`; index avg `0.0443` n `25`; metal avg `0.0054` n `20`; unknown avg `0.6838` n `770`
- 1h: commodity avg `-0.0146` n `12`; crypto_alt avg `0.156` n `230`; crypto_major avg `0.1257` n `8`; equity avg `0.1679` n `98`; fx avg `0.0056` n `6`; index avg `0.0677` n `25`; metal avg `0.0172` n `20`; unknown avg `-0.1202` n `770`
- 4h: commodity avg `-0.0882` n `12`; crypto_alt avg `0.178` n `230`; crypto_major avg `0.147` n `8`; equity avg `0.1039` n `98`; fx avg `-0.0256` n `6`; index avg `0.0343` n `25`; metal avg `-0.0432` n `20`; unknown avg `-0.1288` n `770`
- 24h: commodity avg `-0.3582` n `12`; crypto_alt avg `1.5238` n `230`; crypto_major avg `1.0882` n `8`; equity avg `-0.2168` n `98`; fx avg `-0.192` n `6`; index avg `0.0229` n `25`; metal avg `0.217` n `20`; unknown avg `0.1603` n `745`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1559`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1284`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1272`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.108`, n `666`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1064`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1042`, n `666`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1025`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0992`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0938`, n `666`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0854`, n `666`, weak_sample_signal
