# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-01T08:22:27.564129+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.3131` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0572` n `12`; crypto_alt avg `-0.2019` n `228`; crypto_major avg `-0.3973` n `8`; equity avg `-0.0049` n `88`; fx avg `-0.0177` n `6`; index avg `-0.0054` n `23`; metal avg `0.108` n `20`; unknown avg `0.2797` n `765`
- 1h: commodity avg `-0.1045` n `12`; crypto_alt avg `-0.1349` n `228`; crypto_major avg `-0.4404` n `8`; equity avg `0.0495` n `88`; fx avg `-0.001` n `6`; index avg `0.0086` n `23`; metal avg `0.1145` n `20`; unknown avg `0.214` n `765`
- 4h: commodity avg `-0.2017` n `12`; crypto_alt avg `-1.148` n `228`; crypto_major avg `-1.3662` n `8`; equity avg `-0.2818` n `88`; fx avg `-0.0351` n `6`; index avg `-0.0531` n `23`; metal avg `0.0087` n `20`; unknown avg `-0.2043` n `743`
- 24h: commodity avg `-0.2412` n `12`; crypto_alt avg `-0.897` n `228`; crypto_major avg `-0.9512` n `8`; equity avg `0.3855` n `88`; fx avg `0.0665` n `6`; index avg `-0.0389` n `23`; metal avg `-0.6758` n `20`; unknown avg `-0.1406` n `743`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1177`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1159`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0923`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0908`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0847`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0809`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0719`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0711`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.064`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0599`, n `668`, weak_sample_signal
