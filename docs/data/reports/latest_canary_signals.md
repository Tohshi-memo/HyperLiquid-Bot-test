# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-31T05:07:22.057869+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0022` n `12`; crypto_alt avg `0.1964` n `230`; crypto_major avg `0.2356` n `8`; equity avg `0.1784` n `102`; fx avg `-0.0345` n `6`; index avg `0.0187` n `25`; metal avg `0.0405` n `20`; unknown avg `4.1194` n `779`
- 1h: commodity avg `-0.0703` n `12`; crypto_alt avg `-0.0381` n `230`; crypto_major avg `0.1771` n `8`; equity avg `0.6737` n `102`; fx avg `-0.0143` n `6`; index avg `0.1134` n `25`; metal avg `0.1038` n `20`; unknown avg `0.822` n `779`
- 4h: commodity avg `-0.1078` n `12`; crypto_alt avg `-0.7476` n `230`; crypto_major avg `-0.6364` n `8`; equity avg `-0.132` n `102`; fx avg `0.0101` n `6`; index avg `-0.0862` n `25`; metal avg `-0.0284` n `20`; unknown avg `0.6431` n `779`
- 24h: commodity avg `-0.3422` n `12`; crypto_alt avg `0.286` n `230`; crypto_major avg `1.2135` n `8`; equity avg `9.5397` n `102`; fx avg `-0.0985` n `6`; index avg `1.2928` n `25`; metal avg `0.7426` n `20`; unknown avg `0.1036` n `739`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1374`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.127`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.096`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0934`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0907`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.085`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0809`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0783`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0714`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0664`, n `668`, weak_sample_signal
