# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-12T21:22:26.745302+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0204` n `12`; crypto_alt avg `-0.2316` n `230`; crypto_major avg `-0.2729` n `8`; equity avg `-0.0209` n `92`; fx avg `0.0039` n `6`; index avg `-0.0055` n `25`; metal avg `-0.0072` n `20`; unknown avg `0.1445` n `765`
- 1h: commodity avg `0.0305` n `12`; crypto_alt avg `-0.2139` n `230`; crypto_major avg `-0.2814` n `8`; equity avg `-0.049` n `92`; fx avg `-0.0358` n `6`; index avg `-0.0171` n `25`; metal avg `-0.0054` n `20`; unknown avg `0.06` n `765`
- 4h: commodity avg `0.0781` n `12`; crypto_alt avg `-0.201` n `230`; crypto_major avg `-0.2312` n `8`; equity avg `0.0243` n `92`; fx avg `-0.0589` n `6`; index avg `-0.019` n `25`; metal avg `-0.0056` n `20`; unknown avg `-0.0456` n `765`
- 24h: commodity avg `0.6343` n `12`; crypto_alt avg `-1.6693` n `230`; crypto_major avg `-0.9705` n `8`; equity avg `-0.2338` n `92`; fx avg `-0.0382` n `6`; index avg `-0.0959` n `25`; metal avg `-0.1009` n `20`; unknown avg `0.2168` n `741`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1761`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1609`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1281`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1268`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1207`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1057`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1008`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1001`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0994`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0951`, n `668`, weak_sample_signal
