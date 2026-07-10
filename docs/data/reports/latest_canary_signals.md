# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-10T14:37:28.045140+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.1327` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0432` n `12`; crypto_alt avg `-0.2424` n `229`; crypto_major avg `-0.0992` n `8`; equity avg `-0.0653` n `91`; fx avg `0.002` n `6`; index avg `-0.0124` n `25`; metal avg `-0.0997` n `20`; unknown avg `0.0216` n `766`
- 1h: commodity avg `-0.1168` n `12`; crypto_alt avg `-0.8367` n `229`; crypto_major avg `-0.91` n `8`; equity avg `-0.5803` n `91`; fx avg `-0.0248` n `6`; index avg `0.0083` n `25`; metal avg `0.0123` n `20`; unknown avg `0.1083` n `766`
- 4h: commodity avg `-0.222` n `12`; crypto_alt avg `-1.0071` n `229`; crypto_major avg `-1.1572` n `8`; equity avg `-0.826` n `91`; fx avg `-0.0494` n `6`; index avg `-0.0245` n `25`; metal avg `-0.0396` n `20`; unknown avg `-0.0559` n `766`
- 24h: commodity avg `-0.6776` n `12`; crypto_alt avg `0.376` n `229`; crypto_major avg `0.8946` n `8`; equity avg `-0.7338` n `91`; fx avg `-0.1469` n `6`; index avg `0.0443` n `25`; metal avg `-0.1851` n `20`; unknown avg `-0.2041` n `733`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1271`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1083`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0992`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0958`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0932`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0909`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0884`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0738`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0718`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0718`, n `668`, weak_sample_signal
