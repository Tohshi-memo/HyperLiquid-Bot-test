# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-04T00:22:24.986283+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0283` n `12`; crypto_alt avg `0.2033` n `232`; crypto_major avg `0.1348` n `8`; equity avg `0.0576` n `133`; fx avg `0.0484` n `6`; index avg `0.0045` n `26`; metal avg `-0.0229` n `20`; unknown avg `0.1425` n `792`
- 1h: commodity avg `-0.0432` n `12`; crypto_alt avg `0.3065` n `232`; crypto_major avg `0.104` n `8`; equity avg `0.2448` n `133`; fx avg `-0.0088` n `6`; index avg `0.0092` n `26`; metal avg `0.0093` n `20`; unknown avg `-0.0902` n `790`
- 4h: commodity avg `-0.0` n `12`; crypto_alt avg `-0.044` n `232`; crypto_major avg `-0.1339` n `8`; equity avg `0.1937` n `133`; fx avg `0.0057` n `6`; index avg `0.0022` n `26`; metal avg `0.0053` n `20`; unknown avg `1.4038` n `768`
- 24h: commodity avg `-0.1383` n `12`; crypto_alt avg `4.1212` n `232`; crypto_major avg `5.2992` n `8`; equity avg `1.6094` n `133`; fx avg `-0.2481` n `6`; index avg `0.2458` n `26`; metal avg `0.7941` n `20`; unknown avg `23.0919` n `736`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1163`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1102`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0972`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0825`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0817`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0791`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0746`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0712`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0694`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.065`, n `668`, weak_sample_signal
