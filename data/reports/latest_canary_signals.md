# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-11T00:37:24.727499+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0008` n `12`; crypto_alt avg `0.0082` n `229`; crypto_major avg `-0.0289` n `8`; equity avg `-0.014` n `92`; fx avg `-0.0028` n `6`; index avg `0.0031` n `25`; metal avg `-0.0039` n `20`; unknown avg `0.2051` n `765`
- 1h: commodity avg `0.0337` n `12`; crypto_alt avg `-0.2217` n `229`; crypto_major avg `-0.1851` n `8`; equity avg `0.0153` n `92`; fx avg `0.0007` n `6`; index avg `-0.0025` n `25`; metal avg `-0.0045` n `20`; unknown avg `0.7178` n `765`
- 4h: commodity avg `0.0379` n `12`; crypto_alt avg `0.1974` n `229`; crypto_major avg `-0.0237` n `8`; equity avg `0.0749` n `92`; fx avg `0.01` n `6`; index avg `-0.0189` n `25`; metal avg `0.0279` n `20`; unknown avg `0.2894` n `765`
- 24h: commodity avg `-0.2281` n `12`; crypto_alt avg `1.1729` n `229`; crypto_major avg `1.0641` n `8`; equity avg `-0.194` n `92`; fx avg `-0.2255` n `6`; index avg `0.1652` n `25`; metal avg `0.1892` n `20`; unknown avg `0.1695` n `732`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.121`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1108`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1074`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1072`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1028`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1016`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0916`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0885`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0877`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0832`, n `668`, weak_sample_signal
