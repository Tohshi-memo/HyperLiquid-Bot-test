# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-08T00:52:16.220407+00:00`
- Correlation status: `ready`
- Asset price records: `599`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.16` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0219` n `12`; crypto_alt avg `-0.2536` n `228`; crypto_major avg `-0.2385` n `8`; equity avg `-0.0606` n `65`; fx avg `0.0186` n `5`; index avg `0.013` n `23`; metal avg `-0.0628` n `18`; unknown avg `-0.1281` n `365`
- 1h: commodity avg `0.0756` n `12`; crypto_alt avg `-0.292` n `228`; crypto_major avg `-0.2431` n `8`; equity avg `0.2498` n `65`; fx avg `0.1088` n `5`; index avg `0.1443` n `23`; metal avg `-0.1061` n `18`; unknown avg `-0.1966` n `365`
- 4h: commodity avg `0.0365` n `12`; crypto_alt avg `0.1152` n `228`; crypto_major avg `-0.2751` n `8`; equity avg `0.0183` n `65`; fx avg `0.0665` n `5`; index avg `0.246` n `23`; metal avg `-0.1721` n `18`; unknown avg `-0.3605` n `365`
- 24h: commodity avg `0.6349` n `12`; crypto_alt avg `1.7161` n `228`; crypto_major avg `-1.5395` n `8`; equity avg `-0.8072` n `65`; fx avg `0.1946` n `5`; index avg `-0.6182` n `23`; metal avg `-0.0375` n `18`; unknown avg `-0.3239` n `354`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.137`, n `595`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1112`, n `595`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1075`, n `595`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1023`, n `591`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1002`, n `591`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0993`, n `595`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0926`, n `591`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0912`, n `591`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0815`, n `591`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0703`, n `595`, weak_sample_signal
