# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-26T09:52:28.229629+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.024` n `12`; crypto_alt avg `-0.0564` n `231`; crypto_major avg `-0.0139` n `8`; equity avg `0.0808` n `122`; fx avg `0.0046` n `6`; index avg `0.0053` n `25`; metal avg `0.0149` n `20`; unknown avg `-0.0071` n `797`
- 1h: commodity avg `0.0733` n `12`; crypto_alt avg `-0.7758` n `231`; crypto_major avg `-0.5547` n `8`; equity avg `-0.0124` n `122`; fx avg `0.0004` n `6`; index avg `-0.0096` n `25`; metal avg `-0.0035` n `20`; unknown avg `-0.1307` n `797`
- 4h: commodity avg `-0.1489` n `12`; crypto_alt avg `-0.8534` n `231`; crypto_major avg `-0.8253` n `8`; equity avg `-0.1293` n `122`; fx avg `-0.0034` n `6`; index avg `-0.026` n `25`; metal avg `-0.1389` n `20`; unknown avg `-0.0328` n `781`
- 24h: commodity avg `-0.2568` n `12`; crypto_alt avg `-2.1034` n `231`; crypto_major avg `-1.9095` n `8`; equity avg `0.048` n `122`; fx avg `-0.0351` n `6`; index avg `-0.0714` n `25`; metal avg `0.0948` n `20`; unknown avg `0.6786` n `778`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1895`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1455`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1312`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1205`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1041`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0914`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0908`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0878`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0791`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0763`, n `668`, weak_sample_signal
