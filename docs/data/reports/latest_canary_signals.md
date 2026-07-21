# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-21T22:37:40.159761+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0032` n `12`; crypto_alt avg `-0.0968` n `230`; crypto_major avg `-0.001` n `8`; equity avg `-0.074` n `98`; fx avg `0.0006` n `6`; index avg `-0.0083` n `25`; metal avg `0.0244` n `20`; unknown avg `-0.026` n `771`
- 1h: commodity avg `0.0125` n `12`; crypto_alt avg `-0.2236` n `230`; crypto_major avg `-0.128` n `8`; equity avg `-0.1917` n `98`; fx avg `0.0097` n `6`; index avg `-0.0258` n `25`; metal avg `0.012` n `20`; unknown avg `-0.165` n `771`
- 4h: commodity avg `0.108` n `12`; crypto_alt avg `-0.13` n `230`; crypto_major avg `-0.1349` n `8`; equity avg `0.5145` n `98`; fx avg `0.0002` n `6`; index avg `0.0078` n `25`; metal avg `-0.0096` n `20`; unknown avg `-0.2265` n `771`
- 24h: commodity avg `0.4656` n `12`; crypto_alt avg `0.8846` n `230`; crypto_major avg `0.8007` n `8`; equity avg `4.3733` n `98`; fx avg `0.0679` n `6`; index avg `0.6815` n `25`; metal avg `0.8072` n `20`; unknown avg `0.1755` n `754`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `0.0998`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0912`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0888`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0855`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0774`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0593`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0592`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0564`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0524`, n `666`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0507`, n `668`, weak_sample_signal
