# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-10T03:22:12.407960+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0084` n `12`; crypto_alt avg `-0.0808` n `228`; crypto_major avg `-0.036` n `8`; equity avg `0.0309` n `65`; fx avg `0.0013` n `5`; index avg `0.0045` n `23`; metal avg `0.0242` n `18`; unknown avg `0.0061` n `376`
- 1h: commodity avg `-0.0432` n `12`; crypto_alt avg `0.0913` n `228`; crypto_major avg `0.0288` n `8`; equity avg `0.1744` n `65`; fx avg `0.0013` n `5`; index avg `-0.0081` n `23`; metal avg `0.0455` n `18`; unknown avg `-0.0257` n `376`
- 4h: commodity avg `-0.0545` n `12`; crypto_alt avg `-0.4237` n `228`; crypto_major avg `-0.1866` n `8`; equity avg `0.2033` n `65`; fx avg `0.0023` n `5`; index avg `0.0818` n `23`; metal avg `0.0985` n `18`; unknown avg `-0.3889` n `376`
- 24h: commodity avg `0.3827` n `12`; crypto_alt avg `-1.8268` n `228`; crypto_major avg `-0.9346` n `8`; equity avg `0.7584` n `65`; fx avg `-0.0079` n `5`; index avg `0.336` n `23`; metal avg `0.1554` n `18`; unknown avg `-0.4643` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1353`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1157`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0982`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0918`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0911`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0826`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0767`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.074`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0701`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0697`, n `668`, weak_sample_signal
