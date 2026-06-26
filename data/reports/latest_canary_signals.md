# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-26T02:52:27.744853+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.4957` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_index_leads_crypto: score `1.2418` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0266` n `12`; crypto_alt avg `-0.2333` n `228`; crypto_major avg `-0.2603` n `8`; equity avg `-0.3442` n `86`; fx avg `0.0123` n `6`; index avg `-0.07` n `23`; metal avg `-0.0596` n `20`; unknown avg `0.3882` n `765`
- 1h: commodity avg `-0.0679` n `12`; crypto_alt avg `-1.4582` n `228`; crypto_major avg `-1.4853` n `8`; equity avg `-1.3225` n `86`; fx avg `0.0018` n `6`; index avg `-0.2435` n `23`; metal avg `-0.3845` n `20`; unknown avg `-0.6539` n `765`
- 4h: commodity avg `-0.0843` n `12`; crypto_alt avg `-1.8145` n `228`; crypto_major avg `-1.9314` n `8`; equity avg `-2.0386` n `86`; fx avg `0.033` n `6`; index avg `-0.4357` n `23`; metal avg `-0.6414` n `20`; unknown avg `-1.0569` n `749`
- 24h: commodity avg `0.3233` n `12`; crypto_alt avg `-3.0793` n `228`; crypto_major avg `-3.1657` n `8`; equity avg `-3.9927` n `86`; fx avg `0.044` n `6`; index avg `-0.6067` n `23`; metal avg `-0.1021` n `20`; unknown avg `0.2217` n `716`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1319`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1111`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1038`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0941`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0856`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0724`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0706`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0695`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0651`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0597`, n `668`, weak_sample_signal
