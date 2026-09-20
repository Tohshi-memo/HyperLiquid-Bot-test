# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-20T16:18:02.234783+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0062` n `12`; crypto_alt avg `0.4341` n `234`; crypto_major avg `0.377` n `8`; equity avg `0.0781` n `140`; fx avg `0.0167` n `6`; index avg `0.024` n `26`; metal avg `0.0103` n `20`; unknown avg `0.2941` n `935`
- 1h: commodity avg `0.0053` n `12`; crypto_alt avg `1.212` n `234`; crypto_major avg `0.8337` n `8`; equity avg `0.2037` n `140`; fx avg `0.0288` n `6`; index avg `0.029` n `26`; metal avg `0.0061` n `20`; unknown avg `0.3703` n `889`
- 4h: commodity avg `-0.0027` n `12`; crypto_alt avg `1.4832` n `234`; crypto_major avg `1.174` n `8`; equity avg `0.2476` n `140`; fx avg `0.0166` n `6`; index avg `0.0336` n `26`; metal avg `0.0067` n `20`; unknown avg `1.2789` n `889`
- 24h: commodity avg `0.4407` n `12`; crypto_alt avg `-0.8789` n `234`; crypto_major avg `-1.348` n `8`; equity avg `-0.054` n `140`; fx avg `-0.0239` n `6`; index avg `-0.0324` n `26`; metal avg `-0.0147` n `20`; unknown avg `168.9276` n `795`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1519`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1409`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1328`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1172`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1163`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1146`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0946`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0884`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.08`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.075`, n `668`, weak_sample_signal
