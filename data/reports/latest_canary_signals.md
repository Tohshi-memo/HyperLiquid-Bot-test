# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-08T01:37:24.582422+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-1.8198` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 1h_crypto_equity_divergence: score `-1.5905` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 1h_index_leads_crypto: score `1.4452` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_index_leads_crypto: score `1.3679` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0339` n `12`; crypto_alt avg `-1.2975` n `229`; crypto_major avg `-1.2858` n `8`; equity avg `-0.4055` n `91`; fx avg `-0.0129` n `6`; index avg `-0.0648` n `25`; metal avg `-0.0933` n `20`; unknown avg `0.4121` n `763`
- 1h: commodity avg `-0.0641` n `12`; crypto_alt avg `-1.369` n `229`; crypto_major avg `-1.4275` n `8`; equity avg `0.163` n `91`; fx avg `-0.0364` n `6`; index avg `0.0177` n `25`; metal avg `-0.1231` n `20`; unknown avg `0.222` n `763`
- 4h: commodity avg `-0.1265` n `12`; crypto_alt avg `-1.2646` n `229`; crypto_major avg `-1.2767` n `8`; equity avg `0.5431` n `91`; fx avg `0.0291` n `6`; index avg `0.0912` n `25`; metal avg `-0.1555` n `20`; unknown avg `-0.1516` n `763`
- 24h: commodity avg `0.813` n `12`; crypto_alt avg `-3.1562` n `229`; crypto_major avg `-2.7413` n `8`; equity avg `-1.6877` n `91`; fx avg `-0.2068` n `6`; index avg `-0.1912` n `25`; metal avg `-0.4664` n `20`; unknown avg `-0.3585` n `729`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.126`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1251`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1011`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0995`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0909`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0784`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0736`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.065`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0629`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0629`, n `668`, weak_sample_signal
