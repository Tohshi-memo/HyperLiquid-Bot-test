# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-20T17:37:28.011038+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `1.7636` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0172` n `12`; crypto_alt avg `0.1461` n `234`; crypto_major avg `0.0291` n `8`; equity avg `-0.0295` n `140`; fx avg `-0.024` n `6`; index avg `-0.0035` n `26`; metal avg `-0.0133` n `20`; unknown avg `0.1786` n `943`
- 1h: commodity avg `-0.0132` n `12`; crypto_alt avg `0.4695` n `234`; crypto_major avg `-0.0927` n `8`; equity avg `-0.0168` n `140`; fx avg `-0.0177` n `6`; index avg `-0.0001` n `26`; metal avg `-0.0162` n `20`; unknown avg `9.0505` n `929`
- 4h: commodity avg `0.0575` n `12`; crypto_alt avg `3.0035` n `234`; crypto_major avg `1.7744` n `8`; equity avg `0.2942` n `140`; fx avg `0.0056` n `6`; index avg `0.0277` n `26`; metal avg `0.0108` n `20`; unknown avg `1.1078` n `879`
- 24h: commodity avg `0.4008` n `12`; crypto_alt avg `0.3832` n `234`; crypto_major avg `-0.6651` n `8`; equity avg `0.0024` n `140`; fx avg `-0.0581` n `6`; index avg `-0.0305` n `26`; metal avg `-0.0149` n `20`; unknown avg `162.0426` n `827`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.159`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1439`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1381`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1192`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0925`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0891`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0786`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0747`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0718`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0684`, n `668`, weak_sample_signal
