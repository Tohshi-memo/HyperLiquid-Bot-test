# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-04T10:22:26.576032+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0313` n `12`; crypto_alt avg `-0.2773` n `232`; crypto_major avg `-0.2042` n `8`; equity avg `-0.0306` n `133`; fx avg `-0.0075` n `6`; index avg `0.0045` n `26`; metal avg `0.0039` n `20`; unknown avg `0.1272` n `793`
- 1h: commodity avg `0.0055` n `12`; crypto_alt avg `-0.3821` n `232`; crypto_major avg `-0.35` n `8`; equity avg `0.1341` n `133`; fx avg `-0.0167` n `6`; index avg `0.0267` n `26`; metal avg `0.0131` n `20`; unknown avg `-0.099` n `791`
- 4h: commodity avg `-0.0113` n `12`; crypto_alt avg `0.7995` n `232`; crypto_major avg `0.0691` n `8`; equity avg `0.2683` n `133`; fx avg `-0.0147` n `6`; index avg `0.0202` n `26`; metal avg `0.0188` n `20`; unknown avg `14.0201` n `783`
- 24h: commodity avg `-0.5111` n `12`; crypto_alt avg `2.3075` n `232`; crypto_major avg `3.8862` n `8`; equity avg `2.3595` n `133`; fx avg `-0.0206` n `6`; index avg `0.4386` n `26`; metal avg `0.5125` n `20`; unknown avg `1.9791` n `730`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1177`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1168`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0926`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0883`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0873`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0773`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0766`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0744`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0733`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0625`, n `668`, weak_sample_signal
