# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-19T23:52:25.800783+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0063` n `12`; crypto_alt avg `0.0282` n `230`; crypto_major avg `0.0141` n `8`; equity avg `-0.0405` n `98`; fx avg `-0.001` n `6`; index avg `-0.0609` n `25`; metal avg `0.0154` n `20`; unknown avg `-0.1204` n `767`
- 1h: commodity avg `-0.0606` n `12`; crypto_alt avg `-0.1975` n `230`; crypto_major avg `0.0364` n `8`; equity avg `-0.0999` n `98`; fx avg `0.0043` n `6`; index avg `-0.0283` n `25`; metal avg `-0.0163` n `20`; unknown avg `0.787` n `767`
- 4h: commodity avg `-0.0039` n `12`; crypto_alt avg `0.2067` n `230`; crypto_major avg `0.3015` n `8`; equity avg `0.1588` n `98`; fx avg `0.0167` n `6`; index avg `0.0166` n `25`; metal avg `-0.1351` n `20`; unknown avg `0.0051` n `767`
- 24h: commodity avg `-0.0435` n `12`; crypto_alt avg `-0.1133` n `230`; crypto_major avg `0.3403` n `8`; equity avg `0.4901` n `97`; fx avg `0.0882` n `6`; index avg `-0.0299` n `25`; metal avg `-0.1044` n `20`; unknown avg `0.0368` n `749`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `0.1479`, n `666`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1458`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1383`, n `666`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1276`, n `666`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1264`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1238`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1162`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1073`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0984`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0966`, n `666`, weak_sample_signal
