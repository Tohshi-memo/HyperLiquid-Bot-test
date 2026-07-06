# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-06T19:37:33.147715+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `1.8495` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_metal_divergence: score `1.5389` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0299` n `12`; crypto_alt avg `0.1031` n `229`; crypto_major avg `0.1507` n `8`; equity avg `-0.0527` n `91`; fx avg `-0.0024` n `6`; index avg `-0.0138` n `25`; metal avg `-0.0203` n `20`; unknown avg `-0.0043` n `763`
- 1h: commodity avg `0.0259` n `12`; crypto_alt avg `0.0262` n `229`; crypto_major avg `0.1524` n `8`; equity avg `0.1398` n `91`; fx avg `-0.014` n `6`; index avg `0.0241` n `25`; metal avg `-0.0869` n `20`; unknown avg `-0.0737` n `763`
- 4h: commodity avg `-0.048` n `12`; crypto_alt avg `1.4713` n `229`; crypto_major avg `1.6643` n `8`; equity avg `-0.1852` n `90`; fx avg `0.0195` n `6`; index avg `-0.0222` n `25`; metal avg `0.1254` n `20`; unknown avg `1.4823` n `763`
- 24h: commodity avg `0.0261` n `12`; crypto_alt avg `0.9395` n `229`; crypto_major avg `0.8213` n `8`; equity avg `-0.5551` n `90`; fx avg `0.1842` n `6`; index avg `0.0413` n `25`; metal avg `-0.201` n `20`; unknown avg `0.333` n `729`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1173`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0968`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0891`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0787`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0782`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0735`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0726`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0709`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.064`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0609`, n `668`, weak_sample_signal
