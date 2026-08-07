# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-07T03:37:19.008955+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0307` n `12`; crypto_alt avg `0.0998` n `230`; crypto_major avg `0.0085` n `8`; equity avg `0.0571` n `112`; fx avg `-0.001` n `6`; index avg `0.0318` n `25`; metal avg `0.0285` n `20`; unknown avg `-0.0489` n `782`
- 1h: commodity avg `0.0076` n `12`; crypto_alt avg `-0.1789` n `230`; crypto_major avg `0.0125` n `8`; equity avg `0.1379` n `112`; fx avg `0.0209` n `6`; index avg `0.0374` n `25`; metal avg `0.0222` n `20`; unknown avg `-0.2762` n `782`
- 4h: commodity avg `0.001` n `12`; crypto_alt avg `0.278` n `230`; crypto_major avg `0.0617` n `8`; equity avg `0.097` n `112`; fx avg `-0.0232` n `6`; index avg `-0.1243` n `25`; metal avg `0.1015` n `20`; unknown avg `-0.1078` n `782`
- 24h: commodity avg `0.6223` n `12`; crypto_alt avg `0.5392` n `230`; crypto_major avg `-0.5777` n `8`; equity avg `0.84` n `109`; fx avg `0.0424` n `6`; index avg `-0.1083` n `25`; metal avg `-0.0406` n `20`; unknown avg `113.2126` n `749`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1587`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.126`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1184`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1102`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1095`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0971`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0969`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0848`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0785`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0737`, n `668`, weak_sample_signal
