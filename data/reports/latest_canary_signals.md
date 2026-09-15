# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-15T15:37:30.674691+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0273` n `12`; crypto_alt avg `0.1456` n `233`; crypto_major avg `0.1574` n `8`; equity avg `0.0959` n `137`; fx avg `0.0051` n `6`; index avg `0.0253` n `27`; metal avg `0.0435` n `20`; unknown avg `0.1497` n `909`
- 1h: commodity avg `0.055` n `12`; crypto_alt avg `-0.0191` n `233`; crypto_major avg `-0.1314` n `8`; equity avg `-0.1554` n `137`; fx avg `0.0294` n `6`; index avg `-0.0168` n `27`; metal avg `0.0132` n `20`; unknown avg `-0.0327` n `895`
- 4h: commodity avg `0.4099` n `12`; crypto_alt avg `-0.2705` n `233`; crypto_major avg `-0.8593` n `8`; equity avg `-0.8235` n `137`; fx avg `0.0767` n `6`; index avg `-0.1323` n `27`; metal avg `-0.0111` n `20`; unknown avg `1.5291` n `873`
- 24h: commodity avg `0.2909` n `12`; crypto_alt avg `-1.815` n `233`; crypto_major avg `-1.9605` n `8`; equity avg `-0.9914` n `137`; fx avg `0.2705` n `6`; index avg `-0.0984` n `27`; metal avg `-0.0672` n `20`; unknown avg `-0.2156` n `813`

## Correlations

- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1184`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1013`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0983`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0962`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0878`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0855`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0801`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.078`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0746`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0638`, n `668`, weak_sample_signal
