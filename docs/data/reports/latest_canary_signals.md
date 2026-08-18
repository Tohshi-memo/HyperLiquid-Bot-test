# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-18T14:01:20.541858+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0141` n `12`; crypto_alt avg `0.0107` n `230`; crypto_major avg `0.0409` n `8`; equity avg `-0.034` n `114`; fx avg `0.0008` n `6`; index avg `0.0029` n `25`; metal avg `0.0504` n `20`; unknown avg `0.1` n `795`
- 1h: commodity avg `0.0112` n `12`; crypto_alt avg `-0.1743` n `230`; crypto_major avg `-0.0014` n `8`; equity avg `-0.4952` n `114`; fx avg `0.0245` n `6`; index avg `-0.0561` n `25`; metal avg `-0.0328` n `20`; unknown avg `-0.0613` n `795`
- 4h: commodity avg `0.1275` n `12`; crypto_alt avg `-0.003` n `230`; crypto_major avg `-0.0204` n `8`; equity avg `-0.5618` n `114`; fx avg `0.027` n `6`; index avg `-0.0499` n `25`; metal avg `-0.0715` n `20`; unknown avg `0.05` n `795`
- 24h: commodity avg `0.596` n `12`; crypto_alt avg `-0.7705` n `230`; crypto_major avg `0.0389` n `8`; equity avg `-3.0663` n `114`; fx avg `-0.0363` n `6`; index avg `-0.5858` n `25`; metal avg `-0.2951` n `20`; unknown avg `-0.1251` n `760`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1327`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1282`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1171`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0921`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0912`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0791`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0753`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0721`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0705`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0703`, n `668`, weak_sample_signal
