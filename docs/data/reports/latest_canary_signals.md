# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-28T12:07:25.553648+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0252` n `12`; crypto_alt avg `0.1418` n `228`; crypto_major avg `0.1031` n `8`; equity avg `-0.0101` n `88`; fx avg `0.0044` n `6`; index avg `-0.0049` n `23`; metal avg `0.0025` n `20`; unknown avg `0.0108` n `764`
- 1h: commodity avg `0.0839` n `12`; crypto_alt avg `0.2986` n `228`; crypto_major avg `0.2977` n `8`; equity avg `0.0002` n `88`; fx avg `0.0024` n `6`; index avg `0.0124` n `23`; metal avg `-0.0045` n `20`; unknown avg `0.0868` n `764`
- 4h: commodity avg `0.0166` n `12`; crypto_alt avg `0.326` n `228`; crypto_major avg `0.4562` n `8`; equity avg `0.102` n `88`; fx avg `0.0136` n `6`; index avg `0.0331` n `23`; metal avg `0.01` n `20`; unknown avg `2.2756` n `750`
- 24h: commodity avg `0.1624` n `12`; crypto_alt avg `0.1025` n `228`; crypto_major avg `-0.3189` n `8`; equity avg `0.0901` n `88`; fx avg `0.0045` n `6`; index avg `-0.0478` n `23`; metal avg `-0.0219` n `20`; unknown avg `15.6792` n `690`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2091`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1871`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1368`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1258`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1078`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1003`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0928`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0889`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0849`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0833`, n `668`, weak_sample_signal
