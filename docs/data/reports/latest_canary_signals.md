# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-08T13:52:35.164804+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.1839` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `0.124` n `12`; crypto_alt avg `0.1255` n `228`; crypto_major avg `0.2154` n `8`; equity avg `0.5104` n `74`; fx avg `-0.0099` n `6`; index avg `0.0428` n `23`; metal avg `-0.4959` n `18`; unknown avg `0.1272` n `517`
- 1h: commodity avg `-0.1239` n `12`; crypto_alt avg `0.1673` n `228`; crypto_major avg `0.3764` n `8`; equity avg `-0.1053` n `74`; fx avg `0.0197` n `6`; index avg `0.0098` n `23`; metal avg `-0.3236` n `18`; unknown avg `0.5152` n `517`
- 4h: commodity avg `-0.9838` n `12`; crypto_alt avg `1.1486` n `228`; crypto_major avg `1.2001` n `8`; equity avg `1.0527` n `74`; fx avg `0.0718` n `6`; index avg `0.6343` n `23`; metal avg `0.4707` n `18`; unknown avg `-1.56` n `517`
- 24h: commodity avg `-0.4635` n `12`; crypto_alt avg `2.599` n `228`; crypto_major avg `3.8947` n `8`; equity avg `2.0632` n `74`; fx avg `-0.2785` n `6`; index avg `1.024` n `23`; metal avg `-0.044` n `18`; unknown avg `-2.7333` n `506`

## Correlations

- market_context_score -> fx_forward_1h_return_pct: corr `-0.122`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1171`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1152`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1108`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1014`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0849`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0828`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0777`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0742`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0741`, n `668`, weak_sample_signal
