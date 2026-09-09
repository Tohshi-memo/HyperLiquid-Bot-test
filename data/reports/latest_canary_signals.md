# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-09T23:37:30.426146+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.2089` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0021` n `12`; crypto_alt avg `0.2118` n `233`; crypto_major avg `0.1248` n `8`; equity avg `0.0142` n `134`; fx avg `-0.0037` n `6`; index avg `-0.0136` n `26`; metal avg `-0.0386` n `20`; unknown avg `0.5065` n `797`
- 1h: commodity avg `0.0199` n `12`; crypto_alt avg `0.6454` n `233`; crypto_major avg `0.2639` n `8`; equity avg `0.0245` n `134`; fx avg `0.0002` n `6`; index avg `-0.0161` n `26`; metal avg `-0.0123` n `20`; unknown avg `0.0292` n `795`
- 4h: commodity avg `0.1299` n `12`; crypto_alt avg `-1.9343` n `233`; crypto_major avg `-1.2451` n `8`; equity avg `-0.38` n `134`; fx avg `-0.0108` n `6`; index avg `-0.0362` n `26`; metal avg `-0.0055` n `20`; unknown avg `20.0648` n `691`
- 24h: commodity avg `0.1422` n `12`; crypto_alt avg `-2.8104` n `233`; crypto_major avg `-1.8653` n `8`; equity avg `-0.5401` n `134`; fx avg `-0.0119` n `6`; index avg `-0.1386` n `26`; metal avg `0.5104` n `20`; unknown avg `0.956` n `665`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1406`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1246`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1172`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1065`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1057`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1038`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0998`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0984`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0904`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0883`, n `668`, weak_sample_signal
