# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-09T10:52:13.557887+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0288` n `12`; crypto_alt avg `0.1935` n `228`; crypto_major avg `0.0114` n `8`; equity avg `-0.0397` n `65`; fx avg `0.0006` n `5`; index avg `-0.0108` n `23`; metal avg `-0.0068` n `18`; unknown avg `0.0908` n `376`
- 1h: commodity avg `-0.0363` n `12`; crypto_alt avg `0.3144` n `228`; crypto_major avg `0.0176` n `8`; equity avg `0.0512` n `65`; fx avg `0.0049` n `5`; index avg `-0.0127` n `23`; metal avg `-0.0414` n `18`; unknown avg `0.4976` n `376`
- 4h: commodity avg `-0.0535` n `12`; crypto_alt avg `-0.5627` n `228`; crypto_major avg `-0.3591` n `8`; equity avg `0.0385` n `65`; fx avg `0.0057` n `5`; index avg `0.0114` n `23`; metal avg `-0.0475` n `18`; unknown avg `0.2528` n `376`
- 24h: commodity avg `-0.156` n `12`; crypto_alt avg `2.9966` n `228`; crypto_major avg `1.7947` n `8`; equity avg `2.7883` n `65`; fx avg `-0.0164` n `5`; index avg `1.2617` n `23`; metal avg `-0.2326` n `18`; unknown avg `0.6414` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1202`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1155`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0901`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0835`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0797`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0783`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0779`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0697`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0661`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0661`, n `668`, weak_sample_signal
