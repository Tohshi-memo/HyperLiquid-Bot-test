# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-28T04:37:28.285731+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.4172` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0166` n `12`; crypto_alt avg `-0.2699` n `231`; crypto_major avg `-0.3022` n `8`; equity avg `-0.0807` n `127`; fx avg `-0.0013` n `6`; index avg `-0.0148` n `26`; metal avg `-0.0297` n `20`; unknown avg `-0.0639` n `792`
- 1h: commodity avg `0.0121` n `12`; crypto_alt avg `-0.2431` n `231`; crypto_major avg `-0.3806` n `8`; equity avg `-0.1696` n `127`; fx avg `-0.001` n `6`; index avg `-0.0171` n `26`; metal avg `-0.0039` n `20`; unknown avg `-0.2057` n `792`
- 4h: commodity avg `0.0035` n `12`; crypto_alt avg `-1.9152` n `231`; crypto_major avg `-1.4275` n `8`; equity avg `-0.1796` n `127`; fx avg `-0.0157` n `6`; index avg `-0.0103` n `26`; metal avg `-0.0119` n `20`; unknown avg `-0.0149` n `792`
- 24h: commodity avg `0.3166` n `12`; crypto_alt avg `0.3734` n `231`; crypto_major avg `1.6864` n `8`; equity avg `-0.0841` n `127`; fx avg `-0.0278` n `6`; index avg `0.0534` n `26`; metal avg `-0.0394` n `20`; unknown avg `0.4546` n `775`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1206`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1201`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0975`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0836`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0793`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0634`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0589`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0583`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0576`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0539`, n `668`, weak_sample_signal
