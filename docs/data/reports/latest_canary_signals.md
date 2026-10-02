# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-02T19:22:32.972199+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.5026` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `-2.1682` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `2.1173` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_equity_divergence: score `-2.0561` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 1h_index_leads_crypto: score `1.27` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0223` n `13`; crypto_alt avg `-0.3611` n `235`; crypto_major avg `-0.3363` n `8`; equity avg `0.0455` n `143`; fx avg `0.0073` n `6`; index avg `0.0107` n `26`; metal avg `0.0401` n `20`; unknown avg `-0.0322` n `984`
- 1h: commodity avg `-0.0825` n `13`; crypto_alt avg `-1.942` n `235`; crypto_major avg `-1.2563` n `8`; equity avg `0.0411` n `143`; fx avg `-0.0031` n `6`; index avg `0.0137` n `26`; metal avg `0.1083` n `20`; unknown avg `18.5418` n `982`
- 4h: commodity avg `0.406` n `13`; crypto_alt avg `-3.693` n `235`; crypto_major avg `-2.0966` n `8`; equity avg `-0.0405` n `143`; fx avg `-0.0022` n `6`; index avg `0.0207` n `26`; metal avg `0.0716` n `20`; unknown avg `3.9747` n `976`
- 24h: commodity avg `-0.2129` n `13`; crypto_alt avg `-1.9656` n `235`; crypto_major avg `-1.3148` n `8`; equity avg `0.6742` n `142`; fx avg `-0.1201` n `6`; index avg `0.2804` n `26`; metal avg `-0.2378` n `20`; unknown avg `99.4092` n `824`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1692`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1651`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1423`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1239`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1205`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1116`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1073`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0986`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0943`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0815`, n `668`, weak_sample_signal
