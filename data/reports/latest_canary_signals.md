# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-16T05:07:25.950854+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0074` n `12`; crypto_alt avg `0.1163` n `230`; crypto_major avg `0.0995` n `8`; equity avg `0.0527` n `94`; fx avg `-0.0071` n `6`; index avg `0.0114` n `25`; metal avg `-0.0283` n `20`; unknown avg `0.1637` n `768`
- 1h: commodity avg `-0.053` n `12`; crypto_alt avg `0.1032` n `230`; crypto_major avg `0.1371` n `8`; equity avg `-0.089` n `94`; fx avg `-0.0159` n `6`; index avg `-0.0532` n `25`; metal avg `-0.0327` n `20`; unknown avg `0.1146` n `768`
- 4h: commodity avg `-0.1729` n `12`; crypto_alt avg `0.1697` n `230`; crypto_major avg `0.0408` n `8`; equity avg `0.0433` n `94`; fx avg `-0.0645` n `6`; index avg `0.0188` n `25`; metal avg `-0.0257` n `20`; unknown avg `-0.6113` n `768`
- 24h: commodity avg `-0.1105` n `12`; crypto_alt avg `0.396` n `230`; crypto_major avg `0.2658` n `8`; equity avg `-2.2574` n `93`; fx avg `0.0896` n `6`; index avg `-0.4602` n `25`; metal avg `0.0213` n `20`; unknown avg `-0.1882` n `745`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1572`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1222`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1159`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1107`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1089`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1012`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.094`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0884`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0844`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0828`, n `668`, weak_sample_signal
