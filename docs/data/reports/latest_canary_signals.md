# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-22T00:37:27.857682+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0306` n `12`; crypto_alt avg `-0.0731` n `230`; crypto_major avg `-0.0541` n `8`; equity avg `-0.0798` n `98`; fx avg `-0.0053` n `6`; index avg `-0.0098` n `25`; metal avg `-0.0231` n `20`; unknown avg `0.0011` n `771`
- 1h: commodity avg `-0.0522` n `12`; crypto_alt avg `0.2463` n `230`; crypto_major avg `0.4186` n `8`; equity avg `0.1939` n `98`; fx avg `-0.0112` n `6`; index avg `0.057` n `25`; metal avg `0.0802` n `20`; unknown avg `0.3207` n `771`
- 4h: commodity avg `0.0404` n `12`; crypto_alt avg `0.1618` n `230`; crypto_major avg `0.3134` n `8`; equity avg `0.4246` n `98`; fx avg `-0.0385` n `6`; index avg `0.072` n `25`; metal avg `0.0717` n `20`; unknown avg `-0.0667` n `771`
- 24h: commodity avg `0.4281` n `12`; crypto_alt avg `0.7577` n `230`; crypto_major avg `0.7429` n `8`; equity avg `4.4497` n `98`; fx avg `0.0266` n `6`; index avg `0.7037` n `25`; metal avg `0.7722` n `20`; unknown avg `0.3763` n `755`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `0.1025`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0926`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.09`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0876`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0809`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0631`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0628`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0557`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.051`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0496`, n `666`, weak_sample_signal
