# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-08T21:22:24.398893+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0375` n `12`; crypto_alt avg `-0.067` n `228`; crypto_major avg `0.0197` n `8`; equity avg `-0.0309` n `74`; fx avg `-0.0353` n `6`; index avg `-0.0328` n `23`; metal avg `0.0516` n `18`; unknown avg `0.1176` n `517`
- 1h: commodity avg `0.1394` n `12`; crypto_alt avg `0.6404` n `228`; crypto_major avg `0.8262` n `8`; equity avg `0.1628` n `74`; fx avg `0.0023` n `6`; index avg `0.0917` n `23`; metal avg `0.3143` n `18`; unknown avg `0.2694` n `517`
- 4h: commodity avg `0.111` n `12`; crypto_alt avg `0.5156` n `228`; crypto_major avg `0.9145` n `8`; equity avg `-0.0502` n `74`; fx avg `-0.0153` n `6`; index avg `0.0669` n `23`; metal avg `0.0722` n `18`; unknown avg `-0.057` n `517`
- 24h: commodity avg `-0.6024` n `12`; crypto_alt avg `3.5768` n `228`; crypto_major avg `4.2614` n `8`; equity avg `2.5092` n `74`; fx avg `-0.2933` n `6`; index avg `0.9562` n `23`; metal avg `0.2997` n `18`; unknown avg `-1.9996` n `506`

## Correlations

- market_context_score -> fx_forward_1h_return_pct: corr `-0.1218`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1198`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1117`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0967`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0877`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0837`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0831`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0807`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0706`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0689`, n `668`, weak_sample_signal
