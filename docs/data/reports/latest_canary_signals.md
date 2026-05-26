# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-26T19:26:59.573563+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-1.7346` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.6743` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.1046` n `12`; crypto_alt avg `-0.1208` n `228`; crypto_major avg `-0.0719` n `8`; equity avg `-0.0497` n `67`; fx avg `0.0032` n `6`; index avg `0.0332` n `23`; metal avg `0.128` n `18`; unknown avg `-0.1188` n `418`
- 1h: commodity avg `-0.0111` n `12`; crypto_alt avg `-0.706` n `228`; crypto_major avg `-0.6439` n `8`; equity avg `-0.3715` n `67`; fx avg `0.0121` n `6`; index avg `0.0176` n `23`; metal avg `0.3917` n `18`; unknown avg `-0.0927` n `418`
- 4h: commodity avg `-0.4657` n `12`; crypto_alt avg `-1.6751` n `228`; crypto_major avg `-1.507` n `8`; equity avg `-0.1717` n `67`; fx avg `0.0467` n `6`; index avg `0.1673` n `23`; metal avg `0.2276` n `18`; unknown avg `1.0284` n `418`
- 24h: commodity avg `1.0107` n `12`; crypto_alt avg `-2.656` n `228`; crypto_major avg `-1.8735` n `8`; equity avg `-0.5259` n `67`; fx avg `-0.1073` n `6`; index avg `0.4368` n `23`; metal avg `-1.027` n `18`; unknown avg `0.1679` n `395`

## Correlations

- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1749`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.174`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1733`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1567`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1396`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.138`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1375`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1373`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1308`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1225`, n `668`, weak_sample_signal
