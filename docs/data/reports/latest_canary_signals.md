# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-25T13:37:35.440386+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-1.5533` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.2246` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0508` n `12`; crypto_alt avg `-0.4218` n `228`; crypto_major avg `-0.5051` n `8`; equity avg `-0.7906` n `86`; fx avg `-0.0017` n `6`; index avg `-0.027` n `23`; metal avg `-0.1061` n `20`; unknown avg `-0.093` n `765`
- 1h: commodity avg `0.0901` n `12`; crypto_alt avg `-0.3547` n `228`; crypto_major avg `-0.5641` n `8`; equity avg `-0.8743` n `86`; fx avg `0.0051` n `6`; index avg `-0.043` n `23`; metal avg `0.1594` n `20`; unknown avg `-0.0314` n `765`
- 4h: commodity avg `0.1076` n `12`; crypto_alt avg `-0.8687` n `228`; crypto_major avg `-1.2124` n `8`; equity avg `-0.6661` n `86`; fx avg `-0.0308` n `6`; index avg `0.0122` n `23`; metal avg `0.3409` n `20`; unknown avg `-0.0365` n `765`
- 24h: commodity avg `0.2613` n `12`; crypto_alt avg `-0.8569` n `228`; crypto_major avg `-1.1414` n `8`; equity avg `0.3002` n `86`; fx avg `0.0226` n `6`; index avg `0.5045` n `23`; metal avg `0.1528` n `20`; unknown avg `-0.4885` n `700`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1327`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1056`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1037`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0944`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0837`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0791`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0711`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0699`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0675`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0665`, n `668`, weak_sample_signal
