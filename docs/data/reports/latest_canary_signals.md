# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-17T08:52:28.417348+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0004` n `13`; crypto_alt avg `0.1001` n `236`; crypto_major avg `0.0152` n `8`; equity avg `0.0346` n `151`; fx avg `-0.0002` n `6`; index avg `-0.0074` n `26`; metal avg `0.0048` n `20`; unknown avg `0.0336` n `1193`
- 1h: commodity avg `0.0525` n `13`; crypto_alt avg `-0.0251` n `236`; crypto_major avg `-0.0671` n `8`; equity avg `0.0261` n `151`; fx avg `-0.0139` n `6`; index avg `0.0033` n `26`; metal avg `0.0037` n `20`; unknown avg `-0.0075` n `1175`
- 4h: commodity avg `-0.1903` n `13`; crypto_alt avg `-0.3916` n `236`; crypto_major avg `0.1592` n `8`; equity avg `0.0693` n `151`; fx avg `-0.013` n `6`; index avg `0.0273` n `26`; metal avg `0.0022` n `20`; unknown avg `0.0291` n `1157`
- 24h: commodity avg `0.5035` n `13`; crypto_alt avg `-2.1571` n `236`; crypto_major avg `-1.4884` n `8`; equity avg `-3.8751` n `151`; fx avg `0.0138` n `6`; index avg `-0.5937` n `26`; metal avg `-0.2545` n `20`; unknown avg `8.7193` n `954`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1815`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1445`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1236`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1225`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1017`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0999`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0786`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0751`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0741`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0741`, n `666`, weak_sample_signal
