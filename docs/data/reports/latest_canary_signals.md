# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-21T11:07:20.737391+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.48` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.1917` n `12`; crypto_alt avg `-0.0249` n `228`; crypto_major avg `-0.0549` n `8`; equity avg `-0.0057` n `66`; fx avg `0.0042` n `6`; index avg `0.0113` n `23`; metal avg `0.1203` n `18`; unknown avg `0.881` n `386`
- 1h: commodity avg `1.2251` n `12`; crypto_alt avg `-0.7495` n `228`; crypto_major avg `-0.6269` n `8`; equity avg `-0.7059` n `66`; fx avg `0.012` n `6`; index avg `-0.4272` n `23`; metal avg `-0.4724` n `18`; unknown avg `1.5961` n `386`
- 4h: commodity avg `0.3648` n `12`; crypto_alt avg `-0.7573` n `228`; crypto_major avg `-0.3816` n `8`; equity avg `-0.2309` n `66`; fx avg `0.0181` n `6`; index avg `-0.2425` n `23`; metal avg `-0.13` n `18`; unknown avg `2.4403` n `385`
- 24h: commodity avg `-0.9129` n `12`; crypto_alt avg `1.5291` n `228`; crypto_major avg `1.9753` n `8`; equity avg `0.8367` n `66`; fx avg `0.0751` n `6`; index avg `0.8144` n `23`; metal avg `-0.3583` n `18`; unknown avg `7.8173` n `374`

## Correlations

- risk_on_score -> equity_forward_1h_return_pct: corr `0.0728`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0708`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0662`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0647`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.06`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0578`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0543`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0525`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0522`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0514`, n `668`, weak_sample_signal
