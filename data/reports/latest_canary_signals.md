# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-15T05:22:31.436085+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.76` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0631` n `12`; crypto_alt avg `0.3641` n `228`; crypto_major avg `0.2887` n `8`; equity avg `0.0566` n `74`; fx avg `-0.0045` n `6`; index avg `0.0367` n `23`; metal avg `0.1041` n `18`; unknown avg `0.0705` n `645`
- 1h: commodity avg `0.1058` n `12`; crypto_alt avg `-0.0409` n `228`; crypto_major avg `-0.0642` n `8`; equity avg `0.0392` n `74`; fx avg `0.0091` n `6`; index avg `0.0594` n `23`; metal avg `0.172` n `18`; unknown avg `-0.3884` n `645`
- 4h: commodity avg `0.1745` n `12`; crypto_alt avg `1.03` n `228`; crypto_major avg `0.6711` n `8`; equity avg `0.4161` n `74`; fx avg `0.0206` n `6`; index avg `0.1512` n `23`; metal avg `0.2699` n `18`; unknown avg `-0.3037` n `629`
- 24h: commodity avg `-0.8637` n `12`; crypto_alt avg `3.3067` n `228`; crypto_major avg `3.0121` n `8`; equity avg `1.9044` n `74`; fx avg `0.0351` n `6`; index avg `0.9341` n `23`; metal avg `2.1364` n `18`; unknown avg `3.2521` n `585`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1017`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0986`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0979`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0816`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0724`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0701`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0699`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0663`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0645`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0617`, n `668`, weak_sample_signal
