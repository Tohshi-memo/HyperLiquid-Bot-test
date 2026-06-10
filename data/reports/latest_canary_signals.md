# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-10T19:56:52.506003+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.6461` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0162` n `12`; crypto_alt avg `-0.2794` n `228`; crypto_major avg `-0.2939` n `8`; equity avg `-0.2519` n `74`; fx avg `0.0015` n `6`; index avg `-0.1027` n `23`; metal avg `-0.0102` n `18`; unknown avg `-0.1201` n `550`
- 1h: commodity avg `0.0223` n `12`; crypto_alt avg `-0.4402` n `228`; crypto_major avg `-0.1242` n `8`; equity avg `-0.3284` n `74`; fx avg `-0.0139` n `6`; index avg `-0.2217` n `23`; metal avg `-0.5462` n `18`; unknown avg `-0.1176` n `550`
- 4h: commodity avg `-0.4188` n `12`; crypto_alt avg `-2.039` n `228`; crypto_major avg `-2.3045` n `8`; equity avg `-1.0191` n `74`; fx avg `0.0024` n `6`; index avg `-0.6584` n `23`; metal avg `-1.0026` n `18`; unknown avg `0.3354` n `548`
- 24h: commodity avg `1.048` n `12`; crypto_alt avg `-1.9186` n `228`; crypto_major avg `-2.4039` n `8`; equity avg `-1.3674` n `74`; fx avg `-0.0304` n `6`; index avg `-1.0504` n `23`; metal avg `-2.1758` n `18`; unknown avg `-0.2185` n `537`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1022`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0871`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.08`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0777`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.068`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0652`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0645`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0586`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.054`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0537`, n `668`, weak_sample_signal
