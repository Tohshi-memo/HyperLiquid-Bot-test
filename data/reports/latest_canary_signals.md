# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-14T06:22:29.987369+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0588` n `12`; crypto_alt avg `0.0909` n `230`; crypto_major avg `0.0577` n `8`; equity avg `-0.0358` n `92`; fx avg `0.0225` n `6`; index avg `-0.0167` n `25`; metal avg `-0.0188` n `20`; unknown avg `0.3235` n `766`
- 1h: commodity avg `-0.0046` n `12`; crypto_alt avg `0.0819` n `230`; crypto_major avg `-0.1214` n `8`; equity avg `0.0885` n `92`; fx avg `0.0299` n `6`; index avg `0.0015` n `25`; metal avg `0.0441` n `20`; unknown avg `0.0202` n `750`
- 4h: commodity avg `0.1112` n `12`; crypto_alt avg `0.5375` n `230`; crypto_major avg `0.4056` n `8`; equity avg `0.9217` n `92`; fx avg `-0.0088` n `6`; index avg `0.256` n `25`; metal avg `0.2046` n `20`; unknown avg `0.0626` n `750`
- 24h: commodity avg `1.0068` n `12`; crypto_alt avg `-0.3482` n `230`; crypto_major avg `-0.378` n `8`; equity avg `-0.1975` n `92`; fx avg `-0.1622` n `6`; index avg `0.0321` n `25`; metal avg `0.1705` n `20`; unknown avg `-0.0557` n `750`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1785`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.162`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1119`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1112`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1089`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.103`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1016`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0954`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0929`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.091`, n `668`, weak_sample_signal
