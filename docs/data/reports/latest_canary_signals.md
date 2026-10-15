# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-15T04:07:27.028753+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.05` - Polymarket crypto volume is unusually high.
- 4h_crypto_metal_divergence: score `-1.9826` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.6363` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0024` n `13`; crypto_alt avg `0.0908` n `236`; crypto_major avg `0.0764` n `8`; equity avg `-0.079` n `151`; fx avg `0.0118` n `6`; index avg `0.0109` n `26`; metal avg `-0.0285` n `20`; unknown avg `-0.0689` n `1128`
- 1h: commodity avg `-0.0308` n `13`; crypto_alt avg `-0.5718` n `236`; crypto_major avg `-0.3793` n `8`; equity avg `-0.3646` n `151`; fx avg `-0.0429` n `6`; index avg `-0.0199` n `26`; metal avg `-0.1239` n `20`; unknown avg `-0.4507` n `1128`
- 4h: commodity avg `-0.2988` n `13`; crypto_alt avg `-3.4201` n `236`; crypto_major avg `-1.9211` n `8`; equity avg `-1.0804` n `151`; fx avg `0.1339` n `6`; index avg `-0.2848` n `26`; metal avg `0.0615` n `20`; unknown avg `0.1095` n `1128`
- 24h: commodity avg `-0.4355` n `13`; crypto_alt avg `-5.7182` n `236`; crypto_major avg `-4.1347` n `8`; equity avg `-6.5357` n `151`; fx avg `0.086` n `6`; index avg `-1.1005` n `26`; metal avg `-0.7555` n `20`; unknown avg `1393.3126` n `890`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1463`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1042`, n `666`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1042`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1001`, n `666`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0993`, n `666`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.099`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.096`, n `666`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0822`, n `666`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0748`, n `666`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0734`, n `666`, weak_sample_signal
