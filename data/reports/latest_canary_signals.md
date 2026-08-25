# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-25T22:22:26.305968+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-1.6534` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_metal_divergence: score `-1.5423` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.5089` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0148` n `12`; crypto_alt avg `0.0795` n `231`; crypto_major avg `-0.0809` n `8`; equity avg `-0.0067` n `122`; fx avg `0.0166` n `6`; index avg `-0.0101` n `25`; metal avg `0.0198` n `20`; unknown avg `0.0638` n `795`
- 1h: commodity avg `-0.0297` n `12`; crypto_alt avg `1.0729` n `231`; crypto_major avg `0.9094` n `8`; equity avg `0.154` n `122`; fx avg `0.013` n `6`; index avg `-0.0038` n `25`; metal avg `0.0908` n `20`; unknown avg `0.3321` n `795`
- 4h: commodity avg `-0.1577` n `12`; crypto_alt avg `-1.4303` n `231`; crypto_major avg `-1.446` n `8`; equity avg `0.2074` n `122`; fx avg `-0.006` n `6`; index avg `0.0629` n `25`; metal avg `0.0963` n `20`; unknown avg `-0.3399` n `795`
- 24h: commodity avg `-0.6899` n `12`; crypto_alt avg `-1.7594` n `231`; crypto_major avg `-0.7727` n `8`; equity avg `2.0609` n `122`; fx avg `0.045` n `6`; index avg `0.259` n `25`; metal avg `-0.0387` n `20`; unknown avg `-0.4524` n `778`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.155`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1295`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1232`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1074`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0961`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0961`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0852`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0829`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0817`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0816`, n `668`, weak_sample_signal
