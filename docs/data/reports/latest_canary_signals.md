# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-09T07:20:31.215467+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0141` n `12`; crypto_alt avg `0.0569` n `228`; crypto_major avg `0.0283` n `8`; equity avg `-0.0266` n `65`; fx avg `0.0017` n `5`; index avg `0.0132` n `23`; metal avg `0.0071` n `18`; unknown avg `-0.12` n `376`
- 1h: commodity avg `-0.0006` n `12`; crypto_alt avg `-0.3419` n `228`; crypto_major avg `-0.1137` n `8`; equity avg `-0.003` n `65`; fx avg `0.0017` n `5`; index avg `0.0334` n `23`; metal avg `0.0039` n `18`; unknown avg `0.1464` n `376`
- 4h: commodity avg `0.1082` n `12`; crypto_alt avg `-0.4371` n `228`; crypto_major avg `-0.2762` n `8`; equity avg `-0.0663` n `65`; fx avg `0.0206` n `5`; index avg `0.0724` n `23`; metal avg `-0.0624` n `18`; unknown avg `-0.3802` n `355`
- 24h: commodity avg `-0.0649` n `12`; crypto_alt avg `4.5256` n `228`; crypto_major avg `2.9035` n `8`; equity avg `3.3665` n `65`; fx avg `-0.0002` n `5`; index avg `1.3184` n `23`; metal avg `0.1629` n `18`; unknown avg `1.2102` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1143`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1101`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.097`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.084`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0828`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0793`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0713`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0703`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0655`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0645`, n `668`, weak_sample_signal
