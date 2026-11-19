# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-19T03:22:42.113192+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0245` n `13`; crypto_alt avg `0.3094` n `239`; crypto_major avg `0.2383` n `8`; equity avg `0.0132` n `164`; fx avg `0.0064` n `6`; index avg `0.0155` n `27`; metal avg `0.054` n `20`; unknown avg `8.6174` n `1263`
- 1h: commodity avg `-0.0944` n `13`; crypto_alt avg `-0.1815` n `239`; crypto_major avg `-0.2233` n `8`; equity avg `-0.472` n `164`; fx avg `-0.0049` n `6`; index avg `-0.0497` n `27`; metal avg `-0.335` n `20`; unknown avg `0.4364` n `1263`
- 4h: commodity avg `-0.0291` n `13`; crypto_alt avg `0.2186` n `239`; crypto_major avg `-0.2508` n `8`; equity avg `-0.2374` n `164`; fx avg `-0.0556` n `6`; index avg `-0.0363` n `27`; metal avg `-0.3029` n `20`; unknown avg `3.2479` n `1257`
- 24h: commodity avg `-0.057` n `13`; crypto_alt avg `-0.3254` n `239`; crypto_major avg `-1.6827` n `8`; equity avg `-0.5561` n `164`; fx avg `-0.1309` n `6`; index avg `0.0325` n `27`; metal avg `-0.7158` n `20`; unknown avg `110.0705` n `1129`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1281`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1113`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0965`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0841`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0763`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.065`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0625`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0604`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0564`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0506`, n `668`, weak_sample_signal
