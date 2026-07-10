# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-10T17:22:25.233257+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0613` n `12`; crypto_alt avg `-0.0983` n `229`; crypto_major avg `-0.2147` n `8`; equity avg `-0.0335` n `92`; fx avg `-0.0163` n `6`; index avg `0.006` n `25`; metal avg `0.0452` n `20`; unknown avg `-0.01` n `765`
- 1h: commodity avg `0.0638` n `12`; crypto_alt avg `0.0628` n `229`; crypto_major avg `-0.0744` n `8`; equity avg `0.0582` n `92`; fx avg `0.0002` n `6`; index avg `-0.0168` n `25`; metal avg `-0.0076` n `20`; unknown avg `-0.0403` n `765`
- 4h: commodity avg `-0.1962` n `12`; crypto_alt avg `-0.1477` n `229`; crypto_major avg `-0.4576` n `8`; equity avg `-0.3026` n `92`; fx avg `-0.0562` n `6`; index avg `0.109` n `25`; metal avg `0.0859` n `20`; unknown avg `-0.1768` n `765`
- 24h: commodity avg `-0.3132` n `12`; crypto_alt avg `0.9835` n `229`; crypto_major avg `1.03` n `8`; equity avg `-0.9269` n `92`; fx avg `-0.1785` n `6`; index avg `-0.0124` n `25`; metal avg `-0.1124` n `20`; unknown avg `-0.1793` n `732`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1261`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1089`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1036`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0996`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0961`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.094`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0903`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0816`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0757`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0755`, n `668`, weak_sample_signal
