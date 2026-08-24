# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-24T12:37:24.875732+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `2.0978` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_metal_divergence: score `1.9611` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0217` n `12`; crypto_alt avg `0.3686` n `231`; crypto_major avg `0.3886` n `8`; equity avg `-0.0778` n `122`; fx avg `-0.0056` n `6`; index avg `-0.0254` n `25`; metal avg `0.0122` n `20`; unknown avg `0.0197` n `793`
- 1h: commodity avg `0.0929` n `12`; crypto_alt avg `-0.0388` n `231`; crypto_major avg `0.1716` n `8`; equity avg `-0.2779` n `122`; fx avg `-0.0277` n `6`; index avg `-0.0651` n `25`; metal avg `-0.0579` n `20`; unknown avg `0.124` n `793`
- 4h: commodity avg `0.2288` n `12`; crypto_alt avg `1.6721` n `231`; crypto_major avg `2.1021` n `8`; equity avg `0.0043` n `122`; fx avg `-0.0436` n `6`; index avg `-0.0138` n `25`; metal avg `0.141` n `20`; unknown avg `1.1329` n `793`
- 24h: commodity avg `0.0292` n `12`; crypto_alt avg `1.462` n `231`; crypto_major avg `1.1206` n `8`; equity avg `-1.5871` n `122`; fx avg `-0.1459` n `6`; index avg `-0.1715` n `25`; metal avg `0.1947` n `20`; unknown avg `3.8984` n `777`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1094`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1043`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0958`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0926`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.09`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.081`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0728`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0628`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0616`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0581`, n `668`, weak_sample_signal
