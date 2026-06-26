# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-26T12:07:29.546145+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-2.147` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.7793` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0928` n `12`; crypto_alt avg `0.1892` n `228`; crypto_major avg `0.196` n `8`; equity avg `0.1531` n `86`; fx avg `-0.0049` n `6`; index avg `0.0125` n `23`; metal avg `0.0566` n `20`; unknown avg `0.019` n `765`
- 1h: commodity avg `0.0453` n `12`; crypto_alt avg `-0.1657` n `228`; crypto_major avg `-0.3361` n `8`; equity avg `-0.0879` n `86`; fx avg `-0.0063` n `6`; index avg `-0.0084` n `23`; metal avg `-0.0802` n `20`; unknown avg `-0.0657` n `765`
- 4h: commodity avg `0.0279` n `12`; crypto_alt avg `-1.3695` n `228`; crypto_major avg `-1.8543` n `8`; equity avg `-0.4416` n `86`; fx avg `0.0209` n `6`; index avg `-0.075` n `23`; metal avg `0.2927` n `20`; unknown avg `-0.159` n `765`
- 24h: commodity avg `0.1073` n `12`; crypto_alt avg `-1.8895` n `228`; crypto_major avg `-2.0368` n `8`; equity avg `-4.0466` n `86`; fx avg `0.0699` n `6`; index avg `-0.6114` n `23`; metal avg `0.6148` n `20`; unknown avg `0.6555` n `701`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.2761`, n `668`, moderate_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1877`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1477`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1348`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1037`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0946`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0945`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0883`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0771`, n `668`, weak_sample_signal
