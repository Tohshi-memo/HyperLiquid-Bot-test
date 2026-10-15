# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-15T02:52:24.354390+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-1.6267` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_index_leads_crypto: score `1.1326` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_index_leads_crypto: score `1.0955` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0209` n `13`; crypto_alt avg `0.0756` n `236`; crypto_major avg `-0.0949` n `8`; equity avg `0.0261` n `151`; fx avg `0.0376` n `6`; index avg `-0.0101` n `26`; metal avg `0.0685` n `20`; unknown avg `1.0682` n `1136`
- 1h: commodity avg `0.0034` n `13`; crypto_alt avg `-2.1081` n `236`; crypto_major avg `-1.1634` n `8`; equity avg `-0.0603` n `151`; fx avg `0.0624` n `6`; index avg `-0.0308` n `26`; metal avg `0.0057` n `20`; unknown avg `1.6214` n `1134`
- 4h: commodity avg `-0.2996` n `13`; crypto_alt avg `-2.8706` n `236`; crypto_major avg `-1.4409` n `8`; equity avg `-0.8547` n `151`; fx avg `0.2292` n `6`; index avg `-0.3454` n `26`; metal avg `0.1858` n `20`; unknown avg `1.4366` n `1128`
- 24h: commodity avg `-0.4976` n `13`; crypto_alt avg `-5.3935` n `236`; crypto_major avg `-3.7731` n `8`; equity avg `-6.1871` n `151`; fx avg `0.1344` n `6`; index avg `-1.0611` n `26`; metal avg `-0.6769` n `20`; unknown avg `1396.0817` n `890`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1354`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1241`, n `666`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1054`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1036`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1005`, n `666`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.099`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0949`, n `666`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0824`, n `666`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0758`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0716`, n `668`, weak_sample_signal
