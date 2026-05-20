# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-20T10:07:16.664019+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0451` n `12`; crypto_alt avg `0.0523` n `228`; crypto_major avg `0.078` n `8`; equity avg `0.0971` n `66`; fx avg `-0.0026` n `6`; index avg `-0.068` n `23`; metal avg `0.0336` n `18`; unknown avg `-0.051` n `384`
- 1h: commodity avg `0.1541` n `12`; crypto_alt avg `0.1122` n `228`; crypto_major avg `0.2189` n `8`; equity avg `0.216` n `66`; fx avg `0.0138` n `6`; index avg `0.021` n `23`; metal avg `0.101` n `18`; unknown avg `0.3015` n `384`
- 4h: commodity avg `-0.6094` n `12`; crypto_alt avg `0.1888` n `228`; crypto_major avg `0.4019` n `8`; equity avg `0.7838` n `66`; fx avg `-0.0629` n `6`; index avg `0.3662` n `23`; metal avg `0.7362` n `18`; unknown avg `0.2892` n `384`
- 24h: commodity avg `-0.0546` n `12`; crypto_alt avg `0.5388` n `228`; crypto_major avg `0.5212` n `8`; equity avg `1.4458` n `66`; fx avg `-0.1595` n `6`; index avg `0.186` n `23`; metal avg `-0.759` n `18`; unknown avg `0.9334` n `373`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0838`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.08`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0716`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.071`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0708`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0631`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0524`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0496`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0486`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0457`, n `668`, weak_sample_signal
