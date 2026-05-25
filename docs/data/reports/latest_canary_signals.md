# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-25T09:07:22.906581+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.069` n `12`; crypto_alt avg `0.0478` n `228`; crypto_major avg `0.1232` n `8`; equity avg `0.0519` n `67`; fx avg `-0.0108` n `6`; index avg `0.0335` n `23`; metal avg `0.0197` n `18`; unknown avg `-0.1479` n `397`
- 1h: commodity avg `0.0174` n `12`; crypto_alt avg `0.1714` n `228`; crypto_major avg `0.1176` n `8`; equity avg `0.0282` n `67`; fx avg `-0.0127` n `6`; index avg `0.0643` n `23`; metal avg `0.0067` n `18`; unknown avg `-0.1044` n `397`
- 4h: commodity avg `0.3583` n `12`; crypto_alt avg `0.3869` n `228`; crypto_major avg `0.3026` n `8`; equity avg `0.0615` n `67`; fx avg `0.0796` n `6`; index avg `0.0929` n `23`; metal avg `-0.0448` n `18`; unknown avg `0.2766` n `387`
- 24h: commodity avg `0.0889` n `12`; crypto_alt avg `0.226` n `228`; crypto_major avg `0.1724` n `8`; equity avg `0.5236` n `67`; fx avg `-0.0046` n `6`; index avg `-0.0481` n `23`; metal avg `0.4558` n `18`; unknown avg `-0.3261` n `386`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1392`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1388`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1309`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1261`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1257`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1221`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1208`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1168`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1144`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1143`, n `668`, weak_sample_signal
