# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-08T18:37:25.673652+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0844` n `12`; crypto_alt avg `-0.2111` n `228`; crypto_major avg `-0.1445` n `8`; equity avg `-0.072` n `74`; fx avg `-0.0022` n `6`; index avg `-0.0108` n `23`; metal avg `-0.2616` n `18`; unknown avg `0.0625` n `517`
- 1h: commodity avg `0.0023` n `12`; crypto_alt avg `0.4191` n `228`; crypto_major avg `0.4034` n `8`; equity avg `0.1946` n `74`; fx avg `0.0119` n `6`; index avg `0.1838` n `23`; metal avg `-0.0111` n `18`; unknown avg `-0.0678` n `517`
- 4h: commodity avg `-0.2049` n `12`; crypto_alt avg `0.6618` n `228`; crypto_major avg `0.2821` n `8`; equity avg `0.1405` n `74`; fx avg `0.0067` n `6`; index avg `0.09` n `23`; metal avg `0.4145` n `18`; unknown avg `-0.1383` n `517`
- 24h: commodity avg `-0.8125` n `12`; crypto_alt avg `2.578` n `228`; crypto_major avg `2.9087` n `8`; equity avg `2.4342` n `74`; fx avg `-0.2752` n `6`; index avg `1.1544` n `23`; metal avg `-0.0346` n `18`; unknown avg `-2.0767` n `506`

## Correlations

- market_context_score -> fx_forward_1h_return_pct: corr `-0.1156`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1138`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1074`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0948`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0845`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.083`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0794`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.079`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0722`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0614`, n `668`, weak_sample_signal
