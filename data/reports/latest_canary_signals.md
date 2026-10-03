# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-03T21:07:26.382649+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0818` n `13`; crypto_alt avg `-0.1803` n `235`; crypto_major avg `-0.0993` n `8`; equity avg `-0.0211` n `143`; fx avg `-0.0022` n `6`; index avg `-0.0026` n `26`; metal avg `0.0023` n `20`; unknown avg `-0.0522` n `1077`
- 1h: commodity avg `0.0897` n `13`; crypto_alt avg `-0.0416` n `235`; crypto_major avg `-0.2174` n `8`; equity avg `-0.0239` n `143`; fx avg `0.0042` n `6`; index avg `-0.0046` n `26`; metal avg `-0.0012` n `20`; unknown avg `-0.2393` n `1077`
- 4h: commodity avg `0.0059` n `13`; crypto_alt avg `0.0975` n `235`; crypto_major avg `-0.071` n `8`; equity avg `0.0457` n `143`; fx avg `-0.0005` n `6`; index avg `0.0066` n `26`; metal avg `0.0009` n `20`; unknown avg `0.0541` n `1062`
- 24h: commodity avg `0.1226` n `13`; crypto_alt avg `2.8771` n `235`; crypto_major avg `1.3377` n `8`; equity avg `0.1522` n `143`; fx avg `-0.0212` n `6`; index avg `0.0333` n `26`; metal avg `-0.0009` n `20`; unknown avg `-0.4797` n `898`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1991`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1867`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1572`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1548`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1354`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1322`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1143`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1133`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1069`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0901`, n `668`, weak_sample_signal
