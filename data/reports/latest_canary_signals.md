# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-12T06:37:32.028686+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.2313` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.1667` n `12`; crypto_alt avg `-0.5239` n `228`; crypto_major avg `-0.6221` n `8`; equity avg `-0.1509` n `74`; fx avg `0.0141` n `6`; index avg `-0.0793` n `23`; metal avg `-0.1886` n `18`; unknown avg `-0.3495` n `557`
- 1h: commodity avg `0.0859` n `12`; crypto_alt avg `-0.9917` n `228`; crypto_major avg `-1.1553` n `8`; equity avg `-0.5597` n `74`; fx avg `0.0052` n `6`; index avg `-0.22` n `23`; metal avg `-0.0578` n `18`; unknown avg `-0.7467` n `535`
- 4h: commodity avg `-0.4002` n `12`; crypto_alt avg `-1.4555` n `228`; crypto_major avg `-1.5182` n `8`; equity avg `-0.7556` n `74`; fx avg `0.0148` n `6`; index avg `-0.2869` n `23`; metal avg `-0.2819` n `18`; unknown avg `0.7873` n `535`
- 24h: commodity avg `-2.1197` n `12`; crypto_alt avg `0.2366` n `228`; crypto_major avg `0.3941` n `8`; equity avg `2.6874` n `74`; fx avg `-0.0236` n `6`; index avg `1.5276` n `23`; metal avg `2.5152` n `18`; unknown avg `1.3014` n `532`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.099`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0896`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0814`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.078`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0736`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0727`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0661`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0649`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0581`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0563`, n `668`, weak_sample_signal
