# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-01T09:37:25.026598+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0845` n `12`; crypto_alt avg `-0.3366` n `228`; crypto_major avg `0.0878` n `8`; equity avg `-0.1156` n `69`; fx avg `-0.0092` n `6`; index avg `-0.0752` n `23`; metal avg `-0.1544` n `18`; unknown avg `-0.0855` n `422`
- 1h: commodity avg `-0.1718` n `12`; crypto_alt avg `0.0569` n `228`; crypto_major avg `0.5547` n `8`; equity avg `0.1793` n `69`; fx avg `-0.0019` n `6`; index avg `0.0195` n `23`; metal avg `0.1663` n `18`; unknown avg `0.6722` n `422`
- 4h: commodity avg `0.301` n `12`; crypto_alt avg `-1.0281` n `228`; crypto_major avg `-0.2608` n `8`; equity avg `-0.29` n `69`; fx avg `-0.0579` n `6`; index avg `0.0076` n `23`; metal avg `-0.1496` n `18`; unknown avg `0.8176` n `412`
- 24h: commodity avg `1.1823` n `12`; crypto_alt avg `-0.7173` n `228`; crypto_major avg `-0.6449` n `8`; equity avg `-0.2203` n `69`; fx avg `-0.0242` n `6`; index avg `0.4546` n `23`; metal avg `0.1164` n `18`; unknown avg `2.7257` n `411`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2874`, n `668`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.2118`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.2058`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1551`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.15`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1273`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1068`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1036`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1012`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0952`, n `668`, weak_sample_signal
