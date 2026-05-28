# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-28T00:22:17.056058+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-1.5515` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.3189` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.013` n `12`; crypto_alt avg `0.2249` n `228`; crypto_major avg `0.1378` n `8`; equity avg `-0.0065` n `67`; fx avg `0.0031` n `6`; index avg `0.0524` n `23`; metal avg `0.1466` n `18`; unknown avg `0.0538` n `419`
- 1h: commodity avg `0.1916` n `12`; crypto_alt avg `0.3527` n `228`; crypto_major avg `0.1388` n `8`; equity avg `-0.4073` n `67`; fx avg `0.0289` n `6`; index avg `-0.1755` n `23`; metal avg `0.0959` n `18`; unknown avg `-0.1968` n `419`
- 4h: commodity avg `0.3452` n `12`; crypto_alt avg `-1.836` n `228`; crypto_major avg `-1.5595` n `8`; equity avg `-0.5792` n `67`; fx avg `0.0033` n `6`; index avg `-0.2406` n `23`; metal avg `-0.008` n `18`; unknown avg `0.738` n `419`
- 24h: commodity avg `-0.8166` n `12`; crypto_alt avg `-2.0199` n `228`; crypto_major avg `-1.4872` n `8`; equity avg `-0.6246` n `67`; fx avg `-0.0798` n `6`; index avg `-0.7513` n `23`; metal avg `-1.5655` n `18`; unknown avg `-0.6381` n `400`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.181`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1799`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1731`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1629`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1604`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1476`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.147`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1468`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1403`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1363`, n `668`, weak_sample_signal
