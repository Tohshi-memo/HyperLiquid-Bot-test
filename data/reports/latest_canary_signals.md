# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-24T07:07:30.099955+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.053` n `12`; crypto_alt avg `-0.1904` n `228`; crypto_major avg `-0.2305` n `8`; equity avg `-0.1345` n `86`; fx avg `-0.0062` n `6`; index avg `-0.0161` n `23`; metal avg `-0.0548` n `20`; unknown avg `-0.0527` n `756`
- 1h: commodity avg `-0.1628` n `12`; crypto_alt avg `-0.1586` n `228`; crypto_major avg `-0.1965` n `8`; equity avg `-0.0917` n `86`; fx avg `0.0476` n `6`; index avg `0.0182` n `23`; metal avg `-0.1709` n `20`; unknown avg `-0.1644` n `756`
- 4h: commodity avg `0.0095` n `12`; crypto_alt avg `0.0761` n `228`; crypto_major avg `0.3175` n `8`; equity avg `0.7945` n `86`; fx avg `0.0977` n `6`; index avg `0.2909` n `23`; metal avg `0.3025` n `20`; unknown avg `-0.0493` n `732`
- 24h: commodity avg `-0.3597` n `12`; crypto_alt avg `-0.7947` n `228`; crypto_major avg `-1.3456` n `8`; equity avg `4.3812` n `86`; fx avg `-0.0379` n `6`; index avg `0.025` n `23`; metal avg `-0.2994` n `20`; unknown avg `0.0039` n `572`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1189`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1054`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0994`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0793`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0734`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0728`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0679`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0663`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0629`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0624`, n `668`, weak_sample_signal
