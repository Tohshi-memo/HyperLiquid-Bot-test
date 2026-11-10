# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-10T11:52:27.190584+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0493` n `13`; crypto_alt avg `0.0517` n `239`; crypto_major avg `0.0395` n `8`; equity avg `0.0963` n `160`; fx avg `-0.0105` n `6`; index avg `0.0078` n `27`; metal avg `-0.0352` n `20`; unknown avg `0.0372` n `1264`
- 1h: commodity avg `0.0443` n `13`; crypto_alt avg `0.0856` n `239`; crypto_major avg `0.0866` n `8`; equity avg `-0.0244` n `160`; fx avg `-0.0126` n `6`; index avg `0.0078` n `27`; metal avg `-0.0639` n `20`; unknown avg `18.9087` n `1256`
- 4h: commodity avg `-0.0514` n `13`; crypto_alt avg `-0.4398` n `239`; crypto_major avg `-1.0251` n `8`; equity avg `-0.4334` n `160`; fx avg `-0.0087` n `6`; index avg `-0.045` n `27`; metal avg `-0.2115` n `20`; unknown avg `19.2416` n `1219`
- 24h: commodity avg `-0.1747` n `13`; crypto_alt avg `0.5976` n `239`; crypto_major avg `-0.0166` n `8`; equity avg `3.679` n `160`; fx avg `-0.0165` n `6`; index avg `0.4017` n `27`; metal avg `-0.1422` n `20`; unknown avg `5.0405` n `1159`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.235`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1592`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1457`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1335`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.13`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1204`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1187`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1165`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1052`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1041`, n `668`, weak_sample_signal
