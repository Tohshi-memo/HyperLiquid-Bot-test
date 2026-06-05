# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-05T08:22:24.703346+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-1.5702` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.5236` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.1237` n `12`; crypto_alt avg `-0.2987` n `228`; crypto_major avg `-0.3488` n `8`; equity avg `0.2616` n `74`; fx avg `-0.001` n `6`; index avg `0.0942` n `23`; metal avg `0.136` n `18`; unknown avg `-0.0495` n `424`
- 1h: commodity avg `-0.0108` n `12`; crypto_alt avg `1.184` n `228`; crypto_major avg `1.4323` n `8`; equity avg `0.676` n `74`; fx avg `0.0114` n `6`; index avg `0.1574` n `23`; metal avg `-0.0126` n `18`; unknown avg `0.8047` n `424`
- 4h: commodity avg `-0.4016` n `12`; crypto_alt avg `-2.3792` n `228`; crypto_major avg `-1.4149` n `8`; equity avg `0.0713` n `74`; fx avg `0.0177` n `6`; index avg `0.1087` n `23`; metal avg `0.1553` n `18`; unknown avg `0.2569` n `404`
- 24h: commodity avg `-0.6691` n `12`; crypto_alt avg `-5.286` n `228`; crypto_major avg `-3.6258` n `8`; equity avg `-0.9571` n `73`; fx avg `0.0966` n `6`; index avg `-0.2341` n `23`; metal avg `-0.2913` n `18`; unknown avg `-0.7291` n `402`

## Correlations

- market_context_score -> index_forward_1h_return_pct: corr `0.1134`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0981`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0965`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0947`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0935`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0922`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0862`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0843`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0748`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0708`, n `668`, weak_sample_signal
