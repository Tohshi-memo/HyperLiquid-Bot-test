# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-08T05:22:29.776419+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-1.6443` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.174` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.087` n `12`; crypto_alt avg `-0.06` n `229`; crypto_major avg `-0.1175` n `8`; equity avg `-0.2194` n `91`; fx avg `-0.0169` n `6`; index avg `-0.053` n `25`; metal avg `-0.0875` n `20`; unknown avg `0.0394` n `763`
- 1h: commodity avg `0.1477` n `12`; crypto_alt avg `0.0331` n `229`; crypto_major avg `-0.092` n `8`; equity avg `-0.266` n `91`; fx avg `-0.0282` n `6`; index avg `-0.0906` n `25`; metal avg `0.0197` n `20`; unknown avg `-0.195` n `763`
- 4h: commodity avg `0.2591` n `12`; crypto_alt avg `-1.2189` n `229`; crypto_major avg `-1.4221` n `8`; equity avg `-0.4489` n `91`; fx avg `-0.0752` n `6`; index avg `-0.2481` n `25`; metal avg `0.2222` n `20`; unknown avg `0.3365` n `763`
- 24h: commodity avg `1.0432` n `12`; crypto_alt avg `-1.942` n `229`; crypto_major avg `-1.4072` n `8`; equity avg `-0.9544` n `91`; fx avg `-0.2206` n `6`; index avg `-0.1831` n `25`; metal avg `0.1145` n `20`; unknown avg `-0.2102` n `731`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1346`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1143`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0963`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0951`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0921`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0775`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0742`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.069`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0665`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0653`, n `668`, weak_sample_signal
