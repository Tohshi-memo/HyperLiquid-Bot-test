# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-10T08:37:29.236733+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1157` n `12`; crypto_alt avg `-0.0199` n `229`; crypto_major avg `-0.0291` n `8`; equity avg `0.0294` n `91`; fx avg `0.0031` n `6`; index avg `-0.0225` n `25`; metal avg `-0.0874` n `20`; unknown avg `-0.0358` n `765`
- 1h: commodity avg `0.1219` n `12`; crypto_alt avg `0.3125` n `229`; crypto_major avg `0.5113` n `8`; equity avg `-0.1009` n `91`; fx avg `0.0076` n `6`; index avg `-0.0256` n `25`; metal avg `-0.1434` n `20`; unknown avg `0.0921` n `765`
- 4h: commodity avg `-0.1293` n `12`; crypto_alt avg `0.1501` n `229`; crypto_major avg `0.2485` n `8`; equity avg `-0.8884` n `91`; fx avg `-0.0856` n `6`; index avg `-0.1785` n `25`; metal avg `-0.2171` n `20`; unknown avg `1.1475` n `733`
- 24h: commodity avg `-0.7173` n `12`; crypto_alt avg `0.8378` n `229`; crypto_major avg `1.2776` n `8`; equity avg `-0.0871` n `91`; fx avg `-0.1399` n `6`; index avg `0.1078` n `25`; metal avg `0.0633` n `20`; unknown avg `0.028` n `732`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1074`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0976`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0893`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0878`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0822`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0822`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0815`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0786`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0763`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0748`, n `668`, weak_sample_signal
