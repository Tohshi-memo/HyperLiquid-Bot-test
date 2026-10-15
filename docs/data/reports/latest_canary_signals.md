# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-15T04:22:27.035497+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.08` - Polymarket crypto volume is unusually high.
- 4h_crypto_metal_divergence: score `-1.6047` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.5126` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0423` n `13`; crypto_alt avg `0.3972` n `236`; crypto_major avg `0.3797` n `8`; equity avg `0.451` n `151`; fx avg `0.0049` n `6`; index avg `0.0891` n `26`; metal avg `0.038` n `20`; unknown avg `0.3615` n `1136`
- 1h: commodity avg `0.0086` n `13`; crypto_alt avg `-0.0192` n `236`; crypto_major avg `0.2145` n `8`; equity avg `0.1855` n `151`; fx avg `0.0` n `6`; index avg `0.0788` n `26`; metal avg `-0.0533` n `20`; unknown avg `-0.0445` n `1128`
- 4h: commodity avg `-0.2265` n `13`; crypto_alt avg `-2.9109` n `236`; crypto_major avg `-1.6252` n `8`; equity avg `-0.4603` n `151`; fx avg `0.0882` n `6`; index avg `-0.1126` n `26`; metal avg `-0.0205` n `20`; unknown avg `0.3631` n `1128`
- 24h: commodity avg `-0.3962` n `13`; crypto_alt avg `-5.3124` n `236`; crypto_major avg `-3.774` n `8`; equity avg `-6.0597` n `151`; fx avg `0.0905` n `6`; index avg `-1.0166` n `26`; metal avg `-0.7284` n `20`; unknown avg `1393.279` n `890`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1291`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1048`, n `666`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1024`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1002`, n `666`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0991`, n `666`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0972`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.096`, n `666`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0774`, n `666`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0728`, n `666`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0671`, n `666`, weak_sample_signal
