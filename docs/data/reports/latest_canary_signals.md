# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-15T12:07:34.432175+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.47` - Polymarket crypto volume is unusually high.
- 4h_crypto_equity_divergence: score `1.8334` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.1483` n `12`; crypto_alt avg `0.0179` n `228`; crypto_major avg `-0.1321` n `8`; equity avg `-0.0571` n `74`; fx avg `-0.0036` n `6`; index avg `0.0107` n `23`; metal avg `0.0982` n `18`; unknown avg `0.2358` n `689`
- 1h: commodity avg `0.276` n `12`; crypto_alt avg `0.5285` n `228`; crypto_major avg `0.6499` n `8`; equity avg `0.0577` n `74`; fx avg `0.0057` n `6`; index avg `0.0696` n `23`; metal avg `0.1787` n `18`; unknown avg `0.1516` n `689`
- 4h: commodity avg `0.1686` n `12`; crypto_alt avg `1.3324` n `228`; crypto_major avg `1.8273` n `8`; equity avg `-0.0061` n `74`; fx avg `-0.0054` n `6`; index avg `0.1307` n `23`; metal avg `0.6361` n `18`; unknown avg `0.2353` n `689`
- 24h: commodity avg `-0.9073` n `12`; crypto_alt avg `4.6125` n `228`; crypto_major avg `4.7942` n `8`; equity avg `1.4994` n `74`; fx avg `0.0357` n `6`; index avg `0.9847` n `23`; metal avg `2.6629` n `18`; unknown avg `1.3563` n `529`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.106`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0998`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0795`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0744`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0736`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0726`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0709`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0705`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0666`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0602`, n `668`, weak_sample_signal
