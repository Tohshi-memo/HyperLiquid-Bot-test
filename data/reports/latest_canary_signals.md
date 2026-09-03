# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-03T12:22:29.384895+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1425` n `12`; crypto_alt avg `0.0176` n `232`; crypto_major avg `0.0208` n `8`; equity avg `-0.0533` n `133`; fx avg `-0.0424` n `6`; index avg `-0.0042` n `26`; metal avg `-0.0259` n `20`; unknown avg `0.14` n `792`
- 1h: commodity avg `-0.0337` n `12`; crypto_alt avg `0.1805` n `232`; crypto_major avg `0.2063` n `8`; equity avg `-0.1907` n `133`; fx avg `-0.0333` n `6`; index avg `-0.0169` n `26`; metal avg `0.0417` n `20`; unknown avg `2.0711` n `790`
- 4h: commodity avg `0.2991` n `12`; crypto_alt avg `0.1833` n `232`; crypto_major avg `0.2557` n `8`; equity avg `-0.3858` n `133`; fx avg `-0.1301` n `6`; index avg `-0.0815` n `26`; metal avg `-0.0497` n `20`; unknown avg `0.2652` n `790`
- 24h: commodity avg `0.6165` n `12`; crypto_alt avg `1.8736` n `232`; crypto_major avg `1.8154` n `8`; equity avg `0.8478` n `133`; fx avg `-0.4166` n `6`; index avg `-0.0076` n `26`; metal avg `0.55` n `20`; unknown avg `-0.1879` n `735`

## Correlations

- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1178`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0828`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0786`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0784`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0666`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0574`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0568`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0471`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0444`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0437`, n `668`, weak_sample_signal
