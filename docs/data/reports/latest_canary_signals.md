# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-14T16:07:35.697070+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0598` n `12`; crypto_alt avg `-0.2284` n `233`; crypto_major avg `-0.199` n `8`; equity avg `-0.2065` n `136`; fx avg `-0.0022` n `6`; index avg `-0.0205` n `27`; metal avg `-0.0178` n `20`; unknown avg `-0.0697` n `892`
- 1h: commodity avg `-0.0208` n `12`; crypto_alt avg `0.2268` n `233`; crypto_major avg `0.1408` n `8`; equity avg `0.3863` n `136`; fx avg `-0.0086` n `6`; index avg `0.0962` n `27`; metal avg `0.0472` n `20`; unknown avg `-0.0804` n `892`
- 4h: commodity avg `-0.1066` n `12`; crypto_alt avg `-0.284` n `233`; crypto_major avg `0.1231` n `8`; equity avg `0.7836` n `136`; fx avg `-0.0183` n `6`; index avg `0.0562` n `27`; metal avg `0.0003` n `20`; unknown avg `0.215` n `872`
- 24h: commodity avg `0.3978` n `12`; crypto_alt avg `-0.4166` n `233`; crypto_major avg `1.297` n `8`; equity avg `-0.5004` n `136`; fx avg `0.0395` n `6`; index avg `-0.2181` n `27`; metal avg `-0.407` n `20`; unknown avg `0.9674` n `636`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1165`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1105`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1102`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.105`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0955`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0817`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.071`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0688`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0614`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0605`, n `668`, weak_sample_signal
