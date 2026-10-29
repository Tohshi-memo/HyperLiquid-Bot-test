# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-29T02:22:24.782248+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-1.7478` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.7129` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_index_leads_crypto: score `1.1743` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0191` n `13`; crypto_alt avg `0.1105` n `238`; crypto_major avg `0.035` n `8`; equity avg `-0.0686` n `155`; fx avg `-0.0084` n `6`; index avg `-0.0111` n `27`; metal avg `-0.0592` n `20`; unknown avg `0.0228` n `1238`
- 1h: commodity avg `-0.0692` n `13`; crypto_alt avg `-1.7625` n `238`; crypto_major avg `-1.2982` n `8`; equity avg `-0.8316` n `155`; fx avg `0.0026` n `6`; index avg `-0.1239` n `27`; metal avg `-0.1658` n `20`; unknown avg `2.238` n `1232`
- 4h: commodity avg `-0.0322` n `13`; crypto_alt avg `-2.4007` n `238`; crypto_major avg `-1.8676` n `8`; equity avg `-1.137` n `155`; fx avg `-0.104` n `6`; index avg `-0.1547` n `27`; metal avg `-0.1198` n `20`; unknown avg `4.5073` n `1148`
- 24h: commodity avg `-0.0933` n `13`; crypto_alt avg `-2.2126` n `238`; crypto_major avg `-1.6785` n `8`; equity avg `-0.9268` n `154`; fx avg `0.0337` n `6`; index avg `-0.1262` n `27`; metal avg `-0.129` n `20`; unknown avg `27.3019` n `996`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1227`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1223`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0923`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0895`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0894`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0799`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0768`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0728`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0727`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0658`, n `668`, weak_sample_signal
