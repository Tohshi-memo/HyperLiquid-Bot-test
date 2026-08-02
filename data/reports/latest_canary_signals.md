# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-02T17:22:29.862759+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0428` n `12`; crypto_alt avg `0.0162` n `230`; crypto_major avg `0.0533` n `8`; equity avg `0.0476` n `102`; fx avg `-0.0055` n `6`; index avg `0.0004` n `25`; metal avg `-0.0125` n `20`; unknown avg `-0.037` n `782`
- 1h: commodity avg `0.0123` n `12`; crypto_alt avg `0.1033` n `230`; crypto_major avg `0.393` n `8`; equity avg `0.3434` n `102`; fx avg `0.0017` n `6`; index avg `0.045` n `25`; metal avg `0.0206` n `20`; unknown avg `0.4536` n `782`
- 4h: commodity avg `-0.2132` n `12`; crypto_alt avg `0.1322` n `230`; crypto_major avg `0.4562` n `8`; equity avg `0.3642` n `102`; fx avg `-0.0486` n `6`; index avg `0.0575` n `25`; metal avg `0.0444` n `20`; unknown avg `1.2208` n `782`
- 24h: commodity avg `-1.2653` n `12`; crypto_alt avg `0.4588` n `230`; crypto_major avg `0.7214` n `8`; equity avg `1.346` n `102`; fx avg `-0.1468` n `6`; index avg `0.2814` n `25`; metal avg `0.2904` n `20`; unknown avg `1.5064` n `766`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1261`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1198`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1119`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0885`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0837`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0797`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0782`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0725`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0718`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0702`, n `668`, weak_sample_signal
