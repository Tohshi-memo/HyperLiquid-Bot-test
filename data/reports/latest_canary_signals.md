# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-13T16:24:40.348274+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0033` n `13`; crypto_alt avg `0.2436` n `235`; crypto_major avg `0.0898` n `8`; equity avg `0.2223` n `151`; fx avg `-0.0005` n `6`; index avg `0.023` n `26`; metal avg `-0.0017` n `20`; unknown avg `0.3198` n `1135`
- 1h: commodity avg `0.0713` n `13`; crypto_alt avg `-0.0715` n `235`; crypto_major avg `-0.0874` n `8`; equity avg `0.3958` n `151`; fx avg `-0.0118` n `6`; index avg `0.043` n `26`; metal avg `-0.0913` n `20`; unknown avg `0.8099` n `1127`
- 4h: commodity avg `0.7397` n `13`; crypto_alt avg `1.2882` n `235`; crypto_major avg `0.9072` n `8`; equity avg `0.5985` n `151`; fx avg `0.0313` n `6`; index avg `0.0422` n `26`; metal avg `-0.2765` n `20`; unknown avg `0.7589` n `1091`
- 24h: commodity avg `0.4191` n `13`; crypto_alt avg `-2.0959` n `235`; crypto_major avg `-0.8035` n `8`; equity avg `-1.2394` n `151`; fx avg `0.1531` n `6`; index avg `-0.2508` n `26`; metal avg `-0.2713` n `20`; unknown avg `0.1554` n `1006`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1624`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1478`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1289`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1259`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1079`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1`, n `666`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0927`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0926`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0856`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0828`, n `668`, weak_sample_signal
