# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-07T20:52:20.610013+00:00`
- Correlation status: `ready`
- Asset price records: `583`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.03` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0484` n `12`; crypto_alt avg `-0.1249` n `228`; crypto_major avg `0.0416` n `8`; equity avg `0.0127` n `65`; fx avg `0.0041` n `5`; index avg `-0.0799` n `23`; metal avg `-0.0388` n `18`; unknown avg `-0.0686` n `365`
- 1h: commodity avg `0.2152` n `12`; crypto_alt avg `-0.1717` n `228`; crypto_major avg `0.0146` n `8`; equity avg `0.1824` n `65`; fx avg `-0.0096` n `5`; index avg `-0.0512` n `23`; metal avg `-0.0243` n `18`; unknown avg `-0.1406` n `365`
- 4h: commodity avg `0.4838` n `12`; crypto_alt avg `0.6554` n `228`; crypto_major avg `0.0658` n `8`; equity avg `-0.2187` n `65`; fx avg `-0.0246` n `5`; index avg `-0.2337` n `23`; metal avg `-0.4772` n `18`; unknown avg `-0.5117` n `365`
- 24h: commodity avg `0.7331` n `12`; crypto_alt avg `1.4232` n `228`; crypto_major avg `-1.6459` n `8`; equity avg `-1.0865` n `65`; fx avg `0.1763` n `5`; index avg `-0.8467` n `23`; metal avg `0.1415` n `18`; unknown avg `-0.3531` n `353`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1404`, n `579`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1192`, n `579`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1071`, n `579`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0973`, n `579`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0951`, n `575`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0946`, n `575`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0927`, n `575`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0883`, n `575`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0826`, n `575`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0779`, n `575`, weak_sample_signal
