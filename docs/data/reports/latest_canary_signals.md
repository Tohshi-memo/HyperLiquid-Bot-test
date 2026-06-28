# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-28T19:07:26.638340+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0642` n `12`; crypto_alt avg `-0.0458` n `228`; crypto_major avg `-0.1085` n `8`; equity avg `-0.0278` n `88`; fx avg `0.0` n `6`; index avg `-0.0045` n `23`; metal avg `-0.0042` n `20`; unknown avg `0.0517` n `764`
- 1h: commodity avg `0.0423` n `12`; crypto_alt avg `-0.2365` n `228`; crypto_major avg `-0.2947` n `8`; equity avg `-0.0687` n `88`; fx avg `-0.0051` n `6`; index avg `-0.0137` n `23`; metal avg `0.0115` n `20`; unknown avg `0.7332` n `764`
- 4h: commodity avg `0.0084` n `12`; crypto_alt avg `-1.1125` n `228`; crypto_major avg `-0.8491` n `8`; equity avg `-0.1265` n `88`; fx avg `-0.0202` n `6`; index avg `-0.0412` n `23`; metal avg `0.0056` n `20`; unknown avg `-0.4099` n `764`
- 24h: commodity avg `0.3786` n `12`; crypto_alt avg `-0.9738` n `228`; crypto_major avg `-1.5082` n `8`; equity avg `0.0035` n `88`; fx avg `-0.0306` n `6`; index avg `-0.0492` n `23`; metal avg `-0.0232` n `20`; unknown avg `15.0185` n `690`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.19`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1867`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1355`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1309`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0916`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0911`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0881`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0793`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0774`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0769`, n `668`, weak_sample_signal
