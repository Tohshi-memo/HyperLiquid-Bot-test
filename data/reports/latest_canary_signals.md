# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-07T05:22:30.627944+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0099` n `12`; crypto_alt avg `0.1189` n `230`; crypto_major avg `-0.0481` n `8`; equity avg `0.07` n `112`; fx avg `0.019` n `6`; index avg `0.0263` n `25`; metal avg `0.0496` n `20`; unknown avg `-0.2037` n `782`
- 1h: commodity avg `-0.0204` n `12`; crypto_alt avg `0.0374` n `230`; crypto_major avg `-0.2771` n `8`; equity avg `0.1228` n `112`; fx avg `0.0099` n `6`; index avg `0.0297` n `25`; metal avg `-0.0021` n `20`; unknown avg `-0.4284` n `782`
- 4h: commodity avg `0.1362` n `12`; crypto_alt avg `-0.2485` n `230`; crypto_major avg `-0.5745` n `8`; equity avg `0.8803` n `112`; fx avg `0.0012` n `6`; index avg `0.0983` n `25`; metal avg `0.1493` n `20`; unknown avg `-0.6213` n `782`
- 24h: commodity avg `0.7764` n `12`; crypto_alt avg `0.0559` n `230`; crypto_major avg `-1.6081` n `8`; equity avg `0.7074` n `109`; fx avg `0.0422` n `6`; index avg `-0.0907` n `25`; metal avg `0.0651` n `20`; unknown avg `113.1878` n `749`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1655`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1269`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.124`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1148`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1071`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0823`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.078`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0779`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.072`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0672`, n `668`, weak_sample_signal
