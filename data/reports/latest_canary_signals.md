# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-13T23:07:29.090895+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0506` n `12`; crypto_alt avg `-0.0384` n `228`; crypto_major avg `-0.0126` n `8`; equity avg `0.1458` n `74`; fx avg `0.0042` n `6`; index avg `-0.036` n `23`; metal avg `-0.0012` n `18`; unknown avg `0.243` n `645`
- 1h: commodity avg `-0.0512` n `12`; crypto_alt avg `-0.1688` n `228`; crypto_major avg `-0.0492` n `8`; equity avg `0.1714` n `74`; fx avg `0.0101` n `6`; index avg `-0.0776` n `23`; metal avg `0.1853` n `18`; unknown avg `0.9839` n `644`
- 4h: commodity avg `0.0491` n `12`; crypto_alt avg `0.3785` n `228`; crypto_major avg `0.4886` n `8`; equity avg `0.3411` n `74`; fx avg `-0.0135` n `6`; index avg `0.0595` n `23`; metal avg `0.0225` n `18`; unknown avg `2.1696` n `644`
- 24h: commodity avg `-0.3928` n `12`; crypto_alt avg `2.6118` n `228`; crypto_major avg `1.4549` n `8`; equity avg `0.5685` n `74`; fx avg `0.0334` n `6`; index avg `0.4695` n `23`; metal avg `0.3095` n `18`; unknown avg `0.5218` n `611`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0863`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0853`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0676`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0615`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0614`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0606`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0595`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0585`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0564`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0533`, n `668`, weak_sample_signal
