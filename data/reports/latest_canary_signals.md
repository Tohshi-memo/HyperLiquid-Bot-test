# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-03T23:22:32.501045+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0753` n `12`; crypto_alt avg `-0.0206` n `230`; crypto_major avg `0.0586` n `8`; equity avg `0.0665` n `104`; fx avg `0.0084` n `6`; index avg `0.0254` n `25`; metal avg `0.0085` n `20`; unknown avg `-0.0305` n `783`
- 1h: commodity avg `-0.0181` n `12`; crypto_alt avg `-0.0848` n `230`; crypto_major avg `0.0022` n `8`; equity avg `0.1073` n `104`; fx avg `-0.0001` n `6`; index avg `0.0204` n `25`; metal avg `0.016` n `20`; unknown avg `-0.1018` n `783`
- 4h: commodity avg `-0.1052` n `12`; crypto_alt avg `-0.3347` n `230`; crypto_major avg `-0.4628` n `8`; equity avg `0.4607` n `104`; fx avg `0.0553` n `6`; index avg `0.0996` n `25`; metal avg `0.0415` n `20`; unknown avg `0.0442` n `783`
- 24h: commodity avg `-0.0819` n `12`; crypto_alt avg `0.2055` n `230`; crypto_major avg `0.0104` n `8`; equity avg `2.137` n `104`; fx avg `-0.3101` n `6`; index avg `0.1141` n `25`; metal avg `-0.2657` n `20`; unknown avg `0.0408` n `766`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1404`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1053`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0971`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0921`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0889`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0847`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0842`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0825`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0816`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.08`, n `668`, weak_sample_signal
