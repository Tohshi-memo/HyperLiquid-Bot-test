# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-22T12:07:29.686959+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0716` n `12`; crypto_alt avg `0.0674` n `228`; crypto_major avg `-0.0851` n `8`; equity avg `0.0113` n `79`; fx avg `0.0087` n `6`; index avg `0.0053` n `23`; metal avg `0.0946` n `20`; unknown avg `0.0535` n `722`
- 1h: commodity avg `-0.0184` n `12`; crypto_alt avg `0.5397` n `228`; crypto_major avg `0.3206` n `8`; equity avg `0.0042` n `79`; fx avg `0.0167` n `6`; index avg `0.016` n `23`; metal avg `-0.0666` n `20`; unknown avg `0.2066` n `722`
- 4h: commodity avg `-0.3445` n `12`; crypto_alt avg `0.9535` n `228`; crypto_major avg `0.5329` n `8`; equity avg `0.4345` n `79`; fx avg `0.0548` n `6`; index avg `0.1454` n `23`; metal avg `0.2008` n `18`; unknown avg `0.551` n `701`
- 24h: commodity avg `-0.503` n `12`; crypto_alt avg `0.8567` n `228`; crypto_major avg `0.9968` n `8`; equity avg `0.1067` n `79`; fx avg `0.0337` n `6`; index avg `0.1162` n `23`; metal avg `0.5484` n `18`; unknown avg `0.7541` n `637`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0873`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0868`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0838`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0815`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0771`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0771`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.072`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0652`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0645`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0599`, n `668`, weak_sample_signal
