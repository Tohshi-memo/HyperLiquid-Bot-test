# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-31T18:07:23.937241+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0143` n `13`; crypto_alt avg `0.0193` n `238`; crypto_major avg `-0.0039` n `8`; equity avg `-0.0082` n `156`; fx avg `-0.0086` n `6`; index avg `0.0012` n `27`; metal avg `-0.0029` n `20`; unknown avg `-0.1066` n `1216`
- 1h: commodity avg `0.0032` n `13`; crypto_alt avg `-0.2927` n `238`; crypto_major avg `0.2302` n `8`; equity avg `0.0388` n `156`; fx avg `-0.0111` n `6`; index avg `0.0035` n `27`; metal avg `-0.0112` n `20`; unknown avg `-0.0053` n `1216`
- 4h: commodity avg `-0.054` n `13`; crypto_alt avg `0.5034` n `238`; crypto_major avg `0.4823` n `8`; equity avg `0.1299` n `156`; fx avg `-0.0155` n `6`; index avg `0.0079` n `27`; metal avg `0.0139` n `20`; unknown avg `0.4906` n `1196`
- 24h: commodity avg `-0.3958` n `13`; crypto_alt avg `1.1227` n `238`; crypto_major avg `0.2754` n `8`; equity avg `1.2272` n `156`; fx avg `-0.0173` n `6`; index avg `0.0474` n `27`; metal avg `0.1098` n `20`; unknown avg `0.9777` n `1041`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1518`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1491`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1439`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1426`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1371`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1233`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1205`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1079`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0845`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0837`, n `668`, weak_sample_signal
