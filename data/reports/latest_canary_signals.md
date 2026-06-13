# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-13T10:07:44.258899+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0223` n `12`; crypto_alt avg `0.1293` n `228`; crypto_major avg `0.1071` n `8`; equity avg `0.0226` n `74`; fx avg `0.0003` n `6`; index avg `0.0148` n `23`; metal avg `-0.1113` n `18`; unknown avg `0.0792` n `643`
- 1h: commodity avg `-0.3902` n `12`; crypto_alt avg `0.1646` n `228`; crypto_major avg `-0.107` n `8`; equity avg `-0.1087` n `74`; fx avg `0.1243` n `6`; index avg `-0.0457` n `23`; metal avg `-0.0045` n `18`; unknown avg `0.3581` n `635`
- 4h: commodity avg `-0.1014` n `12`; crypto_alt avg `1.3478` n `228`; crypto_major avg `0.665` n `8`; equity avg `0.2102` n `74`; fx avg `-0.022` n `6`; index avg `0.0466` n `23`; metal avg `0.0478` n `18`; unknown avg `0.4093` n `635`
- 24h: commodity avg `0.2016` n `12`; crypto_alt avg `0.4852` n `228`; crypto_major avg `-0.2367` n `8`; equity avg `-0.9549` n `74`; fx avg `0.0204` n `6`; index avg `0.5156` n `23`; metal avg `0.0016` n `18`; unknown avg `31.8739` n `611`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0857`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.078`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0776`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0742`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0701`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0588`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0556`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0525`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0523`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0514`, n `668`, weak_sample_signal
