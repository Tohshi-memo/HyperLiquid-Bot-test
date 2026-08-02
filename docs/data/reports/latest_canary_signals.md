# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-02T16:07:24.224161+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0288` n `12`; crypto_alt avg `-0.092` n `230`; crypto_major avg `-0.0884` n `8`; equity avg `0.0227` n `102`; fx avg `-0.0055` n `6`; index avg `0.0075` n `25`; metal avg `0.0023` n `20`; unknown avg `-0.0214` n `782`
- 1h: commodity avg `0.0219` n `12`; crypto_alt avg `-0.0569` n `230`; crypto_major avg `-0.0818` n `8`; equity avg `0.0606` n `102`; fx avg `-0.0031` n `6`; index avg `-0.001` n `25`; metal avg `0.0175` n `20`; unknown avg `-0.1005` n `782`
- 4h: commodity avg `-0.1234` n `12`; crypto_alt avg `-0.0399` n `230`; crypto_major avg `0.1106` n `8`; equity avg `0.1399` n `102`; fx avg `-0.0537` n `6`; index avg `0.0312` n `25`; metal avg `0.0435` n `20`; unknown avg `1.081` n `782`
- 24h: commodity avg `-1.0788` n `12`; crypto_alt avg `0.2075` n `230`; crypto_major avg `0.125` n `8`; equity avg `0.9713` n `102`; fx avg `-0.1474` n `6`; index avg `0.2153` n `25`; metal avg `0.2617` n `20`; unknown avg `1.4388` n `766`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1241`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1238`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1081`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0927`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0819`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0817`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0811`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0742`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0726`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0716`, n `668`, weak_sample_signal
