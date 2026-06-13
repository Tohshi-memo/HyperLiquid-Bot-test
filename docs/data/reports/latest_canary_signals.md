# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-13T02:52:28.111551+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0919` n `12`; crypto_alt avg `-0.1977` n `228`; crypto_major avg `-0.2876` n `8`; equity avg `-0.0817` n `74`; fx avg `0.0257` n `6`; index avg `-0.0483` n `23`; metal avg `-0.0159` n `18`; unknown avg `0.1241` n `643`
- 1h: commodity avg `-0.1864` n `12`; crypto_alt avg `-0.4247` n `228`; crypto_major avg `-0.3874` n `8`; equity avg `0.0658` n `74`; fx avg `0.0078` n `6`; index avg `0.1196` n `23`; metal avg `-0.0423` n `18`; unknown avg `0.4272` n `643`
- 4h: commodity avg `0.1345` n `12`; crypto_alt avg `0.7678` n `228`; crypto_major avg `-0.0786` n `8`; equity avg `0.1178` n `74`; fx avg `0.0457` n `6`; index avg `0.2154` n `23`; metal avg `0.05` n `18`; unknown avg `-0.4352` n `643`
- 24h: commodity avg `-0.8778` n `12`; crypto_alt avg `0.0553` n `228`; crypto_major avg `-0.3428` n `8`; equity avg `-0.6324` n `74`; fx avg `0.0164` n `6`; index avg `0.6359` n `23`; metal avg `0.4208` n `18`; unknown avg `40.1721` n `515`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0797`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.078`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0731`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0595`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0585`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0569`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.056`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0538`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0537`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.053`, n `668`, weak_sample_signal
