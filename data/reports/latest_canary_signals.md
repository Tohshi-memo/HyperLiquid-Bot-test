# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-02T11:37:28.881716+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0256` n `12`; crypto_alt avg `-0.0175` n `230`; crypto_major avg `-0.0357` n `8`; equity avg `-0.1674` n `102`; fx avg `-0.0145` n `6`; index avg `-0.0568` n `25`; metal avg `-0.0031` n `20`; unknown avg `-0.0071` n `782`
- 1h: commodity avg `0.0039` n `12`; crypto_alt avg `-0.0931` n `230`; crypto_major avg `-0.0795` n `8`; equity avg `-0.2609` n `102`; fx avg `-0.0085` n `6`; index avg `-0.0618` n `25`; metal avg `-0.0108` n `20`; unknown avg `-0.0305` n `782`
- 4h: commodity avg `0.1358` n `12`; crypto_alt avg `-0.3581` n `230`; crypto_major avg `-0.5041` n `8`; equity avg `-0.1178` n `102`; fx avg `-0.0023` n `6`; index avg `-0.0727` n `25`; metal avg `-0.0301` n `20`; unknown avg `-0.0641` n `782`
- 24h: commodity avg `-1.048` n `12`; crypto_alt avg `0.2936` n `230`; crypto_major avg `0.1924` n `8`; equity avg `0.6444` n `102`; fx avg `-0.0306` n `6`; index avg `0.181` n `25`; metal avg `0.2405` n `20`; unknown avg `0.265` n `765`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.129`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.12`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1046`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0915`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0855`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0829`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0828`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0754`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0715`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0701`, n `668`, weak_sample_signal
