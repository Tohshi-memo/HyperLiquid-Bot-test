# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-12T23:37:22.607355+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-2.1142` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `2.0` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_index_leads_crypto: score `1.1926` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.036` n `13`; crypto_alt avg `-0.6896` n `235`; crypto_major avg `-0.5712` n `8`; equity avg `-0.1765` n `151`; fx avg `0.0051` n `6`; index avg `-0.0147` n `26`; metal avg `0.005` n `20`; unknown avg `-0.4172` n `1135`
- 1h: commodity avg `-0.0499` n `13`; crypto_alt avg `-1.3269` n `235`; crypto_major avg `-1.2508` n `8`; equity avg `-0.4702` n `151`; fx avg `0.0005` n `6`; index avg `-0.0582` n `26`; metal avg `-0.003` n `20`; unknown avg `1.817` n `1133`
- 4h: commodity avg `-0.0678` n `13`; crypto_alt avg `-2.5879` n `235`; crypto_major avg `-2.0577` n `8`; equity avg `-0.6039` n `151`; fx avg `0.0002` n `6`; index avg `-0.0577` n `26`; metal avg `0.0565` n `20`; unknown avg `2.0178` n `1060`
- 24h: commodity avg `0.5561` n `13`; crypto_alt avg `-5.5469` n `235`; crypto_major avg `-3.7579` n `8`; equity avg `-4.0616` n `151`; fx avg `-0.1634` n `6`; index avg `-0.4408` n `26`; metal avg `-0.1561` n `20`; unknown avg `0.3673` n `853`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.2041`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1776`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1545`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1196`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1163`, n `666`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1112`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1003`, n `666`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0863`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0835`, n `666`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0769`, n `666`, weak_sample_signal
