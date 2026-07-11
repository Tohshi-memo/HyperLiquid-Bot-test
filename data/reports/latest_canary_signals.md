# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-11T10:07:25.667189+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0029` n `12`; crypto_alt avg `-0.101` n `230`; crypto_major avg `-0.0556` n `8`; equity avg `-0.0174` n `92`; fx avg `-0.0078` n `6`; index avg `-0.0008` n `25`; metal avg `-0.002` n `20`; unknown avg `-0.0449` n `765`
- 1h: commodity avg `-0.0055` n `12`; crypto_alt avg `-0.1778` n `230`; crypto_major avg `-0.2113` n `8`; equity avg `0.0389` n `92`; fx avg `0.0012` n `6`; index avg `0.0088` n `25`; metal avg `-0.0017` n `20`; unknown avg `-0.0553` n `761`
- 4h: commodity avg `0.0596` n `12`; crypto_alt avg `0.0971` n `230`; crypto_major avg `0.0474` n `8`; equity avg `0.1363` n `92`; fx avg `-0.0142` n `6`; index avg `0.0334` n `25`; metal avg `-0.0012` n `20`; unknown avg `-0.0215` n `759`
- 24h: commodity avg `-0.2216` n `12`; crypto_alt avg `0.0057` n `229`; crypto_major avg `-0.7303` n `8`; equity avg `-0.1311` n `92`; fx avg `-0.0744` n `6`; index avg `0.1351` n `25`; metal avg `0.1495` n `20`; unknown avg `2.9508` n `727`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1144`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1118`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1063`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.105`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.104`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1029`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1018`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0994`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0894`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0892`, n `668`, weak_sample_signal
