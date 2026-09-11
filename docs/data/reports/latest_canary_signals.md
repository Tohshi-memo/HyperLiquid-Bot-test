# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-11T18:37:32.434162+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.26` - Polymarket crypto volume is unusually high.
- 4h_index_leads_crypto: score `1.8388` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_equity_divergence: score `-1.6853` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_metal_divergence: score `-1.6691` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0362` n `12`; crypto_alt avg `-0.1805` n `233`; crypto_major avg `-0.0382` n `8`; equity avg `-0.0194` n `136`; fx avg `0.0062` n `6`; index avg `0.0055` n `26`; metal avg `0.0003` n `20`; unknown avg `0.3603` n `806`
- 1h: commodity avg `0.1166` n `12`; crypto_alt avg `-0.8527` n `233`; crypto_major avg `-0.7434` n `8`; equity avg `-0.2436` n `136`; fx avg `0.0037` n `6`; index avg `-0.0292` n `26`; metal avg `-0.0969` n `20`; unknown avg `0.0694` n `804`
- 4h: commodity avg `-0.0575` n `12`; crypto_alt avg `-1.5564` n `233`; crypto_major avg `-1.7994` n `8`; equity avg `-0.1141` n `136`; fx avg `-0.0039` n `6`; index avg `0.0394` n `26`; metal avg `-0.1303` n `20`; unknown avg `3.0111` n `752`
- 24h: commodity avg `-0.4613` n `12`; crypto_alt avg `0.4054` n `233`; crypto_major avg `1.2447` n `8`; equity avg `0.5644` n `136`; fx avg `-0.1431` n `6`; index avg `0.3419` n `26`; metal avg `0.209` n `20`; unknown avg `1.8231` n `666`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1266`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1229`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1047`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.102`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1017`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0888`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0745`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0684`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0671`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0564`, n `668`, weak_sample_signal
