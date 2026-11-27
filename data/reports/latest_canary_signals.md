# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-27T03:37:29.509854+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.4262` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `1.6264` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0118` n `13`; crypto_alt avg `0.0209` n `239`; crypto_major avg `0.037` n `8`; equity avg `0.1164` n `168`; fx avg `-0.0266` n `6`; index avg `0.0067` n `27`; metal avg `-0.0048` n `20`; unknown avg `-0.0849` n `1263`
- 1h: commodity avg `0.0243` n `13`; crypto_alt avg `-0.0159` n `239`; crypto_major avg `0.2755` n `8`; equity avg `0.4326` n `168`; fx avg `0.0005` n `6`; index avg `0.0383` n `27`; metal avg `-0.0052` n `20`; unknown avg `29.3617` n `1259`
- 4h: commodity avg `0.1585` n `13`; crypto_alt avg `1.8611` n `239`; crypto_major avg `2.5847` n `8`; equity avg `2.7469` n `168`; fx avg `-0.0357` n `6`; index avg `0.2566` n `27`; metal avg `0.9583` n `20`; unknown avg `2.8616` n `1243`
- 24h: commodity avg `0.1934` n `13`; crypto_alt avg `1.7521` n `239`; crypto_major avg `2.135` n `8`; equity avg `2.3345` n `168`; fx avg `0.0041` n `6`; index avg `0.2195` n `27`; metal avg `0.7526` n `20`; unknown avg `182.4511` n `993`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1125`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1114`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1056`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1014`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0955`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0875`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0866`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0856`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0851`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0804`, n `668`, weak_sample_signal
