# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-07T16:37:32.807720+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0366` n `13`; crypto_alt avg `-0.1122` n `235`; crypto_major avg `-0.1822` n `8`; equity avg `-0.0899` n `150`; fx avg `-0.0036` n `6`; index avg `-0.0165` n `26`; metal avg `-0.0234` n `20`; unknown avg `0.3639` n `1076`
- 1h: commodity avg `-0.1887` n `13`; crypto_alt avg `0.5849` n `235`; crypto_major avg `0.1173` n `8`; equity avg `-0.0375` n `150`; fx avg `0.0003` n `6`; index avg `0.0094` n `26`; metal avg `-0.0157` n `20`; unknown avg `-0.0931` n `1068`
- 4h: commodity avg `-0.1971` n `13`; crypto_alt avg `-0.012` n `235`; crypto_major avg `-0.3404` n `8`; equity avg `0.1` n `150`; fx avg `0.0215` n `6`; index avg `0.0221` n `26`; metal avg `0.2485` n `20`; unknown avg `0.161` n `1022`
- 24h: commodity avg `0.7053` n `13`; crypto_alt avg `-4.6829` n `235`; crypto_major avg `-3.2527` n `8`; equity avg `-1.7278` n `150`; fx avg `-0.1662` n `6`; index avg `-0.3103` n `26`; metal avg `-0.5681` n `20`; unknown avg `15.4771` n `988`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.143`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1387`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1365`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0872`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0863`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0789`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0762`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.073`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.071`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0699`, n `668`, weak_sample_signal
