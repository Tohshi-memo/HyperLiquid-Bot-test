# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-22T05:37:24.306370+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0163` n `12`; crypto_alt avg `-0.0546` n `230`; crypto_major avg `-0.1199` n `8`; equity avg `-0.1661` n `98`; fx avg `0.0058` n `6`; index avg `-0.0166` n `25`; metal avg `0.0399` n `20`; unknown avg `1.9249` n `771`
- 1h: commodity avg `-0.0103` n `12`; crypto_alt avg `-0.4507` n `230`; crypto_major avg `-0.7635` n `8`; equity avg `-0.8332` n `98`; fx avg `-0.0107` n `6`; index avg `-0.1376` n `25`; metal avg `0.0222` n `20`; unknown avg `0.2677` n `771`
- 4h: commodity avg `-0.1119` n `12`; crypto_alt avg `-0.6255` n `230`; crypto_major avg `-0.9955` n `8`; equity avg `-1.2711` n `98`; fx avg `0.0263` n `6`; index avg `-0.2304` n `25`; metal avg `0.0022` n `20`; unknown avg `-0.4016` n `771`
- 24h: commodity avg `0.5463` n `12`; crypto_alt avg `-0.6884` n `230`; crypto_major avg `-0.9704` n `8`; equity avg `1.4222` n `98`; fx avg `0.0825` n `6`; index avg `0.1574` n `25`; metal avg `0.6721` n `20`; unknown avg `0.1121` n `755`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0982`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0964`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0898`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0866`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0766`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0711`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0694`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0678`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0637`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0634`, n `666`, weak_sample_signal
