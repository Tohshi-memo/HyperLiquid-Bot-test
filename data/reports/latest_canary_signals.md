# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-14T17:22:29.798708+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0001` n `12`; crypto_alt avg `-0.0528` n `228`; crypto_major avg `0.0438` n `8`; equity avg `-0.0088` n `74`; fx avg `0.0014` n `6`; index avg `-0.014` n `23`; metal avg `0.0012` n `18`; unknown avg `0.7857` n `645`
- 1h: commodity avg `-0.1233` n `12`; crypto_alt avg `-0.1472` n `228`; crypto_major avg `-0.0925` n `8`; equity avg `-0.0699` n `74`; fx avg `0.0273` n `6`; index avg `-0.0507` n `23`; metal avg `0.0475` n `18`; unknown avg `0.4031` n `645`
- 4h: commodity avg `-0.036` n `12`; crypto_alt avg `-0.1938` n `228`; crypto_major avg `-0.2881` n `8`; equity avg `-0.1644` n `74`; fx avg `-0.0155` n `6`; index avg `0.002` n `23`; metal avg `-0.0349` n `18`; unknown avg `0.3686` n `645`
- 24h: commodity avg `-0.2282` n `12`; crypto_alt avg `-1.2927` n `228`; crypto_major avg `-0.3338` n `8`; equity avg `0.485` n `74`; fx avg `-0.0155` n `6`; index avg `0.145` n `23`; metal avg `-0.1241` n `18`; unknown avg `1.7491` n `592`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1315`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1144`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1034`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1002`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0739`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0695`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0675`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0664`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0631`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0595`, n `668`, weak_sample_signal
