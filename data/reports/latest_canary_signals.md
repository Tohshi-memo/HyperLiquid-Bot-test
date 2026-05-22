# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-22T07:07:15.734423+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.27` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0781` n `12`; crypto_alt avg `-0.3061` n `228`; crypto_major avg `-0.1469` n `8`; equity avg `-0.1023` n `67`; fx avg `-0.0211` n `6`; index avg `-0.0391` n `23`; metal avg `-0.138` n `18`; unknown avg `-0.0543` n `386`
- 1h: commodity avg `-0.0132` n `12`; crypto_alt avg `-0.3726` n `228`; crypto_major avg `-0.2672` n `8`; equity avg `-0.0096` n `67`; fx avg `-0.0334` n `6`; index avg `-0.0057` n `23`; metal avg `-0.1369` n `18`; unknown avg `-0.4166` n `386`
- 4h: commodity avg `0.3478` n `12`; crypto_alt avg `-0.5049` n `228`; crypto_major avg `-0.6314` n `8`; equity avg `0.1182` n `67`; fx avg `0.0089` n `6`; index avg `0.126` n `23`; metal avg `-0.0934` n `18`; unknown avg `-0.4661` n `376`
- 24h: commodity avg `-0.7597` n `12`; crypto_alt avg `1.2958` n `228`; crypto_major avg `-0.0415` n `8`; equity avg `1.7178` n `66`; fx avg `0.0895` n `6`; index avg `0.8257` n `23`; metal avg `0.6774` n `18`; unknown avg `2.3291` n `375`

## Correlations

- risk_on_score -> equity_forward_1h_return_pct: corr `0.0682`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0609`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.048`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0469`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0461`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0445`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0424`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0409`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.04`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0397`, n `668`, weak_sample_signal
