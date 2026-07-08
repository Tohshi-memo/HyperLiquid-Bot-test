# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-08T04:07:25.940456+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-2.4258` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_metal_divergence: score `-1.7467` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.5044` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.002` n `12`; crypto_alt avg `-0.0695` n `229`; crypto_major avg `-0.0569` n `8`; equity avg `-0.1407` n `91`; fx avg `-0.0035` n `6`; index avg `-0.0284` n `25`; metal avg `-0.0418` n `20`; unknown avg `-0.0583` n `763`
- 1h: commodity avg `-0.0138` n `12`; crypto_alt avg `-0.2672` n `229`; crypto_major avg `-0.3581` n `8`; equity avg `0.0398` n `91`; fx avg `0.0245` n `6`; index avg `-0.0689` n `25`; metal avg `0.0113` n `20`; unknown avg `0.2089` n `763`
- 4h: commodity avg `-0.0465` n `12`; crypto_alt avg `-1.2026` n `229`; crypto_major avg `-1.4668` n `8`; equity avg `0.959` n `91`; fx avg `-0.068` n `6`; index avg `0.0376` n `25`; metal avg `0.2799` n `20`; unknown avg `-0.0753` n `763`
- 24h: commodity avg `0.9245` n `12`; crypto_alt avg `-2.5715` n `229`; crypto_major avg `-1.8634` n `8`; equity avg `-0.8501` n `91`; fx avg `-0.152` n `6`; index avg `-0.1389` n `25`; metal avg `-0.1278` n `20`; unknown avg `-0.424` n `731`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1311`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1188`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0991`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0979`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0957`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0801`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.079`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0734`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0731`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.072`, n `668`, weak_sample_signal
