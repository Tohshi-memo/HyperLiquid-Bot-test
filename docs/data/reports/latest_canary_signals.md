# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-08T01:37:25.162189+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0303` n `12`; crypto_alt avg `0.1111` n `230`; crypto_major avg `0.06` n `8`; equity avg `0.0313` n `112`; fx avg `0.0047` n `6`; index avg `0.001` n `25`; metal avg `-0.0157` n `20`; unknown avg `-0.0696` n `783`
- 1h: commodity avg `0.0599` n `12`; crypto_alt avg `0.1898` n `230`; crypto_major avg `0.2217` n `8`; equity avg `0.0156` n `112`; fx avg `0.0075` n `6`; index avg `-0.013` n `25`; metal avg `0.0038` n `20`; unknown avg `-0.1354` n `783`
- 4h: commodity avg `-0.0169` n `12`; crypto_alt avg `0.0641` n `230`; crypto_major avg `0.0844` n `8`; equity avg `0.1696` n `112`; fx avg `0.0181` n `6`; index avg `-0.0207` n `25`; metal avg `0.0748` n `20`; unknown avg `-0.3293` n `782`
- 24h: commodity avg `-0.0662` n `12`; crypto_alt avg `-0.5443` n `230`; crypto_major avg `-0.0458` n `8`; equity avg `2.2568` n `112`; fx avg `-0.0625` n `6`; index avg `0.2174` n `25`; metal avg `0.4838` n `20`; unknown avg `-0.1081` n `766`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1588`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0906`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.09`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0787`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0715`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0694`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0639`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.06`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0573`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0547`, n `668`, weak_sample_signal
