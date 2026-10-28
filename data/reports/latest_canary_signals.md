# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-28T12:22:27.882159+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.45` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0355` n `13`; crypto_alt avg `-0.4249` n `238`; crypto_major avg `-0.3052` n `8`; equity avg `-0.0291` n `154`; fx avg `0.0048` n `6`; index avg `0.0244` n `27`; metal avg `0.0597` n `20`; unknown avg `1.3234` n `1237`
- 1h: commodity avg `-0.0492` n `13`; crypto_alt avg `-0.6874` n `238`; crypto_major avg `-0.6033` n `8`; equity avg `-0.188` n `154`; fx avg `0.0585` n `6`; index avg `0.0231` n `27`; metal avg `0.1135` n `20`; unknown avg `0.6512` n `1227`
- 4h: commodity avg `0.0836` n `13`; crypto_alt avg `-0.426` n `238`; crypto_major avg `-0.3586` n `8`; equity avg `-0.1174` n `154`; fx avg `0.0727` n `6`; index avg `0.031` n `27`; metal avg `0.036` n `20`; unknown avg `89.248` n `1196`
- 24h: commodity avg `0.1535` n `13`; crypto_alt avg `1.1699` n `238`; crypto_major avg `1.3811` n `8`; equity avg `2.6089` n `154`; fx avg `0.1433` n `6`; index avg `0.3667` n `27`; metal avg `0.3119` n `20`; unknown avg `7.8038` n `1068`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1499`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1442`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1378`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0944`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0882`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0825`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.074`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0679`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0678`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0655`, n `668`, weak_sample_signal
