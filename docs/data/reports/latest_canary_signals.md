# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-13T15:22:30.590703+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0247` n `12`; crypto_alt avg `-0.1525` n `233`; crypto_major avg `-0.0915` n `8`; equity avg `-0.026` n `136`; fx avg `0.0081` n `6`; index avg `-0.0094` n `27`; metal avg `-0.008` n `20`; unknown avg `145.6899` n `838`
- 1h: commodity avg `0.1042` n `12`; crypto_alt avg `-0.5845` n `233`; crypto_major avg `-0.1677` n `8`; equity avg `-0.0951` n `136`; fx avg `0.0031` n `6`; index avg `-0.0222` n `27`; metal avg `-0.015` n `20`; unknown avg `4.0189` n `836`
- 4h: commodity avg `0.0348` n `12`; crypto_alt avg `0.3535` n `233`; crypto_major avg `0.3987` n `8`; equity avg `0.0576` n `136`; fx avg `0.0028` n `6`; index avg `0.0147` n `27`; metal avg `-0.0064` n `20`; unknown avg `2.6357` n `826`
- 24h: commodity avg `0.326` n `12`; crypto_alt avg `-0.6056` n `233`; crypto_major avg `-1.6772` n `8`; equity avg `-1.6915` n `136`; fx avg `0.0075` n `6`; index avg `-0.2709` n `26`; metal avg `-0.0866` n `20`; unknown avg `2.2039` n `708`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0814`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0793`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0788`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0722`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0693`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0691`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0646`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0645`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0612`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0585`, n `668`, weak_sample_signal
