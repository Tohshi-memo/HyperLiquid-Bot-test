# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-14T14:07:25.823741+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1172` n `12`; crypto_alt avg `0.0717` n `228`; crypto_major avg `0.0233` n `8`; equity avg `-0.0107` n `74`; fx avg `-0.004` n `6`; index avg `-0.0068` n `23`; metal avg `-0.0022` n `18`; unknown avg `0.0384` n `645`
- 1h: commodity avg `0.2159` n `12`; crypto_alt avg `-0.0575` n `228`; crypto_major avg `0.0065` n `8`; equity avg `-0.0617` n `74`; fx avg `-0.006` n `6`; index avg `-0.0498` n `23`; metal avg `-0.0286` n `18`; unknown avg `0.0628` n `645`
- 4h: commodity avg `0.5155` n `12`; crypto_alt avg `-0.6718` n `228`; crypto_major avg `-0.388` n `8`; equity avg `-0.1492` n `74`; fx avg `0.0216` n `6`; index avg `0.1074` n `23`; metal avg `-0.1329` n `18`; unknown avg `0.4007` n `645`
- 24h: commodity avg `-0.088` n `12`; crypto_alt avg `-0.7902` n `228`; crypto_major avg `-0.1187` n `8`; equity avg `0.6096` n `74`; fx avg `0.0005` n `6`; index avg `0.1526` n `23`; metal avg `0.0234` n `18`; unknown avg `-1.0053` n `592`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1349`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1093`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.105`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1003`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0683`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0682`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0681`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0632`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0626`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0597`, n `668`, weak_sample_signal
