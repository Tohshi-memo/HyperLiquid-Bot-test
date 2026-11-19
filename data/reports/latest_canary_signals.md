# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-19T01:17:54.634842+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.065` n `13`; crypto_alt avg `-0.2789` n `239`; crypto_major avg `-0.2916` n `8`; equity avg `-0.2523` n `164`; fx avg `0.0118` n `6`; index avg `-0.0333` n `27`; metal avg `-0.1023` n `20`; unknown avg `-0.0401` n `1261`
- 1h: commodity avg `0.0935` n `13`; crypto_alt avg `0.3294` n `239`; crypto_major avg `0.5016` n `8`; equity avg `0.5073` n `164`; fx avg `0.0432` n `6`; index avg `0.0556` n `27`; metal avg `0.0338` n `20`; unknown avg `10.9455` n `1261`
- 4h: commodity avg `-0.0038` n `13`; crypto_alt avg `0.2714` n `239`; crypto_major avg `0.4074` n `8`; equity avg `1.0361` n `164`; fx avg `0.0088` n `6`; index avg `0.1195` n `27`; metal avg `0.188` n `20`; unknown avg `4.236` n `1249`
- 24h: commodity avg `-0.0648` n `13`; crypto_alt avg `-0.5206` n `239`; crypto_major avg `-1.605` n `8`; equity avg `-0.777` n `164`; fx avg `-0.1038` n `6`; index avg `0.0191` n `27`; metal avg `-0.7214` n `20`; unknown avg `47.0611` n `1127`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1189`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.092`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.087`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0733`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0702`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0688`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0661`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0659`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0553`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0527`, n `668`, weak_sample_signal
