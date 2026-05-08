# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-08T08:52:15.009188+00:00`
- Correlation status: `ready`
- Asset price records: `631`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.02` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0881` n `12`; crypto_alt avg `0.1748` n `228`; crypto_major avg `0.079` n `8`; equity avg `0.0096` n `65`; fx avg `0.0207` n `5`; index avg `0.001` n `23`; metal avg `-0.0734` n `18`; unknown avg `-0.006` n `375`
- 1h: commodity avg `-0.0551` n `12`; crypto_alt avg `0.4031` n `228`; crypto_major avg `0.2695` n `8`; equity avg `0.3874` n `65`; fx avg `0.0314` n `5`; index avg `0.152` n `23`; metal avg `0.2132` n `18`; unknown avg `0.317` n `375`
- 4h: commodity avg `-0.2051` n `12`; crypto_alt avg `0.3271` n `228`; crypto_major avg `0.3425` n `8`; equity avg `0.8256` n `65`; fx avg `0.0653` n `5`; index avg `0.2483` n `23`; metal avg `0.3501` n `18`; unknown avg `0.6977` n `355`
- 24h: commodity avg `1.0247` n `12`; crypto_alt avg `0.7425` n `228`; crypto_major avg `-1.8058` n `8`; equity avg `-0.3968` n `65`; fx avg `0.2615` n `5`; index avg `-0.5567` n `23`; metal avg `-0.3937` n `18`; unknown avg `-0.0231` n `355`

## Correlations

- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1338`, n `623`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1332`, n `623`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1121`, n `627`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1044`, n `627`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0998`, n `627`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0953`, n `627`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0852`, n `623`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.085`, n `623`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0741`, n `623`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0729`, n `627`, weak_sample_signal
