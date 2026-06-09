# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-09T01:52:23.722928+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-1.8942` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `-1.8489` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_index_leads_crypto: score `1.8189` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0209` n `12`; crypto_alt avg `-0.1193` n `228`; crypto_major avg `-0.1233` n `8`; equity avg `0.0852` n `74`; fx avg `-0.0177` n `6`; index avg `0.0519` n `23`; metal avg `-0.0158` n `18`; unknown avg `-0.0363` n `517`
- 1h: commodity avg `-0.116` n `12`; crypto_alt avg `0.6419` n `228`; crypto_major avg `0.3976` n `8`; equity avg `0.4717` n `74`; fx avg `-0.0265` n `6`; index avg `0.3377` n `23`; metal avg `0.4322` n `18`; unknown avg `0.1318` n `517`
- 4h: commodity avg `-0.2526` n `12`; crypto_alt avg `-2.5533` n `228`; crypto_major avg `-2.0235` n `8`; equity avg `-0.1746` n `74`; fx avg `0.2696` n `6`; index avg `-0.2046` n `23`; metal avg `-0.1293` n `18`; unknown avg `-0.2743` n `517`
- 24h: commodity avg `-0.8012` n `12`; crypto_alt avg `-0.4063` n `228`; crypto_major avg `0.1334` n `8`; equity avg `1.5913` n `74`; fx avg `-0.3073` n `6`; index avg `0.7865` n `23`; metal avg `0.1392` n `18`; unknown avg `-2.8642` n `507`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1078`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0921`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0919`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0881`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0824`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0805`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0789`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0781`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0772`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0753`, n `668`, weak_sample_signal
