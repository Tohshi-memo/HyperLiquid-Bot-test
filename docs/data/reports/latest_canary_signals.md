# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-05T21:22:14.795037+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0021` n `12`; crypto_alt avg `-0.071` n `230`; crypto_major avg `-0.0596` n `8`; equity avg `-0.1431` n `108`; fx avg `0.001` n `6`; index avg `-0.0213` n `25`; metal avg `-0.0049` n `20`; unknown avg `-0.0111` n `782`
- 1h: commodity avg `0.075` n `12`; crypto_alt avg `-0.133` n `230`; crypto_major avg `-0.2657` n `8`; equity avg `-0.1933` n `108`; fx avg `0.0009` n `6`; index avg `-0.0141` n `25`; metal avg `0.0209` n `20`; unknown avg `0.0977` n `782`
- 4h: commodity avg `0.1388` n `12`; crypto_alt avg `-0.0173` n `230`; crypto_major avg `0.0379` n `8`; equity avg `-1.0034` n `108`; fx avg `0.0044` n `6`; index avg `-0.08` n `25`; metal avg `0.0506` n `20`; unknown avg `-0.1191` n `782`
- 24h: commodity avg `0.0267` n `12`; crypto_alt avg `0.4509` n `230`; crypto_major avg `0.6746` n `8`; equity avg `-0.7622` n `108`; fx avg `-0.0454` n `6`; index avg `-0.1092` n `25`; metal avg `0.8088` n `20`; unknown avg `0.7173` n `749`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1602`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.143`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1188`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1073`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1009`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0895`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0828`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0685`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.068`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0673`, n `668`, weak_sample_signal
