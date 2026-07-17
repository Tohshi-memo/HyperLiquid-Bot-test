# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-17T16:22:26.272976+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-1.5202` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.013` n `12`; crypto_alt avg `0.0307` n `230`; crypto_major avg `-0.0198` n `8`; equity avg `0.0048` n `96`; fx avg `0.0083` n `6`; index avg `-0.0128` n `25`; metal avg `0.0482` n `20`; unknown avg `0.1499` n `769`
- 1h: commodity avg `0.1909` n `12`; crypto_alt avg `0.5421` n `230`; crypto_major avg `0.3675` n `8`; equity avg `1.0755` n `96`; fx avg `0.0359` n `6`; index avg `0.1069` n `25`; metal avg `0.0855` n `20`; unknown avg `0.0724` n `769`
- 4h: commodity avg `0.3724` n `12`; crypto_alt avg `0.2955` n `230`; crypto_major avg `0.0904` n `8`; equity avg `1.6106` n `96`; fx avg `0.0855` n `6`; index avg `0.2116` n `25`; metal avg `0.3314` n `20`; unknown avg `-0.0458` n `769`
- 24h: commodity avg `0.5485` n `12`; crypto_alt avg `-1.663` n `230`; crypto_major avg `-2.4609` n `8`; equity avg `-1.2712` n `94`; fx avg `0.0808` n `6`; index avg `-0.2849` n `25`; metal avg `-0.1554` n `20`; unknown avg `-0.3432` n `736`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1279`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1027`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0945`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0943`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0879`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0835`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0835`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0824`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0813`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0775`, n `668`, weak_sample_signal
