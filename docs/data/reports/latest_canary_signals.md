# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-17T11:07:25.299592+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0024` n `12`; crypto_alt avg `0.0828` n `230`; crypto_major avg `0.0485` n `8`; equity avg `0.0152` n `114`; fx avg `0.0152` n `6`; index avg `0.0017` n `25`; metal avg `0.0208` n `20`; unknown avg `0.0413` n `792`
- 1h: commodity avg `-0.0953` n `12`; crypto_alt avg `0.3239` n `230`; crypto_major avg `0.4616` n `8`; equity avg `0.1473` n `114`; fx avg `-0.0161` n `6`; index avg `0.0248` n `25`; metal avg `0.065` n `20`; unknown avg `2.0749` n `792`
- 4h: commodity avg `0.1311` n `12`; crypto_alt avg `-0.0905` n `230`; crypto_major avg `0.0701` n `8`; equity avg `0.1614` n `114`; fx avg `0.0027` n `6`; index avg `0.0018` n `25`; metal avg `-0.0201` n `20`; unknown avg `0.0015` n `792`
- 24h: commodity avg `-0.1099` n `12`; crypto_alt avg `0.0686` n `230`; crypto_major avg `1.0189` n `8`; equity avg `1.3343` n `114`; fx avg `-0.0283` n `6`; index avg `0.1554` n `25`; metal avg `0.2092` n `20`; unknown avg `0.1215` n `775`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1678`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1522`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1422`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.138`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1163`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1034`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0904`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0776`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0771`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0757`, n `668`, weak_sample_signal
