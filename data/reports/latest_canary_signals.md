# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-30T09:52:32.239242+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.002` n `12`; crypto_alt avg `0.0931` n `228`; crypto_major avg `0.084` n `8`; equity avg `0.0791` n `88`; fx avg `0.0001` n `6`; index avg `0.0125` n `23`; metal avg `0.1081` n `20`; unknown avg `0.0069` n `765`
- 1h: commodity avg `0.0379` n `12`; crypto_alt avg `0.1724` n `228`; crypto_major avg `0.1733` n `8`; equity avg `0.1526` n `88`; fx avg `-0.0141` n `6`; index avg `-0.0092` n `23`; metal avg `0.1261` n `20`; unknown avg `-0.1032` n `765`
- 4h: commodity avg `0.2507` n `12`; crypto_alt avg `-0.39` n `228`; crypto_major avg `-0.3332` n `8`; equity avg `-0.3642` n `88`; fx avg `0.0439` n `6`; index avg `-0.1164` n `23`; metal avg `0.5669` n `20`; unknown avg `-0.3734` n `739`
- 24h: commodity avg `-0.0311` n `12`; crypto_alt avg `-0.7584` n `228`; crypto_major avg `0.4877` n `8`; equity avg `1.4011` n `88`; fx avg `0.1224` n `6`; index avg `0.1141` n `23`; metal avg `0.2641` n `20`; unknown avg `9.23` n `734`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1157`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0869`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0855`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0809`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0799`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.065`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.06`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.056`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0537`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0536`, n `668`, weak_sample_signal
