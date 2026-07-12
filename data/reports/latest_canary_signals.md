# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-12T03:52:29.603602+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.2` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0021` n `12`; crypto_alt avg `0.0262` n `230`; crypto_major avg `0.0316` n `8`; equity avg `0.0136` n `92`; fx avg `-0.0031` n `6`; index avg `0.0114` n `25`; metal avg `-0.0009` n `20`; unknown avg `-0.3491` n `765`
- 1h: commodity avg `-0.0548` n `12`; crypto_alt avg `0.3158` n `230`; crypto_major avg `0.1337` n `8`; equity avg `0.0439` n `92`; fx avg `-0.0006` n `6`; index avg `-0.0113` n `25`; metal avg `0.0072` n `20`; unknown avg `-0.4202` n `765`
- 4h: commodity avg `0.0114` n `12`; crypto_alt avg `0.582` n `230`; crypto_major avg `0.138` n `8`; equity avg `0.0423` n `92`; fx avg `-0.0022` n `6`; index avg `-0.0398` n `25`; metal avg `-0.0265` n `20`; unknown avg `-0.0382` n `765`
- 24h: commodity avg `0.3688` n `12`; crypto_alt avg `-0.422` n `229`; crypto_major avg `-0.3014` n `8`; equity avg `0.095` n `92`; fx avg `0.0168` n `6`; index avg `-0.1096` n `25`; metal avg `-0.088` n `20`; unknown avg `-0.0278` n `729`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1771`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1572`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1411`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1309`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1247`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1231`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1164`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1114`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1022`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0992`, n `668`, weak_sample_signal
