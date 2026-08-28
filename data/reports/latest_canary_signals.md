# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-28T05:22:24.604977+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.8351` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-1.7858` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0071` n `12`; crypto_alt avg `-0.3312` n `231`; crypto_major avg `-0.2072` n `8`; equity avg `-0.2391` n `127`; fx avg `-0.0009` n `6`; index avg `-0.0327` n `26`; metal avg `-0.0004` n `20`; unknown avg `0.0183` n `792`
- 1h: commodity avg `0.0168` n `12`; crypto_alt avg `-0.3817` n `231`; crypto_major avg `-0.3549` n `8`; equity avg `-0.314` n `127`; fx avg `-0.0074` n `6`; index avg `-0.0502` n `26`; metal avg `-0.0157` n `20`; unknown avg `0.9927` n `792`
- 4h: commodity avg `0.0102` n `12`; crypto_alt avg `-2.4844` n `231`; crypto_major avg `-1.8845` n `8`; equity avg `-0.5304` n `127`; fx avg `-0.0241` n `6`; index avg `-0.0494` n `26`; metal avg `-0.0987` n `20`; unknown avg `1.8023` n `792`
- 24h: commodity avg `0.3382` n `12`; crypto_alt avg `0.4916` n `231`; crypto_major avg `1.5275` n `8`; equity avg `-0.1777` n `127`; fx avg `-0.0356` n `6`; index avg `0.0615` n `26`; metal avg `-0.0547` n `20`; unknown avg `0.5494` n `775`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1195`, n `669`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1173`, n `669`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0973`, n `669`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0813`, n `669`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0781`, n `669`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0681`, n `669`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0596`, n `669`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0589`, n `669`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0588`, n `669`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0541`, n `669`, weak_sample_signal
