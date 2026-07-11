# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-11T11:07:25.413028+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0162` n `12`; crypto_alt avg `0.0251` n `230`; crypto_major avg `0.0474` n `8`; equity avg `-0.0233` n `92`; fx avg `0.0021` n `6`; index avg `-0.0017` n `25`; metal avg `-0.0075` n `20`; unknown avg `-0.1106` n `765`
- 1h: commodity avg `-0.0117` n `12`; crypto_alt avg `0.0624` n `230`; crypto_major avg `0.2271` n `8`; equity avg `0.0254` n `92`; fx avg `-0.0025` n `6`; index avg `-0.0027` n `25`; metal avg `-0.0066` n `20`; unknown avg `-0.1369` n `765`
- 4h: commodity avg `0.0004` n `12`; crypto_alt avg `0.0854` n `230`; crypto_major avg `0.2409` n `8`; equity avg `0.0755` n `92`; fx avg `-0.0047` n `6`; index avg `0.0112` n `25`; metal avg `-0.0038` n `20`; unknown avg `-0.1347` n `759`
- 24h: commodity avg `-0.2708` n `12`; crypto_alt avg `-0.0861` n `229`; crypto_major avg `-0.5723` n `8`; equity avg `-0.4341` n `92`; fx avg `-0.1007` n `6`; index avg `0.0968` n `25`; metal avg `0.1672` n `20`; unknown avg `2.9553` n `727`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1148`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1118`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.105`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1049`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1048`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1027`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1018`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0997`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0902`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0895`, n `668`, weak_sample_signal
