# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-05T08:37:22.095380+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `2.0105` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-1.9925` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `-1.9576` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.1225` n `12`; crypto_alt avg `-0.312` n `228`; crypto_major avg `-0.1384` n `8`; equity avg `0.0348` n `74`; fx avg `-0.0036` n `6`; index avg `-0.0041` n `23`; metal avg `-0.0683` n `18`; unknown avg `-0.0973` n `424`
- 1h: commodity avg `-0.1178` n `12`; crypto_alt avg `-0.6059` n `228`; crypto_major avg `-0.3126` n `8`; equity avg `0.3381` n `74`; fx avg `0.0191` n `6`; index avg `0.1263` n `23`; metal avg `-0.1002` n `18`; unknown avg `0.0199` n `424`
- 4h: commodity avg `-0.5282` n `12`; crypto_alt avg `-2.9873` n `228`; crypto_major avg `-1.9046` n `8`; equity avg `0.053` n `74`; fx avg `0.0312` n `6`; index avg `0.1059` n `23`; metal avg `0.0879` n `18`; unknown avg `-0.1444` n `404`
- 24h: commodity avg `-0.672` n `12`; crypto_alt avg `-5.9377` n `228`; crypto_major avg `-4.1764` n `8`; equity avg `-1.1082` n `73`; fx avg `0.1002` n `6`; index avg `-0.2796` n `23`; metal avg `-0.525` n `18`; unknown avg `-0.8871` n `402`

## Correlations

- market_context_score -> index_forward_1h_return_pct: corr `0.1126`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0974`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0973`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0936`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0933`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0933`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0853`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0826`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0803`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0771`, n `668`, weak_sample_signal
