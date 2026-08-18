# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-18T01:07:26.693545+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0087` n `12`; crypto_alt avg `-0.0129` n `230`; crypto_major avg `-0.0948` n `8`; equity avg `-0.0968` n `114`; fx avg `-0.0195` n `6`; index avg `-0.0276` n `25`; metal avg `0.0329` n `20`; unknown avg `0.0582` n `793`
- 1h: commodity avg `-0.0164` n `12`; crypto_alt avg `0.0516` n `230`; crypto_major avg `-0.081` n `8`; equity avg `0.0157` n `114`; fx avg `-0.0332` n `6`; index avg `0.0383` n `25`; metal avg `0.0904` n `20`; unknown avg `0.0014` n `793`
- 4h: commodity avg `-0.0103` n `12`; crypto_alt avg `-0.2314` n `230`; crypto_major avg `0.083` n `8`; equity avg `0.1206` n `114`; fx avg `-0.06` n `6`; index avg `0.0031` n `25`; metal avg `0.1314` n `20`; unknown avg `-0.1506` n `792`
- 24h: commodity avg `0.6284` n `12`; crypto_alt avg `0.1072` n `230`; crypto_major avg `0.9797` n `8`; equity avg `1.0154` n `114`; fx avg `0.0191` n `6`; index avg `0.0372` n `25`; metal avg `0.0791` n `20`; unknown avg `0.2288` n `776`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.2149`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.166`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.156`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1473`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1378`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1279`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1194`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1024`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0996`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0845`, n `668`, weak_sample_signal
