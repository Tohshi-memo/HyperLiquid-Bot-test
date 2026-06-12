# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-12T18:52:31.186131+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.2919` n `12`; crypto_alt avg `-0.0547` n `228`; crypto_major avg `-0.0745` n `8`; equity avg `0.1107` n `74`; fx avg `0.0003` n `6`; index avg `0.0185` n `23`; metal avg `-0.0844` n `18`; unknown avg `-0.0784` n `643`
- 1h: commodity avg `-0.3103` n `12`; crypto_alt avg `-0.2894` n `228`; crypto_major avg `-0.1997` n `8`; equity avg `-0.1445` n `74`; fx avg `0.0099` n `6`; index avg `-0.0385` n `23`; metal avg `0.0716` n `18`; unknown avg `-0.1326` n `643`
- 4h: commodity avg `-0.6303` n `12`; crypto_alt avg `-0.7902` n `228`; crypto_major avg `-0.2286` n `8`; equity avg `0.2027` n `74`; fx avg `0.0135` n `6`; index avg `0.3876` n `23`; metal avg `0.9238` n `18`; unknown avg `-0.5522` n `643`
- 24h: commodity avg `-1.6177` n `12`; crypto_alt avg `0.0641` n `228`; crypto_major avg `0.8812` n `8`; equity avg `0.9164` n `74`; fx avg `0.0608` n `6`; index avg `0.989` n `23`; metal avg `1.2376` n `18`; unknown avg `41.743` n `514`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.104`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0784`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0757`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0711`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0708`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0682`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0632`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0607`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0592`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0572`, n `668`, weak_sample_signal
