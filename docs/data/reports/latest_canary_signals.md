# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-25T07:37:31.523546+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `1.6126` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0101` n `12`; crypto_alt avg `-0.0893` n `228`; crypto_major avg `0.0728` n `8`; equity avg `-0.0343` n `86`; fx avg `0.0047` n `6`; index avg `-0.007` n `23`; metal avg `0.0107` n `20`; unknown avg `-0.0352` n `757`
- 1h: commodity avg `0.0984` n `12`; crypto_alt avg `-0.0888` n `228`; crypto_major avg `0.2383` n `8`; equity avg `0.1451` n `86`; fx avg `-0.0071` n `6`; index avg `-0.0033` n `23`; metal avg `0.1355` n `20`; unknown avg `0.0449` n `749`
- 4h: commodity avg `0.1577` n `12`; crypto_alt avg `1.0733` n `228`; crypto_major avg `1.6795` n `8`; equity avg `0.5365` n `86`; fx avg `-0.0285` n `6`; index avg `0.0675` n `23`; metal avg `0.0669` n `20`; unknown avg `0.1623` n `733`
- 24h: commodity avg `-0.3224` n `12`; crypto_alt avg `-0.9785` n `228`; crypto_major avg `-0.312` n `8`; equity avg `0.2163` n `86`; fx avg `-0.0398` n `6`; index avg `0.5582` n `23`; metal avg `-1.695` n `20`; unknown avg `-0.6899` n `700`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1073`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0921`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0916`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.081`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0791`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0771`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0627`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.059`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0575`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0542`, n `668`, weak_sample_signal
