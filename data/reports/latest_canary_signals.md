# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-26T08:52:32.297643+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.086` n `13`; crypto_alt avg `0.0852` n `239`; crypto_major avg `0.2405` n `8`; equity avg `0.344` n `168`; fx avg `0.0081` n `6`; index avg `0.0302` n `27`; metal avg `0.1217` n `20`; unknown avg `42.2656` n `1267`
- 1h: commodity avg `-0.0311` n `13`; crypto_alt avg `0.2592` n `239`; crypto_major avg `0.4116` n `8`; equity avg `0.2279` n `168`; fx avg `0.0167` n `6`; index avg `0.0327` n `27`; metal avg `0.2167` n `20`; unknown avg `46.2204` n `1151`
- 4h: commodity avg `-0.313` n `13`; crypto_alt avg `-0.0529` n `239`; crypto_major avg `-0.2332` n `8`; equity avg `-0.5062` n `168`; fx avg `0.0402` n `6`; index avg `-0.0508` n `27`; metal avg `-0.0747` n `20`; unknown avg `47.3096` n `1133`
- 24h: commodity avg `0.4718` n `13`; crypto_alt avg `2.9565` n `239`; crypto_major avg `3.1678` n `8`; equity avg `2.9565` n `168`; fx avg `0.0507` n `6`; index avg `0.2099` n `27`; metal avg `0.7365` n `20`; unknown avg `200.635` n `997`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1247`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1238`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1237`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1164`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1116`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1091`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1079`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1037`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0894`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0876`, n `668`, weak_sample_signal
