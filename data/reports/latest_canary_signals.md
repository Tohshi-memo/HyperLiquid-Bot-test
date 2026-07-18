# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-18T15:37:27.014544+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0306` n `12`; crypto_alt avg `-0.1961` n `230`; crypto_major avg `-0.0131` n `8`; equity avg `-0.0404` n `96`; fx avg `-0.0005` n `6`; index avg `-0.0005` n `25`; metal avg `-0.0159` n `20`; unknown avg `-0.02` n `770`
- 1h: commodity avg `0.0091` n `12`; crypto_alt avg `-0.0618` n `230`; crypto_major avg `-0.0526` n `8`; equity avg `-0.04` n `96`; fx avg `-0.0067` n `6`; index avg `0.0024` n `25`; metal avg `-0.0068` n `20`; unknown avg `-0.0188` n `770`
- 4h: commodity avg `-0.031` n `12`; crypto_alt avg `-0.1224` n `230`; crypto_major avg `0.109` n `8`; equity avg `-0.1367` n `96`; fx avg `-0.0057` n `6`; index avg `-0.0316` n `25`; metal avg `-0.0507` n `20`; unknown avg `-0.0348` n `770`
- 24h: commodity avg `0.4654` n `12`; crypto_alt avg `-0.6023` n `230`; crypto_major avg `0.3971` n `8`; equity avg `-0.0773` n `96`; fx avg `-0.0524` n `6`; index avg `0.0066` n `25`; metal avg `0.0273` n `20`; unknown avg `0.0556` n `737`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1332`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1122`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0983`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0973`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0911`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0896`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0881`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0849`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0839`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0812`, n `668`, weak_sample_signal
