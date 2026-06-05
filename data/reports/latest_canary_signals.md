# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-05T08:52:24.102073+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-1.9027` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.8618` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_equity_divergence: score `-1.6783` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.282` n `12`; crypto_alt avg `-0.3086` n `228`; crypto_major avg `-0.2643` n `8`; equity avg `-0.1003` n `74`; fx avg `0.0093` n `6`; index avg `-0.0093` n `23`; metal avg `-0.022` n `18`; unknown avg `0.1744` n `424`
- 1h: commodity avg `0.1506` n `12`; crypto_alt avg `-1.2179` n `228`; crypto_major avg `-0.9061` n `8`; equity avg `0.1996` n `74`; fx avg `0.0222` n `6`; index avg `0.0001` n `23`; metal avg `-0.1175` n `18`; unknown avg `0.075` n `424`
- 4h: commodity avg `-0.2846` n `12`; crypto_alt avg `-3.1709` n `228`; crypto_major avg `-1.8856` n `8`; equity avg `-0.2073` n `74`; fx avg `0.0433` n `6`; index avg `-0.0238` n `23`; metal avg `0.0171` n `18`; unknown avg `1.1983` n `404`
- 24h: commodity avg `-0.3073` n `12`; crypto_alt avg `-6.6097` n `228`; crypto_major avg `-4.7134` n `8`; equity avg `-0.9499` n `73`; fx avg `0.1054` n `6`; index avg `-0.1814` n `23`; metal avg `-0.4828` n `18`; unknown avg `0.4004` n `402`

## Correlations

- market_context_score -> index_forward_1h_return_pct: corr `0.1109`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0976`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0951`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0938`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.092`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0915`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0903`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0879`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0833`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0803`, n `668`, weak_sample_signal
