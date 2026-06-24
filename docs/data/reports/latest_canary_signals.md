# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-24T01:07:35.296522+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0586` n `12`; crypto_alt avg `-0.2898` n `228`; crypto_major avg `-0.2035` n `8`; equity avg `-0.2885` n `86`; fx avg `-0.0076` n `6`; index avg `-0.0322` n `23`; metal avg `-0.2259` n `20`; unknown avg `0.1263` n `764`
- 1h: commodity avg `-0.0567` n `12`; crypto_alt avg `-0.0246` n `228`; crypto_major avg `0.0377` n `8`; equity avg `0.1559` n `86`; fx avg `0.0002` n `6`; index avg `0.0327` n `23`; metal avg `-0.3257` n `20`; unknown avg `-0.3225` n `764`
- 4h: commodity avg `-0.1421` n `12`; crypto_alt avg `0.0333` n `228`; crypto_major avg `0.4828` n `8`; equity avg `0.3438` n `86`; fx avg `0.0262` n `6`; index avg `0.1361` n `23`; metal avg `-0.3321` n `20`; unknown avg `-0.1399` n `756`
- 24h: commodity avg `-0.4775` n `12`; crypto_alt avg `-2.1721` n `228`; crypto_major avg `-2.8265` n `8`; equity avg `-2.1381` n `86`; fx avg `-0.1626` n `6`; index avg `-0.6213` n `23`; metal avg `-1.3767` n `20`; unknown avg `0.3616` n `588`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1278`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1211`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1187`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1012`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0999`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0868`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0773`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.074`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0677`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0655`, n `668`, weak_sample_signal
