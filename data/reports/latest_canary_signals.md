# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-26T20:22:20.915740+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-1.512` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.2288` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0196` n `12`; crypto_alt avg `-0.0916` n `228`; crypto_major avg `-0.1271` n `8`; equity avg `0.0218` n `67`; fx avg `0.0125` n `6`; index avg `0.046` n `23`; metal avg `0.0516` n `18`; unknown avg `-0.1503` n `418`
- 1h: commodity avg `-0.1199` n `12`; crypto_alt avg `0.3577` n `228`; crypto_major avg `0.0717` n `8`; equity avg `0.1171` n `67`; fx avg `0.0148` n `6`; index avg `0.036` n `23`; metal avg `0.1752` n `18`; unknown avg `-0.36` n `418`
- 4h: commodity avg `-0.4595` n `12`; crypto_alt avg `-0.881` n `228`; crypto_major avg `-1.0735` n `8`; equity avg `0.0685` n `67`; fx avg `0.0359` n `6`; index avg `0.1553` n `23`; metal avg `0.4385` n `18`; unknown avg `0.042` n `418`
- 24h: commodity avg `0.9864` n `12`; crypto_alt avg `-2.3313` n `228`; crypto_major avg `-1.6909` n `8`; equity avg `-0.4954` n `67`; fx avg `-0.1111` n `6`; index avg `0.3798` n `23`; metal avg `-0.8774` n `18`; unknown avg `0.0782` n `395`

## Correlations

- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1741`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1727`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1719`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.157`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1388`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1381`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1357`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.135`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1312`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1254`, n `668`, weak_sample_signal
