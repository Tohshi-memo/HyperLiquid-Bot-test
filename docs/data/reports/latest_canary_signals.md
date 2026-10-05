# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-05T22:37:53.963833+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0045` n `13`; crypto_alt avg `-0.1536` n `235`; crypto_major avg `-0.1617` n `8`; equity avg `-0.0134` n `144`; fx avg `-0.0099` n `6`; index avg `-0.0093` n `26`; metal avg `0.0032` n `20`; unknown avg `0.1698` n `1079`
- 1h: commodity avg `0.0276` n `13`; crypto_alt avg `-0.0154` n `235`; crypto_major avg `0.1496` n `8`; equity avg `0.0389` n `144`; fx avg `0.0243` n `6`; index avg `-0.0213` n `26`; metal avg `0.0329` n `20`; unknown avg `-0.1572` n `1053`
- 4h: commodity avg `0.0111` n `13`; crypto_alt avg `0.8746` n `235`; crypto_major avg `0.6621` n `8`; equity avg `0.1759` n `144`; fx avg `0.0125` n `6`; index avg `0.0038` n `26`; metal avg `0.0275` n `20`; unknown avg `-0.1174` n `979`
- 24h: commodity avg `-0.237` n `13`; crypto_alt avg `0.6294` n `235`; crypto_major avg `0.0994` n `8`; equity avg `0.2737` n `144`; fx avg `-0.0773` n `6`; index avg `0.1038` n `26`; metal avg `0.1201` n `20`; unknown avg `630.2963` n `794`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1975`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1786`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1704`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1275`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1039`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0987`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0973`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0956`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0953`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.094`, n `668`, weak_sample_signal
