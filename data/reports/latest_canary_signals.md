# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-23T14:22:35.674144+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0072` n `12`; crypto_alt avg `0.0415` n `228`; crypto_major avg `0.0992` n `8`; equity avg `-0.0266` n `86`; fx avg `-0.0026` n `6`; index avg `0.074` n `23`; metal avg `-0.0523` n `20`; unknown avg `0.03` n `764`
- 1h: commodity avg `-0.1749` n `12`; crypto_alt avg `0.7727` n `228`; crypto_major avg `0.5245` n `8`; equity avg `1.7304` n `86`; fx avg `-0.0146` n `6`; index avg `0.2862` n `23`; metal avg `0.1555` n `20`; unknown avg `0.4671` n `764`
- 4h: commodity avg `-0.3383` n `12`; crypto_alt avg `0.6856` n `228`; crypto_major avg `0.388` n `8`; equity avg `1.2852` n `86`; fx avg `-0.0429` n `6`; index avg `0.1224` n `23`; metal avg `-0.1113` n `20`; unknown avg `0.247` n `764`
- 24h: commodity avg `-0.5072` n `12`; crypto_alt avg `-4.0875` n `228`; crypto_major avg `-4.5928` n `8`; equity avg `-3.1962` n `85`; fx avg `-0.1608` n `6`; index avg `-0.8303` n `23`; metal avg `-1.1284` n `20`; unknown avg `-0.2227` n `604`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1319`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1246`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1184`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1068`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0833`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0824`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.074`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0673`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0631`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0625`, n `668`, weak_sample_signal
