# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-06T23:22:28.516771+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0015` n `12`; crypto_alt avg `-0.1401` n `230`; crypto_major avg `-0.2442` n `8`; equity avg `0.0819` n `112`; fx avg `-0.0018` n `6`; index avg `-0.0045` n `25`; metal avg `0.0215` n `20`; unknown avg `-0.1316` n `782`
- 1h: commodity avg `0.0002` n `12`; crypto_alt avg `-0.1472` n `230`; crypto_major avg `-0.1755` n `8`; equity avg `0.0449` n `112`; fx avg `-0.0095` n `6`; index avg `-0.0162` n `25`; metal avg `0.0422` n `20`; unknown avg `-0.129` n `782`
- 4h: commodity avg `0.0718` n `12`; crypto_alt avg `-0.1372` n `230`; crypto_major avg `-0.2286` n `8`; equity avg `0.2795` n `112`; fx avg `-0.0014` n `6`; index avg `0.0099` n `25`; metal avg `-0.0032` n `20`; unknown avg `-0.0847` n `781`
- 24h: commodity avg `0.638` n `12`; crypto_alt avg `-0.0016` n `230`; crypto_major avg `-1.2645` n `8`; equity avg `0.4041` n `109`; fx avg `0.0184` n `6`; index avg `-0.1741` n `25`; metal avg `-0.1023` n `20`; unknown avg `113.055` n `749`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.122`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1154`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1093`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1082`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0988`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0956`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0937`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0849`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0748`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0737`, n `668`, weak_sample_signal
