# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-27T07:07:25.515734+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1008` n `13`; crypto_alt avg `0.0916` n `239`; crypto_major avg `0.1927` n `8`; equity avg `0.0717` n `168`; fx avg `-0.0225` n `6`; index avg `-0.0079` n `27`; metal avg `0.0763` n `20`; unknown avg `0.1488` n `1249`
- 1h: commodity avg `0.0052` n `13`; crypto_alt avg `-0.0103` n `239`; crypto_major avg `0.0758` n `8`; equity avg `-0.1295` n `168`; fx avg `-0.0576` n `6`; index avg `-0.0142` n `27`; metal avg `0.1974` n `20`; unknown avg `0.9106` n `1253`
- 4h: commodity avg `0.1264` n `13`; crypto_alt avg `0.1683` n `239`; crypto_major avg `0.6029` n `8`; equity avg `1.367` n `168`; fx avg `-0.0845` n `6`; index avg `0.0766` n `27`; metal avg `0.3659` n `20`; unknown avg `73.5898` n `1231`
- 24h: commodity avg `0.5874` n `13`; crypto_alt avg `2.3405` n `239`; crypto_major avg `3.0109` n `8`; equity avg `3.919` n `168`; fx avg `-0.0198` n `6`; index avg `0.3334` n `27`; metal avg `1.2945` n `20`; unknown avg `216.2297` n `993`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1136`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.109`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.107`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1021`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0994`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0944`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0864`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0833`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.082`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0765`, n `668`, weak_sample_signal
