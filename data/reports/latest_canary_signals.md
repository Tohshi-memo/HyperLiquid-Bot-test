# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-09T02:37:23.056690+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-1.752` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_index_leads_crypto: score `1.7237` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-1.5663` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0622` n `12`; crypto_alt avg `-0.2436` n `228`; crypto_major avg `-0.131` n `8`; equity avg `0.0198` n `74`; fx avg `-0.0012` n `6`; index avg `0.012` n `23`; metal avg `0.0147` n `18`; unknown avg `0.0313` n `517`
- 1h: commodity avg `0.0034` n `12`; crypto_alt avg `-0.9348` n `228`; crypto_major avg `-0.526` n `8`; equity avg `0.0514` n `74`; fx avg `-0.0162` n `6`; index avg `0.0037` n `23`; metal avg `-0.1838` n `18`; unknown avg `-0.1446` n `517`
- 4h: commodity avg `-0.1133` n `12`; crypto_alt avg `-2.5165` n `228`; crypto_major avg `-1.7137` n `8`; equity avg `0.0383` n `74`; fx avg `-0.0842` n `6`; index avg `0.01` n `23`; metal avg `-0.1474` n `18`; unknown avg `-0.1586` n `517`
- 24h: commodity avg `-1.0008` n `12`; crypto_alt avg `-1.1833` n `228`; crypto_major avg `-0.516` n `8`; equity avg `1.0715` n `74`; fx avg `-0.3603` n `6`; index avg `0.4638` n `23`; metal avg `0.1225` n `18`; unknown avg `-2.8188` n `507`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1066`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0922`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0903`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.086`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.086`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0816`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0809`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0783`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0776`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0759`, n `668`, weak_sample_signal
