# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-07T07:07:20.954913+00:00`
- Correlation status: `ready`
- Asset price records: `528`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.28` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.4901` n `12`; crypto_alt avg `0.2166` n `228`; crypto_major avg `0.0664` n `8`; equity avg `0.1066` n `65`; fx avg `-0.0512` n `4`; index avg `0.0092` n `23`; metal avg `0.148` n `18`; unknown avg `0.0114` n `358`
- 1h: commodity avg `-0.6361` n `12`; crypto_alt avg `0.6947` n `228`; crypto_major avg `0.431` n `8`; equity avg `0.2699` n `65`; fx avg `-0.089` n `4`; index avg `0.0835` n `23`; metal avg `0.6946` n `18`; unknown avg `0.0737` n `358`
- 4h: commodity avg `-0.8471` n `12`; crypto_alt avg `1.7026` n `228`; crypto_major avg `0.7854` n `8`; equity avg `0.6666` n `65`; fx avg `-0.083` n `4`; index avg `0.2019` n `23`; metal avg `0.7304` n `18`; unknown avg `0.3636` n `356`
- 24h: commodity avg `-2.5599` n `7`; crypto_alt avg `1.3842` n `223`; crypto_major avg `-0.7496` n `7`; equity avg `1.8352` n `47`; fx avg `-0.1664` n `4`; index avg `1.3493` n `6`; metal avg `2.2965` n `7`; unknown avg `0.655` n `311`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1267`, n `524`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1168`, n `524`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0878`, n `520`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0794`, n `520`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0792`, n `520`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0762`, n `520`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0712`, n `520`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0685`, n `524`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0668`, n `524`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0656`, n `524`, weak_sample_signal
