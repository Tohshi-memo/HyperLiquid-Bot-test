# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-10T11:37:27.204885+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0016` n `13`; crypto_alt avg `-0.0371` n `235`; crypto_major avg `0.0723` n `8`; equity avg `0.0089` n `150`; fx avg `-0.0031` n `6`; index avg `0.0009` n `26`; metal avg `-0.0041` n `20`; unknown avg `-0.0294` n `1117`
- 1h: commodity avg `0.0069` n `13`; crypto_alt avg `0.048` n `235`; crypto_major avg `0.0681` n `8`; equity avg `0.0257` n `150`; fx avg `-0.007` n `6`; index avg `-0.0015` n `26`; metal avg `0.0024` n `20`; unknown avg `0.0357` n `1115`
- 4h: commodity avg `-0.2538` n `13`; crypto_alt avg `-0.2725` n `235`; crypto_major avg `-0.1004` n `8`; equity avg `0.0055` n `150`; fx avg `-0.0094` n `6`; index avg `0.0079` n `26`; metal avg `-0.0006` n `20`; unknown avg `0.1932` n `1099`
- 24h: commodity avg `-0.1516` n `13`; crypto_alt avg `1.4143` n `235`; crypto_major avg `-0.0733` n `8`; equity avg `-0.2945` n `150`; fx avg `-0.0082` n `6`; index avg `-0.0247` n `26`; metal avg `0.0048` n `20`; unknown avg `631.7139` n `954`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1551`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1402`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1224`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1207`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1175`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.107`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1063`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.103`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1024`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0927`, n `668`, weak_sample_signal
