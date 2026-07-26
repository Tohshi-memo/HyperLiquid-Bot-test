# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-26T03:22:26.310234+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0259` n `12`; crypto_alt avg `0.1093` n `230`; crypto_major avg `0.0782` n `8`; equity avg `0.0366` n `100`; fx avg `0.0111` n `6`; index avg `0.0007` n `25`; metal avg `0.0013` n `20`; unknown avg `-0.0885` n `774`
- 1h: commodity avg `-0.0628` n `12`; crypto_alt avg `0.1892` n `230`; crypto_major avg `0.0445` n `8`; equity avg `0.0345` n `100`; fx avg `0.0108` n `6`; index avg `0.0021` n `25`; metal avg `-0.0011` n `20`; unknown avg `-0.1391` n `774`
- 4h: commodity avg `-0.0138` n `12`; crypto_alt avg `0.4298` n `230`; crypto_major avg `0.3985` n `8`; equity avg `0.2198` n `100`; fx avg `0.0056` n `6`; index avg `0.0375` n `25`; metal avg `0.0146` n `20`; unknown avg `-0.2899` n `774`
- 24h: commodity avg `-0.4682` n `12`; crypto_alt avg `0.8587` n `230`; crypto_major avg `1.3233` n `8`; equity avg `0.4582` n `100`; fx avg `0.0096` n `6`; index avg `0.1353` n `25`; metal avg `0.0346` n `20`; unknown avg `-0.215` n `758`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1831`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1724`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1544`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1378`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1321`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1271`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1235`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1214`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1186`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1179`, n `666`, weak_sample_signal
