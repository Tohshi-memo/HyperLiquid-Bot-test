# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-26T23:38:02.331020+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0176` n `12`; crypto_alt avg `0.0246` n `234`; crypto_major avg `0.0323` n `8`; equity avg `0.0011` n `141`; fx avg `0.0018` n `6`; index avg `-0.0006` n `26`; metal avg `0.0019` n `20`; unknown avg `1.9945` n `961`
- 1h: commodity avg `-0.0039` n `12`; crypto_alt avg `0.2785` n `234`; crypto_major avg `0.2537` n `8`; equity avg `0.0328` n `141`; fx avg `0.0038` n `6`; index avg `0.0005` n `26`; metal avg `0.0026` n `20`; unknown avg `0.4212` n `959`
- 4h: commodity avg `0.0529` n `12`; crypto_alt avg `0.0157` n `234`; crypto_major avg `0.3342` n `8`; equity avg `0.0682` n `141`; fx avg `-0.0171` n `6`; index avg `-0.0038` n `26`; metal avg `0.0042` n `20`; unknown avg `168.49` n `929`
- 24h: commodity avg `0.3179` n `12`; crypto_alt avg `0.589` n `234`; crypto_major avg `-0.6515` n `8`; equity avg `0.0219` n `141`; fx avg `0.0115` n `6`; index avg `-0.0586` n `26`; metal avg `-0.0146` n `20`; unknown avg `4.1006` n `884`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1751`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1565`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1552`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1498`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1371`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1298`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1224`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1008`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0953`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.095`, n `668`, weak_sample_signal
