# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-24T01:22:53.943574+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0982` n `12`; crypto_alt avg `-0.0877` n `228`; crypto_major avg `-0.015` n `8`; equity avg `-0.057` n `86`; fx avg `0.0012` n `6`; index avg `-0.0241` n `23`; metal avg `0.0916` n `20`; unknown avg `-0.2264` n `764`
- 1h: commodity avg `-0.021` n `12`; crypto_alt avg `-0.1976` n `228`; crypto_major avg `-0.0787` n `8`; equity avg `-0.086` n `86`; fx avg `-0.0049` n `6`; index avg `-0.0588` n `23`; metal avg `-0.1417` n `20`; unknown avg `-0.6015` n `764`
- 4h: commodity avg `-0.0488` n `12`; crypto_alt avg `-0.0603` n `228`; crypto_major avg `0.462` n `8`; equity avg `0.2831` n `86`; fx avg `0.0266` n `6`; index avg `0.1092` n `23`; metal avg `-0.2523` n `20`; unknown avg `-0.2823` n `756`
- 24h: commodity avg `-0.4417` n `12`; crypto_alt avg `-2.3402` n `228`; crypto_major avg `-2.943` n `8`; equity avg `-2.2091` n `86`; fx avg `-0.1447` n `6`; index avg `-0.636` n `23`; metal avg `-1.2046` n `20`; unknown avg `0.2404` n `588`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1281`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.122`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1189`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1019`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0997`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0868`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0773`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.074`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0683`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0656`, n `668`, weak_sample_signal
