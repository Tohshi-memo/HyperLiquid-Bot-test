# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-12T10:22:24.659514+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0352` n `13`; crypto_alt avg `-0.1833` n `235`; crypto_major avg `-0.0704` n `8`; equity avg `-0.0609` n `151`; fx avg `0.0018` n `6`; index avg `-0.0256` n `26`; metal avg `-0.0086` n `20`; unknown avg `-0.0812` n `1133`
- 1h: commodity avg `0.0528` n `13`; crypto_alt avg `-0.3891` n `235`; crypto_major avg `-0.1153` n `8`; equity avg `-0.042` n `151`; fx avg `0.0097` n `6`; index avg `-0.036` n `26`; metal avg `0.0265` n `20`; unknown avg `-0.1847` n `1105`
- 4h: commodity avg `0.2388` n `13`; crypto_alt avg `-0.7264` n `235`; crypto_major avg `-0.3164` n `8`; equity avg `-0.4971` n `151`; fx avg `-0.0487` n `6`; index avg `-0.0917` n `26`; metal avg `-0.0047` n `20`; unknown avg `0.1407` n `997`
- 24h: commodity avg `-0.0777` n `13`; crypto_alt avg `1.6691` n `235`; crypto_major avg `1.2046` n `8`; equity avg `-1.103` n `151`; fx avg `-0.1122` n `6`; index avg `-0.1501` n `26`; metal avg `0.0354` n `20`; unknown avg `0.011` n `838`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.218`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1839`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1123`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1107`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1009`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0909`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0864`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0864`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.085`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0816`, n `668`, weak_sample_signal
