# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-02T14:22:27.249557+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0033` n `12`; crypto_alt avg `0.0511` n `230`; crypto_major avg `0.082` n `8`; equity avg `0.0034` n `102`; fx avg `-0.0393` n `6`; index avg `-0.0133` n `25`; metal avg `-0.0094` n `20`; unknown avg `0.021` n `782`
- 1h: commodity avg `-0.132` n `12`; crypto_alt avg `0.012` n `230`; crypto_major avg `0.0695` n `8`; equity avg `-0.0303` n `102`; fx avg `-0.0704` n `6`; index avg `-0.0165` n `25`; metal avg `-0.0125` n `20`; unknown avg `-0.0834` n `782`
- 4h: commodity avg `-0.016` n `12`; crypto_alt avg `-0.1795` n `230`; crypto_major avg `-0.0741` n `8`; equity avg `-0.263` n `102`; fx avg `-0.0803` n `6`; index avg `-0.0544` n `25`; metal avg `-0.011` n `20`; unknown avg `-0.1383` n `782`
- 24h: commodity avg `-1.062` n `12`; crypto_alt avg `0.1` n `230`; crypto_major avg `0.0357` n `8`; equity avg `0.813` n `102`; fx avg `-0.1633` n `6`; index avg `0.1971` n `25`; metal avg `0.2364` n `20`; unknown avg `0.2228` n `766`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1248`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.123`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1073`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0872`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0869`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.082`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0804`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0745`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0721`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0718`, n `668`, weak_sample_signal
