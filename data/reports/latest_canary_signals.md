# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-22T10:37:25.035912+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-2.0454` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.9692` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_equity_divergence: score `-1.8112` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 1h_index_leads_crypto: score `1.0065` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.002` n `12`; crypto_alt avg `1.0991` n `230`; crypto_major avg `1.0589` n `8`; equity avg `0.0425` n `121`; fx avg `0.0036` n `6`; index avg `0.0028` n `25`; metal avg `0.014` n `20`; unknown avg `0.195` n `794`
- 1h: commodity avg `-0.0078` n `12`; crypto_alt avg `-1.1884` n `230`; crypto_major avg `-1.015` n `8`; equity avg `-0.1401` n `121`; fx avg `0.0112` n `6`; index avg `-0.0085` n `25`; metal avg `0.0064` n `20`; unknown avg `-0.0848` n `794`
- 4h: commodity avg `-0.0173` n `12`; crypto_alt avg `-1.5733` n `230`; crypto_major avg `-1.9936` n `8`; equity avg `-0.1824` n `121`; fx avg `0.0072` n `6`; index avg `-0.0244` n `25`; metal avg `0.0518` n `20`; unknown avg `0.6793` n `794`
- 24h: commodity avg `0.0356` n `12`; crypto_alt avg `1.9435` n `230`; crypto_major avg `2.8172` n `8`; equity avg `-1.046` n `121`; fx avg `0.0399` n `6`; index avg `-0.106` n `25`; metal avg `-0.1062` n `20`; unknown avg `1.5174` n `777`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1609`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.145`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1359`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1341`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1269`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1231`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1212`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1204`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1166`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.098`, n `668`, weak_sample_signal
