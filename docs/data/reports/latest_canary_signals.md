# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-10T12:07:27.007027+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0171` n `13`; crypto_alt avg `0.0722` n `235`; crypto_major avg `-0.0697` n `8`; equity avg `-0.0082` n `150`; fx avg `0.0001` n `6`; index avg `-0.0009` n `26`; metal avg `0.0046` n `20`; unknown avg `0.0398` n `1109`
- 1h: commodity avg `-0.0234` n `13`; crypto_alt avg `0.1194` n `235`; crypto_major avg `0.0315` n `8`; equity avg `0.0149` n `150`; fx avg `-0.0068` n `6`; index avg `-0.0065` n `26`; metal avg `-0.0019` n `20`; unknown avg `0.1797` n `1109`
- 4h: commodity avg `-0.2618` n `13`; crypto_alt avg `-0.1464` n `235`; crypto_major avg `-0.2293` n `8`; equity avg `0.0103` n `150`; fx avg `-0.0218` n `6`; index avg `0.0051` n `26`; metal avg `-0.0056` n `20`; unknown avg `0.1925` n `1109`
- 24h: commodity avg `-0.1629` n `13`; crypto_alt avg `1.5402` n `235`; crypto_major avg `-0.3518` n `8`; equity avg `-0.2587` n `150`; fx avg `0.0142` n `6`; index avg `-0.0243` n `26`; metal avg `0.0501` n `20`; unknown avg `632.1519` n `954`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1545`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1416`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1211`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1203`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1163`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1052`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1032`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1012`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0987`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0921`, n `668`, weak_sample_signal
