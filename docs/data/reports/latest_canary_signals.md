# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-11T13:22:28.154716+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.27` - Polymarket crypto volume is unusually high.
- 1h_crypto_metal_divergence: score `1.6246` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.086` n `12`; crypto_alt avg `0.1041` n `233`; crypto_major avg `0.0781` n `8`; equity avg `-0.1806` n `136`; fx avg `0.026` n `6`; index avg `-0.0218` n `26`; metal avg `0.0188` n `20`; unknown avg `40.9467` n `796`
- 1h: commodity avg `0.0476` n `12`; crypto_alt avg `2.0045` n `233`; crypto_major avg `1.8965` n `8`; equity avg `0.6301` n `136`; fx avg `-0.0626` n `6`; index avg `0.0997` n `26`; metal avg `0.2719` n `20`; unknown avg `2.0608` n `788`
- 4h: commodity avg `-0.0882` n `12`; crypto_alt avg `0.8373` n `233`; crypto_major avg `1.2254` n `8`; equity avg `0.4808` n `136`; fx avg `-0.0842` n `6`; index avg `0.1258` n `26`; metal avg `0.2258` n `20`; unknown avg `0.3933` n `788`
- 24h: commodity avg `-0.1533` n `12`; crypto_alt avg `0.8729` n `233`; crypto_major avg `1.5497` n `8`; equity avg `1.1302` n `136`; fx avg `-0.1374` n `6`; index avg `0.2964` n `26`; metal avg `0.1508` n `20`; unknown avg `2.4645` n `683`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1344`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1303`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.117`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.11`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0921`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.08`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0789`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0786`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0653`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0652`, n `668`, weak_sample_signal
