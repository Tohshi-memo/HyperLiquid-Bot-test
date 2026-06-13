# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-13T09:07:30.151216+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.2604` n `12`; crypto_alt avg `0.1356` n `228`; crypto_major avg `0.0135` n `8`; equity avg `0.0509` n `74`; fx avg `-0.0643` n `6`; index avg `0.0673` n `23`; metal avg `0.0629` n `18`; unknown avg `0.0656` n `643`
- 1h: commodity avg `0.272` n `12`; crypto_alt avg `0.0677` n `228`; crypto_major avg `0.191` n `8`; equity avg `0.0311` n `74`; fx avg `-0.128` n `6`; index avg `0.067` n `23`; metal avg `0.0688` n `18`; unknown avg `0.366` n `643`
- 4h: commodity avg `0.1423` n `12`; crypto_alt avg `1.2226` n `228`; crypto_major avg `0.9247` n `8`; equity avg `0.2599` n `74`; fx avg `-0.1437` n `6`; index avg `0.1307` n `23`; metal avg `0.1609` n `18`; unknown avg `-0.0246` n `627`
- 24h: commodity avg `0.7817` n `12`; crypto_alt avg `0.9287` n `228`; crypto_major avg `0.3177` n `8`; equity avg `-0.3813` n `74`; fx avg `-0.085` n `6`; index avg `0.8226` n `23`; metal avg `0.3152` n `18`; unknown avg `28.1372` n `619`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0915`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0878`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.08`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0764`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0681`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.062`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0616`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0615`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0573`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0556`, n `668`, weak_sample_signal
