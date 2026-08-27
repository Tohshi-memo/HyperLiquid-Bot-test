# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-27T20:22:31.846563+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.018` n `12`; crypto_alt avg `0.2784` n `231`; crypto_major avg `0.2654` n `8`; equity avg `-0.1227` n `127`; fx avg `-0.0008` n `6`; index avg `-0.0186` n `26`; metal avg `0.0067` n `20`; unknown avg `-0.0181` n `792`
- 1h: commodity avg `-0.0676` n `12`; crypto_alt avg `0.0613` n `231`; crypto_major avg `-0.0269` n `8`; equity avg `0.1542` n `127`; fx avg `0.0014` n `6`; index avg `0.0475` n `26`; metal avg `0.0143` n `20`; unknown avg `0.1537` n `792`
- 4h: commodity avg `0.1723` n `12`; crypto_alt avg `-0.5879` n `231`; crypto_major avg `-0.163` n `8`; equity avg `0.3843` n `127`; fx avg `0.017` n `6`; index avg `0.0502` n `26`; metal avg `0.1105` n `20`; unknown avg `0.4126` n `792`
- 24h: commodity avg `0.3864` n `12`; crypto_alt avg `3.6046` n `231`; crypto_major avg `4.7349` n `8`; equity avg `1.7144` n `127`; fx avg `-0.0332` n `6`; index avg `0.2012` n `26`; metal avg `0.2973` n `20`; unknown avg `1.2514` n `775`

## Correlations

- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1291`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1258`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0907`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0844`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0793`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0752`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0702`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0653`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0631`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0545`, n `668`, weak_sample_signal
