# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-31T05:52:39.566326+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0305` n `12`; crypto_alt avg `-0.0043` n `230`; crypto_major avg `-0.0202` n `8`; equity avg `0.0485` n `102`; fx avg `0.0252` n `6`; index avg `0.0091` n `25`; metal avg `-0.0743` n `20`; unknown avg `-0.4652` n `779`
- 1h: commodity avg `-0.071` n `12`; crypto_alt avg `0.2235` n `230`; crypto_major avg `0.1107` n `8`; equity avg `0.2283` n `102`; fx avg `-0.0071` n `6`; index avg `0.0719` n `25`; metal avg `-0.0928` n `20`; unknown avg `3.586` n `779`
- 4h: commodity avg `-0.1681` n `12`; crypto_alt avg `-0.3742` n `230`; crypto_major avg `-0.401` n `8`; equity avg `0.478` n `102`; fx avg `0.0243` n `6`; index avg `0.1289` n `25`; metal avg `-0.075` n `20`; unknown avg `-0.2264` n `779`
- 24h: commodity avg `-0.5815` n `12`; crypto_alt avg `0.0648` n `230`; crypto_major avg `0.8857` n `8`; equity avg `8.9618` n `102`; fx avg `-0.0759` n `6`; index avg `1.3007` n `25`; metal avg `0.5939` n `20`; unknown avg `0.0786` n `739`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1343`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1219`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0945`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0914`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0911`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.084`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0808`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0746`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0735`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0656`, n `668`, weak_sample_signal
