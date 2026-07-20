# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-20T15:52:27.997773+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0308` n `12`; crypto_alt avg `0.5222` n `230`; crypto_major avg `0.7449` n `8`; equity avg `0.1086` n `98`; fx avg `0.001` n `6`; index avg `0.003` n `25`; metal avg `0.0257` n `20`; unknown avg `-0.0049` n `770`
- 1h: commodity avg `-0.0898` n `12`; crypto_alt avg `1.0476` n `230`; crypto_major avg `1.458` n `8`; equity avg `0.5528` n `98`; fx avg `-0.0481` n `6`; index avg `0.079` n `25`; metal avg `0.0225` n `20`; unknown avg `0.1156` n `770`
- 4h: commodity avg `0.1881` n `12`; crypto_alt avg `0.5947` n `230`; crypto_major avg `0.5949` n `8`; equity avg `-0.533` n `98`; fx avg `-0.0912` n `6`; index avg `-0.0712` n `25`; metal avg `-0.0718` n `20`; unknown avg `-0.1177` n `770`
- 24h: commodity avg `-0.6387` n `12`; crypto_alt avg `1.2959` n `230`; crypto_major avg `1.1982` n `8`; equity avg `0.6226` n `97`; fx avg `-0.1432` n `6`; index avg `0.1779` n `25`; metal avg `0.2388` n `20`; unknown avg `0.1076` n `745`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1508`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1264`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1083`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1035`, n `666`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1002`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0944`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0936`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0848`, n `666`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0847`, n `666`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0787`, n `668`, weak_sample_signal
