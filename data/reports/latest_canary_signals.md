# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-24T09:52:35.498738+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0125` n `12`; crypto_alt avg `-0.0188` n `228`; crypto_major avg `0.1242` n `8`; equity avg `-0.0069` n `86`; fx avg `-0.009` n `6`; index avg `0.0151` n `23`; metal avg `0.005` n `20`; unknown avg `-0.0246` n `764`
- 1h: commodity avg `-0.002` n `12`; crypto_alt avg `-0.1601` n `228`; crypto_major avg `-0.1837` n `8`; equity avg `-0.0833` n `86`; fx avg `0.0071` n `6`; index avg `-0.0137` n `23`; metal avg `-0.0438` n `20`; unknown avg `-0.1509` n `764`
- 4h: commodity avg `-0.0764` n `12`; crypto_alt avg `-0.3672` n `228`; crypto_major avg `-0.3181` n `8`; equity avg `-0.0539` n `86`; fx avg `0.0393` n `6`; index avg `0.0371` n `23`; metal avg `-0.1672` n `20`; unknown avg `-0.2627` n `740`
- 24h: commodity avg `-0.4314` n `12`; crypto_alt avg `0.1491` n `228`; crypto_major avg `0.1676` n `8`; equity avg `4.655` n `86`; fx avg `0.0109` n `6`; index avg `0.0644` n `23`; metal avg `-0.5423` n `20`; unknown avg `-0.0007` n `716`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1186`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1033`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0978`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0797`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.069`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0686`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0673`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0668`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.065`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0642`, n `668`, weak_sample_signal
