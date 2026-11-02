# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-02T03:52:34.334784+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.001` n `13`; crypto_alt avg `-0.0889` n `238`; crypto_major avg `-0.1193` n `8`; equity avg `0.06` n `156`; fx avg `-0.0099` n `6`; index avg `0.0061` n `27`; metal avg `-0.0285` n `20`; unknown avg `0.3906` n `1239`
- 1h: commodity avg `-0.045` n `13`; crypto_alt avg `0.4455` n `238`; crypto_major avg `0.453` n `8`; equity avg `0.7576` n `156`; fx avg `0.0433` n `6`; index avg `0.1003` n `27`; metal avg `0.0993` n `20`; unknown avg `1.6305` n `1207`
- 4h: commodity avg `-0.2984` n `13`; crypto_alt avg `0.218` n `238`; crypto_major avg `0.6214` n `8`; equity avg `1.1648` n `156`; fx avg `0.2151` n `6`; index avg `0.2614` n `27`; metal avg `-0.1085` n `20`; unknown avg `3.7632` n `1191`
- 24h: commodity avg `-0.3906` n `13`; crypto_alt avg `-0.2651` n `238`; crypto_major avg `0.857` n `8`; equity avg `1.5863` n `156`; fx avg `0.2142` n `6`; index avg `0.3493` n `27`; metal avg `0.053` n `20`; unknown avg `3.4104` n `1074`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1856`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1814`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1507`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1446`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1433`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.138`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1356`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1356`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.122`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1206`, n `668`, weak_sample_signal
