# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-13T00:07:29.321911+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0376` n `12`; crypto_alt avg `0.3612` n `230`; crypto_major avg `0.3934` n `8`; equity avg `0.2163` n `92`; fx avg `0.014` n `6`; index avg `0.0292` n `25`; metal avg `0.0848` n `20`; unknown avg `-0.0882` n `766`
- 1h: commodity avg `0.0219` n `12`; crypto_alt avg `0.3552` n `230`; crypto_major avg `0.4263` n `8`; equity avg `0.087` n `92`; fx avg `0.0247` n `6`; index avg `0.0277` n `25`; metal avg `0.1468` n `20`; unknown avg `-0.0803` n `766`
- 4h: commodity avg `-0.1708` n `12`; crypto_alt avg `-0.5666` n `230`; crypto_major avg `-0.4299` n `8`; equity avg `-0.2808` n `92`; fx avg `-0.0294` n `6`; index avg `-0.0748` n `25`; metal avg `-0.1148` n `20`; unknown avg `-0.0528` n `765`
- 24h: commodity avg `-0.0819` n `12`; crypto_alt avg `0.2263` n `230`; crypto_major avg `0.7733` n `8`; equity avg `-0.1803` n `92`; fx avg `-0.0454` n `6`; index avg `-0.0692` n `25`; metal avg `-0.1907` n `20`; unknown avg `0.3885` n `741`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1733`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1587`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.117`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1168`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1156`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0982`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0966`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0941`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0921`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0914`, n `668`, weak_sample_signal
