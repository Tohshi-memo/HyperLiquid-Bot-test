# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-28T02:52:31.233823+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1027` n `12`; crypto_alt avg `-0.0267` n `230`; crypto_major avg `-0.1272` n `8`; equity avg `-0.0724` n `102`; fx avg `-0.0199` n `6`; index avg `-0.0109` n `25`; metal avg `-0.0181` n `20`; unknown avg `0.1132` n `774`
- 1h: commodity avg `-0.2247` n `12`; crypto_alt avg `0.3122` n `230`; crypto_major avg `-0.0651` n `8`; equity avg `-0.299` n `102`; fx avg `-0.0763` n `6`; index avg `-0.053` n `25`; metal avg `-0.001` n `20`; unknown avg `0.1189` n `774`
- 4h: commodity avg `-0.2877` n `12`; crypto_alt avg `-0.586` n `230`; crypto_major avg `-0.9422` n `8`; equity avg `-1.67` n `102`; fx avg `-0.0103` n `6`; index avg `-0.3506` n `25`; metal avg `-0.3268` n `20`; unknown avg `0.2654` n `774`
- 24h: commodity avg `-1.0436` n `12`; crypto_alt avg `-3.8851` n `230`; crypto_major avg `-3.2859` n `8`; equity avg `-3.2754` n `102`; fx avg `-0.1491` n `6`; index avg `-0.6983` n `25`; metal avg `-0.3261` n `20`; unknown avg `1161.8639` n `757`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1841`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1398`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1368`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1329`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1313`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1303`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1177`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1128`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1079`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1064`, n `668`, weak_sample_signal
