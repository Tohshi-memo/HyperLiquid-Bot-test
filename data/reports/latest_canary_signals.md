# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-19T10:22:24.884140+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0392` n `13`; crypto_alt avg `-0.0743` n `239`; crypto_major avg `-0.1021` n `8`; equity avg `0.0968` n `164`; fx avg `-0.002` n `6`; index avg `0.0223` n `27`; metal avg `-0.0331` n `20`; unknown avg `3.9125` n `1264`
- 1h: commodity avg `0.073` n `13`; crypto_alt avg `-0.081` n `239`; crypto_major avg `-0.0277` n `8`; equity avg `0.2578` n `164`; fx avg `-0.0131` n `6`; index avg `0.1152` n `27`; metal avg `0.0423` n `20`; unknown avg `1.1166` n `1264`
- 4h: commodity avg `0.0331` n `13`; crypto_alt avg `0.3465` n `239`; crypto_major avg `0.2397` n `8`; equity avg `1.0064` n `164`; fx avg `0.0956` n `6`; index avg `0.2274` n `27`; metal avg `-0.0226` n `20`; unknown avg `271.7047` n `1220`
- 24h: commodity avg `0.2862` n `13`; crypto_alt avg `0.1285` n `239`; crypto_major avg `-0.4735` n `8`; equity avg `0.4281` n `164`; fx avg `0.0403` n `6`; index avg `0.2625` n `27`; metal avg `-0.1506` n `20`; unknown avg `3.768` n `1161`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1626`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1597`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1344`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1261`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0759`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0667`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0628`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0561`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0501`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0499`, n `668`, weak_sample_signal
